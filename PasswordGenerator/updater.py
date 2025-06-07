import requests, os

def update():
    url = "https://raw.githubusercontent.com/mkskt/password_generator/main/PasswordGenerator/passwordgenerator.py"
    r = requests.get(url)
    if r.status_code == 200:
        with open("passwordgenerator.py", "wb") as f:
            f.write(r.content)
    else:
        print(f"Błąd pobierania pliku: status {r.status_code}")

update()
os.system("python passwordgenerator.py")