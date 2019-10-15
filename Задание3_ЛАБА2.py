a=1997
if a%4!=0:
    print('НЕВИСОКОСНЫЙ')
elif a%4==0 and a%100!=0:
    print('ВИСОКОСНЫЙ')
elif a%100==0 and a%400==0:
    print('ВИСОКСНЫЙ')
else:
    print('НЕВИСОКОСНЫЙ')
