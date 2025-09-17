import os
import hashlib
import time

def generer_affichage_texte():
    return "Bonjour, ceci est un texte affiché en sortie dans la console."


def hash_file_metadata(filepath):
    """Construit un hash SHA-256 à partir des métadonnées d'un fichier."""
    stat = os.stat(filepath)
    # On utilise la taille et la date de modification
    metadata = f"{stat.st_size}-{stat.st_mtime}"
    return hashlib.sha256(metadata.encode('utf-8')).hexdigest()

def hash_file(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()


def main():
    print(generer_affichage_texte())
    start_time = time.time()
    output_file = "hashes.txt"
    nb_files = 0
    with open(output_file, "w", encoding="utf-8") as out:
        folder = "C:\\Users\\USER\\Desktop\\GitHub\\12_Comfy\\ComfyUI\\output\\"
        for root, _, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                out.write(f"{root,file}: {hash_file_metadata(file_path)}\n")
                nb_files += 1
    end_time = time.time()
    print(f"Hashes written to {output_file} in {end_time - start_time:.2f} seconds.")
    print(f"Number of files processed: {nb_files}")

    # path = "C:\\Users\\USER\\Desktop\\GitHub\\06_mochi-1-preview\\models\\README.md"
    # hash1 = hash_file(path)
    # path = "C:\\Users\\USER\\Desktop\\GitHub\\06_mochi-1-preview\\models\\README2.md"
    # hash2 = hash_file(path)
    # if hash1 == hash2:
        # print("The files are identical.")
    # print("Hash 1:", hash1)
    # print("Hash 2:", hash2)

if __name__ == "__main__":
    main()
