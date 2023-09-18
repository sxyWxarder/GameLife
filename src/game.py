'''
Основна логіка гри, 
'''

import settings
import time

class Game:   
    def gameField(self):   # перевірка діапазону
        init = settings.initField(10,10)
        init.initField()
        try:
            while True:
                for x in range(9): 
                    for y in range(9):
                        up = init.field[x-1,y] if x > 0 else 0 # up     
                        left = init.field[x,y-1] if y > 0 else 0  # left
                        down = init.field[x+1,y] if x < 9 else 0  # down 
                        right = init.field[x,y+1] if x < 9 else 0   # right 
                        ul = init.field[x-1, y-1] if x > 0 and y > 0 else 0#up left
                        ur = init.field[x-1, y+1] if x > 0 and y < 9 else 0# up right
                        dl = init.field[x+1,y-1] if x < 9 and y > 0 else 0 # down left
                        dr = field[x+1,y+1]  if x < 9 and y < 9 else 0# down right 
                               
                        sum = up + left + down + right + ul + ur + dl + dr
        except:
            print('Check cell Аhtung')
       
            # Rules
            # Баг
            try:
                #init NewField (newStep )
                for x in range(9):
                    for y in range(9):
                                # Field
                            if sum == 2 or 3:   
                                init.newField[x,y] = 1# лишається жити
                            
                            if sum <=1:
                                init.newField[x,y] = 0#помирає від самотності
                                
                            if sum >= 4:
                                init.newField[x,y] = 0 
                                 # помирає від перенаселення
                            if sum == 3: # оживає 
                                if init.field[x,y] == 0:
                                    self.init.newField[x,y] = 1 
                                    
            except:
                print('Game rules Ahtung')
           
            init.field = init.newField
            time.sleep(3)     
            print(init.field)