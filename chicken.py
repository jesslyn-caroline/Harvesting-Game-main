class Chicken:
    def __init__ (self, name):
        self.name = name
        self.age = 0
        self.health = 100
        self.day_eat_streak = 0 
        self.day_not_eat_streak = 0
        self.feeded = False
        self.alive = True
    
    def feed(self):
        self.feeded = True
    
    def update_health(self):
        if not self.feeded:
            self.day_not_eat_streak += 1
            self.day_eat_streak = 0
            if self.day_not_eat_streak > 3:
                self.health = self.health - (self.day_not_eat_streak * 10)
        
        else:
            self.day_not_eat_streak = 0
            self.day_eat_streak += 1
            if self.health + 10 > 100:
                self.health = 100
            else:
                self.health = self.health + 10
        
        print(self.health)
    
    def possible_to_lay_egg(self):
        if self.day_eat_streak == 3 and self.age > 2:
            self.day_eat_streak = 3
            return True
        
        return False
    
    def age_up(self):
        self.age += 1
    
    def update_status(self):
        self.age_up()
        self.update_health()
        if self.health <= 0:
            self.alive = False
        self.feeded = False

        
### Explanation ###
# 1. Chicken can die if health is lower than 1
# 2. Chicken is able to lay egg when it is more than 3 days old and it has been fed for 3 days straight
# 3. Everytime the chicken is feeded, it will gain health by 10
# 4. Status is updated everyday 