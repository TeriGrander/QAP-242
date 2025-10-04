class Team:
    def __init__(self, name, size, capital, members=[]):
       self.name = name
       self.size = size
       self.capital = capital
       self.members = members
    def show_info(self):
        print(f'Team name: {self.name}, team size: {self.size}, capital: {self.capital}')
        