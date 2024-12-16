class Barn:
    def __init__ (self):
        self.chicken_barn = []
    
    def add_chicken(self, chicken):
        self.chicken_barn.append(chicken)
    
    def print_chicken_barn(self):
        for i in self.chicken_barn:
            print(f'Name: {i.name}')
            print(f'Age: {i.age}')
            print(f'Health: {i.health}')
    
    def check_chicken_status(self):
        died_chicken = []
        for i in self.chicken_barn:
            i.update_status()
            if i.alive == False:
                died_chicken.append(i.name)
                self.chicken_barn.remove(i)
        
        return died_chicken
    
    def collect_eggs(self):
        collectable_eggs = 0
        for i in self.chicken_barn:
            if i.possible_to_lay_egg():
                collectable_eggs += 1
        
        return collectable_eggs
    
    def feed_chicken(self):
        for i in self.chicken_barn:
            i.feed()