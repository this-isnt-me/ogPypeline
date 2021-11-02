import production as pro
import drilling as dri
import force_and_power as fap
import general as gen
import math


def pressure_gradient(value, units):
    mud_weight = dri.mud_weight(value, units)
    press_grad = mud_weight['ppg'] * 0.052
    return dri.pressure_grad(press_grad, 'psi/ft')


def pressure_to_mud_weight(pressure_value, pressure_units,
                           depth_value, depth_units):
    pressure = gen.pressure(pressure_value, pressure_units)
    depth = gen.length(depth_value, depth_units)
    mud_weight = pressure['psi'] / 0.052 / depth['ft']
    return dri.mud_weight(mud_weight, 'ppg')


def hydrostatic_pressure(mud_value, mud_units, depth_value, depth_units):
    mud_weight = dri.mud_weight(mud_value, mud_units)
    depth = gen.length(depth_value, depth_units)
    pressure = mud_weight['ppg'] * 0.052 * depth['ft']
    return gen.pressure(pressure, 'psi')


def triplex_output(diameter_value, diameter_units,
                   length_value, length_units, efficiency=1):
    diameter = gen.length(diameter_value, diameter_units)
    length = gen.length(length_value, length_units)
    pump_output = (diameter['mm']**2) * length['mm'] * 2.3576e-9 * efficiency
    return pro.stroke_volume(pump_output, 'm3/stk')


def duplex_output(diameter_value, diameter_units, length_value, length_units,
                  rod_value, rod_units, efficiency=1):
    diameter = gen.length(diameter_value, diameter_units)
    length = gen.length(length_value, length_units)
    rod = gen.length(rod_value, rod_units)
    pump_output = ((2 * (diameter['mm']**2)) - (rod['mm']**2)) * \
        length['mm'] * 1.57172e-9 * efficiency
    return pro.stroke_volume(pump_output, 'm3/stk')


def hydraulic_horsepower(pressure_value, pressure_units,
                         circulating_value, circulating_units):
    pressure = gen.pressure(pressure_value, pressure_units)
    circ_rate = dri.flow_rate(circulating_value, circulating_units)
    return {'hhp': (pressure['psi'] * circ_rate['gpm']) / 1714}


def drill_collar_in_air(od_value, id_value, diameter_units, dc_type='reg'):
    const = 2.66
    outer_dia = gen.length(od_value, diameter_units)
    inner_dia = gen.length(id_value, diameter_units)
    if dc_type == 'spiral':
        const = 2.56
    dc_weight = const * ((outer_dia['in']**2) - (inner_dia['in']**2))
    return dri.weight_length(dc_weight, 'lb/ft')


def hole_tubular_capacity(diameter_value, diameter_units, washout_value=0):
    diameter = gen.length(diameter_value, diameter_units)
    volume_alpha = ((diameter['in'] * (1 + washout_value))**2) / 1029.4
    volume_beta = 1029.4/((diameter['in'] * (1 + washout_value))**2)
    volume_alpha = pro.pipe_capacity(volume_alpha, 'bbl/ft')
    volume_beta = pro.pipe_cap_length_vol(volume_beta, 'ft/bbl')
    return {**volume_alpha, **volume_beta}


def tubular_displacement(od_value, id_value, diameter_units):
    od_dia = gen.length(od_value, diameter_units)
    id_dia = gen.length(id_value, diameter_units)
    volume_alpha = ((od_dia['in']**2) - (id_dia['in']**2)) / 1029.4
    volume_beta = 1029.4 / ((od_dia['in']**2) - (id_dia['in']**2))
    volume_alpha = pro.pipe_capacity(volume_alpha, 'bbl/ft')
    volume_beta = pro.pipe_cap_length_vol(volume_beta, 'ft/bbl')
    return {**volume_alpha, **volume_beta}


def annular_capacity(od_value, id_value, diameter_units):
    od_dia = gen.length(od_value, diameter_units)
    id_dia = gen.length(id_value, diameter_units)
    volume_alpha = ((od_dia['in']**2) - (id_dia['in']**2)) / 1029.4
    volume_beta = 1029.4 / ((od_dia['in']**2) - (id_dia['in']**2))
    volume_alpha = pro.pipe_capacity(volume_alpha, 'bbl/ft')
    volume_beta = pro.pipe_cap_length_vol(volume_beta, 'ft/bbl')
    return {**volume_alpha, **volume_beta}


def annular_capacity_multiple_tubulars(od_value, id_array, diameter_units):
    od_dia = gen.length(od_value, diameter_units)
    id_total = 0
    for i in range(len(id_array)):
        id_dia = id_array[i]
        id_dia = gen.length(id_dia, diameter_units)
        id_total = id_total + id_dia['in']**2
    volume_alpha = (od_dia['in']**2 - id_total) / 1029.4
    volume_beta = 1029.4 / (od_dia['in']**2 - id_total)
    volume_alpha = pro.pipe_capacity(volume_alpha, 'bbl/ft')
    volume_beta = pro.pipe_cap_length_vol(volume_beta, 'ft/bbl')
    return {**volume_alpha, **volume_beta}


def cuttings_drilled(diameter_value, diameter_units, washout_value, porosity):
    diameter = gen.length(diameter_value, diameter_units)
    cutting_vol = ((diameter['in'] * (1 + washout_value))**2 / 1029.4) *\
        (1 - porosity)
    return pro.pipe_capacity(cutting_vol, 'bbl/ft')


def annular_velocity_annular_capcity(output_value, output_units,
                                     annulus_value, annulus_units):
    pump_output = dri.flow_rate(output_value, output_units)
    annular_capacity = pro.pipe_capacity(annulus_value, annulus_units)
    annular_velocity = pump_output['bbl/min'] / annular_capacity['bbl/ft']
    return fap.velocity(annular_velocity, 'ft/min')


def annular_velocity_flow_rate(hole_id_value, pipe_od_value, dia_units,
                               flow_value, flow_units):
    hole_id = gen.length(hole_id_value, dia_units)
    pipe_od = gen.length(pipe_od_value, dia_units)
    flow_rate = dri.flow_rate(flow_value, flow_units)
    annular_velocity = (24.5 * flow_rate['gpm']) /\
        ((hole_id['in'])**2 - (pipe_od['in'])**2)
    return fap.velocity(annular_velocity, 'ft/min')


def pump_output_flow_rate(od_value, id_value, diameter_units,
                          velocity_value, velocity_units):
    od_dia = gen.length(od_value, diameter_units)
    id_dia = gen.length(id_value, diameter_units)
    annular_velocity = fap.velocity(velocity_value, velocity_units)
    pump_output = (annular_velocity['ft/min'] *
                   (od_dia['in']**2 - id_dia['in']**2)) / 24.5
    return dri.flow_rate(pump_output, 'gpm')


def pump_output_spm(velocity_value, velocity_units, stroke_value, stroke_units,
                    annulus_value, annulus_units):
    annular_velocity = fap.velocity(velocity_value, velocity_units)
    stroke_output = pro.stroke_volume(stroke_value, stroke_units)
    annular_capacity = pro.pipe_capacity(annulus_value, annulus_units)
    return (annular_velocity['ft/min'] * annular_capacity['bbl/ft']) /\
        stroke_output['bbl/stk']


def stroke_pressure_factor(old_spm, new_spm, pressure_old_value,
                           pressure_new_value, pressure_units):
    old_pressure = gen.pressure(pressure_old_value, pressure_units)
    new_pressure = gen.pressure(pressure_new_value, pressure_units)
    return math.log((new_pressure['psi'] / old_pressure['psi'])) /\
        math.log((new_spm / old_spm))


def stroke_pressure_relationship(old_spm, new_spm, pressure_value,
                                 pressure_units, factor=2):
    pressure = gen.pressure(pressure_value, pressure_units)
    new_pressure = pressure['psi'] * ((new_spm / old_spm)**factor)
    return gen.pressure(new_pressure, 'psi')


def buoyancy_factor(value, units):
    mud_weight = dri.mud_weight(value, units)
    return (65.5 - mud_weight['ppg']) / 65.5


def formation_temp(depth_value, depth_units, gradient_value, gradient_units,
                   temp_value, temp_units):
    depth = gen.length(depth_value, depth_units)
    gradient = dri.geothermal_gradient(gradient_value, gradient_units)
    temp = gen.temperature(temp_value, temp_units)
    formation_temp = temp['f'] + (gradient['f/100ft'] * (depth['ft']/100))
    return gen.temperature(formation_temp, 'f')


def accumulator_capacity_surface(volume_value, volume_units, pre_charge_value,
                                 operating_value, minimum_value,
                                 pressure_units):
    bottle_volume = gen.volume(volume_value, volume_units)
    pre_charge = gen.pressure(pre_charge_value, pressure_units)
    operating = gen.pressure(operating_value, pressure_units)
    minimum = gen.pressure(minimum_value, pressure_units)
    to_minimum = (pre_charge['psi'] * bottle_volume['gal_us']) / minimum['psi']
    to_operating = (pre_charge['psi'] * bottle_volume['gal_us']) /\
        operating['psi']
    usable_volume = (bottle_volume['gal_us'] - to_operating) -\
        (bottle_volume['gal_us'] - to_minimum)
    return gen.volume(usable_volume, 'gal_us')


def accumulator_capacity_subsea(volume_value, volume_units, pre_charge_value,
                                operating_value, minimum_value, pressure_units,
                                pres_grad_value, pres_grad_units,
                                depth_value, depth_units):
    pres_grad = dri.pressureGrad(pres_grad_value, pres_grad_units)
    depth = gen.length(depth_value, depth_units)
    bottle_volume = gen.volume(volume_value, volume_units)
    pre_charge = gen.pressure(pre_charge_value, pressure_units)
    operating = gen.pressure(operating_value, pressure_units)
    minimum = gen.pressure(minimum_value, pressure_units)
    hydrostatic_press = pres_grad['psi/ft'] * depth['ft']
    to_minimum = ((pre_charge['psi'] + hydrostatic_press) *
                  bottle_volume['gal_us']) /\
        (minimum['psi'] + hydrostatic_press)
    to_operating = ((pre_charge['psi'] + hydrostatic_press) *
                    bottle_volume['gal_us']) /\
        (operating['psi'] + hydrostatic_press)
    usable_volume = (bottle_volume['gal_us'] - to_operating) -\
        (bottle_volume['gal_us'] - to_minimum)
    return gen.volume(usable_volume, 'gal_us')


def washout_depth_plug(pipe_value, pipe_units,
                       pump_value, pump_units, strokes):
    pipe_capacity = pro.pipe_capacity(pipe_value, pipe_units)
    pump_output = pro.stroke_volume(pump_value, pump_units)
    washout_value = (strokes * pump_output['bbl/stk']) /\
        pipe_capacity['bbl/ft']
    return gen.length(washout_value, 'ft')


def washout_depth_pass(pipe_value, pipe_units, pump_value, pump_units, strokes,
                       annular_value, annular_units):
    pipe_capacity = pro.pipe_capacity(pipe_value, pipe_units)
    annular_capacity = pro.pipe_capacity(annular_value, annular_units)
    pump_output = pro.stroke_volume(pump_value, pump_units)
    washout_value = (strokes * pump_output['bbl/stk']) /\
        (pipe_capacity['bbl/ft'] + annular_capacity['bbl/ft'])
    return gen.length(washout_value, 'ft')


def ecd(pres_value, pres_units, mud_value, mud_units,
        depth_value, depth_units):
    press_loss = gen.pressure(pres_value, pres_units)
    mud_weight = dri.mud_weight(mud_value, mud_units)
    depth = gen.length(depth_value, depth_units)
    ecd = (press_loss['psi'] / 0.052 / depth['ft']) + mud_weight['ppg']
    return dri.mud_weight(ecd, 'ppg')


def fit_test(fit_value, mud_value, mud_units, depth_value, depth_units):
    req_fit = dri.mud_weight(fit_value, mud_units)
    mud_weight = dri.mud_weight(mud_value, mud_units)
    depth = gen.length(depth_value, depth_units)
    req_pressure = (req_fit['ppg'] - mud_weight['ppg']) * 0.052 * depth['ft']
    return gen.pressure(req_pressure, 'psi')


def lot_test(pres_value, pres_units, mud_value, mud_units,
             depth_value, depth_units):
    lot_pres = gen.pressure(pres_value, pres_units)
    mud_weight = dri.mud_weight(mud_value, mud_units)
    depth = gen.length(depth_value, depth_units)
    lot_mud_weight = (lot_pres['psi'] / 0.052 / depth['ft']) +\
        mud_weight['ppg']
    return dri.mud_weight(lot_mud_weight, 'ppg')


def bit_revolutions_mud_motor(bit_rotation_value, bit_rotation_units,
                              flow_value, flow_units, rev_value, rev_units):
    bit_rpm = fap.angular_velocity(bit_rotation_value, bit_rotation_units)
    circ_rate = dri.flow_rate(flow_value, flow_units)
    rotor_rpm = gen.volume(rev_value, rev_units)
    bit_rpm = (rotor_rpm['gal_us'] * circ_rate['gpm']) + bit_rpm['rpm']
    return fap.angular_velocity(bit_rpm, 'rpm')
