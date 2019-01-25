import csv
import itertools
import operator


# Input formatum: https://docs.google.com/spreadsheets/d/1VHSb5TMpmWVqLajR58uWkDm_IRHgKtxUat8jUjt5MJc/edit#gid=941195623

CSV_DELIMITER = ','
SZOMSZEDOS_HETVEGE_MAX = 30
HIANYZOK_EGY_TABORBAN_MAX = 3
STATUSZ_INTERVALLUM = 10
MENTES_INTERVALLUM = 100


csoport_szam = 0
idopont_szam = 0
csoportok = []
idopontok = []
valaszok = []
tiltott = []
with open('input.csv', 'rb') as csvinput:
    csvreader = csv.reader(csvinput, delimiter=CSV_DELIMITER, quotechar='"')
    rows = [row for row in csvreader]

    # Idopontok beolvasasa
    idopontok = rows[0][1:]
    idopont_szam = len(idopontok)
    csoport_szam = (len(rows) - 1) / 2
    #print idopont_szam, idopontok

    # Valaszok beolvasasa
    for row in rows[1 : 1 + csoport_szam]:
        csoport = row[0]
        csoportok.append(csoport)
        valaszok.append([int(valasz_string) for valasz_string in row[1:]])
    #print valaszok

    # Tiltott hetvegek beolvasasa
    for csoport_index in xrange(csoport_szam):
        row = rows[1 + csoport_szam + csoport_index]
        if row[0] != csoportok[csoport_index]:
            print 'Hiba, mas csoport a tiltott tablazatban: {} != {}'.format(row[0], csoportok[csoport_index])
        tiltott.append(set([]))
        for idopont_index in xrange(0, len(row) - 1):
            if row[idopont_index + 1] != '':
                tiltott[csoport_index].add(idopont_index)


# Ahol tul sok hianyzo van, az tiltott hetvege
for csoport_index in xrange(len(valaszok)):
  for idopont_index in xrange(len(valaszok[csoport_index])):
      if valaszok[csoport_index][idopont_index] > HIANYZOK_EGY_TABORBAN_MAX:  # HEURISZTIKA
          tiltott[csoport_index].add(idopont_index)
#print tiltott


def mentes():
    lehetosegek_sorrendben = sorted(lehetosegek, key=operator.itemgetter(0, 1))
    header = ['Rossz', 'Szomszedos']
    header.extend(idopontok)
    with open('lehetosegek.csv', 'wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(header)
        for lehetoseg in lehetosegek_sorrendben:
            csvwriter.writerow(lehetoseg)
            csvfile.flush()
    print '!!! MENTVE !!!'

def szomszedos_darabszam(permutation):
    szomszedos_pont = 0
    idopontok_sorrendben = sorted(permutation)
    for csoport_index in range(csoport_szam - 1):
        idopont1 = idopontok_sorrendben[csoport_index]
        idopont2 = idopontok_sorrendben[csoport_index + 1]
        if idopont2 == idopont1 + 1:
            szomszedos_pont = szomszedos_pont + 1
    return szomszedos_pont

def feljegyez():
    global counter
    lehetoseg = [''] * idopont_szam
    for csoport_index in xrange(csoport_szam):
        idopont_index = csoport_idopontok[csoport_index]
        lehetoseg[idopont_index] = csoportok[csoport_index] + ' (' + str(valaszok[csoport_index][idopont_index]) +')'
    lehetoseg.insert(0, szomszedos_darabszam(csoport_idopontok))
    lehetoseg.insert(0, osszes_hianyzo)
    lehetosegek.append(lehetoseg)
    counter += 1
    if counter % STATUSZ_INTERVALLUM == 0:
        print counter
    if counter % MENTES_INTERVALLUM == 0:
        mentes()

def backtrack(csoport_index):
    global osszes_hianyzo
    if osszes_hianyzo > OSSZES_HIANYZO_MAX:
        return
    if csoport_index == csoport_szam:
        feljegyez()
        return
    for idopont_index in xrange(idopont_szam):
        if idopont_index in tiltott[csoport_index] or foglalt[idopont_index]:
            continue
        foglalt[idopont_index] = True
        csoport_idopontok[csoport_index] = idopont_index
        osszes_hianyzo += valaszok[csoport_index][idopont_index]
        backtrack(csoport_index + 1)
        foglalt[idopont_index] = False
        csoport_idopontok[csoport_index] = -1
        osszes_hianyzo -= valaszok[csoport_index][idopont_index]

OSSZES_HIANYZO_MAX = 0
lehetosegek = []
while len(lehetosegek) < 200:
    OSSZES_HIANYZO_MAX += 1
    counter = 0
    lehetosegek = []
    foglalt = [False] * idopont_szam
    csoport_idopontok = [-1] * csoport_szam
    osszes_hianyzo = 0
    backtrack(0)
    mentes()

print '!!!!!!!!!!! KESZ !!!!!!!!!!!'
