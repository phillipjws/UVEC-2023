from power_up import PowerUp


class EcsCard(PowerUp):
    def __init__(self, position):
        super(EcsCard, self).__init__(position, "ecs_card_image.png")

    def apply_affect(self, character):
        pass  # TODO: need to add a field so they can win the level
