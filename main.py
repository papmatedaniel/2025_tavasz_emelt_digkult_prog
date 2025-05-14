with open("jeladas.txt", "r", encoding="UTF-8") as file:
    adatok = []
    for i in file.readlines():
        adatok.append([])
        sor = i.strip().split("\t")
        szamok = list(map(int, sor[1:4]))
        adatok[-1].append(sor[0])
        adatok[-1].extend(szamok)

print("2. feladat: ")
print(f"Az utolsó jeladás időpontja {adatok[-1][1]}:{adatok[-1][2]}, a jármű rendszáma {adatok[-1][0]} ")

print("3. feladat:")
elsokocsiidopontok = {adatok[0][0]:[]}
for i in adatok:
    if i[0] in elsokocsiidopontok.keys():
        elsokocsiidopontok[i[0]].append(i[1:3])

for i in elsokocsiidopontok.keys():
    print(f"Az első jármű: {i} ")
    print("Jeladásainak időpontjai: ", end="")
    for j in elsokocsiidopontok[i]:
        print(*j, sep=":", end=" ")

print("\n4. feladat: ")
ora = int(input("Kérem, adja meg az órát: "))
perc = int(input("Kérem, adja meg a percet: "))
szamlalo = sum(1 for i in adatok if i[1] == ora and i[2] == perc)
print(f"A jeladások száma: {szamlalo}")

print("5. feladat")
legnagyobbsebesseg = max(i[3] for i in adatok)
legnagyobbjarmuvek = [i[0] for i in adatok if i[3] == legnagyobbsebesseg]
print(f"A legnagyobb sebesség km/h: {legnagyobbsebesseg}")
print("A járművek: ", *legnagyobbjarmuvek, sep=" ")

print("\n6. feladat: ")
rendszam = input("Kérem, adja meg a rendszámot: ")
idopontok = [i[1:4] for i in adatok if i[0] == rendszam]
if len(idopontok) != 0:
    tav = 0.0
    for i in range(len(idopontok)-1):
        print(f"{idopontok[i][0]}:{idopontok[i][1]} {tav} km")
        idopontkulnbseg_percben = (idopontok[i+1][0] * 60 + idopontok[i+1][1]) - (idopontok[i][0] * 60 + idopontok[i][1])
        tav = round(tav + (idopontkulnbseg_percben / 60) * idopontok[i][2], 1)
else:
    print("Nincs ilyen rendszám")

print(f"{idopontok[i+1][0]}:{idopontok[i+1][1]} {tav} km")
elso_utolsoidok = dict()
for i in adatok:
    if i[0] in elso_utolsoidok.keys():    
        elso_utolsoidok[i[0]].append(i[1:3])
    else:
        elso_utolsoidok[i[0]] = [i[1:3]]


with open("ido.txt", "w", encoding="UTF-8") as file:
    for i in elso_utolsoidok.items():
        file.write(f"{i[0]} {i[1][0][0]} {i[1][0][1]} {i[1][-1][0]} {i[1][-1][1]}\n")



# Elkeszitesi ido: 1 ora 10 perc