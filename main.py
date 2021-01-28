#3. Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.
import random
i = (random.randrange(1,6))
a = int(input("kérem a számot: "))

if a == i:
    print("a szám egyenlő")
elif a < i:
    print("kisebb")
else:
    print("nagyobb")
    
print(i , "számra gondoltam")