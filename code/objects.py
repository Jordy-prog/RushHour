class Car():
    '''
    Object that stores parameters for a car.
    '''
    def __init__(self, name, direction, position, color, length):
        '''
        Initializes attributes for car.
        '''
        self.name = name
        self.color = color
        self.length = length
        self.direction = direction
        self.start = position

    def __str__(self):
        '''
        Returns name of car.
        '''
        return f"{self.name}"
