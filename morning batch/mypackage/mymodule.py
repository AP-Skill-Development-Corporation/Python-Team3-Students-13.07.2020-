class calc:
    def add(num1,num2):
        return num1+num2
    
    def sub(num1,num2):
        return num1-num2
    
    def mul(num1,num2):
        return num1*num2
    
    def div(num1,num2):
        return num1/num2
    
    def moddiv(num1,num2):
        return num1%num2
    
    def power(num1,num2):
        return num1**num2
    
    
    

    
class Math:
    def IsEven(num3):
        if num3%2==0:
            return True
        else:
            return False
        
        
    def IsOdd(num4):
        if num4%2!=0:
            return True
        else:
            return False
        
        
        
        
        
class mycalc:
    def __init__(self,val1,val2):
        self.val1=val1
        self.val2=val2
        
        
    def __add__(self):
        return self.val1+self.val2
    
    
    def __sub__(self):
        return self.val1-self.val2
     
        
    def __mul__(self):
        return self.val1*self.val2
    
    def __div__(self):
        return self.val1/self.val2
    
    def __moddiv__(self):
        return self.val1%self.val2
        
    
    def __power__(self):
        return self.val1**self.val2
        
        
        
        
      
        
        
        
    
    