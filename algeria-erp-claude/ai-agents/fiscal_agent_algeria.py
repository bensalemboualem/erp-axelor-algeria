#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🇩🇿 Agent IA Fiscal Algeria - Version Claude avec support Amazigh
Traitement intelligent des calculs fiscaux algériens multilingues
Support: العربية, Français, الدارجة, ⵜⴰⵎⴰⵣⵉⵖⵜ
"""

import asyncio
import json
import logging
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, List, Optional
import re

# Configuration logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger('FiscalAiAgent')

class FiscalAiAgent:
    """🧠 Agent IA pour calculs fiscaux algériens intelligents - Support 4 langues"""
    
    def __init__(self):
        # Base de connaissances fiscales Algeria 2025
        self.tax_knowledge = {
            'tva_rates': {
                'normale': Decimal('19.00'),
                'reduite': Decimal('9.00'),
                'exoneree': Decimal('0.00')
            },
            'irg_brackets': [
                {'min': 0, 'max': 120000, 'rate': Decimal('0.00')},
                {'min': 120001, 'max': 360000, 'rate': Decimal('23.00')},
                {'min': 360001, 'max': 1440000, 'rate': Decimal('27.00')},
                {'min': 1440001, 'max': float('inf'), 'rate': Decimal('35.00')}
            ],
            'abattements_irg': {
                'base': Decimal('10000'),
                'par_enfant': Decimal('2500'),
                'handicape_multiplier': Decimal('1.20')
            }
        }
        
        # Patterns reconnaissance langue étendus
        self.language_patterns = {
            'ar_dz': ['كيفاش', 'واش', 'بصح', 'هكاك', 'ديال', 'نتاع', 'ماشي', 'برك', 'دراري', 'ولاد'],
            'ar': r'[\u0600-\u06FF]',
            'fr': r'[àâäéèêëïîôùûüÿç]',
            'ber': {
                'tifinagh': r'[\u2D30-\u2D7F]',  # Script Tifinagh
                'latin_keywords': [
                    # Mots amazigh courants
                    'deg', 'n', 'akken', 'ma', 'neɣ', 'ad', 'ur', 'ara',
                    'amek', 'melmi', 'anda', 'ayenna', 'wid', 'tid',
                    # Nombres
                    'yiwen', 'sin', 'kraḍ', 'kkuẓ', 'semmus', 'sḍis',
                    # Calculs/argent
                    'asiḍen', 'tigawin', 'azref', 'idrimen', 'tamurt',
                    # Berbère Kabyle
                    'tizi', 'adrar', 'aman', 'tafukt', 'aggur',
                    # Chaoui
                    'amellal', 'aberkan', 'azegzaw', 'amellal',
                    # Mozabite
                    'taghardayt', 'bani', 'mzab',
                    # Targui
                    'tamashek', 'kel', 'akal'
                ]
            }
        }
        
        logger.info("🇩🇿 Agent Fiscal Algeria initialisé - Support 4 langues")
    
    async def process_fiscal_query(self, query: str, context: Dict = None) -> Dict:
        """🧠 Traitement intelligent des requêtes fiscales multilingues"""
        try:
            # 1. Détection de langue
            language = await self.detect_language(query)
            
            # 2. Extraction d'entités (montants, taux, etc.)
            entities = await self.extract_entities(query, language)
            
            # 3. Détermination du type de calcul
            calc_type = await self.determine_calculation_type(query, language)
            
            # 4. Traitement selon le type
            if calc_type == 'tva':
                result = await self.calculate_tva_intelligent(entities)
            elif calc_type == 'irg':
                result = await self.calculate_irg_intelligent(entities)
            else:
                result = await self.provide_general_help(language)
            
            # 5. Formatage réponse selon la langue
            response = await self.format_response(result, language)
            
            return {
                'success': True,
                'response': response,
                'language': language,
                'calculation_type': calc_type,
                'entities': entities,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Erreur traitement: {e}")
            return {
                'success': False,
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    async def detect_language(self, text: str) -> str:
        """🌍 Détection automatique de la langue - Support Amazigh"""
        text_lower = text.lower()
        
        # 1. Détection Tifinagh (script amazigh natif)
        if re.search(self.language_patterns['ber']['tifinagh'], text):
            return 'ber'
        
        # 2. Détection amazigh en caractères latins
        ber_score = sum(1 for word in self.language_patterns['ber']['latin_keywords'] 
                       if word in text_lower)
        if ber_score >= 1:
            return 'ber'
        
        # 3. Détection darija algérienne (priorité haute)
        darija_count = sum(1 for word in self.language_patterns['ar_dz'] 
                          if word in text_lower)
        if darija_count >= 1:
            return 'ar_dz'
        
        # 4. Détection arabe standard
        if re.search(self.language_patterns['ar'], text):
            return 'ar'
        
        # 5. Détection français
        if re.search(self.language_patterns['fr'], text) or any(word in text_lower for word in ['calculer', 'tva', 'irg']):
            return 'fr'
        
        return 'fr'  # Par défaut
    
    async def extract_entities(self, query: str, language: str) -> Dict:
        """🔍 Extraction d'entités (montants, enfants, etc.) - Support Amazigh"""
        entities = {}
        
        # Extraction montants (DZD, DA, dinars, idrimen)
        amount_patterns = [
            r'(\d{1,3}(?:[\s,.]?\d{3})*(?:[.,]\d{2})?)\s*(?:dzd|da|dinar|دج|دينار|idrimen)',
            r'(\d{1,3}(?:[\s,.]?\d{3})*(?:[.,]\d{2})?)'
        ]
        
        for pattern in amount_patterns:
            matches = re.findall(pattern, query.lower(), re.IGNORECASE)
            if matches:
                amount_str = matches[0].replace(' ', '').replace(',', '')
                try:
                    entities['amount'] = float(amount_str)
                    break
                except ValueError:
                    continue
        
        # Extraction nombre d'enfants - Support Amazigh
        children_patterns = {
            'ar': r'(\d+)\s*(?:أطفال|أولاد|طفل)',
            'ar_dz': r'(\d+)\s*(?:دراري|ولاد|طفل)',
            'fr': r'(\d+)\s*(?:enfants?|enfant)',
            'ber': r'(\d+)\s*(?:arrac|mmi|tarwa|uqcic)'  # enfants en amazigh
        }
        
        if language in children_patterns:
            children_matches = re.findall(children_patterns[language], query)
            if children_matches:
                entities['children'] = int(children_matches[0])
        
        # Détection export/zone franche - Support Amazigh
        export_keywords = {
            'ar': ['تصدير', 'صادرات'],
            'ar_dz': ['تصدير', 'صادرات'],
            'fr': ['export', 'exportation'],
            'ber': ['asifeḍ', 'tufɣa', 'azen']  # export/envoi en amazigh
        }
        
        zone_keywords = {
            'ar': ['منطقة', 'حرة'],
            'ar_dz': ['منطقة', 'حرة'],
            'fr': ['zone', 'franche'],
            'ber': ['tamnaḍt', 'tilelli', 'akal']  # zone libre en amazigh
        }
        
        if any(kw in query.lower() for kw in export_keywords.get(language, [])):
            entities['is_export'] = True
        
        if any(kw in query.lower() for kw in zone_keywords.get(language, [])):
            entities['is_zone_franche'] = True
        
        return entities
    
    async def determine_calculation_type(self, query: str, language: str) -> str:
        """🎯 Détermination du type de calcul - Support Amazigh"""
        query_lower = query.lower()
        
        # Keywords TVA - Support Amazigh
        tva_keywords = {
            'ar': ['ضريبة', 'قيمة', 'مضافة'],
            'ar_dz': ['ضريبة', 'تاع', 'البيع'],
            'fr': ['tva', 'taxe', 'valeur', 'ajoutée'],
            'ber': ['tigawin', 'azal', 'tmerci', 'asiḍen']  # taxes/valeur/commerce en amazigh
        }
        
        # Keywords IRG - Support Amazigh
        irg_keywords = {
            'ar': ['ضريبة', 'دخل', 'راتب', 'أجر'],
            'ar_dz': ['ضريبة', 'الراتب', 'الأجر'],
            'fr': ['irg', 'impôt', 'revenu', 'salaire'],
            'ber': ['tigawin', 'n', 'udem', 'azref', 'ksebt']  # impôt du travail/salaire en amazigh
        }
        
        # Score TVA
        tva_score = sum(1 for word in tva_keywords.get(language, tva_keywords['fr']) 
                       if word in query_lower)
        
        # Score IRG
        irg_score = sum(1 for word in irg_keywords.get(language, irg_keywords['fr']) 
                       if word in query_lower)
        
        if tva_score > irg_score:
            return 'tva'
        elif irg_score > 0:
            return 'irg'
        else:
            return 'general'
    
    async def calculate_tva_intelligent(self, entities: Dict) -> Dict:
        """💰 Calcul TVA intelligent"""
        amount = entities.get('amount', 0)
        is_export = entities.get('is_export', False)
        is_zone_franche = entities.get('is_zone_franche', False)
        
        # Détermination du taux
        if is_export or is_zone_franche:
            rate = self.tax_knowledge['tva_rates']['exoneree']
            reason = "Export" if is_export else "Zone franche"
        else:
            rate = self.tax_knowledge['tva_rates']['normale']  # 19% par défaut
            reason = "Taux normal"
        
        # Calcul
        tva_amount = Decimal(str(amount)) * rate / Decimal('100')
        tva_amount = tva_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        total_ttc = Decimal(str(amount)) + tva_amount
        
        return {
            'type': 'tva_calculation',
            'amount_ht': amount,
            'tva_rate': float(rate),
            'tva_amount': float(tva_amount),
            'amount_ttc': float(total_ttc),
            'currency': 'DZD',
            'reason': reason
        }
    
    async def calculate_irg_intelligent(self, entities: Dict) -> Dict:
        """💼 Calcul IRG intelligent"""
        salary = entities.get('amount', 0)
        children = entities.get('children', 0)
        
        # Calcul abattements
        abattements = self.tax_knowledge['abattements_irg']['base']
        abattements += Decimal(str(children)) * self.tax_knowledge['abattements_irg']['par_enfant']
        
        # Base imposable
        base_imposable = max(Decimal(str(salary)) - abattements, Decimal('0'))
        
        # Calcul IRG progressif
        irg_amount = Decimal('0')
        
        for bracket in self.tax_knowledge['irg_brackets']:
            if base_imposable <= bracket['min']:
                continue
            
            # Montant dans cette tranche
            if bracket['max'] == float('inf'):
                amount_in_bracket = base_imposable - Decimal(str(bracket['min']))
            else:
                amount_in_bracket = min(base_imposable, Decimal(str(bracket['max']))) - Decimal(str(bracket['min']))
            
            if amount_in_bracket > 0:
                bracket_irg = amount_in_bracket * bracket['rate'] / Decimal('100')
                irg_amount += bracket_irg
        
        irg_amount = irg_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        net_salary = Decimal(str(salary)) - irg_amount
        
        return {
            'type': 'irg_calculation',
            'gross_salary': salary,
            'abattements': float(abattements),
            'taxable_base': float(base_imposable),
            'irg_amount': float(irg_amount),
            'net_salary': float(net_salary),
            'children': children,
            'currency': 'DZD'
        }
    
    async def format_response(self, result: Dict, language: str) -> str:
        """📝 Formatage selon la langue - Support Amazigh complet"""
        
        if result['type'] == 'tva_calculation':
            templates = {
                'ar': """💰 حساب ضريبة القيمة المضافة:
المبلغ بدون ضريبة: {amount_ht:,.2f} دج
معدل الضريبة: {tva_rate}%
ضريبة القيمة المضافة: {tva_amount:,.2f} دج
المبلغ الإجمالي: {amount_ttc:,.2f} دج""",
                
                'ar_dz': """💰 حساب الضريبة:
المبلغ بلا ضريبة: {amount_ht:,.2f} دج
نسبة الضريبة: {tva_rate}%
الضريبة: {tva_amount:,.2f} دج
المجموع: {amount_ttc:,.2f} دج""",
                
                'fr': """💰 Calcul TVA Algeria:
Montant HT: {amount_ht:,.2f} DZD
Taux TVA: {tva_rate}%
Montant TVA: {tva_amount:,.2f} DZD
Montant TTC: {amount_ttc:,.2f} DZD""",
                
                'ber': """💰 Asiḍen n tigawin:
Azal war tigawin: {amount_ht:,.2f} DZD
Aḍris n tigawin: {tva_rate}%
Tigawin: {tva_amount:,.2f} DZD
Azal s tigawin: {amount_ttc:,.2f} DZD"""
            }
            
            template = templates.get(language, templates['fr'])
            return template.format(**result)
        
        elif result['type'] == 'irg_calculation':
            templates = {
                'ar': """💼 حساب ضريبة الدخل الإجمالي:
الراتب الإجمالي: {gross_salary:,.2f} دج
الإعفاءات: {abattements:,.2f} دج
ضريبة الدخل: {irg_amount:,.2f} دج
الراتب الصافي: {net_salary:,.2f} دج
عدد الأطفال: {children}""",
                
                'ar_dz': """💼 حساب ضريبة الراتب:
الراتب الكامل: {gross_salary:,.2f} دج
التخفيضات: {abattements:,.2f} دج
الضريبة: {irg_amount:,.2f} دج
الراتب الصافي: {net_salary:,.2f} دج
عدد الدراري: {children}""",
                
                'fr': """💼 Calcul IRG Algeria:
Salaire brut: {gross_salary:,.2f} DZD
Abattements: {abattements:,.2f} DZD
IRG: {irg_amount:,.2f} DZD
Salaire net: {net_salary:,.2f} DZD
Enfants: {children}""",
                
                'ber': """💼 Asiḍen n tigawin n udem:
Azref amellal: {gross_salary:,.2f} DZD
Isenkisen: {abattements:,.2f} DZD
Tigawin n udem: {irg_amount:,.2f} DZD
Azref d uzayad: {net_salary:,.2f} DZD
Arrac: {children}"""
            }
            
            template = templates.get(language, templates['fr'])
            return template.format(**result)
        
        elif result['type'] == 'general_help':
            return result['message']
        
        return json.dumps(result, ensure_ascii=False, indent=2)
    
    async def provide_general_help(self, language: str) -> Dict:
        """❓ Aide générale - Support Amazigh"""
        help_messages = {
            'ar': 'يمكنني مساعدتك في حساب الضرائب الجزائرية (TVA, IRG)',
            'ar_dz': 'نقدر نعاونك في الضرائب تاع الجزائر',
            'fr': 'Je peux vous aider avec les calculs fiscaux algériens',
            'ber': 'Zemreɣ ad k-ɛiwneɣ deg tigawin n Dzayer (TVA, IRG)'
        }
        
        return {
            'type': 'general_help',
            'message': help_messages.get(language, help_messages['fr'])
        }

# Test de l'agent avec support Amazigh
async def test_agent_amazigh():
    """🧪 Test de l'agent fiscal avec support Amazigh"""
    agent = FiscalAiAgent()
    
    test_queries = [
        # Tests Amazigh
        "Asiḍen n tigawin deg 100000 idrimen",  # Calcul TVA en amazigh
        "Tigawin n udem azref 200000 s sin n mmi",  # IRG avec enfants
        "Amek ara asiḍneɣ tigawin deg tamurt n Dzayer?",  # Comment calculer en amazigh
        
        # Tests existants
        "احسب ضريبة القيمة المضافة على 100000 دينار",
        "كيفاش نحسب الضريبة على راتب 200000 دج؟",
        "Calculer la TVA sur 150000 DZD",
        "IRG pour salaire 300000 DZD avec 2 enfants"
    ]
    
    print("🧪 TEST AGENT FISCAL ALGERIA - SUPPORT AMAZIGH")
    print("=" * 50)
    print("🌍 Langues supportées: العربية, Français, الدارجة, ⵜⴰⵎⴰⵣⵉⵖⵜ")
    print("=" * 50)
    
    for query in test_queries:
        print(f"\n📝 Query: {query}")
        result = await agent.process_fiscal_query(query)
        if result['success']:
            print(f"✅ Langue détectée: {result['language']}")
            print(f"📊 Réponse:")
            print(result['response'])
        else:
            print(f"❌ Erreur: {result['error']}")
        print("-" * 40)

if __name__ == "__main__":
    asyncio.run(test_agent_amazigh())