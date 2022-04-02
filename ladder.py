class Ladder():

    def __init__(self) -> None:
        pass

    ladder_positions = {
        3: 22,
        5: 8,
        11: 26,
        20: 29
    }

    @classmethod
    def is_present(cls, num):
        if num in cls.ladder_positions:
            return True
    
    @classmethod
    def get_destination(cls, num):
        return cls.ladder_positions[num]
