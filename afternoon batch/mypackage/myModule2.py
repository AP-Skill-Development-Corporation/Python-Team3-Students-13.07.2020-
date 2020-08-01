def Leapyear1(lower,upper):
    for year in range(lower,upper+1):
        if year % 400 ==0 or(year % 100!=0 and year %4==0):
            print(year,"leapyear")
        else:
            print(year,"not leapyear")
            
            
            
            
            
            
            
            
class classname:
    def Leapyear(lower,upper):
        for year in range(lower,upper+1):
            if year % 400 ==0 or(year % 100!=0 and year %4==0):
                print(year,"leapyear")
            else:
                print(year,"not leapyear")
                      