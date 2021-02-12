import random
import time


print(f'Discord: волшебник#0001')

keys = 1

print(f'Starting generation: 100 keys')
print(f'Waiting...')

while True:


    one = random.randint(1,9)
    two = random.randint(1,9)
    three = random.randint(1,9)
    four = random.randint(1,9)
    five = random.randint(1,9)
    six = random.randint(1,9)

    digits1 = one + two + three + four + five + six

    day = random.randint(111,365)
    year = random.randint(95,99)
    rand = random.randint(10000,99999)




    if digits1 % 7 == 0:
            keys +=1
            digits = (f"{one}{two}{three}{four}{five}{six}")
            my_file = open("keys.txt", 'a')
            my_file.write(f"{day}{year}-OEM-0{digits}-{rand}\n")
            
            my_file.close()
            
            if keys == 100:
                    print(f"Done!")
                    break


    