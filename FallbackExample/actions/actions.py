from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted, ConversationPaused


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

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):
        # output a message saying that the conversation will now be
        # continued by a human.

        message = "Sorry, couldn't understand that! Let me connect you to a human..."
        dispatcher.utter_message(text=message)

        # pause tracker
        # undo last user interaction
        return [ConversationPaused(), UserUtteranceReverted()]

class ActionDefaultAskAffirmation(Action):
    def name(self):
        return "action_default_ask_affirmation"

    async def run(self, dispatcher, tracker, domain):
        # select the top three intents from the tracker        
        # ignore the first one -- nlu fallback
        predicted_intents = tracker.latest_message["intent_ranking"][1:4]
        # A prompt asking the user to select an option
        message = "Sorry! What do you want to do?"
        # a mapping between intents and user friendly wordings
        intent_mappings = {
            "supply_contact_info": "Supply Contact Information",
            "affirm": "Agree",
            "deny": "Disagree",
            "greet": "Say Hi!",
            "goodbye": "End the conversation"
        }
        # show the top three intents as buttons to the user
        buttons = [
            {
                "title": intent_mappings[intent['name']],
                "payload": "/{}".format(intent['name'])
            }
            for intent in predicted_intents
        ]
        # add a "none of these button", if the user doesn't
        # agree when any suggestion
        buttons.append({
            "title": "None of These",
            "payload": "/out_of_scope"
        })
        dispatcher.utter_message(text=message, buttons=buttons)
        return []