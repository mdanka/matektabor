import csv
import itertools
import operator


# Input formatum: https://docs.google.com/spreadsheets/d/1VHSb5TMpmWVqLajR58uWkDm_IRHgKtxUat8jUjt5MJc/edit#gid=941195623

CSV_DELIMITER = ','
SZOMSZEDOS_HETVEGE_MAX = 30
HIANYZOK_EGY_TABORBAN_MAX = 3
OSSZES_HIANYZO_MAX = 12
STATUSZ_INTERVALLUM = 1000000
MENTES_INTERVALLUM = 10000000


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
    print idopont_szam, idopontok

    # Valaszok beolvasasa
    for row in rows[1 : 1 + csoport_szam]:
        csoport = row[0]
        csoportok.append(csoport)
        valaszok.append([int(valasz_string) for valasz_string in row[1:]])
    print valaszok

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
print tiltott
counter = 0
lehetosegek = []


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


for permutation in itertools.permutations(range(0, idopont_szam), csoport_szam):
    counter = counter + 1
    if counter % STATUSZ_INTERVALLUM == 0:
        print counter

    if counter % MENTES_INTERVALLUM == 0:
        mentes()

    #if counter > 10 * MENTES_INTERVALLUM:
    #    exit(0)

    # Tiltott hetvegek kiszurese
    skip = False
    for csoport_index in xrange(csoport_szam):
        idopont_index = permutation[csoport_index]
        if idopont_index in tiltott[csoport_index]:
            skip = True
            break
    if skip:
        continue

    # Tul sok osszes hianyzo kiszurese
    rossz_pont = 0
    for csoport_index in xrange(csoport_szam):
        idopont_index = permutation[csoport_index]
        valasz = valaszok[csoport_index][idopont_index]
        rossz_pont = rossz_pont + valasz
        if rossz_pont > OSSZES_HIANYZO_MAX:  # HEURISZTIKA
            skip = True
            break
    if skip:
        continue

    # Szomszedos hetvegek osszeszamolasa
    szomszedos_pont = 0
    idopontok_sorrendben = sorted(permutation)
    for csoport_index in range(csoport_szam - 1):
        idopont1 = idopontok_sorrendben[csoport_index]
        idopont2 = idopontok_sorrendben[csoport_index + 1]
        if idopont2 == idopont1 + 1:
            szomszedos_pont = szomszedos_pont + 1
    if szomszedos_pont > SZOMSZEDOS_HETVEGE_MAX:  # HEURISZTIKA
        continue

    lehetoseg = [''] * idopont_szam
    for csoport_index in range(csoport_szam):
        idopont_index = permutation[csoport_index]
        lehetoseg[idopont_index] = csoportok[csoport_index]
    lehetoseg.insert(0, szomszedos_pont)
    lehetoseg.insert(0, rossz_pont)
    lehetosegek.append(lehetoseg)


mentes()

print '!!!!!!!!!!! KESZ !!!!!!!!!!!'
