import React, { useState } from "react";

export const ThemeProvider = () => {
  const [darkMode, setDarkMode] = useState(false);
  
  const toggleTheme = () => {
    setDarkMode(!darkMode);
    document.body.className = darkMode ? "light-theme" : "dark-theme";
  };

  return (
    <div className={darkMode ? "dark-theme" : "light-theme"}>
      <button onClick={toggleTheme}>
        {darkMode ? "☀️ Mode Clair" : "🌙 Mode Sombre"}
      </button>
      <h1>🇩🇿 Algeria ERP - Theme {darkMode ? "Sombre" : "Clair"}</h1>
    </div>
  );
};

console.log("🌙 Dark/Light Mode Module ready!");
