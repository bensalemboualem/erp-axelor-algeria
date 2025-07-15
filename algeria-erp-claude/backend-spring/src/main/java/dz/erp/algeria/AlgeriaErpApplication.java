package dz.erp.algeria;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cache.annotation.EnableCaching;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.scheduling.annotation.EnableScheduling;

/**
 * 🇩🇿 Algeria ERP by Claude - Application principale
 * 
 * ERP nouvelle génération avec:
 * - Agents IA onboard natifs
 * - Workflows N8N intégrés  
 * - Conformité Algeria 100%
 * - Support multilingue (العربية, Français, الدارجة, ⵜⴰⵎⴰⵣⵉⵖⵜ)
 * 
 * @author Claude AI
 * @version 1.0.0
 */
@SpringBootApplication
@EnableCaching
@EnableAsync
@EnableScheduling
public class AlgeriaErpApplication {
    
    public static void main(String[] args) {
        // Configuration système Algeria
        System.setProperty("user.timezone", "Africa/Algiers");
        System.setProperty("file.encoding", "UTF-8");
        System.setProperty("java.awt.headless", "true");
        
        // Message de démarrage
        System.out.println("🇩🇿 =================================");
        System.out.println("🚀 ALGERIA ERP BY CLAUDE - DÉMARRAGE");
        System.out.println("⭐ Version: 1.0.0");
        System.out.println("🌍 Locale: Algeria (ar_DZ)");
        System.out.println("🕐 Timezone: Africa/Algiers");
        System.out.println("💰 Currency: DZD");
        System.out.println("🤖 AI Agents: ENABLED");
        System.out.println("⚙️  N8N Workflows: ENABLED");
        System.out.println("📱 WhatsApp: ENABLED");
        System.out.println("🇩🇿 =================================");
        
        SpringApplication.run(AlgeriaErpApplication.java, args);
    }
}