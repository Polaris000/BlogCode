from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHandleProvidedInfo(Action):
    def name(self):
        return "action_handle_provided_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        name = tracker.get_slot('name')
        email = tracker.get_slot('email')

        buttons = [
            {
                'title': "That's all",
                'payload': '/goodbye'
            },
            {
                'title': 'Add More Information',
                'payload': '/supply_contact_info'
            },
        ]

        # if name and email are provided, show
        # the user further options

        if name and email:
            dispatcher.utter_message(
                text="Thanks for the information!"\
                    "What would you like to do next?"
            )
            dispatcher.utter_message(buttons=buttons)
        
        # if valid information isn't provided,
        # ask the user for the information
        # again.
        elif name:
            dispatcher.utter_message(text="Invalid data.")
            dispatcher.utter_message(response="utter_ask_for_email")

        elif email:
            dispatcher.utter_message(text="Invalid data.")
            dispatcher.utter_message(response="utter_ask_for_name")

        return []
