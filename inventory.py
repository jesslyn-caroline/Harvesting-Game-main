class Inventory:
    def __init__ (self):
        self.crops = dict()
        self.resource = dict()
    
    def add_crop(self, crop, amount):
        if crop not in self.crops.keys():
            self.crops[crop] = amount
        else:
            self.crops[crop] += amount
    
    def sell_crop(self, crop, amount):
        if crop not in self.crops.keys():
            raise ValueError('Crop not found')
        else:
            if self.crops[crop]- amount < 0:
                raise ValueError('Not enough crops')
            else:
                self.crops[crop] -= amount
    
    def add_resource(self, resource, amount):
        if resource not in self.resource.keys():
            self.resource[resource] = amount
        else:
            self.resource[resource] += amount
    
    def sell_resource(self, resource, amount):
        if resource not in self.resource.keys():
            raise ValueError('Resource not found')
        else:
            if self.resource[resource]- amount < 0:
                raise ValueError('Not enough resource')
            else:
                self.resource[resource] -= amount

    def print_inventory(self):
        print('-' * 80)
        print(f'{'📦 Inventory 📦':^80}')
        print('-' * 80)
        print()
        if len(self.crops) == 0 and len(self.resource) == 0:
            print('Empty')
            print()
            print('-' * 80)
            return False
        
        print()
        print(f'> Crops: ')
        if len(self.crops) == 0:
            print('You dont have any crops.')
        else:
            for i in self.crops.keys():
                print(f'{i}: {self.crops[i]}')
        print()
        print(f'> Resources: ')
        if len(self.resource) == 0:
            print('You dont have any resources.')
        else:
            for i in self.resource.keys():
                print(f'{i}: {self.resource[i]}')
        print()
        print('-' * 80)

        return self.crops.keys() + self.resource.keys()