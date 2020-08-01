class calc:
    def add(n1,n2):
        return n1+n2
    
    def sub(n1,n2):
        return n1-n2
    
    def mul(n1,n2):
        return n1*n2
    
    def div(n1,n2):
        return n1/n2
    
    def moddiv(n1,n2):
        return n1%n2
    
    def power(n1,n2):
        return n1**n2
    
    
    
    
class Math:
    def IsEven(num):
        if num%2==0:
            return True
        else:
            return False
        
    def IsOdd(num):
        if num%2!=0:
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
    
    
    
        