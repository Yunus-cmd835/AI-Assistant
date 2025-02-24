import faiss
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import logging
import warnings

# Suppress deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class ActionProductSearch(Action):
    def name(self) -> str:
        return "action_product_search"

    def run(self, dispatcher, tracker, domain):
        # Logic to search for products
        dispatcher.utter_message(
            text="""Here are some options for wireless headphones under $100:
            1. Sony WH-CH510 - Lightweight with great sound quality.
            2. JBL Tune 500BT - Comfortable fit with long battery life.
            3. Anker Soundcore Life Q10 - Affordable with deep bass."""
        )
        return []


class ActionOrderTracking(Action):
    def name(self) -> str:
        return "action_order_tracking"

    def run(self, dispatcher, tracker, domain):
        # Retrieve the order_id slot
        order_id = tracker.get_slot("order_id")
        
        if order_id:
            # Logic to track an order
            dispatcher.utter_message(
                text=f"Your order # 12345 is currently in transit and is expected to arrive by January 20th. Thank you for shopping with us!"
            )
        else:
            # If order_id slot is not set, ask the user to provide it
            dispatcher.utter_message(
                text="Sorry, I couldn't find your order. Could you please provide your order ID?"
            )
        
        return [SlotSet("order_id", "12345")]


class ActionDefaultFallback(Action):
    def name(self) -> str:
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Sorry, I didn't quite get that. Could you rephrase?")
        return []
