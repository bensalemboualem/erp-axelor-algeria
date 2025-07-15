import asyncio
import logging
from datetime import datetime

class MultiPlatformOrchestrator:
    def __init__(self):
        self.platforms = {
            'whatsapp': None,
            'telegram': None,
            'signal': None
        }
        self.user_preferences = {}
        print("🎯 Orchestrateur Multi-Plateformes Algeria initialisé")
    
    def register_platform(self, platform_name, agent):
        self.platforms[platform_name] = agent
        print(f"✅ {platform_name.title()} Agent enregistré")
    
    def set_user_preference(self, user_id, preferred_platform):
        self.user_preferences[user_id] = preferred_platform
        print(f"📱 Utilisateur {user_id} préfère {preferred_platform}")
    
    async def send_smart_message(self, user_id, message, message_type="normal"):
        platform = self.user_preferences.get(user_id, 'telegram')
        agent = self.platforms.get(platform)
        
        if not agent:
            print(f"❌ Agent {platform} non disponible")
            return False
        
        if message_type == "secure" and platform == "signal":
            return await agent.send_secure_data(user_id, "ERP Data", message)
        else:
            return await agent.send_message(user_id, message)
    
    async def broadcast_notification(self, message, platforms=None):
        if platforms is None:
            platforms = ['telegram', 'signal']
        
        results = {}
        for platform in platforms:
            agent = self.platforms.get(platform)
            if agent:
                if platform == 'telegram':
                    results[platform] = await agent.send_message("@all", message)
                elif platform == 'signal':
                    results[platform] = await agent.send_message("+213ALL", message)
        
        return results
    
    async def handle_fiscal_calculation(self, user_id, calc_type, amount, language="fr"):
        # Simulation calcul fiscal
        if calc_type == "tva":
            tva_amount = amount * 0.19
            result = f"💰 TVA Algeria: {amount:,.0f} DZD + {tva_amount:,.0f} DZD = {amount + tva_amount:,.0f} DZD"
        elif calc_type == "irg":
            irg_amount = max(0, (amount - 120000) * 0.23) if amount > 120000 else 0
            result = f"💼 IRG Algeria: {amount:,.0f} DZD - {irg_amount:,.0f} DZD = {amount - irg_amount:,.0f} DZD net"
        else:
            result = "❓ Type de calcul non reconnu"
        
        await self.send_smart_message(user_id, result)
        return result

async def test_orchestrator():
    print("🧪 TEST ORCHESTRATEUR MULTI-PLATEFORMES")
    print("=" * 50)
    
    # Simulation agents
    class MockAgent:
        def __init__(self, name):
            self.name = name
        async def send_message(self, recipient, text):
            return f"📤 {self.name}: {text[:50]}..."
        async def send_secure_data(self, recipient, data_type, content):
            return f"🔒 {self.name} Secure: {content[:50]}..."
    
    orchestrator = MultiPlatformOrchestrator()
    
    # Enregistrer agents simulés
    orchestrator.register_platform('telegram', MockAgent('Telegram'))
    orchestrator.register_platform('signal', MockAgent('Signal'))
    orchestrator.register_platform('whatsapp', MockAgent('WhatsApp'))
    
    # Configurer préférences utilisateurs
    orchestrator.set_user_preference('+213555123456', 'telegram')
    orchestrator.set_user_preference('+213555789012', 'signal')
    
    # Tests
    print("\n📱 Test envoi intelligent:")
    await orchestrator.send_smart_message('+213555123456', 'Message via plateforme préférée')
    
    print("\n🔒 Test message sécurisé:")
    await orchestrator.send_smart_message('+213555789012', 'Données confidentielles', 'secure')
    
    print("\n💰 Test calcul fiscal:")
    await orchestrator.handle_fiscal_calculation('+213555123456', 'tva', 100000, 'fr')
    await orchestrator.handle_fiscal_calculation('+213555789012', 'irg', 300000, 'fr')
    
    print("\n📢 Test broadcast:")
    await orchestrator.broadcast_notification('🇩🇿 Mise à jour ERP Algeria disponible!')
    
    print("\n✅ Orchestrateur multi-plateformes opérationnel!")

if __name__ == "__main__":
    asyncio.run(test_orchestrator())
