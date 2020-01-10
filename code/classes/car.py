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

    def look_around(self, RushHour):
        free_rear, free_front = 0, 0
        i, j = 1, 1

        if self.direction == 'H':
            while i <= self.col and not RushHour.matrix[self.row][self.col - i]:
                i += 1
                free_rear -= 1
            
            while j < RushHour.boardsize - (self.length - 1) - self.col and not RushHour.matrix[self.row][self.col + (self.length - 1) + j]:
                j += 1
                free_front += 1
        elif self.direction == 'V':
            while i < RushHour.boardsize - self.row and not RushHour.matrix[self.row + i][self.col]:
                i += 1
                free_rear -= 1

            while j < self.row and not RushHour.matrix[self.row - (self.length - 1) - j][self.col]:
                j += 1
                free_front += 1

        return {'rear': free_rear, 'front': free_front}

    def __str__(self):
        '''
        Returns name of car.
        '''
        return f"{self.name}"
