class Mushroom:
    """
    One can put a mushroom in spaghetti sauce, but it needs to be cut first.
    """

    def __init__(self, pieces=1):
        """
        Specify the initial number of pieces of the mushroom.

        :param pieces: This mushroom is cut in this many pieces.
        """
        self.pieces = pieces

    def cut(self):
        """Cut each piece of this mushroom in half."""
        self.pieces *= 2
