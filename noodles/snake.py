class Noodles:
    """Snake named Noodles."""

    def __init__(self):
        """Initilisation."""
        print("Hi, my name is Noodles!")

    def wanna_play(self, game: str) -> bool:
        """
        Ask Noodles to play a game.

        :param game: The game one would like to play with Noodles.
        :return: yes (True) if Noodles wants to play the game - there is an
            odd number of j's in the game's name, as j is the noodliest
            letter in the alphabet - and no (False) otherwise.
        """
        return game.count('j') % 2 == 1
