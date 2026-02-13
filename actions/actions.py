# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCalculatePrice(Action):

    def name(self) -> Text:
        return "action_calculate_price"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        # Recuperar valores dos slots
        cost_base = float(tracker.get_slot("cost_base"))
        operational_pct = float(tracker.get_slot("operational_pct"))
        tax_pct = float(tracker.get_slot("tax_pct"))
        profit_pct = float(tracker.get_slot("profit_pct"))
        discount_pct = float(tracker.get_slot("discount_pct"))

        # Converter percentuais para decimal
        operational = operational_pct / 100
        tax = tax_pct / 100
        profit = profit_pct / 100
        discount = discount_pct / 100

        # Soma dos percentuais
        total_percentage = operational + tax + profit

        # Cálculo do preço via markup
        price_without_discount = cost_base / (1 - total_percentage)

        # Aplicar desconto
        final_price = price_without_discount * (1 - discount)

        # Resposta do bot
        dispatcher.utter_message(
    text=(
        "📊 Detalhamento do cálculo:\n\n"
        f"• Custo base: R$ {cost_base:.2f}\n"
        f"• Custos operacionais: {operational_pct:.1f}%\n"
        f"• Impostos: {tax_pct:.1f}%\n"
        f"• Margem de lucro: {profit_pct:.1f}%\n"
        f"• Desconto aplicado: {discount_pct:.1f}%\n\n"
        "🧮 Método utilizado: precificação por markup\n\n"
        f"➡️ Preço final calculado: R$ {final_price:.2f}"
    )
)

        return []

