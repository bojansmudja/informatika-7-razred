um0 = 0
print('Za poznatu masu rastvorene supstance i rastvora unesi 1')
print('Za poznatu masu rastvora i rastvaraca unesi 2')
print('Za poznatu masu rastvaraca i rastvorene supstance unesi 3')
um0 = int(input())             

if um0 == 1:
    num1 = 1
    num2 = 2
    def ratioFunction(num1, num2):
        num1 = input('Unesi masu rastvorene supstance: ')
        num1 = int(num1) 
        num2 = input('Unesi masu rastvora: ')
        num2 = int(num2) 
        ratio12 = float(num1/num2)
        print('Koncentracija rastvorene supstanceje', '{:.1%}'.format(ratio12) + '.')
    ratioFunction(num1, num2)

    
elif um0 == 2:
    num1 = 1
    num2 = 2
    def ratioFunction1(num1, num2):
        num1 = input('Unesi masu rastvora: ')
        num1 = int(num1) 
        num2 = input('Unesi masu rastvaraca: ')
        num2 = int(num2) 
        ratio12 = float((num1-num2)/num1)
        print('Koncentracija rastvorene supstanceje', '{:.1%}'.format(ratio12) + '.')
    ratioFunction1(num1, num2)

elif um0 == 3:
    num1 = 1
    num2 = 2
    num3 = 3
    def ratioFunction2(num1, num2, num3):
        num1 = input('Unesi masu rastvaraca: ')
        num1 = int(num1) 
        num2 = input('Unesi masu rastvorene supstance: ')
        num2 = int(num2)
        num3 = int(num1+num2)
        ratio12 = float(num2/num3)
        print('Koncentracija rastvorene supstanceje', '{:.1%}'.format(ratio12) + '.')
        print('Ukupna masa rasvora je ', num3)
    ratioFunction2(num1, num2, num3)

else:
    print('Unesite samo brojeve od 1 do 3')
