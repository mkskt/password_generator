import sys
import subprocess
import time

def install_and_import_requests():

    print("Looking for 'requests' module...")
    time.sleep(2)
    try:
        import requests
        return requests
    except ImportError:
        print("'requests' module is not installed. Installing...\n", flush=True)
        time.sleep(3)
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        except subprocess.CalledProcessError as e:
            print("\nCould not install 'requests' module. Possible reasons:")
            print("> No permission to install packages")
            print("> Problem with pip or Python installation")
            print(f"Error details: {e}")
            sys.exit(1)
        try:
            import requests
            return requests
        except ImportError:
            print("Import failed after installation. Shutting down...", flush=True)
            time.sleep(5)
            sys.exit(1)

requests = install_and_import_requests()

def update():
    url = "https://raw.githubusercontent.com/mkskt/password_generator/main/PasswordGenerator/passwordgenerator.py"
    r = requests.get(url)
    if r.status_code == 200:
        print("\nChecking if update is available...\n", flush=True)
        with open("passwordgenerator.py", "wb") as f:
            f.write(r.content)
        time.sleep(3)
        print("\nPassword Generator has been updated.", flush=True)
    else:
        print(f"\nError while downloading: status {r.status_code}", flush=True)

update()

import subprocess

subprocess.Popen(['cmd', '/c', 'start', 'python', 'passwordgenerator.py'])

sys.exit()