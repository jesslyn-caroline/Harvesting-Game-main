import os
import random

from field import Farm, Seeds
from day import Day
from user import User
from market import UpcomingItem, Market
from inventory import Inventory
from chicken import Chicken
from barn import Barn

day = Day()
farm = Farm()
seeds = Seeds()
upcoming_item = UpcomingItem() # To update market items
market = Market()
inventory = Inventory()
user = User()
barn = Barn()

def cls(): os.system('cls' if os.name == 'nt' else 'clear')

# ==== Start of Farm ==== #

def farm_menu():
    print('-' * 80)
    print(f'{'🌽 Farm 🌽':^80}')
    print('-' * 80)
    print()

    farm.print_field()
    seeds.print_seeds_list()

    seed_count = 0
    for seed in seeds.list:
        seed_count += seed['quantity']
    
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
            if int(seed_code) < 1 or int(seed_code) > seeds.count: raise ValueError('> ❗ Invalid seed code!\n')
            seed_code = int(seed_code)
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
            if int(row) < 1 or int(row) > farm.size: raise ValueError('> ❗ Invalid row number!\n')
            row = int(row) - 1
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
            if int(col) < 1 or int(col) > farm.size: raise ValueError('> ❗ Invalid column number!\n')
            col = int(col) - 1
            valid = True
        except ValueError as e:
            print(str(e))
        
    print()

    valid = farm.plant_seed(row, col, seed_code, seeds.list[seed_code - 1]['name'])
    print('-' * 80)
    print()

    if valid:
        seeds.list[seed_code - 1]['quantity'] -= 1
        farm.print_field()
    
    print('-' * 80)

# ==== End of Farm ==== #


# ==== Start of End Day ==== #

def end_day():
    print()
    print(f'> 🌙 End of Day {day.get_day()}')
    day.next_day()
    print(f'> 🌞 Start of Day {day.get_day()}')
    print()

    upcoming_item_list = upcoming_item.check_unlocked_items(day.get_day())
    market.buy.update_item(upcoming_item_list)

    corn_price = random.randint(30, 45)
    potato_price = random.randint(45, 70)
    tomato_price = random.randint(45, 65)
    carrot_price = random.randint(50, 80)
    market.sell.update_price(corn_price, potato_price, tomato_price, carrot_price)

    user.statistic[day.get_day()] = []

    

    died_chicken = barn.check_chicken_status()
    for chicken in died_chicken:
        print(f'> 🐓 {chicken} has died out of starvation')

# ==== End of End Day ==== #


# ==== Start of Market ==== #

def market_menu():
    while True:
        cls()
        print('-' * 80)
        print(f'{'🏪 Market 🏪':^80}')
        print('-' * 80)
        print('1. Buy Items')
        print('2. Sell Items')
        print('3. Exit Market')
        print('-' * 80)

        valid = False
        while not valid:
            try:
                choice = input('> Enter menu number: ')

                if choice == '': raise ValueError('> ❗ Choice may not be empty!\n')
                if choice not in ['1', '2', '3']: raise ValueError('> ❗ Invalid option!\n')
                valid = True

            except ValueError as e:
                print(str(e))


        if choice == '1':
            cls()

            still_buying = True
            while still_buying:
                market.buy.check_items()
                
                valid = False
                while not valid:
                    try:
                        choice = input('> ❓ Do you want to buy item? (y/n): ').lower()
    
                        if choice == '': raise ValueError('> ❗ Choice may not be empty!\n')
                        if choice not in ['y', 'n']: raise ValueError('> ❗ Invalid option!\n')
                            
                        valid = True
    
                    except ValueError as e:
                        print(str(e))
    
                print()
                
                if choice == 'n': 
                    still_buying = False
                    break
                    
                valid = False
                while not valid:
                    try:
                        choice = input('> Enter item number: ')
                        if choice == '': raise ValueError('> ❗ Choice may not be empty!\n')
                        if not choice.isnumeric(): raise ValueError('> ❗ Choice must be a number!\n')
                        if int(choice) < 1 or int(choice) > len(market.buy.items): raise ValueError('> ❗ Out of choices, please enter the correct number!\n')
                        valid = True
    
                    except ValueError as e:
                        print(str(e))
    
                print()
    
                valid = False
                while not valid:
                    try:
                        amount = input('> Enter the amount you want to buy: ')
                        if amount == '': raise ValueError('> ❗ Choice may not be empty!\n')
                        if not amount.isnumeric(): raise ValueError('> ❗ Invalid amount!\n')
                            
                        amount = int(amount)
                        if amount < 1: raise ValueError('> ❗ You must buy at least 1 seed!\n')
                        valid = True
    
                    except ValueError as e:
                        print(str(e))
    
                print()
    
                
                item_to_buy = market.buy.get_item(int(choice))
    
                possible_to_buy = False if user.money - (item_to_buy['price'] * amount) < 0 else True
    
                if not possible_to_buy:
                    print("Sorry, you don't have enough money to buy.")
                else:
                    user.expense(item_to_buy['price'] * amount)
                    user.update_seed(f'{item_to_buy['icon']} {item_to_buy['name']}', amount)
                    print(f'{item_to_buy['icon']} {item_to_buy['name']} seed(s) has been purchased. Total purchase: {item_to_buy['price'] * amount}')
                
                input('\n> Press any key to continue...')
                cls()

        elif choice == '2':
            cls()

            still_selling = True
            while still_selling:
                
                market.sell.check_price()
    
                valid = False
                while not valid:
                    try:
                        choice = input('> ❓ Do you want to sell item? (y/n): ').lower()
    
                        if choice == '': raise ValueError('> ❗ Choice may not be empty!\n')
                        if choice not in ['y', 'n']: raise ValueError('> ❗ Invalid option!\n')
                        valid = True
    
                    except ValueError as e:
                        print(str(e))
    
                print()
    
                if choice == 'n': 
                    still_buying = False
                    break
                
                possible_to_sell = inventory.print_inventory()
                if not possible_to_sell:
                    print("Sorry, you don't have crops or resources to sell")
                else:
                    item_to_sell = input('> 📦 Enter item to sell: ').lower()
                    if item_to_sell in possible_to_sell:
                        amount = input('> 📦 Enter amount of item to sell: ')
                        ## Need to be fixed
                    else:
                        print("You don't have that item to sell")
    
                input('\n> Press any key to continue...')
                cls()

        elif choice == '3':
            print('\nThank you for visiting our market!')

            break
        

# ==== End of Market ==== #


# ==== Start of Statistic ==== #

def statistic_menu():
    user.print_statistic_menu()

# ==== End of Statistic ==== #


# ==== Start of Barn Menu ==== #

def barn_menu():
    while True:
        print('-' * 80)
        print(f'{'🐮 Chicken Barn 🐮':^80}')
        print('-' * 80)
        
        print('> 1. Check Chicken List')
        print('> 2. Feed Chicken')
        print('> 3. Check Collectable Eggs')
        print('> 4. Go Back')

        print('-' * 80)

        valid = False
        while not valid:
            try:
                choice = input('> Enter your choice: ')
                if choice == '': raise ValueError('> ❗ Choice may not be empty!\n')
                if not choice.isnumeric(): raise ValueError('> ❗ Choice must be a number!\n')
                if int(choice) < 1 or int(choice) > 4: raise ValueError('> ❗ Out of choices, please enter the correct number!\n')
                valid = True

            except ValueError as e:
                print(str(e))
        
        cls()
        if choice == '1':
            barn.print_chicken_barn()

        elif choice == '2':
            barn.feed_chicken()
            print('Feeding chicken')

        elif choice == '3':
            collectible_eggs = barn.collect_eggs()
            print(f'You collect {collectible_eggs} eggs')

        elif choice == '4':
            print('Going back...')
            break

        if choice in ['1', '2', '3']:
            input('> Press any key to continue...')
        
        cls()

# ==== End of Barn Menu ==== #


# ==== Pre Program ==== #

upcoming_item_list = upcoming_item.check_unlocked_items(day.get_day())
market.buy.update_item(upcoming_item_list)

corn_price = random.randint(30, 45)
potato_price = random.randint(45, 70)
tomato_price = random.randint(45, 65)
carrot_price = random.randint(50, 80)
market.sell.update_price(corn_price, potato_price, tomato_price, carrot_price)

chick = Chicken("Chic")
barn.add_chicken(chick)

# ==== Main  Program ==== #

while True:
    cls()
    
    print('-' * 80)
    print(f'{'🌽 Welcome to PyFarm 🌽':^80}')
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

    if choice in ['1', '2', '3', '4', '5', '6', '7']: cls()

    if choice == '1':
        farm_menu()
    if choice == '2':
        barn_menu()
    elif choice == '3':
        end_day()
    elif choice == '4':
        market_menu()
    elif choice == '6':
        statistic_menu()
    elif choice == '7':
        print('> Thank you for playing 🎉\n')
        break
    else:
        print('Invalid option!')
    
    input('> Press any key to continue...')
