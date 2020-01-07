class Car():
    '''
    Object that stores parameters for a car.
    '''
    def __init__(self, name, direction, row, col, color, length):
        '''
        Initializes attributes for car.
        '''
        self.name = name
        self.color = color
        self.length = length
        self.direction = direction
        self.row = row
        self.col = col

    def position(self, row, col):
        self.row = row
        self.col = col

    def __str__(self):
        '''
        Returns name of car.
        '''
        return f"{self.name}"
