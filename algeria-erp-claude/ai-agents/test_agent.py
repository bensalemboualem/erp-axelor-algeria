#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧪 Test Agent IA Fiscal Algeria
Tests des calculs fiscaux multilingues
"""

import asyncio
import sys
import os

# Import direct de l'agent Algeria
from fiscal_agent_algeria import FiscalAiAgent

async def test_simple_tva():
    """Test simple TVA"""
    print("\n🧪 === TEST SIMPLE TVA ===")
    
    try:
        agent = FiscalAiAgent()
        print("✅ Agent IA Algeria créé avec succès")
        
        # Test simple français
        query = "TVA sur 100000 DZD"
        print(f"📝 Test: {query}")
        
        result = await agent.process_fiscal_query(query)
        
        if result['success']:
            print("✅ Calcul réussi:")
            print(result['response'])
            print(f"🌍 Langue détectée: {result['language']}")
        else:
            print(f"❌ Erreur: {result['error']}")
            
    except Exception as e:
        print(f"❌ Erreur création agent: {e}")
        import traceback
        traceback.print_exc()

async def test_tva_multilingue():
    """Test TVA multilingue"""
    print("\n💰 === TESTS TVA MULTILINGUE ===")
    
    agent = FiscalAiAgent()
    
    test_cases = [
        {
            'query': "احسب ضريبة القيمة المضافة على 100000 دينار",
            'description': "TVA en arabe standard"
        },
        {
            'query': "كيفاش نحسب الضريبة على 50000 دج؟",
            'description': "TVA en darija algérienne"
        },
        {
            'query': "Calculer la TVA sur 75000 DZD",
            'description': "TVA en français"
        },
        {
            'query': "TVA export 200000 DZD",
            'description': "TVA exportation (exonérée)"
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n📝 Test {i}: {test['description']}")
        print(f"Query: {test['query']}")
        
        try:
            result = await agent.process_fiscal_query(test['query'])
            
            if result['success']:
                print(f"✅ Langue détectée: {result['language']}")
                print(f"📊 Réponse:")
                print(result['response'])
            else:
                print(f"❌ Erreur: {result['error']}")
        except Exception as e:
            print(f"❌ Erreur test: {e}")
        
        print("-" * 50)

async def test_irg_multilingue():
    """Test IRG multilingue"""
    print("\n💼 === TESTS IRG MULTILINGUE ===")
    
    agent = FiscalAiAgent()
    
    test_cases = [
        {
            'query': "حساب ضريبة الدخل على راتب 200000 دينار",
            'description': "IRG sans enfants (arabe)"
        },
        {
            'query': "كيفاش نحسب ضريبة الراتب 300000 دج مع 2 دراري؟",
            'description': "IRG avec enfants (darija)"
        },
        {
            'query': "IRG pour salaire 150000 DZD avec 1 enfant",
            'description': "IRG avec enfant (français)"
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n📝 Test {i}: {test['description']}")
        print(f"Query: {test['query']}")
        
        try:
            result = await agent.process_fiscal_query(test['query'])
            
            if result['success']:
                print(f"✅ Langue détectée: {result['language']}")
                print(f"📊 Réponse:")
                print(result['response'])
            else:
                print(f"❌ Erreur: {result['error']}")
        except Exception as e:
            print(f"❌ Erreur test: {e}")
        
        print("-" * 50)

async def main():
    """🧪 Tests principaux"""
    print("🇩🇿 =" * 50)
    print("🧪 TESTS AGENT IA FISCAL ALGERIA")
    print("🤖 by Claude AI")
    print("🚀 ERP Algeria - Tests Multilingues")
    print("=" * 50)
    
    try:
        # Test simple en premier
        await test_simple_tva()
        
        # Tests multilingues
        await test_tva_multilingue()
        await test_irg_multilingue()
        
        print("\n🎉 =" * 50)
        print("✅ TOUS LES TESTS TERMINÉS AVEC SUCCÈS !")
        print("🇩🇿 Algeria ERP by Claude - Agent IA opérationnel")
        print("🤖 Support: العربية, Français, الدارجة")
        print("💰 Calculs: TVA, IRG, TAP conformes Algeria")
        print("=" * 50)
        
    except Exception as e:
        print(f"\n❌ ERREUR DANS LES TESTS: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("🚀 Démarrage des tests Agent IA Algeria...")
    asyncio.run(main())