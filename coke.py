def due(y):
    d_a= 50-y
    while d_a > 0:
            print('Amount Due:',d_a)
            n_i= insert_amount()
            d_a= d_a - n_i
            if d_a <= 0:
                 return d_a

def owed(d_a):
    if d_a == 0:
         print(f'Change Owed: {d_a}')
    else:
         d_a= 0 - d_a
         print(f'Change Owed: {d_a}')


def insert_amount():
    x= int(input('insert coin: '))
    accepted_amount= [5,10,25]
    if x in accepted_amount:
         return x
    else:
         return 0

def main():
    inserted_amount= insert_amount()

    d_a= due(inserted_amount)
    if d_a <= 0:
        owed(d_a)


main()
