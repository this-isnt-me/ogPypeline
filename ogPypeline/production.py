def nozzle_size(value, units):
	returnDict = {}
	if units == 'mm':
		returnDict['mm'] = value
		returnDict['1/8in'] = value * 0.3149606
		returnDict['16/in'] = value * 0.6299213
		returnDict['32/in'] = value * 1.2598425
		returnDict['64/in'] = value * 2.519685
	elif units == '1/8in':
		returnDict['mm'] = value * 3.175
		returnDict['1/8in'] = value
		returnDict['16/in'] = value * 2.0
		returnDict['32/in'] = value * 4.0
		returnDict['64/in'] = value * 8.0
	elif units == '16/in':
		returnDict['mm'] = value * 1.5875
		returnDict['1/8in'] = value * 0.5
		returnDict['16/in'] = value
		returnDict['32/in'] = value * 2.0
		returnDict['64/in'] = value * 4.0
	elif units == '32/in':
		returnDict['mm'] = value * 0.79375
		returnDict['1/8in'] = value * 0.25
		returnDict['16/in'] = value * 0.5
		returnDict['32/in'] = value
		returnDict['64/in'] = value * 2.0
	elif units == '64/in':
		returnDict['mm'] = value * 0.396875
		returnDict['1/8in'] = value * 0.125
		returnDict['16/in'] = value * 0.25
		returnDict['32/in'] = value * 0.5
		returnDict['64/in'] = value
	return returnDict

def nozzle_speed(value, units):
	returnDict = {}
	if units == 'ft/s':
		returnDict['ft/s'] = value
		returnDict['m/s'] = value * 0.3048
	elif units == 'm/s':
		returnDict['ft/s'] = value * 3.2808399
		returnDict['m/s'] = value
	return returnDict

def oil_production_index(value, units):
	returnDict = {}
	if units == 'bbl/d-psi':
		returnDict['bbl/d-psi'] = value
		returnDict['bbl/hr-psi'] = value * 0.041667
		returnDict['bbl/min-psi'] = value * 0.0006944
		returnDict['ft3/d-psi'] = value * 5.6146008
		returnDict['m3/d-kPa'] = value * 0.0230592
		returnDict['m3/d-MPa'] = value * 23.05916
		returnDict['m3/hr-kPa'] = value * 0.0009601
		returnDict['gal/d-psi'] = value * 41.9999709
		returnDict['l/hr-kPa'] = value * 0.9600727
	elif units == 'bbl/hr-psi':
		returnDict['bbl/d-psi'] = value * 23.9998118
		returnDict['bbl/hr-psi'] = value
		returnDict['bbl/min-psi'] = value * 0.0166664
		returnDict['ft3/d-psi'] = value * 134.7493632
		returnDict['m3/d-kPa'] = value * 0.5534155
		returnDict['m3/d-MPa'] = value * 553.4155
		returnDict['m3/hr-kPa'] = value * 0.0230416
		returnDict['gal/d-psi'] = value * 1007.9913957
		returnDict['l/hr-kPa'] = value * 23.0415636
	elif units == 'bbl/min-psi':
		returnDict['bbl/d-psi'] = value * 1440.0095233
		returnDict['bbl/hr-psi'] = value * 60.0008673
		returnDict['bbl/min-psi'] = value
		returnDict['ft3/d-psi'] = value * 8085.0786669
		returnDict['m3/d-kPa'] = value * 33.20541
		returnDict['m3/d-MPa'] = value * 33205.41
		returnDict['m3/hr-kPa'] = value * 1.3825138
		returnDict['gal/d-psi'] = value * 60480.3580145
		returnDict['l/hr-kPa'] = value * 1382.5138
	elif units == 'ft3/d-psi':
		returnDict['bbl/d-psi'] = value * 0.1781071
		returnDict['bbl/hr-psi'] = value * 0.0074212
		returnDict['bbl/min-psi'] = value * 0.0001237
		returnDict['ft3/d-psi'] = value
		returnDict['m3/d-kPa'] = value * 0.004107
		returnDict['m3/d-MPa'] = value * 4.106999
		returnDict['m3/hr-kPa'] = value * 0.000171
		returnDict['gal/d-psi'] = value * 7.480491
		returnDict['l/hr-kPa'] = value * 0.1709957
	elif units == 'm3/d-kPa':
		returnDict['bbl/d-psi'] = value * 43.3667141
		returnDict['bbl/hr-psi'] = value * 1.8069606
		returnDict['bbl/min-psi'] = value * 0.0301156
		returnDict['ft3/d-psi'] = value * 243.4867893
		returnDict['m3/d-kPa'] = value
		returnDict['m3/d-MPa'] = value * 1000.0
		returnDict['m3/hr-kPa'] = value * 0.0416352
		returnDict['gal/d-psi'] = value * 1821.40073
		returnDict['l/hr-kPa'] = value * 41.6351974
	elif units == 'm3/d-MPa':
		returnDict['bbl/d-psi'] = value * 0.0433667
		returnDict['bbl/hr-psi'] = value * 0.001807
		returnDict['bbl/min-psi'] = value * 3.01e-05
		returnDict['ft3/d-psi'] = value * 0.2434868
		returnDict['m3/d-kPa'] = value * 0.001
		returnDict['m3/d-MPa'] = value
		returnDict['m3/hr-kPa'] = value * 4.16e-05
		returnDict['gal/d-psi'] = value * 1.8214007
		returnDict['l/hr-kPa'] = value * 0.0416352
	elif units == 'm3/hr-kPa':
		returnDict['bbl/d-psi'] = value * 1041.5878115
		returnDict['bbl/hr-psi'] = value * 43.3998325
		returnDict['bbl/min-psi'] = value * 0.7233201
		returnDict['ft3/d-psi'] = value * 5848.0997926
		returnDict['m3/d-kPa'] = value * 24.01814
		returnDict['m3/d-MPa'] = value * 24018.14
		returnDict['m3/hr-kPa'] = value
		returnDict['gal/d-psi'] = value * 43746.6577297
		returnDict['l/hr-kPa'] = value * 1000.0
	elif units == 'gal/d-psi':
		returnDict['bbl/d-psi'] = value * 0.0238095
		returnDict['bbl/hr-psi'] = value * 0.0009921
		returnDict['bbl/min-psi'] = value * 1.65e-05
		returnDict['ft3/d-psi'] = value * 0.1336811
		returnDict['m3/d-kPa'] = value * 0.000549
		returnDict['m3/d-MPa'] = value * 0.549028
		returnDict['m3/hr-kPa'] = value * 2.29e-05
		returnDict['gal/d-psi'] = value
		returnDict['l/hr-kPa'] = value * 0.0228589
	elif units == 'l/hr-kPa':
		returnDict['bbl/d-psi'] = value * 1.0415878
		returnDict['bbl/hr-psi'] = value * 0.0433998
		returnDict['bbl/min-psi'] = value * 0.0007233
		returnDict['ft3/d-psi'] = value * 5.8480998
		returnDict['m3/d-kPa'] = value * 0.0240181
		returnDict['m3/d-MPa'] = value * 24.01814
		returnDict['m3/hr-kPa'] = value * 0.001
		returnDict['gal/d-psi'] = value * 43.7466577
		returnDict['l/hr-kPa'] = value
	return returnDict

def permeability(value, units):
	returnDict = {}
	if units == 'darcy':
		returnDict['darcy'] = value
		returnDict['md'] = value * 1000
		returnDict['ud'] = value * 1000000
		returnDict['m2'] = value * 0.0000000000009869
		returnDict['ft2'] = value * 1.06235016146393e-11
	elif units == 'md':
		returnDict['darcy'] = value * 0.001
		returnDict['md'] = value
		returnDict['ud'] = value * 1000
		returnDict['m2'] = value * 0.0000000000000009869
		returnDict['ft2'] = value * 1.06235016146393e-14
	elif units == 'ud':
		returnDict['darcy'] = value * 0.000001
		returnDict['md'] = value * 0.001
		returnDict['ud'] = value
		returnDict['m2'] = value * 9.869e-19
		returnDict['ft2'] = value * 1.06235016146393e-17
	elif units == 'm2':
		returnDict['darcy'] = value * 1013273887931.91
		returnDict['md'] = value * 1013273887931910
		returnDict['ud'] = value * 1013273887931910000
		returnDict['m2'] = value 
		returnDict['ft2'] = value * 0.0000107642626480086
	elif units == 'ft2':
		returnDict['darcy'] = value * 94130921825.4355
		returnDict['md'] = value * 94130921825435.5
		returnDict['ud'] = value * 94130921825435500
		returnDict['m2'] = value * 92900.0000000001
		returnDict['ft2'] = value 
	return returnDict

def pipe_capacity(value, units):
	returnDict = {}
	if units == 'bbl/ft':
		returnDict['bbl/ft'] = value
		returnDict['m3/m'] = value * 0.521654
		returnDict['bbl/in'] = value * 0.0833333333333333
		returnDict['ft3/ft'] = value * 5.61458333333333
		returnDict['gal(us)/ft'] = value * 42.0
		returnDict['l/m'] = value * 521.61186
		returnDict['dm3/m'] = value * 521.61186
		returnDict['in3/ft'] = value * 9702.0
	elif units == 'm3/m':
		returnDict['bbl/ft'] = value * 1.9169795
		returnDict['m3/m'] = value
		returnDict['bbl/in'] = value * 0.159761193568975
		returnDict['ft3/ft'] = value * 10.7639104167097
		returnDict['gal(us)/ft'] = value * 80.5196415587636
		returnDict['l/m'] = value * 1000.0
		returnDict['dm3/m'] = value * 1000.0
		returnDict['in3/ft'] = value * 18600.0372000744
	elif units == 'bbl/in':
		returnDict['bbl/ft'] = value * 12.000000000000005
		returnDict['m3/m'] = value * 6.259342320000019
		returnDict['bbl/in'] = value
		returnDict['ft3/ft'] = value * 67.375
		returnDict['gal(us)/ft'] = value * 504.0
		returnDict['l/m'] = value * 6259.34232
		returnDict['dm3/m'] = value * 6259.34232
		returnDict['in3/ft'] = value * 116424.0
	elif units == 'ft3/ft':
		returnDict['bbl/ft'] = value * 0.17810760667903536
		returnDict['m3/m'] = value * 0.09290304000000019
		returnDict['bbl/in'] = value * 0.014842300556586271
		returnDict['ft3/ft'] = value
		returnDict['gal(us)/ft'] = value * 7.48051948051948
		returnDict['l/m'] = value * 92.90304
		returnDict['dm3/m'] = value * 92.90304
		returnDict['in3/ft'] = value * 1728.0
	elif units == 'gal(us)/ft':
		returnDict['bbl/ft'] = value * 0.023809523809523808
		returnDict['m3/m'] = value * 0.012419330000000006
		returnDict['bbl/in'] = value * 0.001984126984126984
		returnDict['ft3/ft'] = value * 0.13368055555555555
		returnDict['gal(us)/ft'] = value
		returnDict['l/m'] = value * 12.4193299999999
		returnDict['dm3/m'] = value * 12.4193299999999
		returnDict['in3/ft'] = value * 231.0
	elif units == 'l/m':
		returnDict['bbl/ft'] = value * 0.0019171343228277058
		returnDict['m3/m'] = value * 0.001
		returnDict['bbl/in'] = value * 0.00015976119356897548
		returnDict['ft3/ft'] = value * 0.010763910416709722
		returnDict['gal(us)/ft'] = value * 0.08051964155876429
		returnDict['l/m'] = value
		returnDict['dm3/m'] = value
		returnDict['in3/ft'] = value * 18.6000372000744
	elif units == 'dm3/m':
		returnDict['bbl/ft'] = value * 0.0019171343228277058
		returnDict['m3/m'] = value * 0.001
		returnDict['bbl/in'] = value * 0.00015976119356897548
		returnDict['ft3/ft'] = value * 0.010763910416709722
		returnDict['gal(us)/ft'] = value * 0.08051964155876429
		returnDict['l/m'] = value
		returnDict['dm3/m'] = value
		returnDict['in3/ft'] = value * 18.6000372000744
	elif units == 'in3/ft':
		returnDict['bbl/ft'] = value * 0.00010307153164296021
		returnDict['m3/m'] = value * 5.3763333333333334e-05
		returnDict['bbl/in'] = value * 8.589294303580018e-06
		returnDict['ft3/ft'] = value * 0.0005787037037037037
		returnDict['gal(us)/ft'] = value * 0.004329004329004329
		returnDict['l/m'] = value * 0.05376333333333334
		returnDict['dm3/m'] = value * 0.05376333333333334
		returnDict['in3/ft'] = value
	return returnDict

def pipe_cap_length_vol(value, units):
	returnDict = {}
	if units == 'm/m3':
		returnDict['m/m3'] = value
		returnDict['ft/bbl'] = value * 0.52161186
		returnDict['ft/ft3'] = value * 0.09290304
		returnDict['ft/gal(us)'] = value * 0.01241933
	elif units == 'ft/bbl':
		returnDict['m/m3'] = value * 1.9171343228277056
		returnDict['ft/bbl'] = value
		returnDict['ft/ft3'] = value * 0.178107606679035
		returnDict['ft/gal(us)'] = value * 0.0238095238095238
	elif units == 'ft/ft3':
		returnDict['m/m3'] = value * 1.9171343228277056
		returnDict['ft/bbl'] = value * 5.614583333333341
		returnDict['ft/ft3'] = value
		returnDict['ft/gal(us)'] = value * 0.133680555555555
	elif units == 'ft/gal(us)':
		returnDict['m/m3'] = value * 80.51964155876364
		returnDict['ft/bbl'] = value * 42.000000000000014
		returnDict['ft/ft3'] = value * 7.480519480519511
		returnDict['ft/gal(us)'] = value
	return returnDict

def production_rate(value, units):
	returnDict = {}
	if units == 'm3/d':
		returnDict['m3/d'] = value
		returnDict['STB/d'] = value * 6.2893082
	elif units == 'STB/d':
		returnDict['m3/d'] = value * 0.159
		returnDict['STB/d'] = value
	return returnDict

def rotation(value, units):
	returnDict = {}
	if units == 'rad/sec':
		returnDict['rad/sec'] = value
		returnDict['rpm'] = value * 9.551099
	elif units == 'rpm':
		returnDict['rad/sec'] = value * 0.1047
		returnDict['rpm'] = value
	return returnDict

def section_modulus(value, units):
	returnDict = {}
	if units == 'cm3':
		returnDict['cm3'] = value
		returnDict['in3'] = value * 0.061024
	elif units == 'in3':
		returnDict['cm3'] = value * 16.3869953
		returnDict['in3'] = value
	return returnDict

def moment_of_section(value, units):
	returnDict = {}
	if units == 'cm4':
		returnDict['cm4'] = value
		returnDict['ft4'] = value * 1.2e-06
		returnDict['in4'] = value * 0.0240251
		returnDict['m4'] = value * 1e-08
	elif units == 'ft4':
		returnDict['cm4'] = value * 863097.4841242
		returnDict['ft4'] = value
		returnDict['in4'] = value * 20736.0
		returnDict['m4'] = value * 0.008631
	elif units == 'in4':
		returnDict['cm4'] = value * 41.6231426
		returnDict['ft4'] = value * 4.82e-05
		returnDict['in4'] = value
		returnDict['m4'] = value * 4.162314256e-07
	elif units == 'm4':
		returnDict['cm4'] = value * 100000000.0
		returnDict['ft4'] = value * 115.8617675
		returnDict['in4'] = value * 2402509.6100288
		returnDict['m4'] = value
	return returnDict

def stress_elastic_modulus(value, units):
	returnDict = {}
	if units == 'kg/cm2':
		returnDict['kg/cm2'] = value
		returnDict['kPa'] = value * 98.0654748
		returnDict['Mpa'] = value * 0.0980657
		returnDict['Pa'] = value * 98087.7931034
		returnDict['psi'] = value * 14.22273
	elif units == 'kPa':
		returnDict['kg/cm2'] = value * 0.0101973
		returnDict['kPa'] = value
		returnDict['Mpa'] = value * 0.001
		returnDict['Pa'] = value * 1000.2275862
		returnDict['psi'] = value * 0.145033
	elif units == 'Mpa':
		returnDict['kg/cm2'] = value * 10.1972406
		returnDict['kPa'] = value * 1000.0
		returnDict['Mpa'] = value
		returnDict['Pa'] = value * 1000224.8275862
		returnDict['psi'] = value * 145.0326
	elif units == 'Pa':
		returnDict['kg/cm2'] = value * 1.02e-05
		returnDict['kPa'] = value * 0.001
		returnDict['Mpa'] = value * 1e-06
		returnDict['Pa'] = value
		returnDict['psi'] = value * 0.000145
	elif units == 'psi':
		returnDict['kg/cm2'] = value * 0.07031
		returnDict['kPa'] = value * 6.8949825
		returnDict['Mpa'] = value * 0.006895
		returnDict['Pa'] = value * 6896.5517241
		returnDict['psi'] = value * 1.0
	return returnDict

def stroke_rate(value, units):
	returnDict = {}
	if units == 'stk/hr':
		returnDict['stk/hr'] = value
		returnDict['stk/min'] = value * 60.0
	elif units == 'stk/min':
		returnDict['stk/hr'] = value * 0.016667
		returnDict['stk/min'] = value * 1.0
	return returnDict

def stroke_volume(value, units):
	returnDict = {}
	if units == 'bbl/stk':
		returnDict['bbl/stk'] = value
		returnDict['m3/stk'] = value * 0.1590336
		returnDict['gal/stk'] = value * 42.01681
		returnDict['L/stk'] = value * 159.033501
	elif units == 'm3/stk':
		returnDict['bbl/stk'] = value * 6.2879785
		returnDict['m3/stk'] = value
		returnDict['gal/stk'] = value * 264.2008
		returnDict['L/stk'] = value * 1000.0
	elif units == 'gal/stk':
		returnDict['bbl/stk'] = value * 0.0238
		returnDict['m3/stk'] = value * 0.003785
		returnDict['gal/stk'] = value
		returnDict['L/stk'] = value * 3.784997
	elif units == 'L/stk':
		returnDict['bbl/stk'] = value * 0.006288
		returnDict['m3/stk'] = value * 0.001
		returnDict['gal/stk'] = value * 0.264201
		returnDict['L/stk'] = value
	return returnDict

# def permeability(value, units):
# 	returnDict = {}
# 	if units == 'TD':
# 		returnDict['TD'] = value
# 		returnDict['D'] = value * 0.1590336
# 		returnDict['mD'] = value * 42.01681
# 	elif units == 'D':
# 		returnDict['TD'] = value * 1e-12
# 		returnDict['D'] = value
# 		returnDict['mD'] = value * 264.2008
# 	elif units == 'mD':
# 		returnDict['TD'] = value * 0.0238
# 		returnDict['D'] = value * 0.003785
# 		returnDict['mD'] = value
# 	return returnDict