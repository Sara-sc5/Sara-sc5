import hashlib
import json
import os

HASH_DB = "file_hashes.json"

def calculate_hash(file_path):
    """Restituisce l'hash SHA-256 di un file, oppure None se il file non esiste."""
    if not os.path.exists(file_path):
        print(f"[ERRORE] Il file '{file_path}' non esiste.")
        return None
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def load_hashes():
    """Carica il database di hash, o restituisce un dizionario vuoto se non esiste."""
    return json.load(open(HASH_DB)) if os.path.exists(HASH_DB) else {}

def save_hash(file_path):
    """Salva l'hash del file nel database."""
    hashes = load_hashes()
    hashes[file_path] = calculate_hash(file_path)
    json.dump(hashes, open(HASH_DB, "w"), indent=4)
    print(f"[+] Hash salvato per '{file_path}'.")

def check_integrity(file_path):
    """Confronta l'hash del file con quello salvato per verificarne l'integrità."""
    hashes = load_hashes()
    if file_path not in hashes:
        print(f"[!] Nessun hash registrato per '{file_path}'.")
    elif hashes[file_path] == calculate_hash(file_path):
        print(f"[OK] Il file è integro.")
    else:
        print(f"[ATTENZIONE] Il file è stato modificato!")

if __name__ == "__main__":
    scelta = input("\n1. Salva hash\n2. Controlla integrità\nScelta: ")
    path = input("Inserisci il percorso del file: ")
    save_hash(path) if scelta == "1" else check_integrity(path)