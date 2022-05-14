import random
from math import *



def normaliza(dic):
    ndic = {}
    for cont, paises in dic.items():
        for pais, info in paises.items():
            info['continente']=cont
            ndic[pais] = info
    return ndic


def sorteia_pais(paises):
    lista_paises = []
    for pais in paises:
        lista_paises.append(pais)
    return random.choice(lista_paises)

def haversine(r, f1, l1, f2, l2):
    f1 = radians(f1)
    f2 = radians(f2)
    l1 = radians(l1)
    l2 = radians(l2)
    coef = sqrt(sin((f2-f1)/2)**2+cos(f1)*cos(f2)*sin((l2-l1)/2)**2)
    d=2*r*asin(coef)
    return d

def adiciona_em_ordem(pais, dist, lista):
    item = [pais, dist]
    if len(lista) == 0:
        lista.append(item)
        return lista
    if item in lista:
        return lista
    for i in range(len(lista)):
        if lista[i][1]>dist and item not in lista:
            lista.insert(i, item)
    if item not in lista:
        lista.append(item)
    return lista


def esta_na_lista(pais, lista):
    for p in lista:
        if pais in p:
            return True
    return False

def sorteia_letra(pal, restr):
    import random
    pal = pal.lower()
    final = []
    ce = ['.', ',', '-', ';', ' ']
    for letra in pal:
        if (letra not in ce) and (letra not in restr):
            final.append(letra)
    if len(final) == 0:
        return ''
    return str(random.choice(final))