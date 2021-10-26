def dogleg(value, units):
    return_dict = {}
    if units == 'deg/100ft':
        return_dict['deg/100ft'] = value
        return_dict['deg/30m'] = value * 0.9843004
    elif units == 'deg/30m':
        return_dict['deg/100ft'] = value * 1.01595
        return_dict['deg/30m'] = value
    return return_dict


def axial_spring_con(value, units):
    return_dict = {}
    if units == 'N/m':
        return_dict['N/m'] = value
        return_dict['lb/in'] = value * 1.016
    elif units == 'lb/in':
        return_dict['N/m'] = value * 0.984252
        return_dict['lb/in'] = value
    return return_dict


def axial_dampening_coef(value, units):
    return_dict = {}
    if units == 'N-s/m':
        return_dict['N-s/m'] = value
        return_dict['lb-s/in'] = value * 1.016
    elif units == 'lb-s/in':
        return_dict['N-s/m'] = value * 0.984252
        return_dict['lb-s/in'] = value
    return return_dict


def torsional_spring_con(value, units):
    return_dict = {}
    if units == 'N-m/rad':
        return_dict['N-m/rad'] = value
        return_dict['lb-in/rad'] = value * 1.01595
    elif units == 'lb-in/rad':
        return_dict['N-m/rad'] = value * 0.9843004
        return_dict['lb-in/rad'] = value
    return return_dict


def torsional_dampening_coef(value, units):
    return_dict = {}
    if units == 'N-m-s/rad':
        return_dict['N-m-s/rad'] = value
        return_dict['lb-in-s/rad'] = value * 1.01595
    elif units == 'lb-in-s/rad':
        return_dict['N-m-s/rad'] = value * 0.9843004
        return_dict['lb-in-s/rad'] = value
    return return_dict


def pressure_grad(value, units):
    return_dict = {}
    if units == 'psi/ft':
        return_dict['psi/ft'] = value
        return_dict['kPa/m'] = value * 22.5
        return_dict['Mpa/m'] = value * 0.0225
        return_dict['Pa/m'] = value * 22500
    elif units == 'kPa/m':
        return_dict['psi/ft'] = value * 0.0444444
        return_dict['kPa/m'] = value
        return_dict['Mpa/m'] = value * 0.001
        return_dict['Pa/m'] = value * 1000
    elif units == 'Mpa/m':
        return_dict['psi/ft'] = value * 44.4444444
        return_dict['kPa/m'] = value * 1000
        return_dict['Mpa/m'] = value
        return_dict['Pa/m'] = value * 1000000
    elif units == 'Pa/m':
        return_dict['psi/ft'] = value * 0.0000444
        return_dict['kPa/m'] = value * 0.001
        return_dict['Mpa/m'] = value * 0.000001
        return_dict['Pa/m'] = value
    return return_dict


def yield_slurry(value, units):
    return_dict = {}
    if units == 'ft3/sk':
        return_dict['ft3/sk'] = value
        return_dict['m3/sk'] = value * 0.028317
        return_dict['gal/sk'] = value * 7
    elif units == 'm3/sk':
        return_dict['ft3/sk'] = value * 35
        return_dict['m3/sk'] = value
        return_dict['gal/sk'] = value * 264
    elif units == 'gal/sk':
        return_dict['ft3/sk'] = value * 0.13369
        return_dict['m3/sk'] = value * 0.0037857
        return_dict['gal/sk'] = value
    return return_dict


def footage_cost(value, units):
    return_dict = {}
    if units == 'cur/ft':
        return_dict['cur/ft'] = value
        return_dict['cur/m'] = value * 3.2810014
        return_dict['cur/1000ft'] = value / 0.001
        return_dict['cur/1000m'] = value / 0.003281
    elif units == 'cur/m':
        return_dict['cur/ft'] = value * 0.304785
        return_dict['cur/m'] = value
        return_dict['cur/1000ft'] = value / 0.0003048
        return_dict['cur/1000m'] = value / 0.001
    elif units == 'cur/1000ft':
        return_dict['cur/ft'] = value / 1000
        return_dict['cur/m'] = value / 3281.00
        return_dict['cur/1000ft'] = value
        return_dict['cur/1000m'] = value * 3.2810003
    elif units == 'cur/1000m':
        return_dict['cur/ft'] = value / 305
        return_dict['cur/m'] = value / 1000
        return_dict['cur/1000ft'] = value / 0.3047851
        return_dict['cur/1000m'] = value
    return return_dict


def mud_weight(value, units):
    return_dict = {}
    if units == 'g/cm3':
        return_dict['g/cm3'] = value * 1.0
        return_dict['g/L'] = value * 1000.0
        return_dict['kg/m3'] = value * 1000.0
        return_dict['kg/L'] = value * 1.0
        return_dict['kPa/m'] = value * 9.8114244
        return_dict['lb/ft3'] = value * 62.4336642
        return_dict['lb/bbl'] = value * 350.5070669
        return_dict['ppg'] = value * 8.3454064
        return_dict['psi/ft'] = value * 0.4339843
        return_dict['psi/100ft'] = value * 43.3726579
        return_dict['SG'] = value * 1.0
    elif units == 'g/L':
        return_dict['g/cm3'] = value * 0.001
        return_dict['g/L'] = value * 1.0
        return_dict['kg/m3'] = value * 1.0
        return_dict['kg/L'] = value * 0.001
        return_dict['kPa/m'] = value * 0.0098114
        return_dict['lb/ft3'] = value * 0.0624337
        return_dict['lb/bbl'] = value * 0.3505071
        return_dict['ppg'] = value * 0.0083454
        return_dict['psi/ft'] = value * 0.000434
        return_dict['psi/100ft'] = value * 0.0433727
        return_dict['SG'] = value * 0.001
    elif units == 'kg/m3':
        return_dict['g/cm3'] = value * 0.001
        return_dict['g/L'] = value * 1.0
        return_dict['kg/m3'] = value * 1.0
        return_dict['kg/L'] = value * 0.001
        return_dict['kPa/m'] = value * 0.0098114
        return_dict['lb/ft3'] = value * 0.0624337
        return_dict['lb/bbl'] = value * 0.3505071
        return_dict['ppg'] = value * 0.0083454
        return_dict['psi/ft'] = value * 0.000434
        return_dict['psi/100ft'] = value * 0.0433727
        return_dict['SG'] = value * 0.001
    elif units == 'kg/L':
        return_dict['g/cm3'] = value * 1.0
        return_dict['g/L'] = value * 1000.0
        return_dict['kg/m3'] = value * 1000.0
        return_dict['kg/L'] = value * 1.0
        return_dict['kPa/m'] = value * 9.8114244
        return_dict['lb/ft3'] = value * 62.4336642
        return_dict['lb/bbl'] = value * 350.5070669
        return_dict['ppg'] = value * 8.3454064
        return_dict['psi/ft'] = value * 0.4339843
        return_dict['psi/100ft'] = value * 43.3726579
        return_dict['SG'] = value * 1.0
    elif units == 'kPa/m':
        return_dict['g/cm3'] = value * 0.101922
        return_dict['g/L'] = value * 101.922
        return_dict['kg/m3'] = value * 101.922
        return_dict['kg/L'] = value * 0.101922
        return_dict['kPa/m'] = value * 1.0
        return_dict['lb/ft3'] = value * 6.3633639
        return_dict['lb/bbl'] = value * 35.7243813
        return_dict['ppg'] = value * 0.8505805
        return_dict['psi/ft'] = value * 0.0442325
        return_dict['psi/100ft'] = value * 4.420628
        return_dict['SG'] = value * 0.101922
    elif units == 'lb/ft3':
        return_dict['g/cm3'] = value * 0.016017
        return_dict['g/L'] = value * 16.017
        return_dict['kg/m3'] = value * 16.017
        return_dict['kg/L'] = value * 0.016017
        return_dict['kPa/m'] = value * 0.1571496
        return_dict['lb/ft3'] = value * 1.0
        return_dict['lb/bbl'] = value * 5.6140717
        return_dict['ppg'] = value * 0.1336684
        return_dict['psi/ft'] = value * 0.0069511
        return_dict['psi/100ft'] = value * 0.6946999
        return_dict['SG'] = value * 0.016017
    elif units == 'lb/bbl':
        return_dict['g/cm3'] = value * 0.002853
        return_dict['g/L'] = value * 2.8530095
        return_dict['kg/m3'] = value * 2.8530095
        return_dict['kg/L'] = value * 0.002853
        return_dict['kPa/m'] = value * 0.0279921
        return_dict['lb/ft3'] = value * 0.1781238
        return_dict['lb/bbl'] = value * 1.0
        return_dict['ppg'] = value * 0.0238095
        return_dict['psi/ft'] = value * 0.0012382
        return_dict['psi/100ft'] = value * 0.1237426
        return_dict['SG'] = value * 0.002853
    elif units == 'ppg':
        return_dict['g/cm3'] = value * 0.1198264
        return_dict['g/L'] = value * 119.8264
        return_dict['kg/m3'] = value * 119.8264
        return_dict['kg/L'] = value * 0.1198264
        return_dict['kPa/m'] = value * 1.1756677
        return_dict['lb/ft3'] = value * 7.4812012
        return_dict['lb/bbl'] = value * 42.0
        return_dict['ppg'] = value * 1.0
        return_dict['psi/ft'] = value * 0.0520028
        return_dict['psi/100ft'] = value * 5.1971895
        return_dict['SG'] = value * 0.1198264
    elif units == 'psi/ft':
        return_dict['g/cm3'] = value * 2.304231
        return_dict['g/L'] = value * 2304.231
        return_dict['kg/m3'] = value * 2304.231
        return_dict['kg/L'] = value * 2.304231
        return_dict['kPa/m'] = value * 22.6077883
        return_dict['lb/ft3'] = value * 143.8615846
        return_dict['lb/bbl'] = value * 807.6492492
        return_dict['ppg'] = value * 19.229744
        return_dict['psi/ft'] = value * 1.0
        return_dict['psi/100ft'] = value * 99.9406228
        return_dict['SG'] = value * 2.304231
    elif units == 'psi/100ft':
        return_dict['g/cm3'] = value * 0.023056
        return_dict['g/L'] = value * 23.056
        return_dict['kg/m3'] = value * 23.056
        return_dict['kg/L'] = value * 0.023056
        return_dict['kPa/m'] = value * 0.2262122
        return_dict['lb/ft3'] = value * 1.4394706
        return_dict['lb/bbl'] = value * 8.0812909
        return_dict['ppg'] = value * 0.1924117
        return_dict['psi/ft'] = value * 0.0100059
        return_dict['psi/100ft'] = value * 1.0
        return_dict['SG'] = value * 0.023056
    elif units == 'SG':
        return_dict['g/cm3'] = value * 1.0
        return_dict['g/L'] = value * 1000.0
        return_dict['kg/m3'] = value * 1000.0
        return_dict['kg/L'] = value * 1.0
        return_dict['kPa/m'] = value * 9.8114244
        return_dict['lb/ft3'] = value * 62.4336642
        return_dict['lb/bbl'] = value * 350.5070669
        return_dict['ppg'] = value * 8.3454064
        return_dict['psi/ft'] = value * 0.4339843
        return_dict['psi/100ft'] = value * 43.3726579
        return_dict['SG'] = value * 1.0
    return return_dict


def flow_rate(value, units):
    return_dict = {}
    if units == 'bbl/hr':
        return_dict['bbl/hr'] = value * 1.0
        return_dict['bbl/min'] = value * 0.0166667
        return_dict['ft3/min'] = value * 0.0935764
        return_dict['m3/hr'] = value * 0.1589873
        return_dict['m3/min'] = value * 0.0026498
        return_dict['gal/hr'] = value * 42.0
        return_dict['gpm'] = value * 0.7
        return_dict['L/hr'] = value * 158.9872949
        return_dict['L/min'] = value * 2.6497882
    elif units == 'bbl/min':
        return_dict['bbl/hr'] = value * 60.0
        return_dict['bbl/min'] = value * 1.0
        return_dict['ft3/min'] = value * 5.6145833
        return_dict['m3/hr'] = value * 9.5392377
        return_dict['m3/min'] = value * 0.1589873
        return_dict['gal/hr'] = value * 2520.0
        return_dict['gpm'] = value * 42.0
        return_dict['L/hr'] = value * 9539.2376957
        return_dict['L/min'] = value * 158.9872949
    elif units == 'ft3/min':
        return_dict['bbl/hr'] = value * 10.6864564
        return_dict['bbl/min'] = value * 0.1781076
        return_dict['ft3/min'] = value * 1.0
        return_dict['m3/hr'] = value * 1.6990108
        return_dict['m3/min'] = value * 0.0283168
        return_dict['gal/hr'] = value * 448.8311688
        return_dict['gpm'] = value * 7.4805195
        return_dict['L/hr'] = value * 1699.0107955
        return_dict['L/min'] = value * 28.3168466
    elif units == 'm3/hr':
        return_dict['bbl/hr'] = value * 6.2898108
        return_dict['bbl/min'] = value * 0.1048302
        return_dict['ft3/min'] = value * 0.5885778
        return_dict['m3/hr'] = value * 1.0
        return_dict['m3/min'] = value * 0.0166667
        return_dict['gal/hr'] = value * 264.1720524
        return_dict['gpm'] = value * 4.4028675
        return_dict['L/hr'] = value * 1000.0
        return_dict['L/min'] = value * 16.6666667
    elif units == 'm3/min':
        return_dict['bbl/hr'] = value * 377.3886462
        return_dict['bbl/min'] = value * 6.2898108
        return_dict['ft3/min'] = value * 35.3146667
        return_dict['m3/hr'] = value * 60.0
        return_dict['m3/min'] = value * 1.0
        return_dict['gal/hr'] = value * 15850.3231414
        return_dict['gpm'] = value * 264.1720524
        return_dict['L/hr'] = value * 60000.0
        return_dict['L/min'] = value * 1000.0
    elif units == 'gal/hr':
        return_dict['bbl/hr'] = value * 0.0238095
        return_dict['bbl/min'] = value * 0.0003968
        return_dict['ft3/min'] = value * 0.002228
        return_dict['m3/hr'] = value * 0.0037854
        return_dict['m3/min'] = value * 6.31e-05
        return_dict['gal/hr'] = value * 1.0
        return_dict['gpm'] = value * 0.0166667
        return_dict['L/hr'] = value * 3.7854118
        return_dict['L/min'] = value * 0.0630902
    elif units == 'gpm':
        return_dict['bbl/hr'] = value * 1.4285714
        return_dict['bbl/min'] = value * 0.0238095
        return_dict['ft3/min'] = value * 0.1336806
        return_dict['m3/hr'] = value * 0.2271247
        return_dict['m3/min'] = value * 0.0037854
        return_dict['gal/hr'] = value * 60.0
        return_dict['gpm'] = value * 1.0
        return_dict['L/hr'] = value * 227.124707
        return_dict['L/min'] = value * 3.7854118
    elif units == 'L/hr':
        return_dict['bbl/hr'] = value * 0.0062898
        return_dict['bbl/min'] = value * 0.0001048
        return_dict['ft3/min'] = value * 0.0005886
        return_dict['m3/hr'] = value * 0.001
        return_dict['m3/min'] = value * 1.67e-05
        return_dict['gal/hr'] = value * 0.2641721
        return_dict['gpm'] = value * 0.0044029
        return_dict['L/hr'] = value * 1.0
        return_dict['L/min'] = value * 0.0166667
    elif units == 'L/min':
        return_dict['bbl/hr'] = value * 0.3773886
        return_dict['bbl/min'] = value * 0.0062898
        return_dict['ft3/min'] = value * 0.0353147
        return_dict['m3/hr'] = value * 0.06
        return_dict['m3/min'] = value * 0.001
        return_dict['gal/hr'] = value * 15.8503231
        return_dict['gpm'] = value * 0.2641721
        return_dict['L/hr'] = value * 60.0
        return_dict['L/min'] = value * 1.0
    return return_dict


def drilling_rate(value, units):
    return_dict = {}
    if units == 'ft/d':
        return_dict['ft/d'] = value * 1.0
        return_dict['ft/hr'] = value * 0.0416667
        return_dict['ft/min'] = value * 0.0006944
        return_dict['ft/s'] = value * 1.16e-05
        return_dict['m/d'] = value * 0.3048
        return_dict['m/hr'] = value * 0.0127
        return_dict['m/min'] = value * 0.0002117
        return_dict['m/s'] = value * 3.5e-06
    elif units == 'ft/hr':
        return_dict['ft/d'] = value * 24.0
        return_dict['ft/hr'] = value * 1.0
        return_dict['ft/min'] = value * 0.0166667
        return_dict['ft/s'] = value * 0.0002778
        return_dict['m/d'] = value * 7.3152
        return_dict['m/hr'] = value * 0.3048
        return_dict['m/min'] = value * 0.00508
        return_dict['m/s'] = value * 8.47e-05
    elif units == 'ft/min':
        return_dict['ft/d'] = value * 1440.0
        return_dict['ft/hr'] = value * 60.0
        return_dict['ft/min'] = value * 1.0
        return_dict['ft/s'] = value * 0.0166667
        return_dict['m/d'] = value * 438.9119993
        return_dict['m/hr'] = value * 18.288
        return_dict['m/min'] = value * 0.3048
        return_dict['m/s'] = value * 0.00508
    elif units == 'ft/s':
        return_dict['ft/d'] = value * 86400.0
        return_dict['ft/hr'] = value * 3600.0
        return_dict['ft/min'] = value * 60.0
        return_dict['ft/s'] = value * 1.0
        return_dict['m/d'] = value * 26334.71996
        return_dict['m/hr'] = value * 1097.2799983
        return_dict['m/min'] = value * 18.288
        return_dict['m/s'] = value * 0.3048
    elif units == 'm/d':
        return_dict['ft/d'] = value * 3.2808399
        return_dict['ft/hr'] = value * 0.1367017
        return_dict['ft/min'] = value * 0.0022784
        return_dict['ft/s'] = value * 3.8e-05
        return_dict['m/d'] = value * 1.0
        return_dict['m/hr'] = value * 0.0416667
        return_dict['m/min'] = value * 0.0006944
        return_dict['m/s'] = value * 1.16e-05
    elif units == 'm/hr':
        return_dict['ft/d'] = value * 78.7401576
        return_dict['ft/hr'] = value * 3.2808399
        return_dict['ft/min'] = value * 0.0546807
        return_dict['ft/s'] = value * 0.0009113
        return_dict['m/d'] = value * 24.0
        return_dict['m/hr'] = value * 1.0
        return_dict['m/min'] = value * 0.0166667
        return_dict['m/s'] = value * 0.0002778
    elif units == 'm/min':
        return_dict['ft/d'] = value * 4724.409456
        return_dict['ft/hr'] = value * 196.850394
        return_dict['ft/min'] = value * 3.2808399
        return_dict['ft/s'] = value * 0.0546807
        return_dict['m/d'] = value * 1440.0
        return_dict['m/hr'] = value * 60.0
        return_dict['m/min'] = value * 1.0
        return_dict['m/s'] = value * 0.0166667
    elif units == 'm/s':
        return_dict['ft/d'] = value * 283464.56736
        return_dict['ft/hr'] = value * 11811.02364
        return_dict['ft/min'] = value * 196.850394
        return_dict['ft/s'] = value * 3.2808399
        return_dict['m/d'] = value * 86400.0
        return_dict['m/hr'] = value * 3600.0
        return_dict['m/min'] = value * 60.0
        return_dict['m/s'] = value * 1.0
    return return_dict


def weight_length(value, units):
    return_dict = {}
    if units == 'lb/ft':
        return_dict['lb/ft'] = value
        return_dict['kg/m'] = value * 1.48816
    elif units == 'kg/m':
        return_dict['lb/ft'] = value * 0.671969
        return_dict['kg/m'] = value
    return return_dict


def geothermal_gradient(value, units):
    return_dict = {}
    if units == 'c/100m':
        return_dict['c/100m'] = value
        return_dict['f/100ft'] = value * 0.549
    elif units == 'f/100ft':
        return_dict['c/100m'] = value / 0.549
        return_dict['f/100ft'] = value
    return return_dict
