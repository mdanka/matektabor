import csv
import itertools
import operator

csoportok = ['Okapi', 'Beluga', 'B', 'ZsA', 'ZsB', 'Va', 'Vb']
idopontok = [
  'Feb. 13--15.',
  'Feb. 20--22.',
  'Feb. 27--Marc. 1.',
  'Marc. 6--8.',
  'Marc. 13--15.',
  'Marc. 20--22.',
  'Marc. 27--29.',
  'Tavaszi szunet',
  'Apr. 10--12.',
  'Apr. 17--19.',
  'Apr. 24--26.',
  'Maj. 1--3.',
  'Maj. 8--10.',
  'Maj. 15--17.',
  'Maj. 22--24.',
  'Maj. 29--31.',
  'Jun. 5--7.',
  'Jun. 12--14.',
  'Jun. 19--21.',
  'Jun. 26--28.'
]

tiltott = [
  [0],
  [2, 3, 5, 9, 11, 12, 13],
  [],
  [9],
  [0, 1, 2, 9],
  [0, 1, 2, 3, 4, 5, 6],
  [0]
]

valaszok = []
with open('idopontok.csv', 'rb') as csvinput:
	csvreader = csv.reader(csvinput, delimiter='\t', quotechar='"')
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
	if szomszedos_pont > 3:  # HEURISZTIKA
		continue

	rossz_pont = 0
	skip = False
	for csoport_index in range(csoport_szam):
		idopont_index = permutation[csoport_index]
		if idopont_index in tiltott[csoport_index]:
			skip = True
			break
		valasz = valaszok[csoport_index][idopont_index]
		if valasz > 5:  # HEURISZTIKA
			skip = True
			break
		rossz_pont = rossz_pont + valasz
		if rossz_pont > 15:  # HEURISZTIKA
			skip = True
			break
	if skip:
		continue

	okapi_hamar = permutation[0] <= 9
	b_hamar = permutation[2] <= 9

	lehetoseg = ["" for i in range(idopont_szam)]
	for csoport_index in range(csoport_szam):
		idopont_index = permutation[csoport_index]
		lehetoseg[idopont_index] = csoportok[csoport_index]
	lehetoseg.insert(0, str(b_hamar))
	lehetoseg.insert(0, str(okapi_hamar))
	lehetoseg.insert(0, str(szomszedos_pont))
	lehetoseg.insert(0, str(rossz_pont))
	lehetosegek.append(lehetoseg)

lehetosegek_sorrendben = sorted(lehetosegek, key=operator.itemgetter(0, 1))
header = ['Rossz', 'Szomszedos', 'Okapi hamar', 'B hamar']
header.extend(idopontok)
with open('lehetosegek.csv', 'wb') as csvfile:
	csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	csvwriter.writerow(header)
	for lehetoseg in lehetosegek_sorrendben:
		csvwriter.writerow(lehetoseg)

print '!!!!!!!!!!! KESZ !!!!!!!!!!!'
