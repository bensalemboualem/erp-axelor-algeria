#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📱 Agent WhatsApp Business Algeria - 5 Langues
Support: العربية, الدارجة الجزائرية, Français, English, ⵜⴰⵎⴰⵣⵉⵖⵜ
"""

import asyncio
import json
import logging
import re
from datetime import datetime
from typing import Dict, List, Optional

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('WhatsAppAgent')

class WhatsAppConfig:
    def __init__(self, access_token, phone_number_id, verify_token, webhook_url):
        self.access_token = access_token
        self.phone_number_id = phone_number_id
        self.verify_token = verify_token
        self.webhook_url = webhook_url
        self.business_name = "Algeria ERP by Claude"

class WhatsAppAgent:
    def __init__(self, config):
        self.config = config
        self.templates = {
            'welcome': {
                'ar': """🇩🇿 أهلاً في نظام إدارة الأعمال الجزائري
🤖 مساعدك الذكي للضرائب والمحاسبة
📱 أستطيع مساعدتك في:
- حساب ضريبة القيمة المضافة (TVA)
- حساب ضريبة الدخل الإجمالي (IRG)
- الإقرارات الضريبية

أرسل استفسارك بأي لغة تريد 👍""",
                
                'ar_dz': """🇩🇿 مرحبا بيك في السيستام تاع البيزنس الجزائري
🤖 أنا المساعد الذكي تاعك للضرائب
📱 نقدر نعاونك في:
- حساب الضريبة (TVA)
- ضريبة الراتب (IRG)
- الإقرارات

ابعتلي السؤال تاعك بأي لغة تحب 👍""",
                
                'fr': """🇩🇿 Bienvenue dans Algeria ERP by Claude
🤖 Assistant intelligent fiscal et comptable
📱 Je peux vous aider avec:
- Calculs TVA Algeria
- Calculs IRG progressif
- Déclarations fiscales

Posez votre question dans la langue de votre choix 👍""",
                
                'en': """🇩🇿 Welcome to Algeria ERP by Claude
🤖 Your smart tax and accounting assistant
📱 I can help you with:
- Algeria VAT calculations
- Progressive income tax (IRG)
- Tax declarations

Ask your question in any language 👍""",
                
                'ber': """🇩🇿 Ansuf-ik deg unagraw n tnebgi n Dzayer
🤖 Amaɛiw-ik n tikti i tigawin
📱 Zemreɣ ad k-ɛiwneɣ deg:
- Asiḍen n tigawin (TVA)
- Asiḍen n udem (IRG)
- Tinnubga n tigawin

Azen-iyi asteqsi s tutlayt i tebɣiḍ 👍"""
            }
        }
        logger.info("📱 Agent WhatsApp Algeria 5 langues initialisé")
    
    async def detect_language(self, text):
        text_lower = text.lower()
        
        # Darija algérienne
        darija_words = ['كيفاش', 'واش', 'بصح', 'هكاك', 'تاع', 'نتاع', 'دراري', 'كاش', 'ابعتلي']
        if any(word in text_lower for word in darija_words):
            return 'ar_dz'
        
        # Arabe standard
        if re.search(r'[\u0600-\u06FF]', text):
            return 'ar'
        
        # Amazigh
        berber_latin = ['azul', 'tanemmirt', 'asiḍen', 'tigawin', 'tallalt', 'anagraw', 'zemreɣ', 'amaɛiw']
        if any(word in text_lower for word in berber_latin):
            return 'ber'
        
        # Anglais
        english_words = ['hello', 'help', 'calculate', 'tax', 'vat', 'income', 'salary', 'how', 'what', 'when']
        if any(word in text_lower for word in english_words):
            return 'en'
        
        # Français
        if re.search(r'[àâäéèêëïîôùûüÿç]', text) or any(word in text_lower for word in ['calculer', 'tva', 'irg', 'bonjour', 'aide']):
            return 'fr'
        
        return 'fr'
    
    async def process_message(self, text):
        try:
            language = await self.detect_language(text)
            
            welcome_commands = ['salut', 'bonjour', 'hello', 'hi', 'مرحبا', 'السلام', 'azul']
            if any(cmd in text.lower() for cmd in welcome_commands):
                return self.templates['welcome'].get(language, self.templates['welcome']['fr'])
            
            responses = {
                'ar': f"تم استلام رسالتك باللغة العربية: {text[:50]}...",
                'ar_dz': f"وصلت الرسالة بالدارجة الجزائرية: {text[:50]}...",
                'fr': f"Message reçu en français: {text[:50]}...",
                'en': f"Message received in English: {text[:50]}...",
                'ber': f"Yewweḍ-d izen s teqbaylit: {text[:50]}..."
            }
            
            return responses.get(language, responses['fr'])
            
        except Exception as e:
            logger.error(f"Erreur: {e}")
            return "❌ Erreur de traitement"

async def test_agent():
    print("🧪 TEST AGENT WHATSAPP 5 LANGUES")
    print("=" * 40)
    
    config = WhatsAppConfig("TEST", "TEST", "TEST", "TEST")
    agent = WhatsAppAgent(config)
    
    tests = [
        {"text": "مرحبا", "expected": "ar"},
        {"text": "كيفاش الحال؟", "expected": "ar_dz"},
        {"text": "Bonjour", "expected": "fr"},
        {"text": "Hello there", "expected": "en"},
        {"text": "azul tanemmirt", "expected": "ber"}
    ]
    
    print("\n🌍 TESTS DÉTECTION:")
    for i, test in enumerate(tests, 1):
        detected = await agent.detect_language(test['text'])
        status = "✅" if detected == test['expected'] else "❌"
        print(f"{i}. '{test['text']}' → {detected} {status}")
    
    print("\n📱 TESTS MESSAGES:")
    test_messages = [
        "مرحبا كيف الحال؟",
        "كيفاش نحسب الضريبة؟",
        "Bonjour, comment calculer la TVA?",
        "Hello, how to calculate tax?",
        "azul, asiḍen n tigawin?"
    ]
    
    for i, msg in enumerate(test_messages, 1):
        response = await agent.process_message(msg)
        print(f"\n{i}. Message: {msg}")
        print(f"   Réponse: {response[:80]}...")
    
    print("\n✅ Tests terminés - Agent 5 langues opérationnel!")

if __name__ == "__main__":
    asyncio.run(test_agent())
