import math
class MathHelper(object):
    def __init__(self):
        pass

    @classmethod
    def from_string(self,para):
        return int(para)
        
    @staticmethod
    def is_prime(para):
        for i in range(para):
            if i == 0 or i == para - 1:
                continue
            if para%(i+1)==0:
                return False
        return True

        
    
# print(MathHelper.from_string("1"))
print(MathHelper.is_prime(12))