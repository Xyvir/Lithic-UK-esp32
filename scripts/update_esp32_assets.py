import os
import urllib.request

# Configuration
ESP32_IP = "192.168.4.1"
ASSETS = ["launcher.html", "lithic.html"]
DATA_SRC_DIR = "data/src"

def upload_file(filename):
    local_path = os.path.join(DATA_SRC_DIR, filename)
    url = f"http://{ESP32_IP}/src/{filename}"
    
    if not os.path.exists(local_path):
        print(f"Error: {local_path} not found. Run a PIO build first to download assets.")
        return

    print(f"Uploading {filename} to {url}...")
    try:
        with open(local_path, "rb") as f:
            data = f.read()
            req = urllib.request.Request(url, data=data, method="PUT")
            with urllib.request.urlopen(req, timeout=60) as response:
                if response.status in [200, 201, 204]:
                    print(f"Successfully uploaded {filename}")
                else:
                    print(f"Failed to upload {filename}: Status {response.status}")
    except Exception as e:
        print(f"Failed to upload {filename}: {e}")

def main():
    for asset in ASSETS:
        upload_file(asset)

if __name__ == "__main__":
    main()
