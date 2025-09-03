import unittest
from script import generer_affichage_texte


class TestAffichageTexte(unittest.TestCase):
    def test_generer_affichage_texte(self):
        self.assertEqual(generer_affichage_texte(), "Bonjour, ceci est un texte affiché en sortie.")


if __name__ == "__main__":
    unittest.main()
