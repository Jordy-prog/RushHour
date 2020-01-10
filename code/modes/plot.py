def plot(RushHour):
        stepdata = []

        for i in range(100):
            rush = board.RushHour(board_path)
            steps = 0

            while not rush.game_won(steps):
                steps += 1
                
                if algorithm == '1':
                    random.random_pure(rush)
                elif algorithm == '2':
                    random.random_constraint(rush)

            stepdata.append(steps)

        # moet nog gebruikt worden
        avg_steps = round(sum(stepdata) / len(stepdata), 0)
        sorted_steps = sorted(stepdata)

        steps_dict = {}
        range_list = max(sorted_steps) - min(sorted_steps)
        bracket_width = int(range_list / sqrt(len(sorted_steps)))

        for step in sorted_steps:
            dict_bracket = int(step / bracket_width)
            dict_bracket = f'{min(sorted_steps) + dict_bracket * bracket_width}' + " to " + f'{min(sorted_steps) + dict_bracket * bracket_width + bracket_width}'
            if dict_bracket in steps_dict:
                steps_dict[dict_bracket] += 1
            else:
                steps_dict[dict_bracket] = 1 
        
        plt.bar(list(steps_dict.keys()), steps_dict.values(), color='g')
        plt.xticks(rotation=45)
        plt.xlabel ('Category')
        plt.ylabel ('Frequency')
        plt.title ('Frequency of moved cars')
        plt.show()