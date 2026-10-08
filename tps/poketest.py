import unittest
import requests


class TestPokemonApi(unittest.TestCase):

    def test_obtener_mewtwo(self):
        url = "https://pokeapi.co/api/v2/pokemon/mewtwo"
        response = requests.get(url)

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["name"], "mewtwo")
        self.assertEqual(data["id"], 150)
        self.assertEqual(data["abilities"][0]["ability"]["name"], "pressure")

    def test_obtener_pokemon_inexistente(self):
        url = "https://pokeapi.co/api/v2/pokemon/pokemon12345"
        response = requests.get(url)

        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()