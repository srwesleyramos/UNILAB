class Map:

    def __init__(self):
        self.cache = {}
        self.cheese = []
        self.grid = []
        self.robot = []
        self.type = {
            "AIR": "0",
            "CHEESE": "9",
            "ROBOT": "7",
            "WALL": "1",
        }
        self.wall = []

    #
    # LOADING WORLD
    #

    def load(self, content):
        rows = content.split('\n')

        for i, row in enumerate(rows):
            columns = row.split()

            self.grid.append([])

            for j, column in enumerate(columns):
                if column == self.type["ROBOT"]:
                    self.robot.append((i, j))

                if column == self.type["CHEESE"]:
                    self.cheese.append((i, j))

                if column == self.type["WALL"]:
                    self.wall.append((i, j))

                self.grid[i].append(column)

    #
    # SEARCHING PATH
    #

    def find(self, current, target, trails):
        if (current, target) in self.cache:
            return self.cache[(current, target)]

        # Fazendo validações de segurança

        if current in trails:
            return None

        if current[0] < 0 or current[0] >= len(self.grid):
            return None

        if current[1] < 0 or current[1] >= len(self.grid[0]):
            return None

        # Verificando colisões com objetos

        if self.grid[current[0]][current[1]] == self.type["WALL"]:
            return None

        if self.grid[current[0]][current[1]] == self.type[target]:
            return [current]

        # Calculando caminhos perpendiculares

        moves = [
            (current[0], current[1] + 1),
            (current[0], current[1] - 1),
            (current[0] + 1, current[1]),
            (current[0] - 1, current[1])
        ]

        # Verificando caminhos perpendiculares

        route = None
        steps = None

        for move in moves:
            result = self.find(move, target, trails + [current])

            if result is not None:
                if steps is None or len(result) < steps:
                    steps = len(result)
                    route = result

        # Fazendo cache para melhor eficiência

        if route is not None:
            self.cache[(current, target)] = [current] + route
        else:
            self.cache[(current, target)] = None

        return self.cache[(current, target)]

    #
    # CHECK IF IT IS POSSIBLE
    #

    def check(self):
        return len(self.robot) == 1 and len(self.cheese) == 1 and self.find(self.robot[0], "CHEESE", []) is not None
