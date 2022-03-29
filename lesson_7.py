import string 
import random


class Password:
    EASY_LIST = string.ascii_letters
    MEDIUM_LIST = EASY_LIST + ''.join([str(i) for i in range(10)])
    HARD_LIST = MEDIUM_LIST + string.punctuation

    def easy(self):
        return ''.join([random.choice(self.EASY_LIST) for _ in range(8)])

    def medium(self):
        return ''.join([random.choice(self.MEDIUM_LIST) for _ in range(10)])
    
    def hard(self):
        return ''.join([random.choice(self.HARD_LIST) for _ in range(12)])
p = Password()

print(p.easy())
print(p.medium())
print(p.hard())