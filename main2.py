# 16:00

adatok = []
with open("./e_digkultfor_25maj_fl/3_Konyvkiadas/kiadas.txt", "r", encoding="UTF-8") as file:
    for sor in file.readlines():
        szeletek = sor.strip().split(";")
        ev, honap, *egyebb = szeletek
        *szoveg, szam = egyebb
        adatok.append([int(ev), int(honap), *szoveg, int(szam)])

# 16:10

print("2. feladat:")
szerzo = input("Szerző: ")
kiadas_szamlalo = sum(1 for i in adatok if szerzo in i[3])

if kiadas_szamlalo == 0:
    print("Nem adtak ki")
else:
    print(f"{kiadas_szamlalo} könyvkiadás")

print("3. feladat:")
legnagyobbkiadas = max(i[-1] for i in adatok)
legnagyobbkiadas_szama = sum(1 for i in adatok if i[-1] == legnagyobbkiadas)
print(f"Legnagyobb példányszám: {legnagyobbkiadas}, előfordult {legnagyobbkiadas_szama} alkalommal ")

print("4. feladat:")
for i in adatok:
    if i[2] == "kf" and i[-1] >= 40000:
        print(f"{i[0]}/{i[1]}. {i[3]} ")
        break

print("5. feladat:")
statisztika = {}
for i in adatok:
    if i[0] in statisztika.keys():
        if i[2] == "ma":
            statisztika[i[0]]["mk"] += 1
            statisztika[i[0]]["mp"] += i[-1]
        else:
            statisztika[i[0]]["kk"] += 1
            statisztika[i[0]]["kp"] += i[-1]
    
    else:
        statisztika[i[0]] = {
            "mk": 1,
            "mp": i[-1] if i[2] == "ma" else 0,
            "kk": 1, 
            "kp": i[-1] if i[2] == "kf" else 0
        }

with open("tabla.html", "w", encoding="UTF-8") as file:
    print("<table>", file=file)
    print("Év\tMagyar kiadás\tMagyar példányszám\tKülföldi kiadás\tKülföldi példányszám")
    print("<tr><th>Év</th><th>Magyar kiadás</th><th>Magyar példányszám</th><th>Külföldi \
kiadás</th><th>Külföldi példányszám</th></tr>", file=file)
    
    for key, value in statisztika.items():
        print(f'{key}\t\t{value["mk"]}\t\t{value["mp"]}\t\t{value["kk"]}\t\t{value["kp"]}')
        print(f'<tr><td>{key}</td><td>{value["mk"]}</td><td>{value["mp"]}</td><td>{value["kk"]}</td><td>{value["kp"]}</td></tr> ', file=file)

    print("</table>", file=file)
print("6. feladat")
konyvstatisztika = {}
for i in adatok:
    if i[3] in konyvstatisztika.keys():
        konyvstatisztika[i[3]].append(i[-1])
    else:
        konyvstatisztika[i[3]] = [i[-1]]

print("Legalább kétszer, nagyobb példányszámban újra kiadott könyvek: ")
for k, v in konyvstatisztika.items():
    if len(v) >= 3 and v[0] < v[1] and v[0] < v[2]:
        print(k)

# 16:49

# +5 perc, mert most jöttem rá, hogy a html-be html elemként kellettt beírni az adatokat...
