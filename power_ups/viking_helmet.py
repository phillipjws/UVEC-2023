from power_up import PowerUp


class VikingHelmet(PowerUp):
    def __init__(self, position):
        super(VikingHelmet, self).__init__(position, "viking_helmet_image.png")

    def apply_affect(self, character):
        pass  # TODO: need to add a field so they can win the level
