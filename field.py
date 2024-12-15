class Square:
    def __init__(self, plant = None):
        self.plant = None if plant is None else f"{plant['icon']} {plant['name']}" # Change to plant name if the square has already planted
        self.day_water = 0 
        self.grow_time = None if plant is None else plant['grow_time']


class Farm:
    def __init__(self):
        self.size = 3
        self.field = [[Square() for _ in range(self.size)] for _ in range(self.size)]

    def water_field(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.field[r][c].plant is not None:
                    self.field[r][c].day_water += 1

    def harvest_crop(self):
        harvested_crop = dict()
        for r in range(self.size):
            for c in range(self.size):
                if self.field[r][c].grow_time is not None and self.field[r][c].day_water >= self.field[r][c].grow_time:
                    if self.field[r][c].plant not in harvested_crop.keys():
                        harvested_crop[self.field[r][c].plant] = 1
                    else: harvested_crop[self.field[r][c].plant] += 1
    
    # def update_field(self):
    #     seeds = Seeds()
    #     for r in range(self.size):
    #         for c in range(self.size):
    #             if self.field_detail[r][c] != 0:
    #                 self.field_day[r][c] += 1
    #             if self.field_day[r][c] == seeds.list[self.field_detail[r][c] - 1]['grow_time']:
    #                 self.field[r][c] = seeds.list[self.field_detail[r][c] - 1]['icon']
    
    def print_field(self):
        print(f'> 🌽 Current field size: {self.size} x {self.size}\n')

        detail = {
            "No seed": [],
            "Growing": dict(),
            "Ready to harvest": dict()
        }
        for row in self.field:
            for col in row:
                if col.plant is None:
                    detail["No seed"].append((col, row))
                    print(f'[ 🟤 ]', end=" ")
                else:
                    if col.day_water < col.grow_time:
                        if col.plant not in detail['Growing'].keys():
                            detail['Growing'][col.plant] = []
                        detail['Growing'][col.plant].append((col, row))
                        print(f'[ 🌱 ]', end=" ")
                    else:
                        if col.plant not in detail['Ready to harvest'].keys():
                            detail['Ready to harvest'][col.plant] = []
                        detail['Ready to harvest'][col.plant].append((col, row))
                        print(f'[ {col.plant[0]} ]', end=" ")
            print()
        print()
        print(f'🟤 No seed ({len(detail["No seed"])}):')
        print()

        print(f'🌱 Growing ({len(detail["Growing"])}):')
        for i in detail['Growing']:
            print(f'- {i}:')
            for j in detail['Growing'][i]:
                print(f'  - {j[0].plant}')

        print()

        print(f'🌽 Ready to harvest ({len(detail["Ready to harvest"])})')
        for i in detail["Ready to harvest"]:
            print(f'- {i}:')
            for j in detail["Ready to harvest"][i]:
                print(f'  - {j[0].plant}')

        print()
        
        
    
    def plant_seed(self, row, col, seed_code, seed_name):
        if self.field_detail[row][col] == 0:
            self.field_detail[row][col] = seed_code
            self.field[row][col] = '🌱'
            print(f'> 🌱 {seed_name} seed planted successfully!')
            return True
        
        print('> 🌱 There is already a seed in this field.')
        return False
    
    def harvest(self):
        pass

class Seeds:
    def __init__(self):
        self.list = [
            {
                'code': 1,
                'name': 'Corn',
                'icon': '🌽',
                'grow_time': 3,
                'quantity': 3,
                'unlocked': True 
            },
            {
                'code': 2,
                'name': 'Potato',
                'icon': '🥔',
                'grow_time': 4,
                'quantity': 0,
                'unlocked': False
            },
            {
                'code': 3,
                'name': 'Tomato',
                'icon': '🍅',
                'grow_time': 4,
                'quantity': 0,
                'unlocked': False
            },
            {
                'code': 4,
                'name': 'Carrot',
                'icon': '🥕',
                'grow_time': 3,
                'quantity': 0,
                'unlocked': False
            }
        ]

        self.count = 0
        for seed in self.list:
            if seed['unlocked'] == True: self.count += 1
    
    def print_seeds_list(self):
        print('> 🌱 List of unlocked seed(s):')
        print('-' * 80)

        count = 0
        for seed in self.list:
            if seed['unlocked'] == False: continue
            count += 1
            print(f'> {count}. {seed['icon']} {seed['name']}: {seed['quantity']} seed(s) left.')
        
        print()
