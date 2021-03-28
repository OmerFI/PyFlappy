
class BirdClass():
    """Bird configuration class for making flapping effect.

    Functions:
        get_bird(self) -> str: Is used for getting a bird that is wanted to display on the screen.
    """
    birdlist = ["bird1", "bird2", "bird3", "bird4", "bird5", "bird6", "bird7", "bird8", "bird9", "bird10",
                "bird11", "bird12", "bird13", "bird14", "bird15", "bird16", "bird17", "bird18", "bird19", "bird20",
                "bird21", "bird22", "bird23", "bird24", "bird25", "bird26", "bird27", "bird28", "bird29", "bird28",
                "bird27", "bird26", "bird25", "bird24", "bird23", "bird22", "bird21", "bird20", "bird19", "bird18",
                "bird17", "bird16", "bird15", "bird14", "bird13", "bird12", "bird11", "bird10", "bird9", "bird8",
                "bird7", "bird6", "bird5", "bird4", "bird3", "bird2"]

    def __init__(self):
        self.num = -1

    def get_bird(self) -> str:
        """Is used for getting a bird that is wanted to display on the screen.

        Returns:
            str: bird+number, i.e. bird1, bird23
        """

        if self.num == 54:
            self.num = -1
            return __class__.birdlist[self.num]
        else:
            self.num += 1
            return __class__.birdlist[self.num]
