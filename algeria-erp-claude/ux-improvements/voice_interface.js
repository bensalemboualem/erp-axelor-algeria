class VoiceInterface {
  constructor() {
    this.recognition = new webkitSpeechRecognition();
    this.recognition.lang = "ar-DZ";
    console.log("🎤 Voice Interface Algeria ERP ready!");
  }
  
  startListening() {
    this.recognition.start();
    console.log("🎧 Listening... Say: Hey Algeria ERP");
  }
  
  processCommand(command) {
    if (command.includes("calcule TVA")) {
      return "💰 Calcul TVA en cours...";
    }
    return "❓ Commande non reconnue";
  }
}

const voice = new VoiceInterface();
console.log("🎤 Voice Interface Module ready!");
