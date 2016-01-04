import csv
import itertools
import operator

CSV_DELIMITER = ','
SZOMSZEDOS_HETVEGE_MAX = 2
HIANYZOK_EGY_TABORBAN_MAX = 3
OSSZES_HIANYZO_MAX = 5

csoportok = ['K', 'Lemur', 'Monguz', 'Okapi', 'Beluga', 'B', 'ZsA', 'ZsB']

idopontok = [
    'Jan. 29--31.',
    'Febr. 5--7.',
    'Febr. 12--14.',
    'Febr. 19--21.',
    'Febr. 26-28.',
    'Marc. 4--6.',
    'Marc. 11--15.',
    'Marc. 18--20.',
    'tavaszi szunet',
    'Apr. 1--3.',
    'Apr. 8--10.',
    'Apr. 15--17.',
    'Apr. 22--24.',
    'Apr. 29. -- maj. 1.',
    'Maj. 6--8.',
    'Maj. 13--15.',
    'Maj. 20--22.',
    'Maj. 27--29..',
    'Jun. 3--5.',
    'Jun. 10--12.',
    'Jun. 17--19.',
    'Jun 24--26.'
]

tiltott = [
  [],
  [],
  [],
  [0, 2, 11, 12],
  [0, 1, 8, 16, 17],
  [1],
  [0, 1, 12],
  [0, 1, 12]
]

valaszok = []
with open('idopontok.csv', 'rb') as csvinput:
	csvreader = csv.reader(csvinput, delimiter=CSV_DELIMITER, quotechar='"')
	for row in csvreader:
		valasz_sor = []
		for valasz_string in row:
			valasz_sor.append(int(valasz_string))
		valaszok.append(valasz_sor)

csoport_szam = len(csoportok)
idopont_szam = len(idopontok)

counter = 0
lehetosegek = []
for permutation in itertools.permutations(range(idopont_szam), csoport_szam):
	counter = counter + 1
	if counter % 100000 == 0:
		print counter
	szomszedos_pont = 0
	idopontok_sorrendben = sorted(permutation)
	for csoport_index in range(csoport_szam - 1):
		idopont1 = idopontok_sorrendben[csoport_index]
		idopont2 = idopontok_sorrendben[csoport_index + 1]
		if idopont2 == idopont1 + 1:
			szomszedos_pont = szomszedos_pont + 1
	if szomszedos_pont > SZOMSZEDOS_HETVEGE_MAX:  # HEURISZTIKA
		continue

	rossz_pont = 0
	skip = False
	for csoport_index in range(csoport_szam):
		idopont_index = permutation[csoport_index]
		if idopont_index in tiltott[csoport_index]:
			skip = True
			break
		valasz = valaszok[csoport_index][idopont_index]
		if valasz > HIANYZOK_EGY_TABORBAN_MAX:  # HEURISZTIKA
			skip = True
			break
		rossz_pont = rossz_pont + valasz
		if rossz_pont > OSSZES_HIANYZO_MAX:  # HEURISZTIKA
			skip = True
			break
	if skip:
		continue

	lehetoseg = ["" for i in range(idopont_szam)]
	for csoport_index in range(csoport_szam):
		idopont_index = permutation[csoport_index]
		lehetoseg[idopont_index] = csoportok[csoport_index]
	lehetoseg.insert(0, str(szomszedos_pont))
	lehetoseg.insert(0, str(rossz_pont))
	lehetosegek.append(lehetoseg)

lehetosegek_sorrendben = sorted(lehetosegek, key=operator.itemgetter(0, 1))
header = ['Rossz', 'Szomszedos']
header.extend(idopontok)
with open('lehetosegek.csv', 'wb') as csvfile:
	csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	csvwriter.writerow(header)
	for lehetoseg in lehetosegek_sorrendben:
		csvwriter.writerow(lehetoseg)

print '!!!!!!!!!!! KESZ !!!!!!!!!!!'
