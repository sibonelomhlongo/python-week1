
list=['Monty Python' if n % 6 == 0 else 'Python' if n % 3 == 0 else 'Monty' if n % 2 == 0 else n for n in range(1, 10)]
print(list)
n=5

for i in range(n):
    for j in range(n-1-i):
        print('',end=' ')
    for j in range(i+i+1):
        print('*',end='')
    print()
for i in range(n,9):
    for j in range(i-4):
        print('',end=' ')
    for j in range(7-j*2):
        print('*',end='')
    print()

    
from datetime import datetime
datetime.now()
wait_until = datetime.now().second + 2 
while datetime.now().second != wait_until: 
    print('Still waiting!') 
    print(f'We are at {wait_until} seconds!')
    break
