class Car():
    def __init__(self, name, orientation, row, col, color, length):
        """__init__ function to initialize variables.
        
        Parameters:
            name (string): The name of the car.
            orientation (string): The orientation of the car.
            row (integer): The row of the car on the board.
            col (integer): The column of the car on the board.
            color (string): The colour of the car.
            length (integer): The length of the car.
        """
        self.name = name
        self.orientation = orientation
        self.row = row
        self.col = col
        self.color = color
        self.length = length

    def set_position(self, row, col):
        """Position setter method for row and column of the car.

        Parameters:
            row (integer): The row of the car on the board.
            col (integer): The column of the car on the board. 
        """
        self.row = row
        self.col = col

    def look_around(self, RushHour):
        """Determines the amount of free space in front and behind the car.

        Parameters:
            RushHour (object): The RushHour board object.

        Returns: 
            {'rear': free_rear, 'front': free_front} (dictionary): A dictionary containing 
                the free space in front and behind the car.
        """
        free_rear, free_front = 0, 0

        # Start i, j at 1 to prevent a car from selecting itself
        i, j = 1, 1

        # Loops from car to edge of board and determine free places
        if self.orientation == 'H':
            while i <= self.col and not RushHour.matrix[self.row][self.col - i]:
                i += 1
                free_rear -= 1
            
            while j < RushHour.boardsize - (self.length - 1) - self.col and not RushHour.matrix[self.row][self.col + (self.length - 1) + j]:
                j += 1
                free_front += 1
        elif self.orientation == 'V':
            while i < RushHour.boardsize - self.row and not RushHour.matrix[self.row + i][self.col]:
                i += 1
                free_rear -= 1

            while j <= self.row - (self.length - 1) and not RushHour.matrix[self.row - (self.length - 1) - j][self.col]:
                j += 1
                free_front += 1

        return {'rear': free_rear, 'front': free_front}

    def __repr__(self):
        """Printable representation of the name of the car.

        Returns:
            f"{self.name}" (string): Formatted string of the name of the car.
        """
        
        return f"{self.name}"
