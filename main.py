import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

def main():
    # Récupérer les variables d'environnement
    app_name = os.getenv('APP_NAME')
    app_env = os.getenv('APP_ENV')
    
    print(f"Application: {app_name}")
    print(f"Environnement: {app_env}")
    
    # Votre code principal ici
    print("Hello, World!")

if __name__ == '__main__':
    main()