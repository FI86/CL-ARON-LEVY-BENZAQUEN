# Fichier d'exemples avec le module pathlib

# Import
import subprocess

def main():
    print("Resume des principales fonctionnalites du module subprocess :")
    
    # Executer une commande simple (ex: 'echo Hello World')
    print("\nExecution d'une commande simple :")
    result = subprocess.run(["cmd", "/c", "echo Hello, World!"], capture_output=True, text=True)
    print("Sortie:", result.stdout.strip())
    
    # Executer une commande et recuperer la sortie
    print("\nListe des fichiers du repertoire courant :")
    result = subprocess.run(["dir"], capture_output=True, text=True, shell=True)
    print("Sortie:", result.stdout.strip())
    
    # Executer une commande avec gestion des erreurs
    print("\nExecution d'une commande invalide :")
    result = subprocess.run(["command_invalide"], capture_output=True, text=True, shell=True)
    print("Code de retour:", result.returncode)
    print("Erreur:", result.stderr.strip())
    
    # Utilisation de Popen pour executer une commande en arriere-plan
    print("\nExecution en arriere-plan avec Popen :")
    process = subprocess.Popen(["cmd", "/c", "timeout 5"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    print("Processus lance avec PID:", process.pid)
    process.wait()
    print("Processus termine.")

if __name__ == "__main__":
    main()
