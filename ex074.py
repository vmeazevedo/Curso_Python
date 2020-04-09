import random

r1 = random.randint(0,10)
r2 = random.randint(0,10)
r3 = random.randint(0,10)
r4 = random.randint(0,10)
r5 = random.randint(0,10)

print(f'Os valores sorteador foram: {r1} {r2} {r3} {r4} {r5}')
rt = (r1,r2,r3,r4,r5)
print(f'O maior valor sorteado foi {max(rt)}')
print(f'O menor valor sorteado foi {min(rt)}')