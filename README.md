# Lithic ESP32 WebDAV Server

This project provides a portable, local-first WebDAV server and captive portal for [Lithic](https://lithic.uk), an outliner-style Personal Knowledge Management system. 

It is designed to run on an ESP32, allowing you to sync and edit your `.lith` files (TiddlyWiki based) locally over WiFi; without an internet connection.

Anywhere you can bring your ESP32, you can bring your entire knowledge base and access with your device of choice.

## 🏛️ Methodology: "Software as Hardware"
Lithic ESP32 follows a **"Software as Hardware"** philosophy. By embedding the entire PKMS environment into a dedicated microcontroller, the software becomes a tangible, physical tool. It removes the friction of OS-level sync, browser compatibility issues, and cloud dependency, turning your knowledge base into a robust, "plug-and-play" appliance.

## 🚀 Features


- **Captive Portal**: Automatically redirects connected devices to the Lithic launcher.
- **WebDAV Sync**: Implements a lightweight WebDAV-compatible layer for the Lithic Android launcher and browser-based sync.
- **Dynamic Asset Sync**: The build process automatically pulls the latest `launcher.html` and `lithic.html` from the [main Lithic repository](https://github.com/Xyvir/Lithic-UK).
- **Graceful Upgrades**: Includes scripts for updating UI assets over Wi-Fi without wiping user data in the `/sync/` directory.

## 🛠️ Getting Started

### Prerequisites
- [PlatformIO](https://platformio.org/)
- Python 3.x (for asset sync scripts)

### Installation
1. Clone this repository.
2. Open in PlatformIO.
3. Run **Build** (this will download the latest UI assets from GitHub).
4. Run **Upload Filesystem Image** (First time only - this installs the UI).
5. Run **Upload** (Installs the firmware).

### Updating UI Assets (Without Wiping Data)
If you want to update the Lithic UI but keep your saved files on the ESP32:
1. Connect to the ESP32 AP (Default: `Lithic_XXXX`).
2. Run the update script:
   ```bash
   python scripts/update_esp32_assets.py
   ```

## 🗺️ Roadmap
- [ ] **`WIFI_MODE_APSTA` Support**: Enable concurrent Access Point and Station mode for online connectivity.
- [ ] **SD-Card Integration**: Expand storage capacity beyond LittleFS limits for large wikis and media.
- [ ] **NAT-Traversal (Cloudflare Tunnels)**: Implementation of secure, low-cost "anywhere-access" for self-hosted instances without complex router configuration.

## 🔗 Links

- **Official Website**: [lithic.uk](https://lithic.uk)
- **Core Repository**: [Xyvir/Lithic-UK](https://github.com/Xyvir/Lithic-UK)

## License
MIT
