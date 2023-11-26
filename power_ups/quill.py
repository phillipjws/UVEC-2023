from power_up import PowerUp


class Quill(PowerUp):
    def __init__(self, position):
        super(Quill, self).__init__(position, "quill_image.png")

    def apply_affect(self, character):
        pass  # TODO: need to add a field so they can win the level
