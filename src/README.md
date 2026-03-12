# Lilith Notepad

A highly immersive, full-screen web notepad application featuring a functional, gothic Ouija board virtual keyboard.

## Overview
Lilith Notepad transforms your browser into an atmospheric, dark-themed writing environment. Every keystroke brings the board to life, as a planchette smoothly glides across the screen to pinpoint the character you are channeling. It serves seamlessly as a distraction-free notepad with a unique aesthetic flair.

## Features
- **Interactive Planchette Animation:** The pointer dynamically animates to the exact correct location for letters, numbers, and punctuation using a precise mathematical arc implementation.
- **Dual Input Modes:** Click directly on the integrated Ouija board to type, or type on your physical keyboard to watch the planchette fly across the UI automatically.
- **Persistent Local Storage:** Your dark secrets are never lost. The notepad automatically saves your progress continuously using browser LocalStorage.
- **Gothic Styling:** Built with custom fonts, ambient animations, and a responsive dark-mode UI.
- **Burn Page Protocol:** Instantly clear your thoughts and local storage with the confirmation-gated "Burn Page" capability.

## Installation & Usage
This application is now compiled as a native Linux desktop application powered by **Tauri**, providing excellent performance and avoiding the need for a web browser entirely.

1. Clone the repository:
   ```bash
   git clone https://github.com/BlancoBAM/Lilith-Notepad.git
   cd Lilith-Notepad
   ```

2. To run the app in development mode using Tauri:
   ```bash
   npm install
   npm run tauri dev
   ```

3. To build the release packages (Debian, RPM, AppImage) natively:
   ```bash
   npm run tauri build
   ```
   *The standalone `.AppImage` and `.deb` installers will be generated in `src-tauri/target/release/bundle/`.*

## Built With
- **Frontend UI:** HTML5 & Vanilla JS/CSS
- **Desktop Backend:** Tauri (Rust & WebKit2GTK)

## License
MIT License
