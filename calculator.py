
x = float(input())
y = float(input())
c = input()
if c == '/' and y == 0:
    print ('Деление на 0!')
elif c == '/' and y != 0:
    print (x/y)
if c == 'div' and y == 0:
    print('Деление на 0!')
elif c == 'div' and y != 0:
    print (x//y)
if c == 'mod' and y == 0:
    print('Деление на 0!')
elif c == 'mod' and y != 0:
    print (x%y)
elif c == 'pow':
    print (x**y)    

elif c == '*':
    print (x*y)
    
elif c == '+':
    print (x+y)
  
elif c == '-':
    print (x-y)