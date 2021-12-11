import random
poc_t = int(input("Zadaj počet tabuliek na zadanie údajov: "))
fin_prnt = {}
udajomet = []
for i in range(poc_t):
    print()
    print(f"Tabuľka číslo {i+1}")
    print("~"*15)
    print("Napíš názvy stĺpcov do ktorých chceš doplniť údaje (meno ulica cislo)")
    poc_pol = input("Ak je stĺpec UNIQUE tak pred hodnotu napíš 'UQ' napr. 'UQtel_cislo':")
    poc_ud = int(input("Zadaj počet riadkov údajov pre tabuľku:"))
    udajomet.append(poc_ud)
    poc_zoz = poc_pol.split(" ")
    print("Zadaj hodnoty z ktorých bude program náhodne generovať kombinácie (ľubovoľný počet) napr. Tomáš Viktor Patrik")
    fin_doc = {}
    for j in range(len(poc_zoz)):
        zoz_pol = []
        print(f"$ {poc_zoz[j]}")
        doc = input()
        roz = doc.split(" ")
        for x in range(poc_ud):
            if poc_zoz[j][:1] == "UQ":
                if len(roz) == poc_ud:
                    zoz_pol.append(random.choice(roz))
                    roz.remove(zoz_pol[-1])
                else:
                    print(f"ERROR: Nie je dostatok údajov pre '{poc_zoz[j]}'")
            else:
                zoz_pol.append(random.choice(roz))
        fin_doc.update({poc_zoz[j]: zoz_pol})
    fin_prnt.update({i + 1: fin_doc})

print(fin_prnt)
print("~"*18)
print("Vyber si spôsob výpisu:")
print("1 - https://i.ibb.co/3zRQBMm/prvy.png")
print("2 - https://i.ibb.co/2NyMC5t/druhy.png")
fr = int(input())
# {1: {'fe': ['io', 'op'], 'we': ['yu', 'yu']}, 2: {'cv': ['rt', 'er'], 'hj': ['df', 'fg']}}
print(poc_t)
if fr == 2:
    for i in range(poc_t):
        # print(",".join(d.keys()))
        peto = f"INSERT INTO tabulka{i+1} ({','.join(fin_prnt.get(i+1).keys())})"
        for x in range(udajomet[i]):
            # res = list(test_dict.keys())[0]
            dood = ""
            for y in range(len(fin_prnt.get(i+1).keys())):
                dood += f"{fin_prnt.get(i+1)[y]}"
            print(f"{peto} VALUES ({','.join(list(fin_prnt.get(i+1).values())[0])})")
        #.keys())[1:-1]  ({str(fin_prnt[i])})
elif fr == 1:
    print(f"nie")
