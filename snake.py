class Snake():

    def __init__(self) -> None:
        pass

    snake_positions = {
        17: 4,
        19: 7,
        21: 9,
        27: 1
    }

    @classmethod
    def is_present(cls, num):
        if num in cls.snake_positions:
            return True
    
    @classmethod
    def get_destination(cls, num):
        return cls.snake_positions[num]
