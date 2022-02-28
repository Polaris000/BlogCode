## Failing Gracefuuly

This is the example bot to demonstrate Rasa's support for custom components--specifically, custom intent classifiers.. Its sample code from the post "How do Chatbots Understand?", which can be found on [Medium.com](https://towardsdatascience.com/how-do-chatbots-understand-87227f9f96a7).

It builds upon our existing example, which can be found [here](../RasaChatbot_v2).

### Improvements over Chatbot v2
- addition of fallback mechanisms
- addition of simple, single stage and two stage fallback mechanisms
- support for asking the user to rephrase themselves
- support for asking the user to select from some suggestions
- custom intent classifier

### An example
**Logistic Regression classifier**
```
👨 : hey (should go to intent "greet")

prediction:
-----------
Received user message 'hey' with intent '{'name': 'greet', 'confidence': 0.9377497415166074}' and entities '[]'

🤖 : Hello! Could you please provide your contact information?

```


### Contents
This project follows the format of a standard Rasa project. There's a directory called `data` for training data like nlu, stories, and rules.

There's a directory called `actions`, which contains all your custom actions.

You'll also find the `domain.yml` file, which mentions all your intents, entities, slots, responses and actions.

Finally, there's the `config.yml` file, which specifies the components your bot is comprised of.

The config file has a modification compared to the previous versions of this bot: a custom component. It'll look like this now:
```
  ..
  ..
  - name: DIETClassifier
    entity_recognition: true
    intent_classification: false
    epochs: 5

  - name: lr_classifier.LRIntentClassifier
    max_iter: 100
  ..
  ..
```
You can see that we've also added a `intent_classification: false` field under the `DIETClassifier`, meaning that we'll be using it only for entity extraction, since our custom componenent will be doing the intent classification.

The code for the custom intent classifier which is based on the logistic regression classifier is located in `lr_classifier.py`.

Lastly, we look at the `results` folder. It contains an evaluation of the performance of our bot's intent classification and entity extraction. There aren't any results for the Core part of our bot since we don't have any test cases for that. 

### Usage
1. Clone this repo
2. Navigate to the RasaChatbot directory
3. Install rasa>=2.6.2 in an env.

Modify the files in `data/` or the `domain.yml` file to play around.

### Training the bot
#### Validating the data
Before training the bot, a good practice is to check for any inconsistencies in the stories and rules, though in a project this simple, it's unlikely to occur.
```
$ rasa data validate
```

#### Training
To train the bot, we simply use the rasa train command. We'll provide a name to the model for better organization, but it's not necessary.
```
$ rasa train --fixed-model-name logistic_regression_classifier_model
```

### Chatting with the bot
To test your bot, open a new terminal window and start a rasa shell session.
```
$ rasa shell
```
This will let you chat with your bot in your terminal. If you want a more interactive UI and a little more debugging information like what intents were identified and what entities were extracted, you can use Rasa X.

### Playing with the Logistic Regression classifier
The code for the custom intent classifier which is based on the logistic regression classifier is located in `lr_classifier.py`. You can play around with the different parameters by modifying the fields in `config.yml`. You can also plug in your own sklearn models directly. Simply change the model used in the `train` method in `lr_classifier.py` to, say, `MultinomialNB` to try the Naive Bayes sklearn classifier.

After this, retrain the bot to test it. As always, modify the files in `data` to add more intents or more data to existing intents. Keep in mind that this is a custom intent classifier, so it won't extract entities nor will it affect the response the bot gives, directly.

### Testing
Rasa provides support for evaluating both the NLU and the Core of your bot. All we have to do is create some test data and run rasa test . To run the  tests, execute:
```
rasa test
```
The `results` folder will be updated. 

---

You can find me on medium [here](https://polaris000.medium.com).
