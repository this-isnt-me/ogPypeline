def gas_injection_rate(value, units):
	returnDict = {}
	if units == 'm3/min':
		returnDict['m3/min'] = value
		returnDict['scfm'] = value * 35.335689
	elif units == 'scfm':
		returnDict['m3/min'] = value * 0.0283
		returnDict['scfm'] = value
	return returnDict

def gas_production_index(value, units):
	returnDict = {}
	if units == 'm3/d-MPa':
		returnDict['m3/d-MPa'] = value
		returnDict['m3/d-kPa'] = value * 1000.0
		returnDict['m3/hr-kPa'] = value * 41.6675544
		returnDict['MMSCFD/psi'] = value * 0.2436699
		returnDict['MSCF/hr-psi'] = value * 10.152921
		returnDict['MSCFD/psi'] = value * 243.6699
		returnDict['SCF/hr-psi'] = value * 10152.9209608
		returnDict['SCFD/psi'] = value * 243669.9
	elif units == 'm3/d-kPa':
		returnDict['m3/d-MPa'] = value * 0.001
		returnDict['m3/d-kPa'] = value
		returnDict['m3/hr-kPa'] = value * 0.0416676
		returnDict['MMSCFD/psi'] = value * 0.0002437
		returnDict['MSCF/hr-psi'] = value * 0.0101529
		returnDict['MSCFD/psi'] = value * 0.2436699
		returnDict['SCF/hr-psi'] = value * 10.152921
		returnDict['SCFD/psi'] = value * 243.6699
	elif units == 'm3/hr-kPa':
		returnDict['m3/d-MPa'] = value * 0.0239995
		returnDict['m3/d-kPa'] = value * 23.9994887
		returnDict['m3/hr-kPa'] = value
		returnDict['MMSCFD/psi'] = value * 0.005848
		returnDict['MSCF/hr-psi'] = value * 0.2436649
		returnDict['MSCFD/psi'] = value * 5.847953
		returnDict['SCF/hr-psi'] = value * 243.6649114
		returnDict['SCFD/psi'] = value * 5847.953
	elif units == 'MMSCFD/psi':
		returnDict['m3/d-MPa'] = value * 4.1039127
		returnDict['m3/d-kPa'] = value * 4103.9127114
		returnDict['m3/hr-kPa'] = value * 171.0000063
		returnDict['MMSCFD/psi'] = value
		returnDict['MSCF/hr-psi'] = value * 41.6667014
		returnDict['MSCFD/psi'] = value * 1000.0
		returnDict['SCF/hr-psi'] = value * 41666.7013889
		returnDict['SCFD/psi'] = value * 1000000.0
	elif units == 'MSCF/hr-psi':
		returnDict['m3/d-MPa'] = value * 0.0984938
		returnDict['m3/d-kPa'] = value * 98.493823
		returnDict['m3/hr-kPa'] = value * 4.1039967
		returnDict['MMSCFD/psi'] = value * 0.024
		returnDict['MSCF/hr-psi'] = value
		returnDict['MSCFD/psi'] = value * 24.0
		returnDict['SCF/hr-psi'] = value * 1000.0
		returnDict['SCFD/psi'] = value * 24000.0
	elif units == 'MSCFD/psi':
		returnDict['m3/d-MPa'] = value * 0.0041039
		returnDict['m3/d-kPa'] = value * 4.1039127
		returnDict['m3/hr-kPa'] = value * 0.171
		returnDict['MMSCFD/psi'] = value * 0.001
		returnDict['MSCF/hr-psi'] = value * 0.0416667
		returnDict['MSCFD/psi'] = value
		returnDict['SCF/hr-psi'] = value * 41.6667014
		returnDict['SCFD/psi'] = value * 1000.0
	elif units == 'SCF/hr-psi':
		returnDict['m3/d-MPa'] = value * 9.85e-05
		returnDict['m3/d-kPa'] = value * 0.0984938
		returnDict['m3/hr-kPa'] = value * 0.004104
		returnDict['MMSCFD/psi'] = value * 2.4e-05
		returnDict['MSCF/hr-psi'] = value * 0.001
		returnDict['MSCFD/psi'] = value * 0.024
		returnDict['SCF/hr-psi'] = value
		returnDict['SCFD/psi'] = value * 24.0
	elif units == 'SCFD/psi':
		returnDict['m3/d-MPa'] = value * 4.1e-06
		returnDict['m3/d-kPa'] = value * 0.0041039
		returnDict['m3/hr-kPa'] = value * 0.000171
		returnDict['MMSCFD/psi'] = value * 1e-06
		returnDict['MSCF/hr-psi'] = value * 4.17e-05
		returnDict['MSCFD/psi'] = value * 0.001
		returnDict['SCF/hr-psi'] = value * 0.0416667
		returnDict['SCFD/psi'] = value
	return returnDict

def gas_production_rate(value, units):
	returnDict = {}
	if units == 'm3/min':
		returnDict['m3/min'] = value 
		returnDict['MM'] = value * 0.0508834
		returnDict['MMM3/d'] = value * 0.00144
		returnDict['scfm'] = value * 35.3144754
	elif units == 'MM':
		returnDict['m3/min'] = value * 19.65278
		returnDict['MM'] = value 
		returnDict['MMM3/d'] = value * 0.0283
		returnDict['scfm'] = value * 694.0276159
	elif units == 'MMM3/d':
		returnDict['m3/min'] = value * 694.4445
		returnDict['MM'] = value * 35.3356879
		returnDict['MMM3/d'] = value 
		returnDict['scfm'] = value * 24523.9432143
	elif units == 'scfm':
		returnDict['m3/min'] = value * 0.028317
		returnDict['MM'] = value * 0.0014409
		returnDict['MMM3/d'] = value * 4.08e-05
		returnDict['scfm'] = value 
	return returnDict

def gas_volume(value, units):
	returnDict = {}
	if units == 'bbl':
		returnDict['bbl'] = value
		returnDict['cm3'] = value * 158987.2949285
		returnDict['dm3'] = value * 1589.8729493
		returnDict['ft3'] = value * 5.6145833
		returnDict['in3'] = value * 9702.0
		returnDict['m3'] = value * 0.1589873
		returnDict['yd3'] = value * 0.2079475
		returnDict['fl oz'] = value * 5376.0
		returnDict['gal'] = value * 42.0
		returnDict['L'] = value * 158.9872949
		returnDict['qt'] = value * 168.0
	elif units == 'cm3':
		returnDict['bbl'] = value * 6.3e-06
		returnDict['cm3'] = value
		returnDict['dm3'] = value * 0.01
		returnDict['ft3'] = value * 3.53e-05
		returnDict['in3'] = value * 0.0610237
		returnDict['m3'] = value * 1e-06
		returnDict['yd3'] = value * 1.3e-06
		returnDict['fl oz'] = value * 0.033814
		returnDict['gal'] = value * 0.0002642
		returnDict['L'] = value * 0.001
		returnDict['qt'] = value * 0.0010567
	elif units == 'dm3':
		returnDict['bbl'] = value * 0.000629
		returnDict['cm3'] = value * 100.0
		returnDict['dm3'] = value
		returnDict['ft3'] = value * 0.0035315
		returnDict['in3'] = value * 6.1023744
		returnDict['m3'] = value * 0.0001
		returnDict['yd3'] = value * 0.0001308
		returnDict['fl oz'] = value * 3.3814023
		returnDict['gal'] = value * 0.0264172
		returnDict['L'] = value * 0.1
		returnDict['qt'] = value * 0.1056688
	elif units == 'ft3':
		returnDict['bbl'] = value * 0.1781076
		returnDict['cm3'] = value * 28316.846592
		returnDict['dm3'] = value * 283.1684659
		returnDict['ft3'] = value
		returnDict['in3'] = value * 1728.0
		returnDict['m3'] = value * 0.0283168
		returnDict['yd3'] = value * 0.037037
		returnDict['fl oz'] = value * 957.5064935
		returnDict['gal'] = value * 7.4805195
		returnDict['L'] = value * 28.3168466
		returnDict['qt'] = value * 29.9220779
	elif units == 'in3':
		returnDict['bbl'] = value * 0.0001031
		returnDict['cm3'] = value * 16.387064
		returnDict['dm3'] = value * 0.1638706
		returnDict['ft3'] = value * 0.0005787
		returnDict['in3'] = value
		returnDict['m3'] = value * 1.64e-05
		returnDict['yd3'] = value * 2.14e-05
		returnDict['fl oz'] = value * 0.5541126
		returnDict['gal'] = value * 0.004329
		returnDict['L'] = value * 0.0163871
		returnDict['qt'] = value * 0.017316
	elif units == 'm3':
		returnDict['bbl'] = value * 6.2898108
		returnDict['cm3'] = value * 1000000.0
		returnDict['dm3'] = value * 10000.0
		returnDict['ft3'] = value * 35.3146667
		returnDict['in3'] = value * 61023.7440947
		returnDict['m3'] = value
		returnDict['yd3'] = value * 1.3079506
		returnDict['fl oz'] = value * 33814.0227017
		returnDict['gal'] = value * 264.1720524
		returnDict['L'] = value * 1000.0
		returnDict['qt'] = value * 1056.6882094
	elif units == 'yd3':
		returnDict['bbl'] = value * 4.8089054
		returnDict['cm3'] = value * 764554.857984
		returnDict['dm3'] = value * 7645.5485798
		returnDict['ft3'] = value * 27.0
		returnDict['in3'] = value * 46656.0
		returnDict['m3'] = value * 0.7645549
		returnDict['yd3'] = value
		returnDict['fl oz'] = value * 25852.6753246
		returnDict['gal'] = value * 201.974026
		returnDict['L'] = value * 764.554858
		returnDict['qt'] = value * 807.8961039
	elif units == 'fl oz':
		returnDict['bbl'] = value * 0.000186
		returnDict['cm3'] = value * 29.5735296
		returnDict['dm3'] = value * 0.2957353
		returnDict['ft3'] = value * 0.0010444
		returnDict['in3'] = value * 1.8046875
		returnDict['m3'] = value * 2.96e-05
		returnDict['yd3'] = value * 3.87e-05
		returnDict['fl oz'] = value
		returnDict['gal'] = value * 0.0078125
		returnDict['L'] = value * 0.0295735
		returnDict['qt'] = value * 0.03125
	elif units == ' gal':
		returnDict['bbl'] = value * 0.0238095
		returnDict['cm3'] = value * 3785.411784
		returnDict['dm3'] = value * 37.8541178
		returnDict['ft3'] = value * 0.1336806
		returnDict['in3'] = value * 231.0
		returnDict['m3'] = value * 0.0037854
		returnDict['yd3'] = value * 0.0049511
		returnDict['fl oz'] = value * 128.0
		returnDict['gal'] = value
		returnDict['L'] = value * 3.7854118
		returnDict['qt'] = value * 4.0
	elif units == 'L':
		returnDict['bbl'] = value * 0.0062898
		returnDict['cm3'] = value * 1000.0
		returnDict['dm3'] = value * 10.0
		returnDict['ft3'] = value * 0.0353147
		returnDict['in3'] = value * 61.0237441
		returnDict['m3'] = value * 0.001
		returnDict['yd3'] = value * 0.001308
		returnDict['fl oz'] = value * 33.8140227
		returnDict['gal'] = value * 0.2641721
		returnDict['L'] = value
		returnDict['qt'] = value * 1.0566882
	elif units == 'qt':
		returnDict['bbl'] = value * 0.0059524
		returnDict['cm3'] = value * 946.352946
		returnDict['dm3'] = value * 9.4635295
		returnDict['ft3'] = value * 0.0334201
		returnDict['in3'] = value * 57.75
		returnDict['m3'] = value * 0.0009464
		returnDict['yd3'] = value * 0.0012378
		returnDict['fl oz'] = value * 32.0
		returnDict['gal'] = value * 0.25
		returnDict['L'] = value * 0.9463529
		returnDict['qt'] = value
	return returnDict

def lng_volume(value, units):
	returnDict = {}
	if units == 'BOE':
		returnDict['BOE'] = value
		returnDict['MMBOE'] = value * 1e-06
		returnDict['MMCF'] = value * 0.0056146
		returnDict['KBOE'] = value * 0.001
		returnDict['ton LNG'] = value * 0.1152074
	elif units == 'MMBOE':
		returnDict['BOE'] = value * 1000000.0
		returnDict['MMBOE'] = value
		returnDict['MMCF'] = value * 5614.5833334
		returnDict['KBOE'] = value * 1000.0
		returnDict['ton LNG'] = value * 115207.3732719
	elif units == 'MMCF':
		returnDict['BOE'] = value * 178.1076067
		returnDict['MMBOE'] = value * 0.0001781
		returnDict['MMCF'] = value
		returnDict['KBOE'] = value * 0.1781076
		returnDict['ton LNG'] = value * 20.5193095
	elif units == 'KBOE':
		returnDict['BOE'] = value * 1000.0
		returnDict['MMBOE'] = value * 0.001
		returnDict['MMCF'] = value * 5.6145833
		returnDict['KBOE'] = value
		returnDict['ton LNG'] = value * 115.2073733
	elif units == 'ton LNG':
		returnDict['BOE'] = value * 8.68
		returnDict['MMBOE'] = value * 8.7e-06
		returnDict['MMCF'] = value * 0.0487346
		returnDict['KBOE'] = value * 0.00868
		returnDict['ton LNG'] = value
	return returnDict

def specific_volume(value, units):
	returnDict = {}
	if units == 'bbl/UK ton':
		returnDict['bbl/UK ton'] = value
		returnDict['bbl/US ton'] = value * 0.8928571
		returnDict['ft3/lb'] = value * 0.0025065
		returnDict['in3/lb'] = value * 4.33125
		returnDict['m3/kg'] = value * 0.0001565
		returnDict['UK gal/lb'] = value * 0.0156126
		returnDict['US gal/lb'] = value * 0.01875
		returnDict['l/g'] = value * 0.0001565
		returnDict['l/kg'] = value * 0.1564763
	elif units == 'bbl/US ton':
		returnDict['bbl/UK ton'] = value * 1.12
		returnDict['bbl/US ton'] = value
		returnDict['ft3/lb'] = value * 0.0028073
		returnDict['in3/lb'] = value * 4.851
		returnDict['m3/kg'] = value * 0.0001753
		returnDict['UK gal/lb'] = value * 0.0174862
		returnDict['US gal/lb'] = value * 0.021
		returnDict['l/g'] = value * 0.0001753
		returnDict['l/kg'] = value * 0.1752535
	elif units == 'ft3/lb':
		returnDict['bbl/UK ton'] = value * 398.961039
		returnDict['bbl/US ton'] = value * 356.2152134
		returnDict['ft3/lb'] = value
		returnDict['in3/lb'] = value * 1728.0
		returnDict['m3/kg'] = value * 0.062428
		returnDict['UK gal/lb'] = value * 6.2288384
		returnDict['US gal/lb'] = value * 7.4805195
		returnDict['l/g'] = value * 0.062428
		returnDict['l/kg'] = value * 62.4279606
	elif units == 'in3/lb':
		returnDict['bbl/UK ton'] = value * 0.2308802
		returnDict['bbl/US ton'] = value * 0.2061431
		returnDict['ft3/lb'] = value * 0.0005787
		returnDict['in3/lb'] = value
		returnDict['m3/kg'] = value * 3.61e-05
		returnDict['UK gal/lb'] = value * 0.0036047
		returnDict['US gal/lb'] = value * 0.004329
		returnDict['l/g'] = value * 3.61e-05
		returnDict['l/kg'] = value * 0.0361273
	elif units == 'm3/kg':
		returnDict['bbl/UK ton'] = value * 6390.7427902
		returnDict['bbl/US ton'] = value * 5706.0203484
		returnDict['ft3/lb'] = value * 16.0184634
		returnDict['in3/lb'] = value * 27679.9047102
		returnDict['m3/kg'] = value
		returnDict['UK gal/lb'] = value * 99.7764204
		returnDict['US gal/lb'] = value * 119.8264273
		returnDict['l/g'] = value
		returnDict['l/kg'] = value * 1000.0
	elif units == 'UK gal/lb':
		returnDict['bbl/UK ton'] = value * 64.050632
		returnDict['bbl/US ton'] = value * 57.1880643
		returnDict['ft3/lb'] = value * 0.1605436
		returnDict['in3/lb'] = value * 277.4193
		returnDict['m3/kg'] = value * 0.0100224
		returnDict['UK gal/lb'] = value
		returnDict['US gal/lb'] = value * 1.2009494
		returnDict['l/g'] = value * 0.0100224
		returnDict['l/kg'] = value * 10.0224081
	elif units == 'US gal/lb':
		returnDict['bbl/UK ton'] = value * 53.3333333
		returnDict['bbl/US ton'] = value * 47.6190476
		returnDict['ft3/lb'] = value * 0.1336806
		returnDict['in3/lb'] = value * 231.0
		returnDict['m3/kg'] = value * 0.0083454
		returnDict['UK gal/lb'] = value * 0.8326746
		returnDict['US gal/lb'] = value
		returnDict['l/g'] = value * 0.0083454
		returnDict['l/kg'] = value * 8.3454045
	elif units == 'l/g':
		returnDict['bbl/UK ton'] = value * 6390.7427902
		returnDict['bbl/US ton'] = value * 5706.0203484
		returnDict['ft3/lb'] = value * 16.0184634
		returnDict['in3/lb'] = value * 27679.90471
		returnDict['m3/kg'] = value
		returnDict['UK gal/lb'] = value * 99.7764204
		returnDict['US gal/lb'] = value * 119.8264273
		returnDict['l/g'] = value
		returnDict['l/kg'] = value * 1000.0
	elif units == 'l/kg':
		returnDict['bbl/UK ton'] = value * 6.3907428
		returnDict['bbl/US ton'] = value * 5.7060203
		returnDict['ft3/lb'] = value * 0.0160185
		returnDict['in3/lb'] = value * 27.6799047
		returnDict['m3/kg'] = value * 0.001
		returnDict['UK gal/lb'] = value * 0.0997764
		returnDict['US gal/lb'] = value * 0.1198264
		returnDict['l/g'] = value * 0.001
		returnDict['l/kg'] = value
	return returnDict

def gas_volume(value, units):
	returnDict = {}
	if units == 'bbl':
		returnDict['bbl'] = value
		returnDict['cm3'] = value * 158987.2949285
		returnDict['dm3'] = value * 1589.8729493
		returnDict['ft3'] = value * 5.6145833
		returnDict['in3'] = value * 9702.0
		returnDict['m3'] = value * 0.1589873
		returnDict['yd3'] = value * 0.2079475
		returnDict['fl oz'] = value * 5376.0
		returnDict['gal'] = value * 42.0
		returnDict['L'] = value * 158.9872949
		returnDict['qt'] = value * 168.0
	elif units == 'cm3':
		returnDict['bbl'] = value * 6.3e-06
		returnDict['cm3'] = value
		returnDict['dm3'] = value * 0.01
		returnDict['ft3'] = value * 3.53e-05
		returnDict['in3'] = value * 0.0610237
		returnDict['m3'] = value * 1e-06
		returnDict['yd3'] = value * 1.3e-06
		returnDict['fl oz'] = value * 0.033814
		returnDict['gal'] = value * 0.0002642
		returnDict['L'] = value * 0.001
		returnDict['qt'] = value * 0.0010567
	elif units == 'dm3':
		returnDict['bbl'] = value * 0.000629
		returnDict['cm3'] = value * 100.0
		returnDict['dm3'] = value
		returnDict['ft3'] = value * 0.0035315
		returnDict['in3'] = value * 6.1023744
		returnDict['m3'] = value * 0.0001
		returnDict['yd3'] = value * 0.0001308
		returnDict['fl oz'] = value * 3.3814023
		returnDict['gal'] = value * 0.0264172
		returnDict['L'] = value * 0.1
		returnDict['qt'] = value * 0.1056688
	elif units == 'ft3':
		returnDict['bbl'] = value * 0.1781076
		returnDict['cm3'] = value * 28316.846592
		returnDict['dm3'] = value * 283.1684659
		returnDict['ft3'] = value
		returnDict['in3'] = value * 1728.0
		returnDict['m3'] = value * 0.0283168
		returnDict['yd3'] = value * 0.037037
		returnDict['fl oz'] = value * 957.5064935
		returnDict['gal'] = value * 7.4805195
		returnDict['L'] = value * 28.3168466
		returnDict['qt'] = value * 29.9220779
	elif units == 'in3':
		returnDict['bbl'] = value * 0.0001031
		returnDict['cm3'] = value * 16.387064
		returnDict['dm3'] = value * 0.1638706
		returnDict['ft3'] = value * 0.0005787
		returnDict['in3'] = value
		returnDict['m3'] = value * 1.64e-05
		returnDict['yd3'] = value * 2.14e-05
		returnDict['fl oz'] = value * 0.5541126
		returnDict['gal'] = value * 0.004329
		returnDict['L'] = value * 0.0163871
		returnDict['qt'] = value * 0.017316
	elif units == 'm3':
		returnDict['bbl'] = value * 6.2898108
		returnDict['cm3'] = value * 1000000.0
		returnDict['dm3'] = value * 10000.0
		returnDict['ft3'] = value * 35.3146667
		returnDict['in3'] = value * 61023.7440947
		returnDict['m3'] = value
		returnDict['yd3'] = value * 1.3079506
		returnDict['fl oz'] = value * 33814.0227017
		returnDict['gal'] = value * 264.1720524
		returnDict['L'] = value * 1000.0
		returnDict['qt'] = value * 1056.6882094
	elif units == 'yd3':
		returnDict['bbl'] = value * 4.8089054
		returnDict['cm3'] = value * 764554.857984
		returnDict['dm3'] = value * 7645.5485798
		returnDict['ft3'] = value * 27.0
		returnDict['in3'] = value * 46656.0
		returnDict['m3'] = value * 0.7645549
		returnDict['yd3'] = value
		returnDict['fl oz'] = value * 25852.6753246
		returnDict['gal'] = value * 201.974026
		returnDict['L'] = value * 764.554858
		returnDict['qt'] = value * 807.8961039
	elif units == 'fl oz':
		returnDict['bbl'] = value * 0.000186
		returnDict['cm3'] = value * 29.5735296
		returnDict['dm3'] = value * 0.2957353
		returnDict['ft3'] = value * 0.0010444
		returnDict['in3'] = value * 1.8046875
		returnDict['m3'] = value * 2.96e-05
		returnDict['yd3'] = value * 3.87e-05
		returnDict['fl oz'] = value
		returnDict['gal'] = value * 0.0078125
		returnDict['L'] = value * 0.0295735
		returnDict['qt'] = value * 0.03125
	elif units == ' gal':
		returnDict['bbl'] = value * 0.0238095
		returnDict['cm3'] = value * 3785.411784
		returnDict['dm3'] = value * 37.8541178
		returnDict['ft3'] = value * 0.1336806
		returnDict['in3'] = value * 231.0
		returnDict['m3'] = value * 0.0037854
		returnDict['yd3'] = value * 0.0049511
		returnDict['fl oz'] = value * 128.0
		returnDict['gal'] = value
		returnDict['L'] = value * 3.7854118
		returnDict['qt'] = value * 4.0
	elif units == 'L':
		returnDict['bbl'] = value * 0.0062898
		returnDict['cm3'] = value * 1000.0
		returnDict['dm3'] = value * 10.0
		returnDict['ft3'] = value * 0.0353147
		returnDict['in3'] = value * 61.0237441
		returnDict['m3'] = value * 0.001
		returnDict['yd3'] = value * 0.001308
		returnDict['fl oz'] = value * 33.8140227
		returnDict['gal'] = value * 0.2641721
		returnDict['L'] = value
		returnDict['qt'] = value * 1.0566882
	elif units == 'qt':
		returnDict['bbl'] = value * 0.0059524
		returnDict['cm3'] = value * 946.352946
		returnDict['dm3'] = value * 9.4635295
		returnDict['ft3'] = value * 0.0334201
		returnDict['in3'] = value * 57.75
		returnDict['m3'] = value * 0.0009464
		returnDict['yd3'] = value * 0.0012378
		returnDict['fl oz'] = value * 32.0
		returnDict['gal'] = value * 0.25
		returnDict['L'] = value * 0.9463529
		returnDict['qt'] = value
	return returnDict