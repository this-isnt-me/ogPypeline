def electric_current(value, units):
    returnDict = {}
    if units == 'amp':
        returnDict['amp'] = value
        returnDict['biot'] = value * 0.1
        returnDict['camp'] = value * 100.0
        returnDict['gilbert'] = value * 1.2566371
        returnDict['kamp'] = value * 0.001
        returnDict['mamp'] = value * 1000.0
        returnDict['v/ohm'] = value
        returnDict['w/v'] = value
    elif units == 'biot':
        returnDict['amp'] = value * 10.0
        returnDict['biot'] = value
        returnDict['camp'] = value * 1000.0
        returnDict['gilbert'] = value * 12.5663709
        returnDict['kamp'] = value * 0.01
        returnDict['mamp'] = value * 10000.0
        returnDict['v/ohm'] = value * 10.0
        returnDict['w/v'] = value * 10.0
    elif units == 'camp':
        returnDict['amp'] = value * 0.01
        returnDict['biot'] = value * 0.001
        returnDict['camp'] = value
        returnDict['gilbert'] = value * 0.0125664
        returnDict['kamp'] = value * 1e-05
        returnDict['mamp'] = value * 10.0
        returnDict['v/ohm'] = value * 0.01
        returnDict['w/v'] = value * 0.01
    elif units == 'gilbert':
        returnDict['amp'] = value * 0.7957747
        returnDict['biot'] = value * 0.0795775
        returnDict['camp'] = value * 79.57747
        returnDict['gilbert'] = value
        returnDict['kamp'] = value * 0.0007958
        returnDict['mamp'] = value * 795.7747
        returnDict['v/ohm'] = value * 0.7957747
        returnDict['w/v'] = value * 0.7957747
    elif units == 'kamp':
        returnDict['amp'] = value * 1000.0
        returnDict['biot'] = value * 100.0
        returnDict['camp'] = value * 100000.0
        returnDict['gilbert'] = value * 1256.6370858
        returnDict['kamp'] = value
        returnDict['mamp'] = value * 1000000.0
        returnDict['v/ohm'] = value * 1000.0
        returnDict['w/v'] = value * 1000.0
    elif units == 'mamp':
        returnDict['amp'] = value * 0.001
        returnDict['biot'] = value * 0.0001
        returnDict['camp'] = value * 0.1
        returnDict['gilbert'] = value * 0.0012566
        returnDict['kamp'] = value * 1e-06
        returnDict['mamp'] = value
        returnDict['v/ohm'] = value * 0.001
        returnDict['w/v'] = value * 0.001
    elif units == 'v/ohm':
        returnDict['amp'] = value
        returnDict['biot'] = value * 0.1
        returnDict['camp'] = value * 100.0
        returnDict['gilbert'] = value * 1.2566371
        returnDict['kamp'] = value * 0.001
        returnDict['mamp'] = value * 1000.0
        returnDict['v/ohm'] = value
        returnDict['w/v'] = value
    elif units == 'w/v':
        returnDict['amp'] = value
        returnDict['biot'] = value * 0.1
        returnDict['camp'] = value * 100.0
        returnDict['gilbert'] = value * 1.2566371
        returnDict['kamp'] = value * 0.001
        returnDict['mamp'] = value * 1000.0
        returnDict['v/ohm'] = value
        returnDict['w/v'] = value
    else:
        raise Exception("""Invalid Input. Make sure values are passed as
        integers, units are passed as stings and that the
        correct units are input. Consult the
        documnetation for more information on each function.""")
    return returnDict


def fracture_conductivity(value, units):
    returnDict = {}
    if units == 'darcy-in':
        returnDict['darcy-in'] = value
        returnDict['mu.m2-m'] = value * 22.7837142
    elif units == 'mu.m2-m':
        returnDict['darcy-in'] = value * 0.043891
        returnDict['mu.m2-m'] = value
    else:
        raise Exception("""Invalid Input. Make sure values are passed as
        integers, units are passed as stings and that the
        correct units are input. Consult the
        documnetation for more information on each function.""")
    return returnDict


def heat_capacity(value, units):
    returnDict = {}
    if units == 'Btu/lb-F':
        returnDict['Btu/lb-F'] = value
        returnDict['J/kg-C'] = value * 4186.8
    elif units == 'J/kg-C':
        returnDict['Btu/lb-F'] = value * 0.0002388
        returnDict['J/kg-C'] = value
    else:
        raise Exception("""Invalid Input. Make sure values are passed as
        integers, units are passed as stings and that the
        correct units are input. Consult the
        documnetation for more information on each function.""")
    return returnDict


def power_area(value, units):
    returnDict = {}
    if units == 'HP/in2':
        returnDict['HP/in2'] = value
        returnDict['kW/mm2'] = value * 0.001156
    elif units == 'kW/mm2':
        returnDict['HP/in2'] = value * 865.0519031
        returnDict['kW/mm2'] = value
    else:
        raise Exception("""Invalid Input. Make sure values are passed as
        integers, units are passed as stings and that the
        correct units are input. Consult the
        documnetation for more information on each function.""")
    return returnDict


def angular_velocity(value, units):
    returnDict = {}
    if units == 'deg/hr':
        returnDict['deg/hr'] = value
        returnDict['deg/min'] = value * 0.0166667
        returnDict['deg/sec'] = value * 0.0002778
        returnDict['rad/hr'] = value * 0.0174533
        returnDict['rad/min'] = value * 0.0002909
        returnDict['rad/sec'] = value * 4.8e-06
        returnDict['rph'] = value * 0.0027778
        returnDict['rpm'] = value * 4.63e-05
        returnDict['rps'] = value * 7.72e-07
    elif units == 'deg/min':
        returnDict['deg/hr'] = value * 60.0
        returnDict['deg/min'] = value
        returnDict['deg/sec'] = value * 0.0166667
        returnDict['rad/hr'] = value * 1.0471976
        returnDict['rad/min'] = value * 0.0174533
        returnDict['rad/sec'] = value * 0.0002909
        returnDict['rph'] = value * 0.1666667
        returnDict['rpm'] = value * 0.0027778
        returnDict['rps'] = value * 4.63e-05
    elif units == 'deg/sec':
        returnDict['deg/hr'] = value * 3600.0
        returnDict['deg/min'] = value * 60.0
        returnDict['deg/sec'] = value
        returnDict['rad/hr'] = value * 62.8318543
        returnDict['rad/min'] = value * 1.0471976
        returnDict['rad/sec'] = value * 0.0174533
        returnDict['rph'] = value * 10.0
        returnDict['rpm'] = value * 0.1666667
        returnDict['rps'] = value * 0.0027778
    elif units == 'rad/hr':
        returnDict['deg/hr'] = value * 57.2957784
        returnDict['deg/min'] = value * 0.9549296
        returnDict['deg/sec'] = value * 0.0159155
        returnDict['rad/hr'] = value
        returnDict['rad/min'] = value * 0.0166667
        returnDict['rad/sec'] = value * 0.0002778
        returnDict['rph'] = value * 0.1591549
        returnDict['rpm'] = value * 0.0026526
        returnDict['rps'] = value * 4.42e-05
    elif units == 'rad/min':
        returnDict['deg/hr'] = value * 3437.746704
        returnDict['deg/min'] = value * 57.2957784
        returnDict['deg/sec'] = value * 0.9549296
        returnDict['rad/hr'] = value * 60.0
        returnDict['rad/min'] = value
        returnDict['rad/sec'] = value * 0.0166667
        returnDict['rph'] = value * 9.5492964
        returnDict['rpm'] = value * 0.1591549
        returnDict['rps'] = value * 0.0026526
    elif units == 'rad/sec':
        returnDict['deg/hr'] = value * 206264.80224
        returnDict['deg/min'] = value * 3437.746704
        returnDict['deg/sec'] = value * 57.2957784
        returnDict['rad/hr'] = value * 3600.0
        returnDict['rad/min'] = value * 60.0
        returnDict['rad/sec'] = value
        returnDict['rph'] = value * 572.957784
        returnDict['rpm'] = value * 9.5492964
        returnDict['rps'] = value * 0.1591549
    elif units == 'rph':
        returnDict['deg/hr'] = value * 360.0
        returnDict['deg/min'] = value * 6.0
        returnDict['deg/sec'] = value * 0.1
        returnDict['rad/hr'] = value * 6.2831854
        returnDict['rad/min'] = value * 0.1047198
        returnDict['rad/sec'] = value * 0.0017453
        returnDict['rph'] = value
        returnDict['rpm'] = value * 0.0166667
        returnDict['rps'] = value * 0.0002778
    elif units == 'rpm':
        returnDict['deg/hr'] = value * 21600.0
        returnDict['deg/min'] = value * 360.0
        returnDict['deg/sec'] = value * 6.0
        returnDict['rad/hr'] = value * 376.9911258
        returnDict['rad/min'] = value * 6.2831854
        returnDict['rad/sec'] = value * 0.1047198
        returnDict['rph'] = value * 60.0
        returnDict['rpm'] = value
        returnDict['rps'] = value * 0.0166667
    elif units == 'rps':
        returnDict['deg/hr'] = value * 1296000.0
        returnDict['deg/min'] = value * 21600.0
        returnDict['deg/sec'] = value * 360.0
        returnDict['rad/hr'] = value * 22619.4675453
        returnDict['rad/min'] = value * 376.9911258
        returnDict['rad/sec'] = value * 6.2831854
        returnDict['rph'] = value * 3600.0
        returnDict['rpm'] = value * 60.0
        returnDict['rps'] = value
    else:
        raise Exception("""Invalid Input. Make sure values are passed as
        integers, units are passed as stings and that the
        correct units are input. Consult the
        documnetation for more information on each function.""")
    return returnDict


def force(value, units):
    returnDict = {}
    if units == 'daN':
        returnDict['daN'] = value
        returnDict['dyn'] = value * 1000000.0
        returnDict['gf'] = value * 1019.72
        returnDict['kgf'] = value * 1.02
        returnDict['kN'] = value * 0.01
        returnDict['kip'] = value * 0.00225
        returnDict['klbs'] = value * 0.00225
        returnDict['MN'] = value * 1e-05
        returnDict['N'] = value * 10.0
        returnDict['ozf'] = value * 35.97
        returnDict['lbf'] = value * 2.25
        returnDict['pdl'] = value * 72.39
        returnDict['sn'] = value * 0.01
        returnDict['tf-metric'] = value * 0.00102
        returnDict['tf-long'] = value * 0.001
        returnDict['tf-short'] = value * 0.00112
        returnDict['hN'] = value * 0.1
        returnDict['J/m'] = value
        returnDict['mN'] = value * 10000.0
    elif units == 'dyn':
        returnDict['daN'] = value * 1e-06
        returnDict['dyn'] = value
        returnDict['gf'] = value * 0.00102
        returnDict['kgf'] = value * 1.02e-06
        returnDict['kN'] = value * 1e-08
        returnDict['kip'] = value * 2.25e-09
        returnDict['klbs'] = value * 2.25e-09
        returnDict['MN'] = value * 1e-11
        returnDict['N'] = value * 1e-05
        returnDict['ozf'] = value * 3.6e-05
        returnDict['lbf'] = value * 2.25e-06
        returnDict['pdl'] = value * 7.2e-05
        returnDict['sn'] = value * 9.95e-09
        returnDict['tf-metric'] = value * 1.01e-09
        returnDict['tf-long'] = value * 9.94e-10
        returnDict['tf-short'] = value * 1.11e-09
        returnDict['hN'] = value * 1.0000000000000001e-07
        returnDict['J/m'] = value * 1e-05
        returnDict['mN'] = value * 0.01
    elif units == 'gf':
        returnDict['daN'] = value * 0.00098
        returnDict['dyn'] = value * 980.0
        returnDict['gf'] = value
        returnDict['kgf'] = value * 0.001
        returnDict['kN'] = value * 9.8e-06
        returnDict['kip'] = value * 2.2e-06
        returnDict['klbs'] = value * 2.2e-06
        returnDict['MN'] = value * 9.79e-09
        returnDict['N'] = value * 0.01
        returnDict['ozf'] = value * 0.04
        returnDict['lbf'] = value * 0.0022
        returnDict['pdl'] = value * 0.07
        returnDict['sn'] = value * 9.8e-06
        returnDict['tf-metric'] = value * 1e-06
        returnDict['tf-long'] = value * 9.84e-07
        returnDict['tf-short'] = value * 1.1e-06
        returnDict['hN'] = value * 0.0001
        returnDict['J/m'] = value * 0.01
        returnDict['mN'] = value * 10.0
    elif units == 'kgf':
        returnDict['daN'] = value * 0.98
        returnDict['dyn'] = value * 980665.0
        returnDict['gf'] = value * 1000.0
        returnDict['kgf'] = value
        returnDict['kN'] = value * 0.01
        returnDict['kip'] = value * 0.0022
        returnDict['klbs'] = value * 0.0022
        returnDict['MN'] = value * 9.8e-06
        returnDict['N'] = value * 9.81
        returnDict['ozf'] = value * 35.27
        returnDict['lbf'] = value * 2.2
        returnDict['pdl'] = value * 70.93
        returnDict['sn'] = value * 0.01
        returnDict['tf-metric'] = value * 0.001
        returnDict['tf-long'] = value * 0.00098
        returnDict['tf-short'] = value * 0.0011
        returnDict['hN'] = value * 0.0981
        returnDict['J/m'] = value * 9.81
        returnDict['mN'] = value * 9810.0
    elif units == 'kN':
        returnDict['daN'] = value * 100.0
        returnDict['dyn'] = value * 100000000.0
        returnDict['gf'] = value * 101971.62
        returnDict['kgf'] = value * 101.97
        returnDict['kN'] = value
        returnDict['kip'] = value * 0.22
        returnDict['klbs'] = value * 0.22
        returnDict['MN'] = value * 0.001
        returnDict['N'] = value * 1000.0
        returnDict['ozf'] = value * 3596.94
        returnDict['lbf'] = value * 224.81
        returnDict['pdl'] = value * 7233.05
        returnDict['sn'] = value
        returnDict['tf-metric'] = value * 0.1
        returnDict['tf-long'] = value * 0.098
        returnDict['tf-short'] = value * 0.11
        returnDict['hN'] = value * 10.0
        returnDict['J/m'] = value * 1000.0
        returnDict['mN'] = value * 1000000.0
    elif units == 'kip':
        returnDict['daN'] = value * 444.82
        returnDict['dyn'] = value * 445000000.0
        returnDict['gf'] = value * 453592.37
        returnDict['kgf'] = value * 453.59
        returnDict['kN'] = value * 4.45
        returnDict['kip'] = value
        returnDict['klbs'] = value
        returnDict['MN'] = value * 0.00445
        returnDict['N'] = value * 4448.22
        returnDict['ozf'] = value * 16000.0
        returnDict['lbf'] = value * 1000.0
        returnDict['pdl'] = value * 32174.05
        returnDict['sn'] = value * 4.45
        returnDict['tf-metric'] = value * 0.45
        returnDict['tf-long'] = value * 0.45
        returnDict['tf-short'] = value * 0.5
        returnDict['hN'] = value * 44.482200000000006
        returnDict['J/m'] = value * 4448.22
        returnDict['mN'] = value * 4448220.0
    elif units == 'klbs':
        returnDict['daN'] = value * 444.82
        returnDict['dyn'] = value * 445000000.0
        returnDict['gf'] = value * 453592.37
        returnDict['kgf'] = value * 453.59
        returnDict['kN'] = value * 4.45
        returnDict['kip'] = value
        returnDict['klbs'] = value
        returnDict['MN'] = value * 0.00445
        returnDict['N'] = value * 4448.22
        returnDict['ozf'] = value * 16000.0
        returnDict['lbf'] = value * 1000.0
        returnDict['pdl'] = value * 32174.05
        returnDict['sn'] = value * 4.45
        returnDict['tf-metric'] = value * 0.45
        returnDict['tf-long'] = value * 0.45
        returnDict['tf-short'] = value * 0.5
        returnDict['hN'] = value * 44.482200000000006
        returnDict['J/m'] = value * 4448.22
        returnDict['mN'] = value * 4448220.0
    elif units == 'MN':
        returnDict['daN'] = value * 100000.0
        returnDict['dyn'] = value * 100000000000.0
        returnDict['gf'] = value * 102000000.0
        returnDict['kgf'] = value * 101971.62
        returnDict['kN'] = value * 1000.0
        returnDict['kip'] = value * 224.81
        returnDict['klbs'] = value * 224.81
        returnDict['MN'] = value
        returnDict['N'] = value * 1000000.0
        returnDict['ozf'] = value * 3596943.09
        returnDict['lbf'] = value * 224808.94
        returnDict['pdl'] = value * 7233013.85
        returnDict['sn'] = value * 1000.0
        returnDict['tf-metric'] = value * 101.97
        returnDict['tf-long'] = value * 100.36
        returnDict['tf-short'] = value * 112.4
        returnDict['hN'] = value * 10000.0
        returnDict['J/m'] = value * 1000000.0
        returnDict['mN'] = value * 1000000000.0
    elif units == 'N':
        returnDict['daN'] = value * 0.1
        returnDict['dyn'] = value * 100000.0
        returnDict['gf'] = value * 101.97
        returnDict['kgf'] = value * 0.1
        returnDict['kN'] = value * 0.001
        returnDict['kip'] = value * 0.000225
        returnDict['klbs'] = value * 0.000225
        returnDict['MN'] = value * 1e-06
        returnDict['N'] = value
        returnDict['ozf'] = value * 3.6
        returnDict['lbf'] = value * 0.22
        returnDict['pdl'] = value * 7.23
        returnDict['sn'] = value * 0.001
        returnDict['tf-metric'] = value * 0.000102
        returnDict['tf-long'] = value * 0.0001
        returnDict['tf-short'] = value * 0.000112
        returnDict['hN'] = value * 0.01
        returnDict['J/m'] = value
        returnDict['mN'] = value * 1000.0
    elif units == 'ozf':
        returnDict['daN'] = value * 0.03
        returnDict['dyn'] = value * 27801.39
        returnDict['gf'] = value * 28.35
        returnDict['kgf'] = value * 0.03
        returnDict['kN'] = value * 0.000278
        returnDict['kip'] = value * 6.3e-05
        returnDict['klbs'] = value * 6.3e-05
        returnDict['MN'] = value * 2.78e-07
        returnDict['N'] = value * 0.28
        returnDict['ozf'] = value
        returnDict['lbf'] = value * 0.06
        returnDict['pdl'] = value * 2.01
        returnDict['sn'] = value * 0.000278
        returnDict['tf-metric'] = value * 2.83e-05
        returnDict['tf-long'] = value * 2.79e-05
        returnDict['tf-short'] = value * 3.13e-05
        returnDict['hN'] = value * 0.0028000000000000004
        returnDict['J/m'] = value * 0.28
        returnDict['mN'] = value * 280.0
    elif units == 'lbf':
        returnDict['daN'] = value * 0.44
        returnDict['dyn'] = value * 444822.16
        returnDict['gf'] = value * 453.59
        returnDict['kgf'] = value * 0.45
        returnDict['kN'] = value * 0.00445
        returnDict['kip'] = value * 0.001
        returnDict['klbs'] = value * 0.001
        returnDict['MN'] = value * 4.45e-06
        returnDict['N'] = value * 4.45
        returnDict['ozf'] = value * 16.0
        returnDict['lbf'] = value
        returnDict['pdl'] = value * 32.17
        returnDict['sn'] = value * 0.00445
        returnDict['tf-metric'] = value * 0.000454
        returnDict['tf-long'] = value * 0.000446
        returnDict['tf-short'] = value * 0.0005
        returnDict['hN'] = value * 0.044500000000000005
        returnDict['J/m'] = value * 4.45
        returnDict['mN'] = value * 4450.0
    elif units == 'pdl':
        returnDict['daN'] = value * 0.01
        returnDict['dyn'] = value * 13825.5
        returnDict['gf'] = value * 14.1
        returnDict['kgf'] = value * 0.01
        returnDict['kN'] = value * 0.000138
        returnDict['kip'] = value * 3.11e-05
        returnDict['klbs'] = value * 3.11e-05
        returnDict['MN'] = value * 1.38e-07
        returnDict['N'] = value * 0.14
        returnDict['ozf'] = value * 0.5
        returnDict['lbf'] = value * 0.03
        returnDict['pdl'] = value
        returnDict['sn'] = value * 0.000138
        returnDict['tf-metric'] = value * 1.41e-05
        returnDict['tf-long'] = value * 1.39e-05
        returnDict['tf-short'] = value * 1.55e-05
        returnDict['hN'] = value * 0.0014000000000000002
        returnDict['J/m'] = value * 0.14
        returnDict['mN'] = value * 140.0
    elif units == 'sn':
        returnDict['daN'] = value * 100.0
        returnDict['dyn'] = value * 100000000.0
        returnDict['gf'] = value * 101971.62
        returnDict['kgf'] = value * 101.97
        returnDict['kN'] = value
        returnDict['kip'] = value * 0.22
        returnDict['klbs'] = value * 0.22
        returnDict['MN'] = value * 0.001
        returnDict['N'] = value * 1000.0
        returnDict['ozf'] = value * 3596.94
        returnDict['lbf'] = value * 224.81
        returnDict['pdl'] = value * 7233.01
        returnDict['sn'] = value
        returnDict['tf-metric'] = value * 0.1
        returnDict['tf-long'] = value * 0.098
        returnDict['tf-short'] = value * 0.11
        returnDict['hN'] = value * 10.0
        returnDict['J/m'] = value * 1000.0
        returnDict['mN'] = value * 1000000.0
    elif units == 'tf-metric':
        returnDict['daN'] = value * 980.66
        returnDict['dyn'] = value * 981000000.0
        returnDict['gf'] = value * 1000000.0
        returnDict['kgf'] = value * 1000.0
        returnDict['kN'] = value * 9.81
        returnDict['kip'] = value * 2.2
        returnDict['klbs'] = value * 2.2
        returnDict['MN'] = value * 0.01
        returnDict['N'] = value * 9806.65
        returnDict['ozf'] = value * 35273.96
        returnDict['lbf'] = value * 2204.62
        returnDict['pdl'] = value * 70931.64
        returnDict['sn'] = value * 9.81
        returnDict['tf-metric'] = value
        returnDict['tf-long'] = value * 0.98
        returnDict['tf-short'] = value * 1.1
        returnDict['hN'] = value * 98.06649999999999
        returnDict['J/m'] = value * 9806.65
        returnDict['mN'] = value * 9806650.0
    elif units == 'tf-long':
        returnDict['daN'] = value * 996.4
        returnDict['dyn'] = value * 996000000.0
        returnDict['gf'] = value * 1016046.91
        returnDict['kgf'] = value * 1016.05
        returnDict['kN'] = value * 9.96
        returnDict['kip'] = value * 2.24
        returnDict['klbs'] = value * 2.24
        returnDict['MN'] = value * 0.01
        returnDict['N'] = value * 9964.02
        returnDict['ozf'] = value * 35840.0
        returnDict['lbf'] = value * 2240.0
        returnDict['pdl'] = value * 72069.87
        returnDict['sn'] = value * 9.96
        returnDict['tf-metric'] = value * 1.02
        returnDict['tf-long'] = value
        returnDict['tf-short'] = value * 1.12
        returnDict['hN'] = value * 99.64020000000001
        returnDict['J/m'] = value * 9964.02
        returnDict['mN'] = value * 9964020.0
    elif units == 'tf-short':
        returnDict['daN'] = value * 889.64
        returnDict['dyn'] = value * 890000000.0
        returnDict['gf'] = value * 907184.74
        returnDict['kgf'] = value * 907.18
        returnDict['kN'] = value * 8.9
        returnDict['kip'] = value * 2.0
        returnDict['klbs'] = value * 2.0
        returnDict['MN'] = value * 0.01
        returnDict['N'] = value * 8896.44
        returnDict['ozf'] = value * 32000.0
        returnDict['lbf'] = value * 2000.0
        returnDict['pdl'] = value * 64348.1
        returnDict['sn'] = value * 8.9
        returnDict['tf-metric'] = value * 0.91
        returnDict['tf-long'] = value * 0.89
        returnDict['tf-short'] = value
        returnDict['hN'] = value * 88.96440000000001
        returnDict['J/m'] = value * 8896.44
        returnDict['mN'] = value * 8896440.0
    elif units == 'hN':
        returnDict['daN'] = value * 10.0
        returnDict['dyn'] = value * 10000000.0
        returnDict['gf'] = value * 10197.16
        returnDict['kgf'] = value * 10.2
        returnDict['kN'] = value * 0.1
        returnDict['kip'] = value * 0.02
        returnDict['klbs'] = value * 0.02
        returnDict['MN'] = value * 0.0001
        returnDict['N'] = value * 100.0
        returnDict['ozf'] = value * 359.69
        returnDict['lbf'] = value * 22.48
        returnDict['pdl'] = value * 723.3
        returnDict['sn'] = value * 0.1
        returnDict['tf-metric'] = value * 0.01
        returnDict['tf-long'] = value * 0.0098
        returnDict['tf-short'] = value * 0.011
        returnDict['hN'] = value
        returnDict['J/m'] = value * 100.0
        returnDict['mN'] = value * 100000.0
    elif units == 'J/m':
        returnDict['daN'] = value * 0.1
        returnDict['dyn'] = value * 100000.0
        returnDict['gf'] = value * 101.97
        returnDict['kgf'] = value * 0.1
        returnDict['kN'] = value * 0.001
        returnDict['kip'] = value * 0.000225
        returnDict['klbs'] = value * 0.000225
        returnDict['MN'] = value * 1e-06
        returnDict['N'] = value
        returnDict['ozf'] = value * 3.6
        returnDict['lbf'] = value * 0.22
        returnDict['pdl'] = value * 7.23
        returnDict['sn'] = value * 0.001
        returnDict['tf-metric'] = value * 0.000102
        returnDict['tf-long'] = value * 0.0001
        returnDict['tf-short'] = value * 0.000112
        returnDict['hN'] = value * 0.01
        returnDict['J/m'] = value
        returnDict['mN'] = value * 1000.0
    elif units == 'mN':
        returnDict['daN'] = value * 0.0001
        returnDict['dyn'] = value * 100.0
        returnDict['gf'] = value * 0.1
        returnDict['kgf'] = value * 0.0001
        returnDict['kN'] = value * 9.81e-07
        returnDict['kip'] = value * 2.21e-07
        returnDict['klbs'] = value * 2.21e-07
        returnDict['MN'] = value * 9.83e-10
        returnDict['N'] = value * 0.00098
        returnDict['ozf'] = value * 0.00353
        returnDict['lbf'] = value * 0.000221
        returnDict['pdl'] = value * 0.01
        returnDict['sn'] = value * 1.38e-06
        returnDict['tf-metric'] = value * 1.41e-07
        returnDict['tf-long'] = value * 1.39e-07
        returnDict['tf-short'] = value * 1.56e-07
        returnDict['hN'] = value * 9.8e-06
        returnDict['J/m'] = value * 0.00098
        returnDict['mN'] = value
    else:
        raise Exception("""Invalid Input. Make sure values are passed as
        integers, units are passed as stings and that the
        correct units are input. Consult the
        documnetation for more information on each function.""")
    return returnDict


def power(value, units):
    returnDict = {}
    if units == 'BTU/sec':
        returnDict['BTU/sec'] = value
        returnDict['BTU/min'] = value * 59.9999772
        returnDict['cal/min'] = value * 15116.064775
        returnDict['cal/sec'] = value * 251.9344129
        returnDict['ft-lb/min'] = value * 46678.8010423
        returnDict['ft-lb/sec'] = value * 777.9798223
        returnDict['hp'] = value * 1.4145088
        returnDict['hp-elec'] = value * 1.4139397
        returnDict['hp-met'] = value * 1.4341275
        returnDict['J/s'] = value * 1054.799
        returnDict['kcal/min'] = value * 15.1160648
        returnDict['kcal/s'] = value * 0.2519344
        returnDict['kg-m/min'] = value * 6453.5725342
        returnDict['kg-m/sec'] = value * 107.5595642
        returnDict['kW'] = value * 1.054799
        returnDict['MW'] = value * 0.0010548
        returnDict['N-m/s'] = value * 1054.799
        returnDict['ton-ref'] = value * 0.299927
        returnDict['var'] = value * 1054.799
        returnDict['W'] = value * 1054.799
    elif units == 'BTU/min':
        returnDict['BTU/sec'] = value * 0.0166667
        returnDict['BTU/min'] = value
        returnDict['cal/min'] = value * 251.9345085
        returnDict['cal/sec'] = value * 4.1989085
        returnDict['ft-lb/min'] = value * 777.9803124
        returnDict['ft-lb/sec'] = value * 12.9663353
        returnDict['hp'] = value * 0.0235752
        returnDict['hp-elec'] = value * 0.0235657
        returnDict['hp-met'] = value * 0.0239021
        returnDict['J/s'] = value * 17.57999
        returnDict['kcal/min'] = value * 0.2519345
        returnDict['kcal/s'] = value * 0.0041989
        returnDict['kg-m/min'] = value * 107.559583
        returnDict['kg-m/sec'] = value * 1.7926601
        returnDict['kW'] = value * 0.01758
        returnDict['MW'] = value * 1.76e-05
        returnDict['N-m/s'] = value * 17.57999
        returnDict['ton-ref'] = value * 0.0049988
        returnDict['var'] = value * 17.57999
        returnDict['W'] = value * 17.57999
    elif units == 'cal/min':
        returnDict['BTU/sec'] = value * 6.62e-05
        returnDict['BTU/min'] = value * 0.0039693
        returnDict['cal/min'] = value
        returnDict['cal/sec'] = value * 0.0166667
        returnDict['ft-lb/min'] = value * 3.088026
        returnDict['ft-lb/sec'] = value * 0.0514671
        returnDict['hp'] = value * 9.36e-05
        returnDict['hp-elec'] = value * 9.35e-05
        returnDict['hp-met'] = value * 9.49e-05
        returnDict['J/s'] = value * 0.06978
        returnDict['kcal/min'] = value * 0.001
        returnDict['kcal/s'] = value * 1.67e-05
        returnDict['kg-m/min'] = value * 0.4269347
        returnDict['kg-m/sec'] = value * 0.0071156
        returnDict['kW'] = value * 6.98e-05
        returnDict['MW'] = value * 6.98e-08
        returnDict['N-m/s'] = value * 0.06978
        returnDict['ton-ref'] = value * 1.98e-05
        returnDict['var'] = value * 0.06978
        returnDict['W'] = value * 0.06978
    elif units == 'cal/sec':
        returnDict['BTU/sec'] = value * 0.0039693
        returnDict['BTU/min'] = value * 0.2381571
        returnDict['cal/min'] = value * 60.0
        returnDict['cal/sec'] = value
        returnDict['ft-lb/min'] = value * 185.28156
        returnDict['ft-lb/sec'] = value * 3.0880252
        returnDict['hp'] = value * 0.0056146
        returnDict['hp-elec'] = value * 0.0056123
        returnDict['hp-met'] = value * 0.0056925
        returnDict['J/s'] = value * 4.1868
        returnDict['kcal/min'] = value * 0.06
        returnDict['kcal/s'] = value * 0.001
        returnDict['kg-m/min'] = value * 25.6160818
        returnDict['kg-m/sec'] = value * 0.4269348
        returnDict['kW'] = value * 0.0041868
        returnDict['MW'] = value * 4.2e-06
        returnDict['N-m/s'] = value * 4.1868
        returnDict['ton-ref'] = value * 0.0011905
        returnDict['var'] = value * 4.1868
        returnDict['W'] = value * 4.1868
    elif units == 'ft-lb/min':
        returnDict['BTU/sec'] = value * 2.14e-05
        returnDict['BTU/min'] = value * 0.0012854
        returnDict['cal/min'] = value * 0.3238315
        returnDict['cal/sec'] = value * 0.0053972
        returnDict['ft-lb/min'] = value
        returnDict['ft-lb/sec'] = value * 0.0166667
        returnDict['hp'] = value * 3.03e-05
        returnDict['hp-elec'] = value * 3.03e-05
        returnDict['hp-met'] = value * 3.07e-05
        returnDict['J/s'] = value * 0.022597
        returnDict['kcal/min'] = value * 0.0003238
        returnDict['kcal/s'] = value * 5.4e-06
        returnDict['kg-m/min'] = value * 0.1382549
        returnDict['kg-m/sec'] = value * 0.0023042
        returnDict['kW'] = value * 2.26e-05
        returnDict['MW'] = value * 2.26e-08
        returnDict['N-m/s'] = value * 0.022597
        returnDict['ton-ref'] = value * 6.4e-06
        returnDict['var'] = value * 0.022597
        returnDict['W'] = value * 0.022597
    elif units == 'ft-lb/sec':
        returnDict['BTU/sec'] = value * 0.0012854
        returnDict['BTU/min'] = value * 0.0771228
        returnDict['cal/min'] = value * 19.4298931
        returnDict['cal/sec'] = value * 0.3238316
        returnDict['ft-lb/min'] = value * 60.000015
        returnDict['ft-lb/sec'] = value
        returnDict['hp'] = value * 0.0018182
        returnDict['hp-elec'] = value * 0.0018175
        returnDict['hp-met'] = value * 0.0018434
        returnDict['J/s'] = value * 1.3558179
        returnDict['kcal/min'] = value * 0.0194299
        returnDict['kcal/s'] = value * 0.0003238
        returnDict['kg-m/min'] = value * 8.2952955
        returnDict['kg-m/sec'] = value * 0.138255
        returnDict['kW'] = value * 0.0013558
        returnDict['MW'] = value * 1.4e-06
        returnDict['N-m/s'] = value * 1.3558179
        returnDict['ton-ref'] = value * 0.0003855
        returnDict['var'] = value * 1.3558179
        returnDict['W'] = value * 1.3558179
    elif units == 'hp':
        returnDict['BTU/sec'] = value * 0.7069592
        returnDict['BTU/min'] = value * 42.4175366
        returnDict['cal/min'] = value * 10686.4412439
        returnDict['cal/sec'] = value * 178.1073541
        returnDict['ft-lb/min'] = value * 33000.0084082
        returnDict['ft-lb/sec'] = value * 550.0000022
        returnDict['hp'] = value
        returnDict['hp-elec'] = value * 0.9995977
        returnDict['hp-met'] = value * 1.0138697
        returnDict['J/s'] = value * 745.69987
        returnDict['kcal/min'] = value * 10.6864412
        returnDict['kcal/s'] = value * 0.1781074
        returnDict['kg-m/min'] = value * 4562.4125543
        returnDict['kg-m/sec'] = value * 76.0402247
        returnDict['kW'] = value * 0.7456999
        returnDict['MW'] = value * 0.0007457
        returnDict['N-m/s'] = value * 745.69987
        returnDict['ton-ref'] = value * 0.2120361
        returnDict['var'] = value * 745.69987
        returnDict['W'] = value * 745.69987
    elif units == 'hp-elec':
        returnDict['BTU/sec'] = value * 0.7072437
        returnDict['BTU/min'] = value * 42.4346089
        returnDict['cal/min'] = value * 10690.742333
        returnDict['cal/sec'] = value * 178.1790389
        returnDict['ft-lb/min'] = value * 33013.2902833
        returnDict['ft-lb/sec'] = value * 550.2213667
        returnDict['hp'] = value * 1.0004025
        returnDict['hp-elec'] = value
        returnDict['hp-met'] = value * 1.0142777
        returnDict['J/s'] = value * 746.0
        returnDict['kcal/min'] = value * 10.6907423
        returnDict['kcal/s'] = value * 0.178179
        returnDict['kg-m/min'] = value * 4564.2488384
        returnDict['kg-m/sec'] = value * 76.0708295
        returnDict['kW'] = value * 0.746
        returnDict['MW'] = value * 0.000746
        returnDict['N-m/s'] = value * 746.0
        returnDict['ton-ref'] = value * 0.2121215
        returnDict['var'] = value * 746.0
        returnDict['W'] = value * 746.0
    elif units == 'hp-met':
        returnDict['BTU/sec'] = value * 0.6972881
        returnDict['BTU/min'] = value * 41.8372678
        returnDict['cal/min'] = value * 10540.2515047
        returnDict['cal/sec'] = value * 175.6708584
        returnDict['ft-lb/min'] = value * 32548.5706927
        returnDict['ft-lb/sec'] = value * 542.4760422
        returnDict['hp'] = value * 0.9863201
        returnDict['hp-elec'] = value * 0.9859233
        returnDict['hp-met'] = value
        returnDict['J/s'] = value * 735.49875
        returnDict['kcal/min'] = value * 10.5402515
        returnDict['kcal/s'] = value * 0.1756709
        returnDict['kg-m/min'] = value * 4499.9990823
        returnDict['kg-m/sec'] = value * 75.0
        returnDict['kW'] = value * 0.7354987
        returnDict['MW'] = value * 0.0007355
        returnDict['N-m/s'] = value * 735.49875
        returnDict['ton-ref'] = value * 0.2091355
        returnDict['var'] = value * 735.49875
        returnDict['W'] = value * 735.49875
    elif units == 'J/s':
        returnDict['BTU/sec'] = value * 0.000948
        returnDict['BTU/min'] = value * 0.0568829
        returnDict['cal/min'] = value * 14.3307538
        returnDict['cal/sec'] = value * 0.2388459
        returnDict['ft-lb/min'] = value * 44.2537403
        returnDict['ft-lb/sec'] = value * 0.7375622
        returnDict['hp'] = value * 0.001341
        returnDict['hp-elec'] = value * 0.0013405
        returnDict['hp-met'] = value * 0.0013596
        returnDict['J/s'] = value
        returnDict['kcal/min'] = value * 0.0143308
        returnDict['kcal/s'] = value * 0.0002388
        returnDict['kg-m/min'] = value * 6.118296
        returnDict['kg-m/sec'] = value * 0.1019716
        returnDict['kW'] = value * 0.001
        returnDict['MW'] = value * 1e-06
        returnDict['N-m/s'] = value
        returnDict['ton-ref'] = value * 0.0002843
        returnDict['var'] = value
        returnDict['W'] = value
    elif units == 'kcal/min':
        returnDict['BTU/sec'] = value * 0.0661548
        returnDict['BTU/min'] = value * 3.9692855
        returnDict['cal/min'] = value * 1000.0
        returnDict['cal/sec'] = value * 16.6666667
        returnDict['ft-lb/min'] = value * 3088.026
        returnDict['ft-lb/sec'] = value * 51.4670871
        returnDict['hp'] = value * 0.0935765
        returnDict['hp-elec'] = value * 0.0935389
        returnDict['hp-met'] = value * 0.0948744
        returnDict['J/s'] = value * 69.78
        returnDict['kcal/min'] = value
        returnDict['kcal/s'] = value * 0.0166667
        returnDict['kg-m/min'] = value * 426.934697
        returnDict['kg-m/sec'] = value * 7.1155797
        returnDict['kW'] = value * 0.06978
        returnDict['MW'] = value * 6.98e-05
        returnDict['N-m/s'] = value * 69.78
        returnDict['ton-ref'] = value * 0.0198416
        returnDict['var'] = value * 69.78
        returnDict['W'] = value * 69.78
    elif units == 'kcal/s':
        returnDict['BTU/sec'] = value * 3.969287
        returnDict['BTU/min'] = value * 238.1571321
        returnDict['cal/min'] = value * 60000.0
        returnDict['cal/sec'] = value * 1000.0
        returnDict['ft-lb/min'] = value * 185281.5599975
        returnDict['ft-lb/sec'] = value * 3088.0252256
        returnDict['hp'] = value * 5.6145913
        returnDict['hp-elec'] = value * 5.6123324
        returnDict['hp-met'] = value * 5.6924638
        returnDict['J/s'] = value * 4186.8
        returnDict['kcal/min'] = value * 60.0
        returnDict['kcal/s'] = value
        returnDict['kg-m/min'] = value * 25616.0818187
        returnDict['kg-m/sec'] = value * 426.934784
        returnDict['kW'] = value * 4.1868
        returnDict['MW'] = value * 0.0041868
        returnDict['N-m/s'] = value * 4186.8
        returnDict['ton-ref'] = value * 1.1904962
        returnDict['var'] = value * 4186.8
        returnDict['W'] = value * 4186.8
    elif units == 'kg-m/min':
        returnDict['BTU/sec'] = value * 0.000155
        returnDict['BTU/min'] = value * 0.0092972
        returnDict['cal/min'] = value * 2.3422786
        returnDict['cal/sec'] = value * 0.039038
        returnDict['ft-lb/min'] = value * 7.2330172
        returnDict['ft-lb/sec'] = value * 0.1205503
        returnDict['hp'] = value * 0.0002192
        returnDict['hp-elec'] = value * 0.0002191
        returnDict['hp-met'] = value * 0.0002222
        returnDict['J/s'] = value * 0.1634442
        returnDict['kcal/min'] = value * 0.0023423
        returnDict['kcal/s'] = value * 3.9e-05
        returnDict['kg-m/min'] = value
        returnDict['kg-m/sec'] = value * 0.0166667
        returnDict['kW'] = value * 0.0001634
        returnDict['MW'] = value * 1.634e-07
        returnDict['N-m/s'] = value * 0.1634442
        returnDict['ton-ref'] = value * 4.65e-05
        returnDict['var'] = value * 0.1634442
        returnDict['W'] = value * 0.1634442
    elif units == 'kg-m/sec':
        returnDict['BTU/sec'] = value * 0.0092972
        returnDict['BTU/min'] = value * 0.5578302
        returnDict['cal/min'] = value * 140.5366867
        returnDict['cal/sec'] = value * 2.3422781
        returnDict['ft-lb/min'] = value * 433.9809426
        returnDict['ft-lb/sec'] = value * 7.2330139
        returnDict['hp'] = value * 0.0131509
        returnDict['hp-elec'] = value * 0.0131456
        returnDict['hp-met'] = value * 0.0133333
        returnDict['J/s'] = value * 9.80665
        returnDict['kcal/min'] = value * 0.1405367
        returnDict['kcal/s'] = value * 0.0023423
        returnDict['kg-m/min'] = value * 59.9999878
        returnDict['kg-m/sec'] = value
        returnDict['kW'] = value * 0.0098067
        returnDict['MW'] = value * 9.8e-06
        returnDict['N-m/s'] = value * 9.80665
        returnDict['ton-ref'] = value * 0.0027885
        returnDict['var'] = value * 9.80665
        returnDict['W'] = value * 9.80665
    elif units == 'kW':
        returnDict['BTU/sec'] = value * 0.9480479
        returnDict['BTU/min'] = value * 56.8828537
        returnDict['cal/min'] = value * 14330.7537976
        returnDict['cal/sec'] = value * 238.8458966
        returnDict['ft-lb/min'] = value * 44253.7403261
        returnDict['ft-lb/sec'] = value * 737.5621538
        returnDict['hp'] = value * 1.3410221
        returnDict['hp-elec'] = value * 1.3404826
        returnDict['hp-met'] = value * 1.3596216
        returnDict['J/s'] = value * 1000.0
        returnDict['kcal/min'] = value * 14.3307538
        returnDict['kcal/s'] = value * 0.2388459
        returnDict['kg-m/min'] = value * 6118.2960301
        returnDict['kg-m/sec'] = value * 101.9716213
        returnDict['kW'] = value
        returnDict['MW'] = value * 0.001
        returnDict['N-m/s'] = value * 1000.0
        returnDict['ton-ref'] = value * 0.2843451
        returnDict['var'] = value * 1000.0
        returnDict['W'] = value * 1000.0
    elif units == 'MW':
        returnDict['BTU/sec'] = value * 948.0479219
        returnDict['BTU/min'] = value * 56882.8537445
        returnDict['cal/min'] = value * 14330753.7976498
        returnDict['cal/sec'] = value * 238845.8966275
        returnDict['ft-lb/min'] = value * 44253740.3261324
        returnDict['ft-lb/sec'] = value * 737562.1538095
        returnDict['hp'] = value * 1341.0220924
        returnDict['hp-elec'] = value * 1340.4825737
        returnDict['hp-met'] = value * 1359.6216173
        returnDict['J/s'] = value * 1000000.0
        returnDict['kcal/min'] = value * 14330.7537976
        returnDict['kcal/s'] = value * 238.8458966
        returnDict['kg-m/min'] = value * 6118296.0300824
        returnDict['kg-m/sec'] = value * 101971.6212978
        returnDict['kW'] = value * 1000.0
        returnDict['MW'] = value
        returnDict['N-m/s'] = value * 1000000.0
        returnDict['ton-ref'] = value * 284.3451363
        returnDict['var'] = value * 1000000.0
        returnDict['W'] = value * 1000000.0
    elif units == 'N-m/s':
        returnDict['BTU/sec'] = value * 0.000948
        returnDict['BTU/min'] = value * 0.0568829
        returnDict['cal/min'] = value * 14.3307538
        returnDict['cal/sec'] = value * 0.2388459
        returnDict['ft-lb/min'] = value * 44.2537403
        returnDict['ft-lb/sec'] = value * 0.7375622
        returnDict['hp'] = value * 0.001341
        returnDict['hp-elec'] = value * 0.0013405
        returnDict['hp-met'] = value * 0.0013596
        returnDict['J/s'] = value
        returnDict['kcal/min'] = value * 0.0143308
        returnDict['kcal/s'] = value * 0.0002388
        returnDict['kg-m/min'] = value * 6.118296
        returnDict['kg-m/sec'] = value * 0.1019716
        returnDict['kW'] = value * 0.001
        returnDict['MW'] = value * 1e-06
        returnDict['N-m/s'] = value
        returnDict['ton-ref'] = value * 0.0002843
        returnDict['var'] = value
        returnDict['W'] = value
    elif units == 'ton-ref':
        returnDict['BTU/sec'] = value * 3.334145
        returnDict['BTU/min'] = value * 200.0486257
        returnDict['cal/min'] = value * 50399.1521926
        returnDict['cal/sec'] = value * 839.9858699
        returnDict['ft-lb/min'] = value * 155633.8923466
        returnDict['ft-lb/sec'] = value * 2593.8975553
        returnDict['hp'] = value * 4.7161774
        returnDict['hp-elec'] = value * 4.7142799
        returnDict['hp-met'] = value * 4.7815891
        returnDict['J/s'] = value * 3516.85284
        returnDict['kcal/min'] = value * 50.3991522
        returnDict['kcal/s'] = value * 0.8399859
        returnDict['kg-m/min'] = value * 21517.1467694
        returnDict['kg-m/sec'] = value * 358.619186
        returnDict['kW'] = value * 3.5168528
        returnDict['MW'] = value * 0.0035169
        returnDict['N-m/s'] = value * 3516.85284
        returnDict['ton-ref'] = value
        returnDict['var'] = value * 3516.85284
        returnDict['W'] = value * 3516.85284
    elif units == 'var':
        returnDict['BTU/sec'] = value * 0.000948
        returnDict['BTU/min'] = value * 0.0568829
        returnDict['cal/min'] = value * 14.3307538
        returnDict['cal/sec'] = value * 0.2388459
        returnDict['ft-lb/min'] = value * 44.2537403
        returnDict['ft-lb/sec'] = value * 0.7375622
        returnDict['hp'] = value * 0.001341
        returnDict['hp-elec'] = value * 0.0013405
        returnDict['hp-met'] = value * 0.0013596
        returnDict['J/s'] = value
        returnDict['kcal/min'] = value * 0.0143308
        returnDict['kcal/s'] = value * 0.0002388
        returnDict['kg-m/min'] = value * 6.118296
        returnDict['kg-m/sec'] = value * 0.1019716
        returnDict['kW'] = value * 0.001
        returnDict['MW'] = value * 1e-06
        returnDict['N-m/s'] = value
        returnDict['ton-ref'] = value * 0.0002843
        returnDict['var'] = value
        returnDict['W'] = value
    elif units == 'W':
        returnDict['BTU/sec'] = value * 0.000948
        returnDict['BTU/min'] = value * 0.0568829
        returnDict['cal/min'] = value * 14.3307538
        returnDict['cal/sec'] = value * 0.2388459
        returnDict['ft-lb/min'] = value * 44.2537403
        returnDict['ft-lb/sec'] = value * 0.7375622
        returnDict['hp'] = value * 0.001341
        returnDict['hp-elec'] = value * 0.0013405
        returnDict['hp-met'] = value * 0.0013596
        returnDict['J/s'] = value
        returnDict['kcal/min'] = value * 0.0143308
        returnDict['kcal/s'] = value * 0.0002388
        returnDict['kg-m/min'] = value * 6.118296
        returnDict['kg-m/sec'] = value * 0.1019716
        returnDict['kW'] = value * 0.001
        returnDict['MW'] = value * 1e-06
        returnDict['N-m/s'] = value
        returnDict['ton-ref'] = value * 0.0002843
        returnDict['var'] = value
        returnDict['W'] = value
    else:
        raise Exception("""Invalid Input. Make sure values are passed as
        integers, units are passed as stings and that the
        correct units are input. Consult the
        documnetation for more information on each function.""")
    return returnDict


def velocity(value, units):
    returnDict = {}
    if units == 'ft/d':
        returnDict['ft/d'] = value
        returnDict['ft/hr'] = value * 0.0416667
        returnDict['ft/min'] = value * 0.0006944
        returnDict['ft/s'] = value * 1.16e-05
        returnDict['kph'] = value * 1.27e-05
        returnDict['k/min'] = value * 2.116e-07
        returnDict['k/sec'] = value * 3.528e-09
        returnDict['knot'] = value * 6.9e-06
        returnDict['mach'] = value * 1.0366974e-08
        returnDict['m/d'] = value * 0.3048
        returnDict['m/hr'] = value * 0.0127
        returnDict['m/min'] = value * 0.0002117
        returnDict['m/sec'] = value * 3.5e-06
        returnDict['mph'] = value * 7.9e-06
        returnDict['mi/min'] = value * 1.317e-07
        returnDict['mi/sec'] = value * 2.194e-09
    elif units == 'ft/hr':
        returnDict['ft/d'] = value * 24.0
        returnDict['ft/hr'] = value
        returnDict['ft/min'] = value * 0.0166667
        returnDict['ft/s'] = value * 0.0002778
        returnDict['kph'] = value * 0.0003048
        returnDict['k/min'] = value * 5.1e-06
        returnDict['k/sec'] = value * 8.5e-08
        returnDict['knot'] = value * 0.0001646
        returnDict['mach'] = value * 2.4833e-07
        returnDict['m/d'] = value * 7.3152
        returnDict['m/hr'] = value * 0.3048
        returnDict['m/min'] = value * 0.00508
        returnDict['m/sec'] = value * 8.47e-05
        returnDict['mph'] = value * 0.0001894
        returnDict['mi/min'] = value * 3.2e-06
        returnDict['mi/sec'] = value * 5.33e-08
    elif units == 'ft/min':
        returnDict['ft/d'] = value * 1440.0
        returnDict['ft/hr'] = value * 60.0
        returnDict['ft/min'] = value
        returnDict['ft/s'] = value * 0.0166667
        returnDict['kph'] = value * 0.0166667
        returnDict['k/min'] = value * 0.0003048
        returnDict['k/sec'] = value * 5.1e-06
        returnDict['knot'] = value * 0.0098747
        returnDict['mach'] = value * 1.49e-05
        returnDict['m/d'] = value * 438.912
        returnDict['m/hr'] = value * 438.912
        returnDict['m/min'] = value * 0.3048
        returnDict['m/sec'] = value * 0.00508
        returnDict['mph'] = value * 0.0113636
        returnDict['mi/min'] = value * 0.0001894
        returnDict['mi/sec'] = value * 3.2e-06
    elif units == 'ft/s':
        returnDict['ft/d'] = value * 86400.0
        returnDict['ft/hr'] = value * 3600.0
        returnDict['ft/min'] = value * 60.0
        returnDict['ft/s'] = value
        returnDict['kph'] = value * 1.09728
        returnDict['k/min'] = value * 0.018288
        returnDict['k/sec'] = value * 0.0003048
        returnDict['knot'] = value * 0.5924838
        returnDict['mach'] = value * 0.0008957
        returnDict['m/d'] = value * 26334.72
        returnDict['m/hr'] = value * 1097.28
        returnDict['m/min'] = value * 18.288
        returnDict['m/sec'] = value * 0.3048
        returnDict['mph'] = value * 0.6818182
        returnDict['mi/min'] = value * 0.0113636
        returnDict['mi/sec'] = value * 0.0001894
    elif units == 'kph':
        returnDict['ft/d'] = value * 78740.1574803
        returnDict['ft/hr'] = value * 3280.839895
        returnDict['ft/min'] = value * 54.6806649
        returnDict['ft/s'] = value * 0.9113444
        returnDict['kph'] = value
        returnDict['k/min'] = value * 0.0166667
        returnDict['k/sec'] = value * 0.0002778
        returnDict['knot'] = value * 0.5399568
        returnDict['mach'] = value * 0.0008163
        returnDict['m/d'] = value * 24000.0
        returnDict['m/hr'] = value * 1000.0
        returnDict['m/min'] = value * 16.6666667
        returnDict['m/sec'] = value * 0.2777778
        returnDict['mph'] = value * 0.6213712
        returnDict['mi/min'] = value * 0.0103562
        returnDict['mi/sec'] = value * 0.0001726
    elif units == 'k/min':
        returnDict['ft/d'] = value * 4724409.4488189
        returnDict['ft/hr'] = value * 196850.3937008
        returnDict['ft/min'] = value * 3280.839895
        returnDict['ft/s'] = value * 54.6806649
        returnDict['kph'] = value * 60.0
        returnDict['k/min'] = value
        returnDict['k/sec'] = value * 0.0166667
        returnDict['knot'] = value * 32.3974082
        returnDict['mach'] = value * 0.0489778
        returnDict['m/d'] = value * 1440000.0
        returnDict['m/hr'] = value * 60000.0
        returnDict['m/min'] = value * 1000.0
        returnDict['m/sec'] = value * 16.6666667
        returnDict['mph'] = value * 37.2822715
        returnDict['mi/min'] = value * 0.6213712
        returnDict['mi/sec'] = value * 0.0103562
    elif units == 'k/sec':
        returnDict['ft/d'] = value * 283464566.929133
        returnDict['ft/hr'] = value * 11811023.6220472
        returnDict['ft/min'] = value * 196850.3937008
        returnDict['ft/s'] = value * 3280.839895
        returnDict['kph'] = value * 3600.0
        returnDict['k/min'] = value * 60.0
        returnDict['k/sec'] = value
        returnDict['knot'] = value * 1943.8444924
        returnDict['mach'] = value * 2.93867
        returnDict['m/d'] = value * 86400000.0
        returnDict['m/hr'] = value * 3600000.0
        returnDict['m/min'] = value * 60000.0
        returnDict['m/sec'] = value * 1000.0
        returnDict['mph'] = value * 2236.9362921
        returnDict['mi/min'] = value * 37.2822715
        returnDict['mi/sec'] = value * 0.6213712
    elif units == 'knot':
        returnDict['ft/d'] = value * 145826.7716535
        returnDict['ft/hr'] = value * 6076.1154856
        returnDict['ft/min'] = value * 101.2685914
        returnDict['ft/s'] = value * 1.6878099
        returnDict['kph'] = value * 1.852
        returnDict['k/min'] = value * 0.0308667
        returnDict['k/sec'] = value * 0.0005144
        returnDict['knot'] = value
        returnDict['mach'] = value * 0.0015118
        returnDict['m/d'] = value * 44448.0
        returnDict['m/hr'] = value * 1852.0
        returnDict['m/min'] = value * 30.8666667
        returnDict['m/sec'] = value * 0.5144444
        returnDict['mph'] = value * 1.1507794
        returnDict['mi/min'] = value * 0.0191797
        returnDict['mi/sec'] = value * 0.0003197
    elif units == 'mach':
        returnDict['ft/d'] = value * 96460157.480315
        returnDict['ft/hr'] = value * 4019173.2283465
        returnDict['ft/min'] = value * 66986.2204724
        returnDict['ft/s'] = value * 1116.4370079
        returnDict['kph'] = value * 1225.044
        returnDict['k/min'] = value * 20.4174
        returnDict['k/sec'] = value * 0.34029
        returnDict['knot'] = value * 661.4708423
        returnDict['mach'] = value
        returnDict['m/d'] = value * 29401056.0
        returnDict['m/hr'] = value * 1225044.0
        returnDict['m/min'] = value * 20417.4
        returnDict['m/sec'] = value * 340.29
        returnDict['mph'] = value * 761.2070508
        returnDict['mi/min'] = value * 12.6867842
        returnDict['mi/sec'] = value * 0.2114464
    elif units == 'm/d':
        returnDict['ft/d'] = value * 3.2808399
        returnDict['ft/hr'] = value * 0.1367017
        returnDict['ft/min'] = value * 0.0022784
        returnDict['ft/s'] = value * 3.8e-05
        returnDict['kph'] = value * 4.17e-05
        returnDict['k/min'] = value * 6.95e-07
        returnDict['k/sec'] = value * 1.158e-08
        returnDict['knot'] = value * 2.25e-05
        returnDict['mach'] = value * 3.40124e-08
        returnDict['m/d'] = value
        returnDict['m/hr'] = value * 0.0416667
        returnDict['m/min'] = value * 0.0006944
        returnDict['m/sec'] = value * 1.16e-05
        returnDict['mph'] = value * 2.59e-05
        returnDict['mi/min'] = value * 4.317e-07
        returnDict['mi/sec'] = value * 7.194e-09
    elif units == 'm/hr':
        returnDict['ft/d'] = value * 78.7401575
        returnDict['ft/hr'] = value * 3.2808399
        returnDict['ft/min'] = value * 0.0546807
        returnDict['ft/s'] = value * 0.0009113
        returnDict['kph'] = value * 0.001
        returnDict['k/min'] = value * 1.67e-05
        returnDict['k/sec'] = value * 2.7833e-07
        returnDict['knot'] = value * 0.00054
        returnDict['mach'] = value * 8.162976e-07
        returnDict['m/d'] = value * 24.0
        returnDict['m/hr'] = value
        returnDict['m/min'] = value * 0.0166667
        returnDict['m/sec'] = value * 0.0002778
        returnDict['mph'] = value * 0.0006214
        returnDict['mi/min'] = value * 1.04e-05
        returnDict['mi/sec'] = value * 1.733e-07
    elif units == 'm/min':
        returnDict['ft/d'] = value * 4724.4094488
        returnDict['ft/hr'] = value * 196.8503937
        returnDict['ft/min'] = value * 3.2808399
        returnDict['ft/s'] = value * 0.0546807
        returnDict['kph'] = value * 0.06
        returnDict['k/min'] = value * 0.001
        returnDict['k/sec'] = value * 1.67e-05
        returnDict['knot'] = value * 0.0323974
        returnDict['mach'] = value * 4.9e-05
        returnDict['m/d'] = value * 1440.0
        returnDict['m/hr'] = value * 60.0
        returnDict['m/min'] = value
        returnDict['m/sec'] = value * 0.0166667
        returnDict['mph'] = value * 0.0372823
        returnDict['mi/min'] = value * 0.0006214
        returnDict['mi/sec'] = value * 1.04e-05
    elif units == 'm/sec':
        returnDict['ft/d'] = value * 283464.5669291
        returnDict['ft/hr'] = value * 11811.023622
        returnDict['ft/min'] = value * 196.8503937
        returnDict['ft/s'] = value * 3.2808399
        returnDict['kph'] = value * 3.6
        returnDict['k/min'] = value * 0.06
        returnDict['k/sec'] = value * 0.001
        returnDict['knot'] = value * 1.9438445
        returnDict['mach'] = value * 0.0029387
        returnDict['m/d'] = value * 86400.0
        returnDict['m/hr'] = value * 3600.0
        returnDict['m/min'] = value * 60.0
        returnDict['m/sec'] = value
        returnDict['mph'] = value * 2.2369363
        returnDict['mi/min'] = value * 0.0372823
        returnDict['mi/sec'] = value * 0.0006214
    elif units == 'mph':
        returnDict['ft/d'] = value * 126720.0
        returnDict['ft/hr'] = value * 5280.0
        returnDict['ft/min'] = value * 88.0
        returnDict['ft/s'] = value * 1.4666667
        returnDict['kph'] = value * 1.609344
        returnDict['k/min'] = value * 0.0268224
        returnDict['k/sec'] = value * 0.000447
        returnDict['knot'] = value * 0.8689762
        returnDict['mach'] = value * 0.0013137
        returnDict['m/d'] = value * 38624.256
        returnDict['m/hr'] = value * 1609.344
        returnDict['m/min'] = value * 26.8224
        returnDict['m/sec'] = value * 0.44704
        returnDict['mph'] = value
        returnDict['mi/min'] = value * 0.0166667
        returnDict['mi/sec'] = value * 0.0002778
    elif units == 'mi/min':
        returnDict['ft/d'] = value * 7603200.0
        returnDict['ft/hr'] = value * 316800.0
        returnDict['ft/min'] = value * 5280.0
        returnDict['ft/s'] = value * 88.0
        returnDict['kph'] = value * 96.56064
        returnDict['k/min'] = value * 1.609344
        returnDict['k/sec'] = value * 0.0268224
        returnDict['knot'] = value * 52.1385745
        returnDict['mach'] = value * 0.0788222
        returnDict['m/d'] = value * 2317455.36
        returnDict['m/hr'] = value * 96560.64
        returnDict['m/min'] = value * 1609.344
        returnDict['m/sec'] = value * 26.8224
        returnDict['mph'] = value * 60.0
        returnDict['mi/min'] = value
        returnDict['mi/sec'] = value * 0.0166667
    elif units == 'mi/sec':
        returnDict['ft/d'] = value * 456191999.999999
        returnDict['ft/hr'] = value * 19008000.0
        returnDict['ft/min'] = value * 316800.0
        returnDict['ft/s'] = value * 5280.0
        returnDict['kph'] = value * 5793.6384
        returnDict['k/min'] = value * 96.56064
        returnDict['k/sec'] = value * 1.609344
        returnDict['knot'] = value * 3128.3144708
        returnDict['mach'] = value * 4.7293309
        returnDict['m/d'] = value * 139047321.6
        returnDict['m/hr'] = value * 5793638.4
        returnDict['m/min'] = value * 96560.64
        returnDict['m/sec'] = value * 1609.344
        returnDict['mph'] = value * 3600.0
        returnDict['mi/min'] = value * 60.0
        returnDict['mi/sec'] = value
    else:
        raise Exception("""Invalid Input. Make sure values are passed as
        integers, units are passed as stings and that the
        correct units are input. Consult the
        documnetation for more information on each function.""")
    return returnDict


def conductivity(value, units):
    returnDict = {}
    if units == 'S/m':
        returnDict['S/m'] = value * 1.0
        returnDict['pS/m'] = value * 1000000000000.0
        returnDict['mho/m'] = value * 1.0
        returnDict['mho/cm'] = value * 0.01
        returnDict['abmho/m'] = value * 1e-09
        returnDict['abmho/cm'] = value * 1e-11
        returnDict['stmho/m'] = value * 898752432400.0
        returnDict['stmho/cm'] = value * 8987524324.0
        returnDict['S/cm'] = value * 0.01
        returnDict['mS/m'] = value * 1000.0
        returnDict['mS/cm'] = value * 10.0
        returnDict['uS/m'] = value * 1000000.0
        returnDict['uS/cm'] = value * 10000.0
    elif units == 'pS/m':
        returnDict['S/m'] = value * 1e-12
        returnDict['pS/m'] = value * 1.0
        returnDict['mho/m'] = value * 1e-12
        returnDict['mho/cm'] = value * 1e-14
        returnDict['abmho/m'] = value * 1e-21
        returnDict['abmho/cm'] = value * 1e-23
        returnDict['stmho/m'] = value * 0.8987524324
        returnDict['stmho/cm'] = value * 0.008987524324
        returnDict['S/cm'] = value * 1e-14
        returnDict['mS/m'] = value * 1e-09
        returnDict['mS/cm'] = value * 1e-11
        returnDict['uS/m'] = value * 1e-06
        returnDict['uS/cm'] = value * 1e-08
    elif units == 'mho/m':
        returnDict['S/m'] = value * 1.0
        returnDict['pS/m'] = value * 1000000000000.0
        returnDict['mho/m'] = value * 1.0
        returnDict['mho/cm'] = value * 0.01
        returnDict['abmho/m'] = value * 1e-09
        returnDict['abmho/cm'] = value * 1e-11
        returnDict['stmho/m'] = value * 898752432400.0
        returnDict['stmho/cm'] = value * 8987524324.0
        returnDict['S/cm'] = value * 0.01
        returnDict['mS/m'] = value * 1000.0
        returnDict['mS/cm'] = value * 10.0
        returnDict['uS/m'] = value * 1000000.0
        returnDict['uS/cm'] = value * 10000.0
    elif units == 'mho/cm':
        returnDict['S/m'] = value * 100.0
        returnDict['pS/m'] = value * 100000000000000.0
        returnDict['mho/m'] = value * 100.0
        returnDict['mho/cm'] = value * 1.0
        returnDict['abmho/m'] = value * 1e-07
        returnDict['abmho/cm'] = value * 1e-09
        returnDict['stmho/m'] = value * 89875243240000.0
        returnDict['stmho/cm'] = value * 898752432400.0
        returnDict['S/cm'] = value * 1.0
        returnDict['mS/m'] = value * 100000.0
        returnDict['mS/cm'] = value * 1000.0
        returnDict['uS/m'] = value * 100000000.0
        returnDict['uS/cm'] = value * 1000000.0
    elif units == 'abmho/m':
        returnDict['S/m'] = value * 999999999.9999999
        returnDict['pS/m'] = value * 1.0000000000000001e+21
        returnDict['mho/m'] = value * 999999999.9999999
        returnDict['mho/cm'] = value * 10000000.0
        returnDict['abmho/m'] = value * 1.0
        returnDict['abmho/cm'] = value * 0.01
        returnDict['stmho/m'] = value * 8.987524324e+20
        returnDict['stmho/cm'] = value * 8.987524324e+18
        returnDict['S/cm'] = value * 10000000.0
        returnDict['mS/m'] = value * 1000000000000.0
        returnDict['mS/cm'] = value * 10000000000.0
        returnDict['uS/m'] = value * 1000000000000000.0
        returnDict['uS/cm'] = value * 10000000000000.0
    elif units == 'abmho/cm':
        returnDict['S/m'] = value * 100000000000.0
        returnDict['pS/m'] = value * 1.0000000000000001e+23
        returnDict['mho/m'] = value * 100000000000.0
        returnDict['mho/cm'] = value * 999999999.9999999
        returnDict['abmho/m'] = value * 100.0
        returnDict['abmho/cm'] = value * 1.0
        returnDict['stmho/m'] = value * 8.987524324e+22
        returnDict['stmho/cm'] = value * 8.987524324e+20
        returnDict['S/cm'] = value * 1000000000.0
        returnDict['mS/m'] = value * 100000000000000.0
        returnDict['mS/cm'] = value * 1000000000000.0
        returnDict['uS/m'] = value * 1e+17
        returnDict['uS/cm'] = value * 1000000000000000.0
    elif units == 'stmho/m':
        returnDict['S/m'] = value * 1.112653456001929e-12
        returnDict['pS/m'] = value * 1.112653456001929
        returnDict['mho/m'] = value * 1.112653456001929e-12
        returnDict['mho/cm'] = value * 1.1126534560019289e-14
        returnDict['abmho/m'] = value * 1.112653456001929e-21
        returnDict['abmho/cm'] = value * 1.1126534560019288e-23
        returnDict['stmho/m'] = value * 1.0
        returnDict['stmho/cm'] = value * 0.01
        returnDict['S/cm'] = value * 1.112653456002e-14
        returnDict['mS/m'] = value * 1.112653456002e-09
        returnDict['mS/cm'] = value * 1.112653456002e-11
        returnDict['uS/m'] = value * 1.112653456002e-06
        returnDict['uS/cm'] = value * 1.112653456002e-08
    elif units == 'stmho/cm':
        returnDict['S/m'] = value * 1.112653456001929e-10
        returnDict['pS/m'] = value * 111.26534560019289
        returnDict['mho/m'] = value * 1.112653456001929e-10
        returnDict['mho/cm'] = value * 1.112653456001929e-12
        returnDict['abmho/m'] = value * 1.112653456001929e-19
        returnDict['abmho/cm'] = value * 1.112653456001929e-21
        returnDict['stmho/m'] = value * 100.0
        returnDict['stmho/cm'] = value * 1.0
        returnDict['S/cm'] = value * 1.112653456002e-12
        returnDict['mS/m'] = value * 1.112653456002e-07
        returnDict['mS/cm'] = value * 1.112653456002e-09
        returnDict['uS/m'] = value * 0.0001112653456002
        returnDict['uS/cm'] = value * 1.112653456002e-06
    elif units == 'S/cm':
        returnDict['S/m'] = value * 100.0
        returnDict['pS/m'] = value * 100000000000000.0
        returnDict['mho/m'] = value * 100.0
        returnDict['mho/cm'] = value * 1.0
        returnDict['abmho/m'] = value * 1e-07
        returnDict['abmho/cm'] = value * 1e-09
        returnDict['stmho/m'] = value * 89875243239994.25
        returnDict['stmho/cm'] = value * 898752432399.9426
        returnDict['S/cm'] = value * 1.0
        returnDict['mS/m'] = value * 100000.0
        returnDict['mS/cm'] = value * 1000.0
        returnDict['uS/m'] = value * 100000000.0
        returnDict['uS/cm'] = value * 1000000.0
    elif units == 'mS/m':
        returnDict['S/m'] = value * 0.001
        returnDict['pS/m'] = value * 999999999.9999999
        returnDict['mho/m'] = value * 0.001
        returnDict['mho/cm'] = value * 1e-05
        returnDict['abmho/m'] = value * 1e-12
        returnDict['abmho/cm'] = value * 1e-14
        returnDict['stmho/m'] = value * 898752432.3999426
        returnDict['stmho/cm'] = value * 8987524.323999427
        returnDict['S/cm'] = value * 1e-05
        returnDict['mS/m'] = value * 1.0
        returnDict['mS/cm'] = value * 0.01
        returnDict['uS/m'] = value * 1000.0
        returnDict['uS/cm'] = value * 10.0
    elif units == 'mS/cm':
        returnDict['S/m'] = value * 0.1
        returnDict['pS/m'] = value * 100000000000.0
        returnDict['mho/m'] = value * 0.1
        returnDict['mho/cm'] = value * 0.001
        returnDict['abmho/m'] = value * 1e-10
        returnDict['abmho/cm'] = value * 1e-12
        returnDict['stmho/m'] = value * 89875243239.99426
        returnDict['stmho/cm'] = value * 898752432.3999426
        returnDict['S/cm'] = value * 0.001
        returnDict['mS/m'] = value * 100.0
        returnDict['mS/cm'] = value * 1.0
        returnDict['uS/m'] = value * 100000.0
        returnDict['uS/cm'] = value * 1000.0
    elif units == 'uS/m':
        returnDict['S/m'] = value * 1e-06
        returnDict['pS/m'] = value * 1000000.0
        returnDict['mho/m'] = value * 1e-06
        returnDict['mho/cm'] = value * 1e-08
        returnDict['abmho/m'] = value * 1e-15
        returnDict['abmho/cm'] = value * 1e-17
        returnDict['stmho/m'] = value * 898752.4323999427
        returnDict['stmho/cm'] = value * 8987.524323999425
        returnDict['S/cm'] = value * 1e-08
        returnDict['mS/m'] = value * 0.001
        returnDict['mS/cm'] = value * 1e-05
        returnDict['uS/m'] = value * 1.0
        returnDict['uS/cm'] = value * 0.01
    elif units == 'uS/cm':
        returnDict['S/m'] = value * 0.0001
        returnDict['pS/m'] = value * 100000000.0
        returnDict['mho/m'] = value * 0.0001
        returnDict['mho/cm'] = value * 1e-06
        returnDict['abmho/m'] = value * 1e-13
        returnDict['abmho/cm'] = value * 1e-15
        returnDict['stmho/m'] = value * 89875243.23999426
        returnDict['stmho/cm'] = value * 898752.4323999427
        returnDict['S/cm'] = value * 1e-06
        returnDict['mS/m'] = value * 0.1
        returnDict['mS/cm'] = value * 0.001
        returnDict['uS/m'] = value * 100.0
        returnDict['uS/cm'] = value * 1.0
    else:
        raise Exception("""Invalid Input. Make sure values are passed as
        integers, units are passed as stings and that the
        correct units are input. Consult the
        documnetation for more information on each function.""")
    return returnDict


def resistivity(value, units):
    returnDict = {}
    if units == 'ohm.m':
        returnDict['ohm.m'] = value * 1.0
        returnDict['ohm.cm'] = value * 100.0
        returnDict['ohm.in'] = value * 39.37007874
        returnDict['m-ohm.cm'] = value * 100000000.0
        returnDict['m-ohm.in'] = value * 39370078.74
        returnDict['ab-ohm.cm'] = value * 100000000000.0
        returnDict['stat-ohm.cm'] = value * 1.112653456e-10
        returnDict['circular_mil-ohm/ft'] = value * 601530493.4
        returnDict['ohm.mm2/m'] = value * 1000000.0
    elif units == 'ohm.cm':
        returnDict['ohm.m'] = value * 0.01
        returnDict['ohm.cm'] = value * 1.0
        returnDict['ohm.in'] = value * 0.3937007874
        returnDict['m-ohm.cm'] = value * 1000000.0
        returnDict['m-ohm.in'] = value * 393700.7874
        returnDict['ab-ohm.cm'] = value * 1000000000.0
        returnDict['stat-ohm.cm'] = value * 1.112653456e-12
        returnDict['circular_mil-ohm/ft'] = value * 6015304.934
        returnDict['ohm.mm2/m'] = value * 10000.0
    elif units == 'ohm.in':
        returnDict['ohm.m'] = value * 0.0254000000001016
        returnDict['ohm.cm'] = value * 2.5400000000101604
        returnDict['ohm.in'] = value * 1.0
        returnDict['m-ohm.cm'] = value * 2540000.00001
        returnDict['m-ohm.in'] = value * 999999.9999999
        returnDict['ab-ohm.cm'] = value * 2540000000.01
        returnDict['stat-ohm.cm'] = value * 2.826139778251e-12
        returnDict['circular_mil-ohm/ft'] = value * 15278874.53242
        returnDict['ohm.mm2/m'] = value * 25400.0000001
    elif units == 'm-ohm.cm':
        returnDict['ohm.m'] = value * 1e-08
        returnDict['ohm.cm'] = value * 1e-06
        returnDict['ohm.in'] = value * 3.937007874000248e-07
        returnDict['m-ohm.cm'] = value * 1.0
        returnDict['m-ohm.in'] = value * 0.3937007874
        returnDict['ab-ohm.cm'] = value * 1000.0
        returnDict['stat-ohm.cm'] = value * 1.112653456e-18
        returnDict['circular_mil-ohm/ft'] = value * 6.015304934
        returnDict['ohm.mm2/m'] = value * 0.01
    elif units == 'm-ohm.in':
        returnDict['ohm.m'] = value * 2.54000000001016e-08
        returnDict['ohm.cm'] = value * 2.54000000001016e-06
        returnDict['ohm.in'] = value * 1.0000000000001e-06
        returnDict['m-ohm.cm'] = value * 2.5400000000101604
        returnDict['m-ohm.in'] = value * 1.0
        returnDict['ab-ohm.cm'] = value * 2540.00000001
        returnDict['stat-ohm.cm'] = value * 2.826139778251e-18
        returnDict['circular_mil-ohm/ft'] = value * 15.27887453242
        returnDict['ohm.mm2/m'] = value * 0.0254000000001
    elif units == 'ab-ohm.cm':
        returnDict['ohm.m'] = value * 1e-11
        returnDict['ohm.cm'] = value * 1e-09
        returnDict['ohm.in'] = value * 3.9370078740002477e-10
        returnDict['m-ohm.cm'] = value * 0.001
        returnDict['m-ohm.in'] = value * 0.0003937007874000248
        returnDict['ab-ohm.cm'] = value * 1.0
        returnDict['stat-ohm.cm'] = value * 1.112653456e-21
        returnDict['circular_mil-ohm/ft'] = value * 0.006015304934
        returnDict['ohm.mm2/m'] = value * 1e-05
    elif units == 'stat-ohm.cm':
        returnDict['ohm.m'] = value * 8987524324.015581
        returnDict['ohm.cm'] = value * 898752432401.558
        returnDict['ohm.in'] = value * 353839540314.19684
        returnDict['m-ohm.cm'] = value * 8.987524324015581e+17
        returnDict['m-ohm.in'] = value * 3.538395403141968e+17
        returnDict['ab-ohm.cm'] = value * 8.987524324015581e+20
        returnDict['stat-ohm.cm'] = value * 1.0
        returnDict['circular_mil-ohm/ft'] = value * 5.40626994107e+18
        returnDict['ohm.mm2/m'] = value * 8987524324016000.0
    elif units == 'circular_mil-ohm/ft':
        returnDict['ohm.m'] = value * 1.662426113010084e-09
        returnDict['ohm.cm'] = value * 1.6624261130100838e-07
        returnDict['ohm.in'] = value * 6.544984696864392e-08
        returnDict['m-ohm.cm'] = value * 0.1662426113010084
        returnDict['m-ohm.in'] = value * 0.06544984696864392
        returnDict['ab-ohm.cm'] = value * 166.24261130100842
        returnDict['stat-ohm.cm'] = value * 1.8497041599851776e-19
        returnDict['circular_mil-ohm/ft'] = value * 1.0
        returnDict['ohm.mm2/m'] = value * 0.00166242611301
    elif units == 'ohm.mm2/m':
        returnDict['ohm.m'] = value * 1e-06
        returnDict['ohm.cm'] = value * 0.0001
        returnDict['ohm.in'] = value * 3.937007874000248e-05
        returnDict['m-ohm.cm'] = value * 100.0
        returnDict['m-ohm.in'] = value * 39.370078740002484
        returnDict['ab-ohm.cm'] = value * 99999.99999999999
        returnDict['stat-ohm.cm'] = value * 1.1126534559999482e-16
        returnDict['circular_mil-ohm/ft'] = value * 601.5304934000304
        returnDict['ohm.mm2/m'] = value * 1.0
    else:
        raise Exception("""Invalid Input. Make sure values are passed as
        integers, units are passed as stings and that the
        correct units are input. Consult the
        documnetation for more information on each function.""")
    return returnDict
