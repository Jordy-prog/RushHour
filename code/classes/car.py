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

    def add_move(self, distance): ## POTENTIEEL VERWIJDEREN
        '''
        Add a move to the car's memory.
        '''
        try:
            if not len(self.moves[-1]) % 2:
                self.moves.append([distance])
            else:
                self.moves[-1].append(distance)
        except IndexError:
            self.moves.append([distance])

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
            free_rear_while, free_front_while = 0,0
            while i < RushHour.boardsize - self.row and not RushHour.matrix[self.row + i][self.col]:
                i += 1
                free_rear -= 1

            while j < self.row and not RushHour.matrix[self.row - (self.length - 1) - j][self.col]:
                j += 1
                free_front += 1

        return [free_rear, free_front]

    def __str__(self):
        '''
        Returns name of car.
        '''
        return f"{self.name}"
