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
        self.moves = []

    def position(self, row, col):
        '''
        Position setter method.
        '''
        self.row = row
        self.col = col

    def add_move(self, distance):
        try:
            if not len(self.moves[-1]) % 2:
                self.moves.append([distance])
            else:
                self.moves[-1].append(distance)
        except IndexError:
            self.moves.append([distance])

    def __str__(self):
        '''
        Returns name of car.
        '''
        return f"{self.name}"
