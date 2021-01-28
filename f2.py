#2. Készíts egy programot, ami bekér egy számot a felhasználótól, majd kiírja, hogy a megadott szám páros-e vagy páratlan!

a = int(input("Kérnék egy számot: "))

if a % 2 == 0:
    print("ez a szám páros ")
else:
    print("ez a szám páratlan ")