def fluid_consistency(value, units):
    returnDict = {}
    if units == 'dyne-s^n/cm2':
        returnDict['dyne-s^n/cm2'] = value
        returnDict['eq.cp'] = value * 99.4285714
        returnDict['lbf-s^n/100ft2'] = value * 0.2088
        returnDict['lbf-s^n/ft2'] = value * 0.002088
        returnDict['Pa-s^n'] = value * 0.0999761
    elif units == 'eq.cp':
        returnDict['dyne-s^n/cm2'] = value * 0.0100575
        returnDict['eq.cp'] = value
        returnDict['lbf-s^n/100ft2'] = value * 0.0021
        returnDict['lbf-s^n/ft2'] = value * 2.1e-05
        returnDict['Pa-s^n'] = value * 0.0010055
    elif units == 'lbf-s^n/100ft2':
        returnDict['dyne-s^n/cm2'] = value * 4.789272
        returnDict['eq.cp'] = value * 476.1904762
        returnDict['lbf-s^n/100ft2'] = value
        returnDict['lbf-s^n/ft2'] = value * 0.01
        returnDict['Pa-s^n'] = value * 0.4788125
    elif units == 'lbf-s^n/ft2':
        returnDict['dyne-s^n/cm2'] = value * 478.9272031
        returnDict['eq.cp'] = value * 47619.047619
        returnDict['lbf-s^n/100ft2'] = value * 100.0
        returnDict['lbf-s^n/ft2'] = value
        returnDict['Pa-s^n'] = value * 47.8812545
    elif units == 'Pa-s^n':
        returnDict['dyne-s^n/cm2'] = value * 10.0023946
        returnDict['eq.cp'] = value * 994.5238095
        returnDict['lbf-s^n/100ft2'] = value * 2.0885
        returnDict['lbf-s^n/ft2'] = value * 0.020885
        returnDict['Pa-s^n'] = value
    else:
        raise Exception("""Invalid Input. Make sure values are passed as
        integers, units are passed as stings and that the
        correct units are input. Consult the
        documnetation for more information on each function.""")
    return returnDict


def fluid_yield_point(value, units):
    returnDict = {}
    if units == 'dyne/cm2':
        returnDict['dyne/cm2'] = value
        returnDict['kPa'] = value * 0.0999587
        returnDict['Mpa'] = value * 0.0001
        returnDict['lbf/100ft2'] = value * 0.208768
    elif units == 'kPa':
        returnDict['dyne/cm2'] = value * 10.0041338
        returnDict['kPa'] = value
        returnDict['Mpa'] = value * 0.001
        returnDict['lbf/100ft2'] = value * 2.088543
    elif units == 'Mpa':
        returnDict['dyne/cm2'] = value * 10004.1337753
        returnDict['kPa'] = value * 1000.0
        returnDict['Mpa'] = value
        returnDict['lbf/100ft2'] = value * 2088.543
    elif units == 'lbf/100ft2':
        returnDict['dyne/cm2'] = value * 4.7900061
        returnDict['kPa'] = value * 0.4788027
        returnDict['Mpa'] = value * 0.0004788
        returnDict['lbf/100ft2'] = value
    else:
        raise Exception("""Invalid Input. Make sure values are passed as
        integers, units are passed as stings and that the
        correct units are input. Consult the
        documnetation for more information on each function.""")
    return returnDict


def liquid_production_rates(value, units):
    returnDict = {}
    if units == 'BPD':
        returnDict['BPD'] = value
        returnDict['BPH'] = value * 0.0416667
        returnDict['BPM'] = value * 0.0006944
        returnDict['BPS'] = value * 1.16e-05
        returnDict['ft3/day'] = value * 5.6145928
        returnDict['ft3/hr'] = value * 0.2339414
        returnDict['ft3/min'] = value * 0.003899
        returnDict['ft3/sec'] = value * 6.5e-05
        returnDict['m3/day'] = value * 0.1589873
        returnDict['m3/hr'] = value * 0.0066245
        returnDict['m3/min'] = value * 0.0001104
        returnDict['gal/day'] = value * 42.0000211
        returnDict['gph'] = value * 1.7500009
        returnDict['gpm'] = value * 0.0291667
        returnDict['gal/sec'] = value * 0.0004861
        returnDict['UK gal/day'] = value * 34.9723169
        returnDict['UK gph'] = value * 1.4571799
        returnDict['UK gpm'] = value * 0.0242863
        returnDict['UK gal/sec'] = value * 0.0004048
    elif units == 'BPH':
        returnDict['BPD'] = value * 24.0
        returnDict['BPH'] = value
        returnDict['BPM'] = value * 0.0166667
        returnDict['BPS'] = value * 0.0002778
        returnDict['ft3/day'] = value * 134.750226
        returnDict['ft3/hr'] = value * 5.6145928
        returnDict['ft3/min'] = value * 0.0935765
        returnDict['ft3/sec'] = value * 0.0015596
        returnDict['m3/day'] = value * 3.8156952
        returnDict['m3/hr'] = value * 0.1589873
        returnDict['m3/min'] = value * 0.0026498
        returnDict['gal/day'] = value * 1008.0005072
        returnDict['gph'] = value * 42.0000211
        returnDict['gpm'] = value * 0.7000004
        returnDict['gal/sec'] = value * 0.0116667
        returnDict['UK gal/day'] = value * 839.3356049
        returnDict['UK gph'] = value * 34.9723169
        returnDict['UK gpm'] = value * 0.5828719
        returnDict['UK gal/sec'] = value * 0.0097145
    elif units == 'BPM':
        returnDict['BPD'] = value * 1440.0
        returnDict['BPH'] = value * 60.0
        returnDict['BPM'] = value
        returnDict['BPS'] = value * 0.0166667
        returnDict['ft3/day'] = value * 8085.0135609
        returnDict['ft3/hr'] = value * 336.875565
        returnDict['ft3/min'] = value * 5.6145928
        returnDict['ft3/sec'] = value * 0.0935765
        returnDict['m3/day'] = value * 228.941712
        returnDict['m3/hr'] = value * 9.539238
        returnDict['m3/min'] = value * 0.1589873
        returnDict['gal/day'] = value * 60480.0304326
        returnDict['gph'] = value * 2520.001268
        returnDict['gpm'] = value * 42.0000211
        returnDict['gal/sec'] = value * 0.7000004
        returnDict['UK gal/day'] = value * 50360.1362929
        returnDict['UK gph'] = value * 2098.3390122
        returnDict['UK gpm'] = value * 34.9723169
        returnDict['UK gal/sec'] = value * 0.5828719
    elif units == 'BPS':
        returnDict['BPD'] = value * 86400.0
        returnDict['BPH'] = value * 3600.0
        returnDict['BPM'] = value * 60.0
        returnDict['BPS'] = value
        returnDict['ft3/day'] = value * 485100.8136513
        returnDict['ft3/hr'] = value * 20212.5339021
        returnDict['ft3/min'] = value * 336.875565
        returnDict['ft3/sec'] = value * 5.6145928
        returnDict['m3/day'] = value * 13736.50272
        returnDict['m3/hr'] = value * 572.35428
        returnDict['m3/min'] = value * 9.539238
        returnDict['gal/day'] = value * 3628801.8259581
        returnDict['gph'] = value * 151200.0760816
        returnDict['gpm'] = value * 2520.001268
        returnDict['gal/sec'] = value * 42.0000211
        returnDict['UK gal/day'] = value * 3021608.1775768
        returnDict['UK gph'] = value * 125900.3407324
        returnDict['UK gpm'] = value * 2098.3390122
        returnDict['UK gal/sec'] = value * 34.9723169
    elif units == 'ft3/day':
        returnDict['BPD'] = value * 0.1781073
        returnDict['BPH'] = value * 0.0074211
        returnDict['BPM'] = value * 0.0001237
        returnDict['BPS'] = value * 2.1e-06
        returnDict['ft3/day'] = value
        returnDict['ft3/hr'] = value * 0.0416667
        returnDict['ft3/min'] = value * 0.0006944
        returnDict['ft3/sec'] = value * 1.16e-05
        returnDict['m3/day'] = value * 0.0283168
        returnDict['m3/hr'] = value * 0.0011799
        returnDict['m3/min'] = value * 1.97e-05
        returnDict['gal/day'] = value * 7.4805107
        returnDict['gph'] = value * 0.3116879
        returnDict['gpm'] = value * 0.0051948
        returnDict['gal/sec'] = value * 8.66e-05
        returnDict['UK gal/day'] = value * 6.2288252
        returnDict['UK gph'] = value * 0.2595344
        returnDict['UK gpm'] = value * 0.0043256
        returnDict['UK gal/sec'] = value * 7.21e-05
    elif units == 'ft3/hr':
        returnDict['BPD'] = value * 4.2745754
        returnDict['BPH'] = value * 0.1781073
        returnDict['BPM'] = value * 0.0029685
        returnDict['BPS'] = value * 4.95e-05
        returnDict['ft3/day'] = value * 24.0
        returnDict['ft3/hr'] = value
        returnDict['ft3/min'] = value * 0.0166667
        returnDict['ft3/sec'] = value * 0.0002778
        returnDict['m3/day'] = value * 0.6796032
        returnDict['m3/hr'] = value * 0.0283168
        returnDict['m3/min'] = value * 0.0283168
        returnDict['gal/day'] = value * 179.5322567
        returnDict['gph'] = value * 7.4805107
        returnDict['gpm'] = value * 0.1246752
        returnDict['gal/sec'] = value * 0.0020779
        returnDict['UK gal/day'] = value * 149.491805
        returnDict['UK gph'] = value * 6.2288252
        returnDict['UK gpm'] = value * 0.1038138
        returnDict['UK gal/sec'] = value * 0.0017302
    elif units == 'ft3/min':
        returnDict['BPD'] = value * 256.4745234
        returnDict['BPH'] = value * 10.6864385
        returnDict['BPM'] = value * 0.1781073
        returnDict['BPS'] = value * 0.0029685
        returnDict['ft3/day'] = value * 1440.0
        returnDict['ft3/hr'] = value * 60.0
        returnDict['ft3/min'] = value
        returnDict['ft3/sec'] = value * 0.0166667
        returnDict['m3/day'] = value * 40.776192
        returnDict['m3/hr'] = value * 1.699008
        returnDict['m3/min'] = value * 0.0283168
        returnDict['gal/day'] = value * 10771.9354046
        returnDict['gph'] = value * 448.8306419
        returnDict['gpm'] = value * 7.4805107
        returnDict['gal/sec'] = value * 0.1246752
        returnDict['UK gal/day'] = value * 8969.5083027
        returnDict['UK gph'] = value * 373.7295126
        returnDict['UK gpm'] = value * 6.2288252
        returnDict['UK gal/sec'] = value * 0.1038138
    elif units == 'ft3/sec':
        returnDict['BPD'] = value * 15388.4714062
        returnDict['BPH'] = value * 641.1863086
        returnDict['BPM'] = value * 10.6864385
        returnDict['BPS'] = value * 0.1781073
        returnDict['ft3/day'] = value * 86400.0
        returnDict['ft3/hr'] = value * 3600.0
        returnDict['ft3/min'] = value * 60.0
        returnDict['ft3/sec'] = value
        returnDict['m3/day'] = value * 2446.57152
        returnDict['m3/hr'] = value * 101.94048
        returnDict['m3/min'] = value * 1.699008
        returnDict['gal/day'] = value * 646316.1242772
        returnDict['gph'] = value * 26929.8385115
        returnDict['gpm'] = value * 448.8306419
        returnDict['gal/sec'] = value * 7.4805107
        returnDict['UK gal/day'] = value * 538170.4981644
        returnDict['UK gph'] = value * 22423.7707568
        returnDict['UK gpm'] = value * 373.7295126
        returnDict['UK gal/sec'] = value * 6.2288252
    elif units == 'm3/day':
        returnDict['BPD'] = value * 6.2898106
        returnDict['BPH'] = value * 0.2620754
        returnDict['BPM'] = value * 0.0043679
        returnDict['BPS'] = value * 7.28e-05
        returnDict['ft3/day'] = value * 35.3147248
        returnDict['ft3/hr'] = value * 1.4714469
        returnDict['ft3/min'] = value * 0.0245241
        returnDict['ft3/sec'] = value * 0.0004087
        returnDict['m3/day'] = value
        returnDict['m3/hr'] = value * 0.0416667
        returnDict['m3/min'] = value * 0.0006944
        returnDict['gal/day'] = value * 264.1721769
        returnDict['gph'] = value * 11.007174
        returnDict['gpm'] = value * 0.1834529
        returnDict['gal/sec'] = value * 0.0030575
        returnDict['UK gal/day'] = value * 219.9692483
        returnDict['UK gph'] = value * 9.1653853
        returnDict['UK gpm'] = value * 0.1527564
        returnDict['UK gal/sec'] = value * 0.0025459
    elif units == 'm3/hr':
        returnDict['BPD'] = value * 150.9554537
        returnDict['BPH'] = value * 6.2898106
        returnDict['BPM'] = value * 0.1048302
        returnDict['BPS'] = value * 0.0017472
        returnDict['ft3/day'] = value * 847.5533959
        returnDict['ft3/hr'] = value * 35.3147248
        returnDict['ft3/min'] = value * 0.5885787
        returnDict['ft3/sec'] = value * 0.0098096
        returnDict['m3/day'] = value * 24.0
        returnDict['m3/hr'] = value
        returnDict['m3/min'] = value * 0.0166667
        returnDict['gal/day'] = value * 6340.1322446
        returnDict['gph'] = value * 264.1721769
        returnDict['gpm'] = value * 4.4028696
        returnDict['gal/sec'] = value * 0.0733812
        returnDict['UK gal/day'] = value * 5279.2619592
        returnDict['UK gph'] = value * 219.9692483
        returnDict['UK gpm'] = value * 3.6661541
        returnDict['UK gal/sec'] = value * 0.0611026
    elif units == 'm3/min':
        returnDict['BPD'] = value * 9057.3272205
        returnDict['BPH'] = value * 377.3886342
        returnDict['BPM'] = value * 6.2898106
        returnDict['BPS'] = value * 0.1048302
        returnDict['ft3/day'] = value * 50853.2037518
        returnDict['ft3/hr'] = value * 2118.8834897
        returnDict['ft3/min'] = value * 35.3147248
        returnDict['ft3/sec'] = value * 0.5885787
        returnDict['m3/day'] = value * 1440.0
        returnDict['m3/hr'] = value * 60.0
        returnDict['m3/min'] = value
        returnDict['gal/day'] = value * 380407.9346755
        returnDict['gph'] = value * 15850.3306115
        returnDict['gpm'] = value * 264.1721769
        returnDict['gal/sec'] = value * 4.4028696
        returnDict['UK gal/day'] = value * 316755.7175507
        returnDict['UK gph'] = value * 13198.1548979
        returnDict['UK gpm'] = value * 219.9692483
        returnDict['UK gal/sec'] = value * 3.6661541
    elif units == 'gal/day':
        returnDict['BPD'] = value * 0.0238095
        returnDict['BPH'] = value * 0.0009921
        returnDict['BPM'] = value * 1.65e-05
        returnDict['BPS'] = value * 2.75e-07
        returnDict['ft3/day'] = value * 0.1336807
        returnDict['ft3/hr'] = value * 0.00557
        returnDict['ft3/min'] = value * 9.28e-05
        returnDict['ft3/sec'] = value * 1.5e-06
        returnDict['m3/day'] = value * 0.0037854
        returnDict['m3/hr'] = value * 0.0001577
        returnDict['m3/min'] = value * 2.6e-06
        returnDict['gal/day'] = value
        returnDict['gph'] = value * 0.0416667
        returnDict['gpm'] = value * 0.0006944
        returnDict['gal/sec'] = value * 1.16e-05
        returnDict['UK gal/day'] = value * 0.8326738
        returnDict['UK gph'] = value * 0.0346947
        returnDict['UK gpm'] = value * 0.0005782
        returnDict['UK gal/sec'] = value * 9.6e-06
    elif units == 'gph':
        returnDict['BPD'] = value * 0.5714283
        returnDict['BPH'] = value * 0.0238095
        returnDict['BPM'] = value * 0.0003968
        returnDict['BPS'] = value * 6.6e-06
        returnDict['ft3/day'] = value * 3.2083371
        returnDict['ft3/hr'] = value * 0.1336807
        returnDict['ft3/min'] = value * 0.002228
        returnDict['ft3/sec'] = value * 3.71e-05
        returnDict['m3/day'] = value * 0.0908498
        returnDict['m3/hr'] = value * 0.0037854
        returnDict['m3/min'] = value * 6.31e-05
        returnDict['gal/day'] = value * 24.0
        returnDict['gph'] = value
        returnDict['gpm'] = value * 0.0166667
        returnDict['gal/sec'] = value * 0.0002778
        returnDict['UK gal/day'] = value * 19.984171
        returnDict['UK gph'] = value * 0.8326738
        returnDict['UK gpm'] = value * 0.0138779
        returnDict['UK gal/sec'] = value * 0.0002313
    elif units == 'gpm':
        returnDict['BPD'] = value * 34.285697
        returnDict['BPH'] = value * 1.4285707
        returnDict['BPM'] = value * 0.0238095
        returnDict['BPS'] = value * 0.0003968
        returnDict['ft3/day'] = value * 192.500226
        returnDict['ft3/hr'] = value * 8.0208428
        returnDict['ft3/min'] = value * 0.1336807
        returnDict['ft3/sec'] = value * 0.002228
        returnDict['m3/day'] = value * 5.4509904
        returnDict['m3/hr'] = value * 0.2271246
        returnDict['m3/min'] = value * 0.0037854
        returnDict['gal/day'] = value * 1440.0
        returnDict['gph'] = value * 60.0
        returnDict['gpm'] = value
        returnDict['gal/sec'] = value * 0.0166667
        returnDict['UK gal/day'] = value * 1199.0502608
        returnDict['UK gph'] = value * 49.9604275
        returnDict['UK gpm'] = value * 0.8326738
        returnDict['UK gal/sec'] = value * 0.0138779
    elif units == 'gal/sec':
        returnDict['BPD'] = value * 2057.141822
        returnDict['BPH'] = value * 85.7142426
        returnDict['BPM'] = value * 1.4285707
        returnDict['BPS'] = value * 0.0238095
        returnDict['ft3/day'] = value * 11550.0135609
        returnDict['ft3/hr'] = value * 481.250565
        returnDict['ft3/min'] = value * 8.0208428
        returnDict['ft3/sec'] = value * 0.1336807
        returnDict['m3/day'] = value * 327.059424
        returnDict['m3/hr'] = value * 13.627476
        returnDict['m3/min'] = value * 0.2271246
        returnDict['gal/day'] = value * 86400.0
        returnDict['gph'] = value * 3600.0
        returnDict['gpm'] = value * 60.0
        returnDict['gal/sec'] = value
        returnDict['UK gal/day'] = value * 71943.0156464
        returnDict['UK gph'] = value * 2997.6256519
        returnDict['UK gpm'] = value * 49.9604275
        returnDict['UK gal/sec'] = value * 0.8326738
    elif units == 'UK gal/day':
        returnDict['BPD'] = value * 0.028594
        returnDict['BPH'] = value * 0.0011914
        returnDict['BPM'] = value * 1.99e-05
        returnDict['BPS'] = value * 3.3167e-07
        returnDict['ft3/day'] = value * 0.1605439
        returnDict['ft3/hr'] = value * 0.0066893
        returnDict['ft3/min'] = value * 0.0001115
        returnDict['ft3/sec'] = value * 1.9e-06
        returnDict['m3/day'] = value * 0.0045461
        returnDict['m3/hr'] = value * 0.0001894
        returnDict['m3/min'] = value * 3.2e-06
        returnDict['gal/day'] = value * 1.2009505
        returnDict['gph'] = value * 0.0500396
        returnDict['gpm'] = value * 0.000834
        returnDict['gal/sec'] = value * 1.39e-05
        returnDict['UK gal/day'] = value
        returnDict['UK gph'] = value * 0.0416667
        returnDict['UK gpm'] = value * 0.0006944
        returnDict['UK gal/sec'] = value * 1.16e-05
    elif units == 'UK gph':
        returnDict['BPD'] = value * 0.6862571
        returnDict['BPH'] = value * 0.028594
        returnDict['BPM'] = value * 0.0004766
        returnDict['BPS'] = value * 7.9e-06
        returnDict['ft3/day'] = value * 3.853054
        returnDict['ft3/hr'] = value * 0.1605439
        returnDict['ft3/min'] = value * 0.0026757
        returnDict['ft3/sec'] = value * 4.46e-05
        returnDict['m3/day'] = value * 0.1091062
        returnDict['m3/hr'] = value * 0.0045461
        returnDict['m3/min'] = value * 7.58e-05
        returnDict['gal/day'] = value * 28.8228118
        returnDict['gph'] = value * 1.2009505
        returnDict['gpm'] = value * 0.0200158
        returnDict['gal/sec'] = value * 0.0003336
        returnDict['UK gal/day'] = value * 24.0
        returnDict['UK gph'] = value
        returnDict['UK gpm'] = value * 0.0166667
        returnDict['UK gal/sec'] = value * 0.0002778
    elif units == 'UK gpm':
        returnDict['BPD'] = value * 41.1754247
        returnDict['BPH'] = value * 1.7156427
        returnDict['BPM'] = value * 0.028594
        returnDict['BPS'] = value * 0.0004766
        returnDict['ft3/day'] = value * 231.183241
        returnDict['ft3/hr'] = value * 9.632635
        returnDict['ft3/min'] = value * 0.1605439
        returnDict['ft3/sec'] = value * 0.0026757
        returnDict['m3/day'] = value * 6.5463696
        returnDict['m3/hr'] = value * 0.2727654
        returnDict['m3/min'] = value * 0.0045461
        returnDict['gal/day'] = value * 1729.3687077
        returnDict['gph'] = value * 72.0570295
        returnDict['gpm'] = value * 1.2009505
        returnDict['gal/sec'] = value * 0.0200158
        returnDict['UK gal/day'] = value * 1440.0
        returnDict['UK gph'] = value * 60.0
        returnDict['UK gpm'] = value
        returnDict['UK gal/sec'] = value * 0.0166667
    elif units == 'UK gal/sec':
        returnDict['BPD'] = value * 2470.5254822
        returnDict['BPH'] = value * 102.9385618
        returnDict['BPM'] = value * 1.7156427
        returnDict['BPS'] = value * 0.028594
        returnDict['ft3/day'] = value * 13870.9944627
        returnDict['ft3/hr'] = value * 577.9581026
        returnDict['ft3/min'] = value * 9.632635
        returnDict['ft3/sec'] = value * 0.1605439
        returnDict['m3/day'] = value * 392.782176
        returnDict['m3/hr'] = value * 16.365924
        returnDict['m3/min'] = value * 0.2727654
        returnDict['gal/day'] = value * 103762.1224649
        returnDict['gph'] = value * 4323.4217694
        returnDict['gpm'] = value * 72.0570295
        returnDict['gal/sec'] = value * 1.2009505
        returnDict['UK gal/day'] = value * 86400.0
        returnDict['UK gph'] = value * 3600.0
        returnDict['UK gpm'] = value * 60.0
        returnDict['UK gal/sec'] = value
    else:
        raise Exception("""Invalid Input. Make sure values are passed as
        integers, units are passed as stings and that the
        correct units are input. Consult the
        documnetation for more information on each function.""")
    return returnDict


def viscocity(value, units):
    returnDict = {}
    if units == 'cp':
        returnDict['cp'] = value
        returnDict['g/(cm.s)'] = value * 0.01
        returnDict['kg/(m.hr)'] = value * 3.6
        returnDict['kg/(m.s)'] = value * 0.001
        returnDict['kg-f.s/m2'] = value * 0.000102
        returnDict['kPa-s'] = value * 1e-06
        returnDict['N.s/m2'] = value * 0.001
        returnDict['Pa-s'] = value * 0.001
        returnDict['dyne-s/cm2'] = value * 0.01
        returnDict['lbf-s/ft2'] = value * 2.09e-05
        returnDict['lbf-s/in2'] = value * 1.450377e-07
        returnDict['lb/(ft.hr)'] = value * 2.4190883
        returnDict['lb/(ft.s)'] = value * 0.000672
        returnDict['poundal.s/ft2'] = value * 0.000672
        returnDict['reyn'] = value * 1.450377e-07
    elif units == 'g/(cm.s)':
        returnDict['cp'] = value * 100.0
        returnDict['g/(cm.s)'] = value
        returnDict['kg/(m.hr)'] = value * 359.9999971
        returnDict['kg/(m.s)'] = value * 0.1
        returnDict['kg-f.s/m2'] = value * 0.0101972
        returnDict['kPa-s'] = value * 0.0001
        returnDict['N.s/m2'] = value * 0.1
        returnDict['Pa-s'] = value * 0.1
        returnDict['dyne-s/cm2'] = value
        returnDict['lbf-s/ft2'] = value * 0.0020885
        returnDict['lbf-s/in2'] = value * 1.45e-05
        returnDict['lb/(ft.hr)'] = value * 241.9088329
        returnDict['lb/(ft.s)'] = value * 0.0671969
        returnDict['poundal.s/ft2'] = value * 0.0671969
        returnDict['reyn'] = value * 1.45e-05
    elif units == 'kg/(m.hr)':
        returnDict['cp'] = value * 0.2777778
        returnDict['g/(cm.s)'] = value * 0.0027778
        returnDict['kg/(m.hr)'] = value
        returnDict['kg/(m.s)'] = value * 0.0002778
        returnDict['kg-f.s/m2'] = value * 2.83e-05
        returnDict['kPa-s'] = value * 2.777778e-07
        returnDict['N.s/m2'] = value * 0.000278
        returnDict['Pa-s'] = value * 0.0002778
        returnDict['dyne-s/cm2'] = value * 0.0027778
        returnDict['lbf-s/ft2'] = value * 5.8e-06
        returnDict['lbf-s/in2'] = value * 4.02781e-08
        returnDict['lb/(ft.hr)'] = value * 0.671969
        returnDict['lb/(ft.s)'] = value * 0.0001867
        returnDict['poundal.s/ft2'] = value * 0.0001867
        returnDict['reyn'] = value * 4.02781e-08
    elif units == 'kg/(m.s)':
        returnDict['cp'] = value * 1000.0
        returnDict['g/(cm.s)'] = value * 10.0
        returnDict['kg/(m.hr)'] = value * 3599.9999712
        returnDict['kg/(m.s)'] = value
        returnDict['kg-f.s/m2'] = value * 0.1019716
        returnDict['kPa-s'] = value * 0.001
        returnDict['N.s/m2'] = value
        returnDict['Pa-s'] = value
        returnDict['dyne-s/cm2'] = value * 10.0
        returnDict['lbf-s/ft2'] = value * 0.0208854
        returnDict['lbf-s/in2'] = value * 0.000145
        returnDict['lb/(ft.hr)'] = value * 2419.0883293
        returnDict['lb/(ft.s)'] = value * 0.671969
        returnDict['poundal.s/ft2'] = value * 0.671969
        returnDict['reyn'] = value * 0.000145
    elif units == 'kg-f.s/m2':
        returnDict['cp'] = value * 9806.65
        returnDict['g/(cm.s)'] = value * 98.0665
        returnDict['kg/(m.hr)'] = value * 35303.9397176
        returnDict['kg/(m.s)'] = value * 9.80665
        returnDict['kg-f.s/m2'] = value
        returnDict['kPa-s'] = value * 0.0098067
        returnDict['N.s/m2'] = value * 9.80665
        returnDict['Pa-s'] = value * 9.80665
        returnDict['dyne-s/cm2'] = value * 98.0665
        returnDict['lbf-s/ft2'] = value * 0.2048161
        returnDict['lbf-s/in2'] = value * 0.0014223
        returnDict['lb/(ft.hr)'] = value * 23723.1525646
        returnDict['lb/(ft.s)'] = value * 6.5897646
        returnDict['poundal.s/ft2'] = value * 6.5897646
        returnDict['reyn'] = value * 0.0014223
    elif units == 'kPa-s':
        returnDict['cp'] = value * 1000000.0
        returnDict['g/(cm.s)'] = value * 10000.0
        returnDict['kg/(m.hr)'] = value * 3599999.9712
        returnDict['kg/(m.s)'] = value * 1000.0
        returnDict['kg-f.s/m2'] = value * 101.9716213
        returnDict['kPa-s'] = value
        returnDict['N.s/m2'] = value * 1000.0
        returnDict['Pa-s'] = value * 1000.0
        returnDict['dyne-s/cm2'] = value * 10000.0
        returnDict['lbf-s/ft2'] = value * 20.8854342
        returnDict['lbf-s/in2'] = value * 0.1450377
        returnDict['lb/(ft.hr)'] = value * 2419088.3293091
        returnDict['lb/(ft.s)'] = value * 671.9689751
        returnDict['poundal.s/ft2'] = value * 671.9689751
        returnDict['reyn'] = value * 0.1450377
    elif units == 'N.s/m2':
        returnDict['cp'] = value * 1000.0
        returnDict['g/(cm.s)'] = value * 10.0
        returnDict['kg/(m.hr)'] = value * 3599.9999712
        returnDict['kg/(m.s)'] = value
        returnDict['kg-f.s/m2'] = value * 0.1019716
        returnDict['kPa-s'] = value * 0.001
        returnDict['N.s/m2'] = value
        returnDict['Pa-s'] = value
        returnDict['dyne-s/cm2'] = value * 10.0
        returnDict['lbf-s/ft2'] = value * 0.0208854
        returnDict['lbf-s/in2'] = value * 0.000145
        returnDict['lb/(ft.hr)'] = value * 2419.0883293
        returnDict['lb/(ft.s)'] = value * 0.671969
        returnDict['poundal.s/ft2'] = value * 0.671969
        returnDict['reyn'] = value * 0.000145
    elif units == 'Pa-s':
        returnDict['cp'] = value * 1000.0
        returnDict['g/(cm.s)'] = value * 10.0
        returnDict['kg/(m.hr)'] = value * 3599.9999712
        returnDict['kg/(m.s)'] = value
        returnDict['kg-f.s/m2'] = value * 0.1019716
        returnDict['kPa-s'] = value * 0.001
        returnDict['N.s/m2'] = value
        returnDict['Pa-s'] = value
        returnDict['dyne-s/cm2'] = value * 10.0
        returnDict['lbf-s/ft2'] = value * 0.0208854
        returnDict['lbf-s/in2'] = value * 0.000145
        returnDict['lb/(ft.hr)'] = value * 2419.0883293
        returnDict['lb/(ft.s)'] = value * 0.671969
        returnDict['poundal.s/ft2'] = value * 0.671969
        returnDict['reyn'] = value * 0.000145
    elif units == 'dyne-s/cm2':
        returnDict['cp'] = value * 100.0
        returnDict['g/(cm.s)'] = value
        returnDict['kg/(m.hr)'] = value * 359.9999971
        returnDict['kg/(m.s)'] = value * 0.1
        returnDict['kg-f.s/m2'] = value * 0.0101972
        returnDict['kPa-s'] = value * 0.0001
        returnDict['N.s/m2'] = value * 0.1
        returnDict['Pa-s'] = value * 0.1
        returnDict['dyne-s/cm2'] = value
        returnDict['lbf-s/ft2'] = value * 0.0020885
        returnDict['lbf-s/in2'] = value * 1.45e-05
        returnDict['lb/(ft.hr)'] = value * 241.9088329
        returnDict['lb/(ft.s)'] = value * 0.0671969
        returnDict['poundal.s/ft2'] = value * 0.0671969
        returnDict['reyn'] = value * 1.45e-05
    elif units == 'lbf-s/ft2':
        returnDict['cp'] = value * 47880.2589803
        returnDict['g/(cm.s)'] = value * 478.8025898
        returnDict['kg/(m.hr)'] = value * 172368.9309503
        returnDict['kg/(m.s)'] = value * 47.880259
        returnDict['kg-f.s/m2'] = value * 4.8824276
        returnDict['kPa-s'] = value * 0.0478803
        returnDict['N.s/m2'] = value * 47.880259
        returnDict['Pa-s'] = value * 47.880259
        returnDict['dyne-s/cm2'] = value * 478.8025898
        returnDict['lbf-s/ft2'] = value
        returnDict['lbf-s/in2'] = value * 0.0069444
        returnDict['lb/(ft.hr)'] = value * 115826.5757036
        returnDict['lb/(ft.s)'] = value * 32.1740486
        returnDict['poundal.s/ft2'] = value * 32.1740486
        returnDict['reyn'] = value * 0.0069444
    elif units == 'lbf-s/in2':
        returnDict['cp'] = value * 6894757.293
        returnDict['g/(cm.s)'] = value * 68947.57293
        returnDict['kg/(m.hr)'] = value * 24821126.056231
        returnDict['kg/(m.s)'] = value * 6894.757293
        returnDict['kg-f.s/m2'] = value * 703.0695796
        returnDict['kPa-s'] = value * 6.8947573
        returnDict['N.s/m2'] = value * 6894.757293
        returnDict['Pa-s'] = value * 6894.757293
        returnDict['dyne-s/cm2'] = value * 68947.57293
        returnDict['lbf-s/ft2'] = value * 144.0
        returnDict['lbf-s/in2'] = value
        returnDict['lb/(ft.hr)'] = value * 16679026.9009154
        returnDict['lb/(ft.s)'] = value * 4633.062992
        returnDict['poundal.s/ft2'] = value * 4633.062992
        returnDict['reyn'] = value * 0.9997398074849999
    elif units == 'lb/(ft.hr)':
        returnDict['cp'] = value * 0.4133789
        returnDict['g/(cm.s)'] = value * 0.0041338
        returnDict['kg/(m.hr)'] = value * 1.4881639
        returnDict['kg/(m.s)'] = value * 0.0004134
        returnDict['kg-f.s/m2'] = value * 4.22e-05
        returnDict['kPa-s'] = value * 4.1384274e-07
        returnDict['N.s/m2'] = value * 0.0004134
        returnDict['Pa-s'] = value * 0.0004134
        returnDict['dyne-s/cm2'] = value * 0.0041338
        returnDict['lbf-s/ft2'] = value * 8.6e-06
        returnDict['lbf-s/in2'] = value * 5.972184e-08
        returnDict['lb/(ft.hr)'] = value
        returnDict['lb/(ft.s)'] = value * 0.0002778
        returnDict['poundal.s/ft2'] = value * 0.0002778
        returnDict['reyn'] = value * 5.99401e-08
    elif units == 'lb/(ft.s)':
        returnDict['cp'] = value * 1488.1639436
        returnDict['g/(cm.s)'] = value * 14.8816394
        returnDict['kg/(m.hr)'] = value * 5357.390154
        returnDict['kg/(m.s)'] = value * 1.4881639
        returnDict['kg-f.s/m2'] = value * 0.1517505
        returnDict['kPa-s'] = value * 0.0014882
        returnDict['N.s/m2'] = value * 1.4881639
        returnDict['Pa-s'] = value * 1.4881639
        returnDict['dyne-s/cm2'] = value * 14.8816394
        returnDict['lbf-s/ft2'] = value * 0.031081
        returnDict['lbf-s/in2'] = value * 0.0002158
        returnDict['lb/(ft.hr)'] = value * 3600.000028
        returnDict['lb/(ft.s)'] = value
        returnDict['poundal.s/ft2'] = value
        returnDict['reyn'] = value * 0.0002157837713
    elif units == 'poundal.s/ft2':
        returnDict['cp'] = value * 1488.1639436
        returnDict['g/(cm.s)'] = value * 14.8816394
        returnDict['kg/(m.hr)'] = value * 5357.390154
        returnDict['kg/(m.s)'] = value * 1.4881639
        returnDict['kg-f.s/m2'] = value * 0.1517505
        returnDict['kPa-s'] = value * 0.0014882
        returnDict['N.s/m2'] = value * 1.4881639
        returnDict['Pa-s'] = value * 1.4881639
        returnDict['dyne-s/cm2'] = value * 14.8816394
        returnDict['lbf-s/ft2'] = value * 0.031081
        returnDict['lbf-s/in2'] = value * 0.0002158
        returnDict['lb/(ft.hr)'] = value * 3600.000028
        returnDict['lb/(ft.s)'] = value
        returnDict['poundal.s/ft2'] = value
        returnDict['reyn'] = value * 0.0002157837713
    elif units == 'reyn':
        returnDict['cp'] = value * 6894757.293
        returnDict['g/(cm.s)'] = value * 68947.57293
        returnDict['kg/(m.hr)'] = value * 24821126.056231
        returnDict['kg/(m.s)'] = value * 6894.757293
        returnDict['kg-f.s/m2'] = value * 703.0695796
        returnDict['kPa-s'] = value * 6.8947573
        returnDict['N.s/m2'] = value * 6894.757293
        returnDict['Pa-s'] = value * 6894.757293
        returnDict['dyne-s/cm2'] = value * 68947.57293
        returnDict['lbf-s/ft2'] = value * 144.0
        returnDict['lbf-s/in2'] = value * 0.9999936
        returnDict['lb/(ft.hr)'] = value * 16679026.9009154
        returnDict['lb/(ft.s)'] = value * 4633.062992
        returnDict['poundal.s/ft2'] = value * 4633.062992
        returnDict['reyn'] = value
    else:
        raise Exception("""Invalid Input. Make sure values are passed as
        integers, units are passed as stings and that the
        correct units are input. Consult the
        documnetation for more information on each function.""")
    return returnDict


def oil_volume(value, units):
    returnDict = {}
    if units == 'bbl':
        returnDict['bbl'] = value
        returnDict['BOE'] = value
        returnDict['gal'] = value * 42.0
        returnDict['kL'] = value * 0.1589873
        returnDict['MMBOE'] = value * 1e-06
        returnDict['KBOE'] = value * 0.001
        returnDict['toe'] = value * 0.1363636
    elif units == 'BOE':
        returnDict['bbl'] = value
        returnDict['BOE'] = value
        returnDict['gal'] = value * 42.0
        returnDict['kL'] = value * 0.1589873
        returnDict['MMBOE'] = value * 1e-06
        returnDict['KBOE'] = value * 0.001
        returnDict['toe'] = value * 0.1363636
    elif units == 'gal':
        returnDict['bbl'] = value * 0.0238095
        returnDict['BOE'] = value * 0.0238095
        returnDict['gal'] = value
        returnDict['kL'] = value * 0.0037854
        returnDict['MMBOE'] = value * 2.38e-08
        returnDict['KBOE'] = value * 2.38e-05
        returnDict['toe'] = value * 0.0032468
    elif units == 'kL':
        returnDict['bbl'] = value * 6.2898108
        returnDict['BOE'] = value * 6.2898108
        returnDict['gal'] = value * 264.1720524
        returnDict['kL'] = value
        returnDict['MMBOE'] = value * 6.3e-06
        returnDict['KBOE'] = value * 0.0062898
        returnDict['toe'] = value * 0.8577015
    elif units == 'MMBOE':
        returnDict['bbl'] = value * 1000000.0
        returnDict['BOE'] = value * 1000000.0
        returnDict['gal'] = value * 42000000.0
        returnDict['kL'] = value * 158987.2949287
        returnDict['MMBOE'] = value
        returnDict['KBOE'] = value * 1000.0
        returnDict['toe'] = value * 136363.6363636
    elif units == 'KBOE':
        returnDict['bbl'] = value * 1000.0
        returnDict['BOE'] = value * 1000.0
        returnDict['gal'] = value * 42000.0
        returnDict['kL'] = value * 158.9872949
        returnDict['MMBOE'] = value * 0.001
        returnDict['KBOE'] = value
        returnDict['toe'] = value * 136.3636364
    elif units == 'toe':
        returnDict['bbl'] = value * 7.3333333
        returnDict['BOE'] = value * 7.3333333
        returnDict['gal'] = value * 308.0
        returnDict['kL'] = value * 1.1659068
        returnDict['MMBOE'] = value * 7.3e-06
        returnDict['KBOE'] = value * 0.0073333
        returnDict['toe'] = value
    else:
        raise Exception("""Invalid Input. Make sure values are passed as
        integers, units are passed as stings and that the
        correct units are input. Consult the
        documnetation for more information on each function.""")
    return returnDict


def surface_tension(value, units):
    returnDict = {}
    if units == 'N/m':
        returnDict['N/m'] = value * 1.0
        returnDict['mN/m'] = value * 1000.0
        returnDict['gf/cm'] = value * 1.019716213
        returnDict['dyn/cm'] = value * 1000.0
        returnDict['erg/cm2'] = value * 1000.0
        returnDict['erg/mm2'] = value * 10.0
        returnDict['pdl/in'] = value * 0.1837185501
        returnDict['lbf/ft'] = value * 0.005710147098
    elif units == 'mN/m':
        returnDict['N/m'] = value * 0.001
        returnDict['mN/m'] = value * 1.0
        returnDict['gf/cm'] = value * 0.001019716213
        returnDict['dyn/cm'] = value * 1.0
        returnDict['erg/cm2'] = value * 1.0
        returnDict['erg/mm2'] = value * 0.01
        returnDict['pdl/in'] = value * 0.0001837185501
        returnDict['lbf/ft'] = value * 5.710147098e-06
    elif units == 'gf/cm':
        returnDict['N/m'] = value * 0.9806649999787735
        returnDict['mN/m'] = value * 980.6649999787735
        returnDict['gf/cm'] = value * 1.0
        returnDict['dyn/cm'] = value * 980.6649999788
        returnDict['erg/cm2'] = value * 980.6649999788
        returnDict['erg/mm2'] = value * 9.806649999788
        returnDict['pdl/in'] = value * 0.1801663519299
        returnDict['lbf/ft'] = value * 0.005599741403739
    elif units == 'dyn/cm':
        returnDict['N/m'] = value * 0.001
        returnDict['mN/m'] = value * 1.0
        returnDict['gf/cm'] = value * 0.0010197162129999724
        returnDict['dyn/cm'] = value * 1.0
        returnDict['erg/cm2'] = value * 1.0
        returnDict['erg/mm2'] = value * 0.01
        returnDict['pdl/in'] = value * 0.0001837185501
        returnDict['lbf/ft'] = value * 5.710147098e-06
    elif units == 'erg/cm2':
        returnDict['N/m'] = value * 0.001
        returnDict['mN/m'] = value * 1.0
        returnDict['gf/cm'] = value * 0.0010197162129999724
        returnDict['dyn/cm'] = value * 1.0
        returnDict['erg/cm2'] = value * 1.0
        returnDict['erg/mm2'] = value * 0.01
        returnDict['pdl/in'] = value * 0.0001837185501
        returnDict['lbf/ft'] = value * 5.710147098e-06
    elif units == 'erg/mm2':
        returnDict['N/m'] = value * 0.1
        returnDict['mN/m'] = value * 100.0
        returnDict['gf/cm'] = value * 0.10197162129999725
        returnDict['dyn/cm'] = value * 100.0
        returnDict['erg/cm2'] = value * 100.0
        returnDict['erg/mm2'] = value * 1.0
        returnDict['pdl/in'] = value * 0.01837185501
        returnDict['lbf/ft'] = value * 0.0005710147098
    elif units == 'pdl/in':
        returnDict['N/m'] = value * 5.443108490980847
        returnDict['mN/m'] = value * 5443.108490980846
        returnDict['gf/cm'] = value * 5.550425977371651
        returnDict['dyn/cm'] = value * 5443.108490980846
        returnDict['erg/cm2'] = value * 5443.108490980846
        returnDict['erg/mm2'] = value * 54.43108490980846
        returnDict['pdl/in'] = value * 1.0
        returnDict['lbf/ft'] = value * 0.03108095015387
    elif units == 'lbf/ft':
        returnDict['N/m'] = value * 175.1268369864331
        returnDict['mN/m'] = value * 175126.8369864331
        returnDict['gf/cm'] = value * 178.57967500647274
        returnDict['dyn/cm'] = value * 175126.8369864331
        returnDict['erg/cm2'] = value * 175126.8369864331
        returnDict['erg/mm2'] = value * 1751.268369864331
        returnDict['pdl/in'] = value * 32.1740485747501
        returnDict['lbf/ft'] = value * 1.0
    else:
        raise Exception("""Invalid Input. Make sure values are passed as
        integers, units are passed as stings and that the
        correct units are input. Consult the
        documnetation for more information on each function.""")
    return returnDict


def additive_volume(value, units):
    returnDict = {}
    if units == 'sack':
        returnDict['sack'] = value
        returnDict['ft3'] = value * 3.7333680555556
        returnDict['m3'] = value * 0.10571721050064
        returnDict['bbl'] = value * 0.88658833230262
    elif units == 'ft3':
        returnDict['sack'] = value * 0.267854651649442
        returnDict['ft3'] = value
        returnDict['m3'] = value * 0.0283168
        returnDict['bbl'] = value * 0.17811
    elif units == 'm3':
        returnDict['sack'] = value * 9.45919775280058
        returnDict['ft3'] = value * 35.3147248276641
        returnDict['m3'] = value
        returnDict['bbl'] = value * 6.2898
    elif units == 'bbl':
        returnDict['sack'] = value * 1.12791919718008
        returnDict['ft3'] = value * 5.61450788838358
        returnDict['m3'] = value * 0.158987567172247
        returnDict['bbl'] = value
    else:
        raise Exception("""Invalid Input. Make sure values are passed as
        integers, units are passed as stings and that the
        correct units are input. Consult the
        documnetation for more information on each function.""")
    return returnDict
