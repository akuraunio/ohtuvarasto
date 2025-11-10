from varasto import Varasto

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    esimerkkitulostus1(mehua, olutta)

    virhe_esimerkki()

    lisaaminen2(olutta, 1000.0, "Olutvarasto")
    lisaaminen2(mehua, -666.0, "Mehuvarasto")

    ottaminen2(olutta, 1000.0, "Olutvarasto")
    ottaminen2(mehua, -32.9, "Mehuvarasto")

def varaston_tilanne(varasto):
    osa1 = f"saldo = {varasto.saldo}\n"
    osa2 = f"tilavuus = {varasto.tilavuus}\n "
    osa3 = f"paljonko_mahtuu = {varasto.paljonko_mahtuu()}"
    return osa1+osa2+osa3

def lisaaminen1(varasto, maara, nimi):
    varasto.lisaa_varastoon(maara)
    print(f"Lisätään {maara}")
    print(f"{nimi}: {varasto}")

def ottaminen1(varasto, maara, nimi):
    varasto.ota_varastosta(maara)
    print(f"Otetaan {maara}")
    print(f"{nimi}: {varasto}")

def virhe_esimerkki():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-50.0)
    print(huono)

def lisaaminen2(varasto, maara, nimi):
    print(f"{nimi}: {varasto}")
    varasto.lisaa_varastoon(maara)
    print(f"{nimi}.lisaa_varastoon({maara})")
    print(f"{nimi}: {varasto}")

def ottaminen2(varasto, maara, nimi):
    print(f"{nimi}: {varasto}")
    saatiin = varasto.ota_varastosta(maara)
    print(f"{nimi}.otaVarastosta({maara})")
    print(f"saatiin {saatiin}")
    print(f"{nimi}: {varasto}")

def esimerkkitulostus1(mehua, olutta):
    print(f"Luonnin jälkeen:\nMehuvarasto: {mehua}\nOlutvarasto: {olutta}")
    print(f"Olut getterit:\n{varaston_tilanne(olutta)}")
    print("Mehu setterit:")
    lisaaminen1(mehua, 50.7, "Mehuvarasto")
    ottaminen1(mehua, 3.14, "Mehuvarasto")

if __name__ == "__main__":
    main()
