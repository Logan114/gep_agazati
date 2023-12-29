from classok import Jatekosok
gepek = open("gep.txt", "r")
gepek_lista = gepek.readlines()[1:] 
jatekosok_lista = []


def adatgyujtes():
    for i in range (0,len(gepek_lista),1):
        jelen_sor = gepek_lista[i]
        crab = jelen_sor.strip().split("!")
        id = crab[0]
        hely = crab[1]
        tipus = crab[2]
        ip = crab[3]
        jatekosok = Jatekosok(id,hely,tipus,ip)
        jatekosok_lista.append(jatekosok)
    return jatekosok_lista



def gepek_szama(lista):
    print("\n*** 1. feladat***\n")
    gsz = len(lista) 
    print(f"A gépek száma: {gsz}")



def atlag(lista):
    print("\n*** 2. feladat***\n")
    paros_termek_id = []
    for n in range (0,len(lista),1):
        tsz = int(lista[n].hely[1:])
        if tsz %2 == 0:
            parosgep:int = int(lista[n].id)
            paros_termek_id.append(parosgep)
    atlag = round(sum(paros_termek_id) / len(paros_termek_id)) 
    print (f"A páros teremszámú termek azonosító átlaga: {atlag}.")


  
def legkissebb(lista):
    print("\n*** 3. feladat***\n")
    legkissebb_lista = []
    for n in range (0,len(lista),1):
        if lista[n].tipus == "asztali":
            azn:int = int(lista[n].id)
            legkissebb_lista.append(int(azn))
    legkissebb_id = min(legkissebb_lista)
    legkissebb_terem = (lista[legkissebb_id-1].hely)
    print(f"A legkissebb asztali gép azonosítója {legkissebb_id}, helye: {legkissebb_terem}")
