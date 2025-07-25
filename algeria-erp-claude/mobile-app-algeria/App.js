import React from "react";
import { View, Text, TouchableOpacity } from "react-native";

export default function AlgeriaERPApp() {
  return (
    <View style={{flex: 1, padding: 20, backgroundColor: "#1a472a"}}>
      <Text style={{fontSize: 24, color: "white", textAlign: "center"}}>
        🇩🇿 Algeria ERP Mobile
      </Text>
      <TouchableOpacity style={{backgroundColor: "#28a745", padding: 15, marginTop: 20}}>
        <Text style={{color: "white", textAlign: "center"}}>
          💰 Calculer TVA
        </Text>
      </TouchableOpacity>
      <TouchableOpacity style={{backgroundColor: "#dc3545", padding: 15, marginTop: 10}}>
        <Text style={{color: "white", textAlign: "center"}}>
          📊 Mode Offline
        </Text>
      </TouchableOpacity>
    </View>
  );
}

console.log("📱 Mobile App Algeria ERP ready!");
