## init 
import numpy as np
import random
class Settings: 
    def __init__(self, ln, wd):
        self.ln = ln # length
        self.wd = wd # width
        

    def initField(self): 
        limit = 40
        field = np.zeros(100).reshape(self.ln, self.wd)        
        counter = 0
        
        #Field
        try:
            while counter != limit: # заповнення середовища (перша ітерація)        
                x = random.randint(0,9) # замінити х та у 
                y = random.randint(0,9)

                field[x,y] = 1 
                counter += 1
            print(field)
        except:
            print('Init field error')

        #NewField
        try:
            newField = np.zeros(100).reshape(10,10)
            newField[x,y] 
        except:
            print('Init newField ahtung')
        pass 