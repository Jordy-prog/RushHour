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
        self.free_rear = 0
        self.free_front = 0

    def position(self, row, col):
        '''
        Position setter method.
        '''
        self.row = row
        self.col = col
    
    def freespace(self, front, rear):
        '''
        Freespace setter method.
        '''
        self.free_rear = rear
        self.free_front = front

    def __str__(self):
        '''
        Returns name of car.
        '''
        return f"{self.name}"
