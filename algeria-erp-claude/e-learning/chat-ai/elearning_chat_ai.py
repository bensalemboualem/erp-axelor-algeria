import asyncio
import json
from datetime import datetime

class ELearningChatAI:
    def __init__(self):
        self.knowledge_base = {
            "fiscal_algeria": {
                "tva": "TVA Algeria: 19% normale, 9% réduite, 0% export",
                "irg": "IRG progressif: 0-120k (0%), 120-360k (23%), 360k-1.44M (27%), +1.44M (35%)"
            },
            "social_algeria": {
                "cnas": "CNAS: Sécurité sociale salariés, cotisations employeur 26%",
                "casnos": "CASNOS: Non-salariés, cotisation 15% revenus"
            }
        }
        print("🧠 Chat IA Formateur Algeria initialisé")
    
    async def process_question(self, question, language="fr"):
        if "tva" in question.lower():
            return "💰 TVA Algeria: Taux normal 19%, réduit 9%, export 0%. Questions?"
        elif "irg" in question.lower():
            return "💼 IRG progressif Algeria avec abattements famille. Exemple?"
        else:
            return "📚 Posez votre question sur fiscal/social Algeria. Je suis là pour vous former!"

if __name__ == "__main__":
    chat = ELearningChatAI()
    print("✅ Chat IA E-Learning opérationnel")
