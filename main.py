import os
import random


def cls(): os.system('cls' if os.name == 'nt' else 'clear')

# === Start of UserStats Class ===
class UserStats:
    def __init__(self):
        self.day = 1
        self.money = 1000
        self.diary = {1: {"Profit": 0, "Expense" : 0}}

    def next_day(self):
        self.day += 1
        self.diary[self.day] = {"Profit": 0, "Expense" : 0}

    def profit(self, amount):
        self.money += amount
        self.diary[self.day]["Profit"] += amount

    def expense(self, amount):
        if self.money - amount < 0:
            return False
            
        self.money -= amount
        self.diary[self.day]["Expense"] += amount
        return True
    
    def check_progress(self):
        if self.day == 4:
            seeds.list['Potato Seed']['unlocked'] = True
            inventory.list['Potato Seed']['quantity'] = 5
            market_items.list['Potato Seed']['unlocked'] = True

            print('> 🥳 Congratulations! You have reached Day 4.')
            print('> 🥔 Potato Seed is now unlocked. You received 5 potato seeds.')

            return

        if self.day >= 8 and self.money > 1100:
            seeds.list['Tomato Seed']['unlocked'] = True
            inventory.list['Tomato Seed']['quantity'] = 5
            market_items.list['Tomato Seed']['unlocked'] = True

            print('> 🥳 Congratulations! You have passed Day 8 and got more than 1100 🪙.')
            print('> 😄 For this achievement, you will receive Tomato Seed!')
            print('> 🍅 Tomato Seed is now unlocked. You received 5 tomato seeds.')

            return

        if self.day >= 12 and self.money > 1500 and inventory.list['Corn']['quantity'] >= 15 and inventory.list['Potato']['quantity'] >= 10 and inventory.list['Tomato']['quantity'] >= 5:
            seeds.list['Carrot Seed']['unlocked'] = True
            inventory.list['Carrot Seed']['quantity'] = 5
            market_items.list['Carrot Seed']['unlocked'] = True

            print('> 🥳 Congratulations! You have reached the following conditions:')
            print('\t- You have passed day 12.')
            print('\t- You have more than 1500 🪙')
            print('\t- You have at least 15 corns in your inventory 🌽')
            print('\t- You have at least 10 potatoes in your inventory 🥔')
            print('\t- You have at least 5 tomatoes in your inventory 🍅')
            print('> 🥕 Carrot Seed is now unlocked. You received 5 carrot seeds.')

            return

    def print_statistic(self):
        print(f'> 📅 Day: {self.day}')
        print(f'> 🪙 Money: {self.money}')
        print()
        print('> 📔 Diary:')
        for day in self.diary.keys():
            print(f'Day {day}:')
            print(f'Profit: {self.diary[day]["Profit"]}')
            print(f'Expense: {self.diary[day]["Expense"]}')
            print()
        print()

# === End of UserStats Class ===


# === Start of Chicken Class ===

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

# === End of Chicken Class ===


# === Start of Barn Class ===

class Barn:
    def __init__ (self):
        self.barn = []

class ChickenBarn(Barn):
    def __init__ (self):
        super().__init__()
        self.barn.append(Chicken('Chick'))

    def collect_eggs(self):
        count = 0
        for chicken in self.barn:
            if chicken.possible_to_lay_egg():
                count += 1
        
        return count
    
    def make_chicken_feed (self, quantity):
        return quantity * 3 # 1 corn to make 3 chicken feed
    
    def print_chicken_barn(self):
        print(f'> 🐔 Total: {len(self.barn)} chickens')
        count = 0
        for chicken in self.barn:
            count += 1
            print(f'> {count}. 🐔 Name: {chicken.name} - [ Age: {chicken.age} days ][ Health: {chicken.health} ]')
        
        return count
    
    def feed_chickens(self, index):
        count = 0
        for chicken in self.barn:
            count += 1
            if count == index:
                chicken.feed()
                return chicken.name
    
    def update_chickens_status(self):
        alive_chickens = []
        dead_chickens = []
        for chicken in self.barn:
            chicken.update_status()
            if chicken.alive: alive_chickens.append(chicken)
            else: dead_chickens.append(chicken)
        
        self.barn = alive_chickens

        return dead_chickens


# === End of Barn Class ===


# === Start of Inventory Class ===

class Inventory:
    def __init__(self):

        self.list = {
            'Corn Seed': {
                'quantity': 5,
                'icon': '🌽',
                'type': 'seed'
            },
            'Corn': {
                'quantity': 0,
                'icon': '🌽',
                'type': 'crop'
            },
            'Potato Seed': {
                'quantity': 0,
                'icon': '🥔',
                'type': 'seed'
            },
            'Potato': {
                'quantity': 0,
                'icon': '🥔',
                'type': 'crop'
            },
            'Tomato Seed': {
                'quantity': 0,
                'icon': '🍅',
                'type': 'seed'
            },
            'Tomato': {
                'quantity': 0,
                'icon': '🍅',
                'type': 'crop'
            },
            'Carrot Seed': {
                'quantity': 0,
                'icon': '🥕',
                'type': 'seed'
            },
            'Carrot': {
                'quantity': 0,
                'icon': '🥕',
                'type': 'crop'
            },
            'Egg': {
                'quantity': 0,
                'icon': '🥚',
                'type': 'product'
            },
            'Milk': {
                'quantity': 0,
                'icon': '🥛',
                'type': 'product'
            },
            'Chicken Feed': {
                'quantity': 0,
                'icon': '🫘',
                'type': 'product'
            },
        }
    
    def print_inventory(self):
        for item_name in self.list:
            item = self.list[item_name]
            if item['quantity'] > 0: print(f'> {item['icon']} {item_name}: {item['quantity']}')

    def print_sellable_items(self):
        count = 0
        for item_name in self.list:
            item = self.list[item_name]
            if item['type'] in ['crop', 'product'] and item['quantity'] > 0: 
                count += 1
                print(f'> {item['icon']} {item_name}: {item['quantity']}')
        
        return count
        


            
                
# === End of Inventory Class ===


# === Start of Farm Class ===
class Farm:
    def __init__(self):
        self.size = 3
        self.field = [['No seed' for _ in range(self.size)] for _ in range(self.size)]
        self.field_detail = [['' for _ in range(self.size)] for _ in range(self.size)]
        self.field_day = [[0 for _ in range(self.size)] for _ in range(self.size)]

    def update_field(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.field_detail[row][col] == '': continue
                self.field_day[row][col] += 1
                if self.field_day[row][col] == seeds.list[self.field_detail[row][col]]['grow_time']:
                    self.field[row][col] = seeds.list[self.field_detail[row][col]]['icon']

    def print_field(self):
        print(f'> 🌽 Current field size: {self.size} x {self.size}\n')
        for row in self.field:
            count = 0
            for col in row:
                count += 1
                if col == 'No seed': print(f'{col:^9}', end='')
                else: print(f'{col:^8}', end='')
                if count < self.size: print('|', end='')
            print()
        print()

    def plant_seed(self, row, col, seed_name):
        if self.field_detail[row][col] == '':
            self.field_detail[row][col] = seed_name
            self.field[row][col] = '🌱'
            print(f'> 🌱 {seed_name} planted successfully!')
            return True

        print('> 🌱 There is already a seed in this field.')
        return False

    def harvest(self):
        crops = {
            'Corn': 0,
            'Potato': 0,
            'Tomato': 0,
            'Carrot': 0
        }

        for row in range(self.size):
            for col in range(self.size):
                seed_name = self.field_detail[row][col]
                if seed_name == '': continue
                seed = seeds.list[seed_name]
                if self.field_day[row][col] >= seed['grow_time']:
                    self.field[row][col] = 'No seed'
                    self.field_detail[row][col] = ''
                    self.field_day[row][col] = 0
                    crop_name = seed_name.replace(' Seed', '')
                    inventory.list[crop_name]['quantity'] += 1
                    crops[crop_name] += 1

        return crops
        
# === End of Farm Class ===


# === Start of Seeds Class ===

class Seeds:
    def __init__(self):
        self.list = {
            'Corn Seed': {
                'code': 1,
                'icon': '🌽',
                'grow_time': 3,
                'unlocked': True 
            },
            'Potato Seed': {
                'code': 2,
                'icon': '🥔',
                'grow_time': 4,
                'unlocked': False
            },
            'Tomato Seed': {
                'code': 3,
                'icon': '🍅',
                'grow_time': 4,
                'unlocked': False
            },
            'Carrot Seed': {
                'code': 4,
                'icon': '🥕',
                'grow_time': 3,
                'unlocked': False
            }
        }


    def count(self):
        count = 0
        for seed_name in self.list:
            seed = self.list[seed_name]
            if seed['unlocked'] == True: count += 1
        return count

    def print_seeds_list(self):
        print('> 🌱 List of unlocked seed(s):')
        print('-' * 80)

        count = 0
        for seed_name in self.list:
            seed = self.list[seed_name]
            if seed['unlocked'] == False: continue
            count += 1
            print(f'> {count}. {seed['icon']} {seed_name}: {inventory.list[seed_name]['quantity']} seed(s) left.')

        print()
        
# === End of Seeds Class ===


# === Start of Market Item Class ===

class MarketItems:
    def __init__(self):
        self.list = {
            'Corn Seed': {
                'icon': '🌽',
                'price': 25,
                'unlocked': True
            },
            'Potato Seed': {
                'icon': '🥔',
                'price': 45,
                'unlocked': False
            },
            'Tomato Seed': {
                'icon': '🍅',
                'price': 60,
                'unlocked': False
            },
            'Carrot Seed': {
                'icon': '🥕',
                'price': 45,
                'unlocked': False
            },
            'Chicken': {
                'icon': '🐔',
                'price': 120,
                'unlocked': True
            },
            'Cow': {
                'icon': '🐄',
                'price': 180,
                'unlocked': True
            },
            'Chicken Feed': {
                'icon': '🫘',
                'price': 15,
                'unlocked': True
            }
        }
        
# === End of Market Item Class ===


# === Start of Market Class ===

class Market:
    def __init__(self):
        self.buy = Buy()
        self.sell = Sell()
        
# === End of Market Class ===



# === Start of Buy (Market) Class ===

class Buy:
    def __init__(self): pass

    def show_items(self):
        print('-' * 80)
        print(f'{'🏪 Buy Item 🏪':^80}')
        print('-' * 80)
        print(f'You currently have {stats.money} 🪙')
        print('-' * 80)

        print('> 🌽 List of available item(s):')
        print('-' * 80)

        count = 0
        for item_name in market_items.list:
            item = market_items.list[item_name]
            if item['unlocked'] == False: continue
            count += 1
            print(f'> {count}. {item['icon']} {item_name}: {item['price']} 🪙')

        print('-' * 80)
        return count

    def get_item(self, index):
        count = 0
        for item_name in market_items.list:
            item = market_items.list[item_name]
            if item['unlocked'] == False: continue
            count += 1
            if count == index:
                return item_name, item

        return False, False
        
# === End of Buy (Market) Class ===


# === Start of Sell (Market) Class ===

class Sell:
    def __init__ (self): # Adjust the random price
        self.list = {
            'Corn': {
                'icon': '🌽',
                'price': random.randint(45, 55)
            },
            'Potato': {
                'icon': '🥔',
                'price': random.randint(45, 55)
            },
            'Tomato': {
                'icon': '🍅',
                'price': random.randint(45, 55)
            },
            'Carrot': {
                'icon': '🥕',
                'price': random.randint(45, 55)
            },
            'Egg': {
                'icon': '🥚',
                'price': random.randint(45, 55)
            },
            'Milk': {
                'icon': '🥛',
                'price': random.randint(45, 55)
            }
        }

    def update_price(self):
        for item_name in self.list:
            self.list[item_name]['price'] = random.randint(45, 55)

    def print_price(self):
        count = 0
        for item_name in self.list:
            item = self.list[item_name]
            count += 1
            print(f'> {count}. {item['icon']} {item_name}: {item['price']} 🪙')

    def get_item(self, index):
        count = 0
        for item_name in self.list:
            item = self.list[item_name]
            count += 1
            if count == index:
                return item_name, item

        return False, False

    
# === End of Sell (Market) Class ===

# User Instances
stats = UserStats()
inventory = Inventory()

# Farm Instances
farm = Farm()
seeds = Seeds()

# Market Instances
market = Market()
market_items = MarketItems()

# Barn Instance
chicken_barn = ChickenBarn()

# === Start of Farm Menu ===

def farm_menu():
    print('-' * 80)
    print(f'{'🌽 Farm 🌽':^80}')
    print('-' * 80 + '\n')

    farm.print_field()

    print('-' * 80)
    print('1. Plant Seed 🌱')
    print('2. Harvest 🌾')
    print('3. Back to Main Menu 👈')

    print('-' * 80)

    choice = input('> Enter menu number: ')

    if choice not in ['1', '2', '3']:
        print('> ❗ Invalid option!\n')
        return

    if choice in ['1', '2']: cls()

    if choice == '1': farm_plant_menu()
    elif choice == '2': farm_harvest_menu()
    else:
        print('-' * 80)
        return
        
# === End of Farm Menu ===

# === Start of Farm Plant Menu ===

def farm_plant_menu():
    print('-' * 80)
    print(f'{'🌱 Plant Seed 🌱':^80}')
    print('-' * 80 + '\n')

    farm.print_field()

    print('-' * 80 + '\n')

    seeds.print_seeds_list()

    seed_count = 0
    for seed_name in seeds.list:
        seed = seeds.list[seed_name]
        if seed['unlocked'] == True: seed_count += inventory.list[seed_name]['quantity']

    if seed_count == 0:
        print('> 🌱 There are no seeds left to be planted. You can buy them at the market.')
        print('-' * 80)
        return

    valid = False
    while valid is False:
        choice = input('> ❓ Do you want to plant any seed? (y/n): ').lower()
        try:
            if choice == '': raise ValueError('> ❗ Choice may not be empty!\n')
            if choice not in ['y', 'n']: raise ValueError('> ❗ Invalid option!\n')
            valid = True
        except ValueError as e:
            print(str(e))

    print()

    if choice == 'n': return

    valid = False
    while valid is False:
        seed_code = input('> 🌱 Enter seed code number: ')
        try:
            if seed_code == '': raise ValueError('> ❗ Seed code may not be empty!\n')
            if not seed_code.isnumeric(): raise ValueError('> ❗ Seed code must be a number!\n')

            seed_code = int(seed_code)

            if seed_code < 1 or seed_code > seeds.count(): raise ValueError('> ❗ Invalid seed code!\n')

            if seed_code == 1: seed_name = 'Corn Seed'
            elif seed_code == 2: seed_name = 'Potato Seed'
            elif seed_code == 3: seed_name = 'Tomato Seed'
            elif seed_code == 4: seed_name = 'Carrot Seed'

            if inventory.list[seed_name]['quantity'] == 0: raise ValueError(f'> ❗ There are no {seed_name} left to be planted. You can buy them at the market.\n')
            # seed_code = seed_code
            valid = True

        except ValueError as e:
            print(str(e))

    print()

    valid = False
    while valid is False:
        row = input('> 🌱 Enter row number: ')
        try:
            if row == '': raise ValueError('> ❗ Row number may not be empty!\n')
            if not row.isnumeric(): raise ValueError('> ❗ Row number must be a number!\n')
            row = int(row)
            if row < 1 or row > farm.size: raise ValueError('> ❗ Invalid row number!\n')
            row -= 1
            valid = True
        except ValueError as e:
            print(str(e))

    print()

    valid = False
    while valid is False:
        col = input('> 🌱 Enter column number: ')
        try:
            if col == '': raise ValueError('> ❗ Column number may not be empty!\n')
            if not col.isnumeric(): raise ValueError('> ❗ Column number must be a number!\n')
            col = int(col)
            if col < 1 or col > farm.size: raise ValueError('> ❗ Invalid column number!\n')
            col -= 1
            valid = True
        except ValueError as e:
            print(str(e))

    print()

    valid = farm.plant_seed(row, col, seed_name)
    print('-' * 80)

    if valid:
        inventory.list[seed_name]['quantity'] -= 1
        print()
        farm.print_field()
        print('-' * 80)
        
# === End of Farm Plant Menu ===


# === Start of Farm Harvest Menu ===

def farm_harvest_menu():
    print('-' * 80)
    print(f'{'🌾 Harvest 🌾':^80}')
    print('-' * 80 + '\n')

    farm.print_field()

    print('-' * 80)

    harvestable_count = 0

    for row in range(farm.size):
        for col in range(farm.size):
            if farm.field_detail[row][col] == '': continue
            if farm.field_day[row][col] >= seeds.list[farm.field_detail[row][col]]['grow_time']:
                harvestable_count += 1

    if harvestable_count == 0:
        print('> 🌾 There are no crops to be harvested')
        print('-' * 80)
        return

    print(f'> 🌾 There are {harvestable_count} crops to be harvested')
    input('> 🌽 Press any key to harvest all...')

    print('-' * 80)

    crop_quantity = farm.harvest()

    for crop_name in crop_quantity:
        seed_name = crop_name + ' Seed'
        if crop_quantity[crop_name] > 0: print(f'> {seeds.list[seed_name]['icon']} You harvested {crop_quantity[crop_name]} {crop_name}')

    print('-' * 80)
    
# === End of Farm Harvest Menu ===


# === Start of End Day Function ===

def end_day():
    print(f'\n> 🌙 End of Day {stats.day}')
    stats.next_day()
    print(f'> 🌞 Start of Day {stats.day}')
    farm.update_field()
    stats.check_progress()
    market.sell.update_price()
    dead_chickens = chicken_barn.update_chickens_status()
    if len(dead_chickens) > 0: 
        print()
        for chicken in dead_chickens: print(f'> 🐔 {chicken.name} died at age {chicken.age} days...')
    print('-' * 80)
    
# === End of End Day Function ===


# === Start of Market Menu ===

def market_menu():
    print('-' * 80)
    print(f'{'🏪 Market 🏪':^80}')
    print('-' * 80)

    print('> 1. Buy 🌽')
    print('> 2. Sell 🪙')
    print('> 3. Back to Main Menu 👈')

    print('-' * 80)

    valid = False

    while valid is False:
        choice = input('> Enter menu number: ')

        try:
            if choice not in ['1', '2', '3']:
                raise ValueError('> ❗ Invalid option!\n')
            valid = True
        except ValueError as e:
            print(str(e))

    if choice in ['1', '2']: cls()

    if choice == '1': market_buy_menu()
    elif choice == '2': market_sell_menu()
    else:
        print('-' * 80)
        return
        
# === End of Market Menu ===


# === Start of Market Buy Menu ===

def market_buy_menu():
    itemCount = market.buy.show_items()

    valid = False

    while valid is False:
        choice = input('> Enter item code that you want to buy: ')

        try:
            if choice == '': raise ValueError('> ❗ Item code may not be empty!\n')
            if not choice.isnumeric(): raise ValueError('> ❗ Item code must be a number!\n')

            choice = int(choice)

            if choice < 1 or choice > itemCount: raise ValueError('> ❗ Invalid item code!\n')

            valid = True

        except ValueError as e:
            print(str(e))

    valid = False

    while valid is False:
        quantity = input('> Enter quantity: ')

        try:
            if quantity == '': raise ValueError('> ❗ Quantity may not be empty!\n')    
            if not quantity.isnumeric(): raise ValueError('> ❗ Quantity must be a number!\n')

            quantity = int(quantity)
            if quantity < 1: raise ValueError('> ❗ Quantity must be at least 1!\n')

            valid = True

        except ValueError as e:
            print(str(e))

    print()
    
    item_name, item = market.buy.get_item(choice)

    if item_name == False:
        print('> ❗ There is no such item in the market!')
    else:
        total_price = item['price'] * quantity

        possible_to_buy = stats.expense(total_price)

        if possible_to_buy == False:
            print('> ❗ You do not have enough money to buy this item!')
        else:
            if item_name in ['Chicken', 'Cow']: 
                for i in range (quantity):
                    chicken_name = input('> 🐔 What do you want to name?: ').title()
                    pass
                    
            else: 
                inventory.list[item_name]['quantity'] += quantity
                
            print(f'> 💰 You bought {quantity} {item['icon']} {item_name} for {total_price} 🪙')

    print()
    
# === End of Market Buy Menu ===


# === Start of Market Sell Menu ===

def market_sell_menu():
    print('-' * 80)
    print(f'{"Sales Price":^80}')
    print('-' * 80)
    market.sell.print_price()
    print('-' * 80)

    valid = False
    while valid == False:
        choice = input('> ❓ Do you want to sell items (y/n)? ').lower()

        try:
            if choice == '': raise ValueError('> ❗ Choice may not be empty!\n')
            if choice not in ['y', 'n']: raise ValueError('> ❗ Invalid option!\n')

            valid = True

        except ValueError as e:
            print(str(e))
        
    if choice == 'y':
        print('-' * 80)
        print('> 📦 Items in Inventory:')
        itemCount = inventory.print_sellable_items()
        print('-' * 80)

        valid = False

    while valid is False:
        choice = input('> Enter item code that you want to sell: ')

        try:
            if choice == '': raise ValueError('> ❗ Item code may not be empty!\n')
            if not choice.isnumeric(): raise ValueError('> ❗ Item code must be a number!\n')

            choice = int(choice)

            if choice < 1 or choice > itemCount: raise ValueError('> ❗ Invalid item code!\n')

            valid = True

        except ValueError as e:
            print(str(e))
    
    valid = False

    while valid is False:
        quantity = input('> Enter quantity: ')

        try:
            if quantity == '': raise ValueError('> ❗ Quantity may not be empty!\n')    
            if not quantity.isnumeric(): raise ValueError('> ❗ Quantity must be a number!\n')

            quantity = int(quantity)
            if quantity < 1: raise ValueError('> ❗ Quantity must be at least 1!\n')

            valid = True

        except ValueError as e:
            print(str(e))

    print()
    
    item_name, item = market.sell.get_item(choice)

    if item_name == False:
        print('> ❗ There is no such item in your inventory!')
    else:
        if inventory.list[item_name]['quantity'] - quantity < 0:
            print('> ❗ You do not have enough of this item in your inventory!')
        else:
            total_price = item['price'] * quantity
            inventory.list[item_name]['quantity'] -= quantity
            stats.profit(total_price)
            print(f'> 💰 You sold {quantity} {item["icon"]} {item_name} for {total_price} 🪙')

    print()

# === End of Market Sell Menu ===

    
# === Start of Show Inventory Function ===

def show_inventory():
    print('-' * 80)
    print(f'{'📦 Inventory 📦':^80}')
    print('-' * 80)
    inventory.print_inventory()
    print('-' * 80)
    
# === End of Show Inventory Function ===


# === Start of User Stats Function ===

def show_stats():
    print('-' * 80)
    print(f'{'📊 Stats 📊':^80}')
    print('-' * 80)
    stats.print_statistic()
    print('-' * 80)

# === End of User Stats Function ===


# === Start of Barn Menu Function ===

def barn_menu():
    print('-' * 80)
    print(f'{"Barn 🐮":^80}')
    print('-' * 80)

    print('> 1. Chicken 🐔')
    print('> 2. Cow 🐮')
    print('> 3. Back to Main Menu 🏠')

    print('-' * 80)

    valid = False
    while valid == False:
        choice = input('> Enter menu number: ')

        try:
            if choice == '': raise ValueError('> ❗ Choice may not be empty!\n')
            if choice not in ['1', '2', '3']: raise ValueError('> ❗ Invalid option!\n')

            valid = True

        except ValueError as e:
            print(str(e))

    if choice == '1': chicken_barn_menu()
    # elif choice == '2': cow_menu()
    else:
        print('-' * 80)

# === End of Barn Menu Function ===


# === Start of Chicken Barn Menu Function ===

def chicken_barn_menu():
    print('-' * 80)
    print(f'{"Chicken Barn 🐔":^80}')
    print('-' * 80)
    chicken_count = chicken_barn.print_chicken_barn()
    print()
    print(f'Chicken Feed: {inventory.list["Chicken Feed"]["quantity"]}')

    print('-' * 80)

    print('What do you want to do?')
    print('1. Feed 🐔')
    print('2. Collect Eggs 🥚')
    print('3. Make Chicken Feed ')
    print('4. Back to Main Menu 🏠')
    print()

    valid = False

    while valid == False:
        choice = input('> Enter menu number: ')

        try:
            if choice == '': raise ValueError('> ❗ Choice may not be empty!\n')
            if choice not in ['1', '2', '3']: raise ValueError('> ❗ Invalid option!\n')

            valid = True

        except ValueError as e:
            print(str(e))

    if choice == '1': 
        cls()

        print('-' * 80)
        chicken_count = chicken_barn.print_chicken_barn()
        print()
        print(f'Chicken Feed: {inventory.list["Chicken Feed"]["quantity"]}')
        print('-' * 80)
        print()

        valid = False

        while valid == False:
            amount = input('> How many chickens do you want to feed? ')

            try:
                if amount == '': raise ValueError('> ❗ Amount may not be empty!\n')
                if not amount.isnumeric(): raise ValueError('> ❗ Amount must be a number!\n')

                amount = int(amount)
                if amount < 1: raise ValueError('> ❗ Amount must be at least 1!\n')

                valid = True

            except ValueError as e:
                print(str(e))

        if inventory.list['Chicken Feed']['quantity'] - amount < 0:
            print('> ❗ There are not enough Chicken Feed!')
        else:
            inventory.list['Chicken Feed']['quantity'] -= amount
            for i in range(amount):
                valid = False

                while valid == False:
                    chicken = input('> Which chicken do you want to feed? ')

                    try:
                        if chicken == '': raise ValueError('> ❗ Choice may not be empty!\n')
                        if not chicken.isnumeric(): raise ValueError('> ❗ Choice must be a number!\n')

                        chicken = int(chicken)
                        if chicken < 1 or chicken > chicken_count: raise ValueError('> ❗ Invalid choice!\n')

                        valid = True
                    
                    except ValueError as e:
                        print(str(e))
                
                chicken_name = chicken_barn.feed_chickens(chicken)
                print(f'> {chicken_name} has been fed.')
                print()
                
        
    elif choice == '2':
        amount = chicken_barn.collect_eggs()

        print()
        if amount == 0: print('> ❗ There are no eggs to collect.')
        else: print(f'> You have collected {amount} eggs.')
        print()
    
    elif choice == '3':
        print(f'Chicken Feed Left in Inventory: {inventory.list["Chicken Feed"]["quantity"]}')
        
        valid = False

        while valid == False:
            choice = input('> Do you want to make chicken feed? (y/n) ')

            try:
                if choice == '': raise ValueError('> ❗ Choice may not be empty!\n')
                if choice not in ['y', 'n']: raise ValueError('> ❗ Invalid option!\n')

                valid = True

            except ValueError as e:
                print(str(e))

        valid = False

        while valid == False:
            amount = input('How many corns do you want to use to make chicken feed? ')

            try:
                if amount == '': raise ValueError('> ❗ Amount may not be empty!\n')
                if not amount.isnumeric(): raise ValueError('> ❗ Amount must be a number!\n')

                amount = int(amount)
                if amount < 1: raise ValueError('> ❗ Amount must be at least 1!\n')

                valid = True

            except ValueError as e:
                print(str(e))
        
        if inventory.list['Corn']['quantity'] - amount < 0:
            print('> ❗ There are not enough corns!')
        else:
            inventory.list['Corn']['quantity'] -= amount
            produced_feed_count = chicken_barn.make_feed(amount)
            inventory.list['Chicken Feed']['quantity'] += produced_feed_count
            print(f'> You have made {produced_feed_count} chicken feed.')
            
    elif choice == '4':
        print('-' * 80)


if __name__ == '__main__':
    while True:
        cls()

        print('-' * 80)
        print(f'{'🌽 Welcome to PyFarm 🌽':^80}')
        print('-' * 80)
        print(f'Coins: {stats.money} 🪙')
        print(f'Day: {stats.day}')
        print('-' * 80)

        print('> 1. Farm 🌽')
        print('> 2. Barn 🐮')
        print('> 3. End the Day (Go to Next Day) 🌙')
        print('> 4. Market 🏪')
        print('> 5. Inventory 📦')
        print('> 6. Statistic 📊')
        print('> 7. Exit ⛔')

        print('-' * 80)

        choice = input('> Enter menu number: ')

        if choice in ['1', '2', '4', '5', '6']: cls()

        if choice == '1':
            farm_menu()
        elif choice == '2':
            barn_menu()
        elif choice == '3':
            end_day()
        elif choice == '4':
            market_menu()
        elif choice == '5':
            show_inventory()
        elif choice == '6':
            show_stats()
        elif choice == '7':
            print('> Thank you for playing 🎉\n')
            break
        else:
            print('Invalid option!')

        input('> Press any key to continue...')
