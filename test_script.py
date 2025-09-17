import unittest
import os
import shutil
import hashlib
from script import generer_affichage_texte
from script import hash_file_metadata
from script import hash_file

class TestAffichageTexte(unittest.TestCase):
    def test_generer_affichage_texte(self):
        self.assertEqual(generer_affichage_texte(), "Bonjour, ceci est un texte affiché en sortie dans la console.")

class TestHashFile(unittest.TestCase):
    def test_hash_file(self):
        # Test avec un fichier connu
        test_file_path = "test_file.txt"
        with open(test_file_path, "w") as f:
            f.write("Ceci est un fichier de test.")
        stat = os.stat(test_file_path)
        print(f"{stat.st_size}-{stat.st_ctime}-{stat.st_mtime}")
        expected_hash = hashlib.sha256(b"Ceci est un fichier de test.").hexdigest()
        actual_hash = hash_file(test_file_path)
        self.assertEqual(expected_hash, actual_hash)
        
        # Nettoyage
        os.remove(test_file_path)

class TestHashFileMetadata(unittest.TestCase):
    def test_hash_file_metadata(self):
        # Test avec un fichier connu
        test_file_path = "test_file.txt"
        with open(test_file_path, "w") as f:
            f.write("Ceci est un fichier de test.")
        stat = os.stat(test_file_path)
        print(f"{stat.st_size}-{stat.st_mtime}")
        shutil.copy2(test_file_path, "test_file2.txt")  # Copier avec métadonnées
        stat = os.stat("test_file2.txt")
        print(f"{stat.st_size}-{stat.st_mtime}")
        expected_hash = hash_file_metadata(test_file_path)
        actual_hash = hash_file_metadata("test_file2.txt")
        self.assertEqual(expected_hash, actual_hash)
        
        # Nettoyage
        os.remove(test_file_path)
        os.remove("test_file2.txt")

if __name__ == "__main__":
    unittest.main()
