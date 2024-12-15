class User:
    def __init__(self):
        self.money = 500
        self.tools = ['Hoe', 'Watering Can']
        self.seeds = dict()
        self.statistic = {1: {"Profit": 0, "Expense" : 0}}

    def profit(self, amount):
        self.money += amount
        self.statistic[len(self.statistic)]["Profit"] += amount
    
    def expense(self, amount):
        self.money -= amount
        self.statistic[len(self.statistic)]["Expense"] += amount
    
    def add_tool(self, tool):
        self.tools.append(tool)
    
    def update_seed(self, seed, amount):
        if seed not in self.seeds.keys():
            self.seeds[seed] = amount
        else:
            self.seeds[seed] += amount
    
    def print_statistic_menu(self):
        print('-' * 80)
        print(f'{'📊 Statistic 📊':^80}')
        print('-' * 80)
        print()
        print(f'> 💰 Money: {self.money}')
        print()
        print(f'> 🛠️ Tools: ')
        for i in self.tools:
            print(f'{i}')
        print()
        print(f'> 🫘 Seeds: ')
        if len(self.seeds) == 0:
            print('You dont have any seeds.')
        else:
            for i in self.seeds.keys():
                print(f'{i}: {self.seeds[i]}')
        print()
        print(f'> 🧾 Profit and Expense History: ')
        for i in self.statistic.keys():
            print(f'Day {i}: ')
            print(f'Profit: {self.statistic[i]["Profit"]}')
            print(f'Expense: {self.statistic[i]["Expense"]}')
        print()
        print('-' * 80)
