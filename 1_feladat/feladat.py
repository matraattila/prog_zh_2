eloado_pont = dict()

while True:
    try:
        sor = input().split(":")
        pont = int(sor[2])
        eloado = sor[1]

        try:
            eloado_pont[eloado] += pont
        except KeyError:
            eloado_pont[eloado] = pont
    except:
        break

# Csökkenő sorrendbe rendezés, pontszám alapján
sorted_dict = sorted(eloado_pont.items(), key=lambda kv: (kv[1]), reverse=True)

pont_eloadok = dict()
for eloado,pont in sorted_dict:
    if pont not in pont_eloadok:
        pont_eloadok[pont] = [eloado]
    else:
        if eloado not in pont_eloadok[pont]:
            pont_eloadok[pont].append(eloado)

for key,value in pont_eloadok.items():
    print("{0} ({1}) :".format(key, len(value), ":"), end=" ")
    print(', '.join(value), end=" ")
    print()