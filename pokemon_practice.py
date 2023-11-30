class BasePokemon:

    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category

    def __str__(self):
        return f"{self.name}/{self.category}"


class EmojiMixin:
    emoji = {
        "grass": "🍀",
        "fire": "🔥",
        "water": "💧",
        "electric": "⚡️",
    }

    def __str__(self):
        return f"{self.name}/{self.emoji[self.category]}"


class Pokemon(EmojiMixin, BasePokemon):

    def __init__(self, name: str, category: str):
        super().__init__(name, category)


if __name__ == "__main__":
    pikachu = Pokemon(name="Pikachu", category="electric")
    charmander = Pokemon(name="Bulbasaur", category="grass")
    print(pikachu)
    print(charmander)
