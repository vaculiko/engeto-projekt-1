kosik = {}
oddelovac = "=" * 40
potraviny = {
    "mleko": [30, 5],  # index '0'-> cena, index '1' -> pocet
    "maso": [100, 1],
    "banan": [30, 10],
    "jogurt": [10, 5],
    "chleb": [20, 5],
    "jablko": [10, 10],
    "pomeranc": [15, 10]
}

# Uvitani uzivatele
print(
    "Vitejte u naseho nakupniho kosiku!".center(len(oddelovac)),
    oddelovac, sep="\n"
)

# vypsat nabídku zboží (bez počtu kusů)
for potravina in potraviny:
    print(
        f"| POTRAVINA: {potravina: <10}| CENA: {potraviny[potravina][0]: <3}|".center(len(oddelovac))
    )
else:
    print(oddelovac)

# umožnit uživateli vložit zboží do košíku
# ukončit při potvrzení klávesy "q"
while (zbozi := input("ZBOZI:")) != "q":
    # zamítnout zboží, které není v nabídce
    if zbozi not in potraviny:
        print(f"Zbozi \'{zbozi}\' neni v nabidce")

    # vloži vícekrát stejnou položku, pokud je skladem
    elif zbozi not in kosik and potraviny[zbozi][1] > 0:
        kosik[zbozi] = [potraviny[zbozi][0], 1]
        potraviny[zbozi][1] = potraviny[zbozi][1] - 1

    elif zbozi in kosik and potraviny[zbozi][1] > 0:
        kosik[zbozi][1] = kosik[zbozi][1] + 1
        potraviny[zbozi][1] = potraviny[zbozi][1] - 1

    # zamítnout, pokud není na skladě
    elif potraviny[zbozi][1] == 0:
        print(f"Zbozi \'{zbozi}\' jiz neni skladem")

else:
    print(oddelovac, kosik, sep="\n")

# TODO DOMA - vypsat hezky obsah nákupního košíku
# TODO DOMA - sečíst cenu za nákup
