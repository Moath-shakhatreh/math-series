def febonacci (n):
 '''
This function take a number and return a number
 from febonacci series it's location
specefied by the number that the funcion taked  
 '''
 if n <= 1:
    return n
 else:
    return febonacci(n-1) + febonacci(n-2)
 


def lucas(n):
 '''
This function take a number and return a number
 from lucas series it's location
specefied by the number that the funcion taked  
 '''
 if n==0:
  return 2
 elif n==1 :
  return 1
 else :
  return lucas(n-1) + lucas(n-2)
 

 

def sum (n,a=0,b=1):
 '''
  This function take three arguments the last two speciefy the series type 
 and the first argument specify the location of the number in the series 
 that the function return it
 '''
 if n==0:
   return a
 elif n==1 :
   return b
 elif n>1 :
   return sum(n-1,a,b) + sum (n-2,a,b)