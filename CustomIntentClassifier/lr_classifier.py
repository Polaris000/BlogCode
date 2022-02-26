import logging
import os
import typing
from typing import Any, Dict, List, Optional, Text, Type

import joblib
from rasa.nlu.classifiers.classifier import IntentClassifier
from rasa.nlu.components import Component
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.featurizers.featurizer import SparseFeaturizer
from rasa.nlu.model import Metadata
from rasa.shared.nlu.constants import TEXT
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.training_data.training_data import TrainingData
from scipy.sparse import vstack
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

logger = logging.getLogger(__name__)

if typing.TYPE_CHECKING:
    import sklearn


class LRIntentClassifier(IntentClassifier):
    """Intent classifier using the sklearn framework"""

    @classmethod
    def required_components(cls) -> List[Type[Component]]:
        return [SparseFeaturizer]

    defaults = {
        "class_weight": "balanced",
        "max_iter": 100,
        "solver": "lbfgs",
        "verbose": 1
    }

    def __init__(
        self,
        component_config: Optional[Dict[Text, Any]] = None,
        clf = None,
        le = None,
    ) -> None:
        """Construct a new intent classifier using the sklearn framework."""

        super().__init__(component_config)

        if le is not None:
            self.le = le
        else:
            self.le = LabelEncoder()
        self.clf = clf

    @classmethod
    def required_packages(cls) -> List[Text]:
        return ["sklearn"]

    def train(
        self,
        training_data: TrainingData,
        config: Optional[RasaNLUModelConfig] = None,
        **kwargs: Any,
    ) -> None:
        """Train the intent classifier on a data set."""

        labels = [
            example.get("intent") for example in training_data.intent_examples
        ]
        self.le = LabelEncoder()

        y = self.le.fit_transform(labels)
        X = vstack(
            [
                example.get_sparse_features(TEXT)[1].features.tocsr()
                for example in training_data.intent_examples
            ]
        )

        self.clf = LogisticRegression(
            verbose=self.component_config["verbose"],
            class_weight=self.component_config["class_weight"],
            max_iter=self.component_config["max_iter"],
            solver=self.component_config["solver"],

        )

        self.clf.fit(X, y)

    def process(self, message: Message, **kwargs: Any) -> None:
        """Return the most likely intent and its probability for a message."""

        X = message.get_sparse_features(TEXT)[1].features.reshape(1, -1)

        probs = self.clf.predict_proba(X).flatten()
        intents = self.le.inverse_transform(self.clf.classes_)

        ranking = [
            {"name": intent, "confidence": confidence} for intent, confidence in zip(intents, probs)
        ]

        top_intent = max(ranking, key=lambda x:x['confidence'])

        message.set("intent", top_intent, add_to_output=True)
        message.set("intent_ranking", [ranking], add_to_output=True)


    def persist(self, file_name: Text, model_dir: Text) -> Optional[Dict[Text, Any]]:
        """Persist this model into the passed directory."""

        classifier_file_name = file_name + "_classifier.joblib"
        encoder_file_name = file_name + "_encoder.joblib"

        joblib.dump(
            self.le.classes_,
            os.path.join(model_dir, encoder_file_name)
        )
        joblib.dump(
            self.clf,
            os.path.join(model_dir, classifier_file_name)
        )

        return {
            "classifier": classifier_file_name,
            "encoder": encoder_file_name
        }

    @classmethod
    def load(
        cls,
        meta: Dict[Text, Any],
        model_dir: Text,
        model_metadata: Optional[Metadata] = None,
        cached_component: Optional["LRIntentClassifier"] = None,
        **kwargs: Any,
    ) -> "LRIntentClassifier":
        """Loads trained component (see parent class for full docstring)."""

        classifier_file = os.path.join(model_dir, meta.get("classifier"))
        encoder_file = os.path.join(model_dir, meta.get("encoder"))

        classifier = joblib.load(classifier_file)
        classes = joblib.load(encoder_file)

        encoder = LabelEncoder()
        encoder.classes_ = classes

        return cls(meta, classifier, encoder)
