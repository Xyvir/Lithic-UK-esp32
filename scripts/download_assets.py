import os
import urllib.request
import sys

# PlatformIO SCons environment
from SCons.Script import Import
Import("env")

PROJECT_DIR = env.subst("$PROJECT_DIR")
DATA_SRC_DIR = os.path.join(PROJECT_DIR, "data", "src")

# Configuration
ASSETS = {
    "launcher.html": "https://raw.githubusercontent.com/Xyvir/Lithic-UK/refs/heads/main/src/launcher.html",
    "lithic.html": "https://raw.githubusercontent.com/Xyvir/Lithic-UK/refs/heads/main/src/lithic-light.html"
}

def download_file(url, dest_path):
    print(f"--- Lithic Asset Sync: Downloading {os.path.basename(dest_path)} ---")
    sys.stdout.flush()
    
    # We remove the try/except here so that if the download fails (e.g. no internet),
    # the entire build process STOPS. This is the best "blocking" behavior.
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=60) as response:
        content = response.read()
        with open(dest_path, "wb") as f:
            f.write(content)
    
    print(f"Successfully updated {dest_path}")
    sys.stdout.flush()

def main():
    if not os.path.exists(DATA_SRC_DIR):
        os.makedirs(DATA_SRC_DIR)

    for filename, url in ASSETS.items():
        dest_path = os.path.join(DATA_SRC_DIR, filename)
        download_file(url, dest_path)

# Run the sync
try:
    main()
except Exception as e:
    print(f"\n!!! LITHIC ERROR: Failed to download assets: {e} !!!")
    print("Check your internet connection or GitHub availability.\n")
    sys.stdout.flush()
    # Exit with error to block the build
    sys.exit(1)
