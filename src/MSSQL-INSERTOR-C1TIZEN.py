import random
lang = input("Language - 'EN' / 'SK': ")
if lang.lower() == "sk":
    naz_tab = input("Napíš názov tabuľky: ")
    print("~" * 20)
    print("Napíš názvy stĺpcov do ktorých chceš doplniť údaje 'meno priezvisko cislo'")
    poc_pol = input("Ak je stĺpec UNIQUE tak pred hodnotu napíš 'UQ' napr. 'UQid_kontakt': ")
    poc_zoz = poc_pol.split(" ")
    poc_ud = int(input("Zadaj počet riadkov údajov pre tabuľku: "))
    print("Zadaj hodnoty z ktorých bude program náhodne generovať kombinácie (ľubovoľný počet) napr. 'Tomáš Viktor Patrik'")
    fin_doc = []
else:
    naz_tab = input("Name of table: ")
    print("~"*20)
    print("Name all columns you want use 'name city p_num'")
    poc_pol = input("If column is UNIQUE use 'UQ' in front of the name e.g. 'UQid_person': ")
    poc_zoz = poc_pol.split(" ")
    poc_ud = int(input("Number of inserts: "))
    print("Enter values for random selection (any number) e.g. 'Thomas Victor Patric'")
    fin_doc = []
switCh = False
for j in range(len(poc_zoz)):
    zoz_pol = []
    print(f"$ {poc_zoz[j]}")
    doc = input()
    roz = doc.split(" ")
    for x in range(poc_ud):
        if poc_zoz[j][:2] == "UQ":
            if not switCh:
                if len(roz) < poc_ud:
                    if lang.lower() == "sk":
                        print(f"ERROR: Nie je dostatok údajov pre '{poc_zoz[j]}'")
                        res_req = input("Program spusť znova.")
                    else:
                        print(f"ERROR: Not enough values for '{poc_zoz[j]}'")
                        res_req = input("Start a new instance of program and try again.")
            chdd = random.choice(roz)
            zoz_pol.append(f"'{chdd}'")
            roz.remove(chdd)
            switCh = True
        else:
            zoz_pol.append(f"'{random.choice(roz)}'")
    fin_doc.append(zoz_pol)

print("~"*20)
flipper3d = [list(row) for row in zip(*reversed(fin_doc))]

for i in range(len(flipper3d)):
    flipper3d[i].reverse()
    print(f"INSERT INTO {naz_tab} ({','.join(poc_zoz)}) VALUES ({','.join(flipper3d[i])})")
print("~~~ Made by c1tizen with <3 ~~~")
if lang.lower() == "sk":
    skip = input("Stlačením ENTER sa program zatvorí...")
else:
    skip = input("Press ENTER to exit...")
