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
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
    except Exception as e:
        print(f"Error downloading update: {e}")
        sys.exit(1)

    print("\nChecking if update is available...\n", flush=True)
    with open("passwordgenerator.py", "wb") as f:
        f.write(r.content)
    time.sleep(3)
    print("\nPassword Generator has been updated.", flush=True)

update()

print("\nLaunching updated Password Generator...\n")

time.sleep(2)

subprocess.Popen(['cmd', '/c', 'start', sys.executable, 'passwordgenerator.py'])

sys.exit()