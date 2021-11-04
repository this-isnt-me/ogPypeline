import production as pro
import drilling as dri
import force_and_power as fap
import fluid as flu
import general as gen
import math


def max_drilling_rate(mud_in_value, mud_out_value, mud_units,
                      circ_value, circ_units, diameter_value, diameter_units):
    mud_weight_in = dri.mud_weight(mud_in_value, mud_units)
    mud_weight_out = dri.mud_weight(mud_out_value, mud_units)
    circ_rate = dri.flow_rate(circ_value, circ_units)
    hole_dia = gen.length(diameter_value, diameter_units)
    max_rate = (67 * (mud_weight_out['ppg'] - mud_weight_in['ppg']) *
                circ_rate['gpm']) / (hole_dia['in']**2)
    return dri.drilling_rate(max_rate, 'ft/hr')


def mud_on_drilling_rate(pv_1_value, pv_2_value, pv_units,
                         rop_value, rop_units):
    pv1 = flu.viscosity(pv_1_value, pv_units)
    pv2 = flu.viscosity(pv_2_value, pv_units)
    rop = dri.drilling_rate(rop_value, rop_units)
    factor = 0.003 * (pv1['cp'] - pv2['cp'])
    rop2 = rop['ft/hr'] * (10**factor)
    return dri.drilling_rate(rop2, 'ft/hr')


def cuttings_concentration(annular_velocity_value, slip_velocity_value,
                           velocity_units):
    annular_velocity = fap.velocity(annular_velocity_value, velocity_units)
    slip_velocity = fap.velocity(slip_velocity_value, velocity_units)
    return ((annular_velocity['ft/min'] - slip_velocity['ft/min']) /
            annular_velocity['ft/min']) * 100


def d_exponent(rop_value, rop_units, rotary_value, rotary_units,
               wob_value, wob_units, bit_value, bit_units):
    rop = dri.drilling_rate(rop_value, rop_units)
    rpm = fap.angular_velocity(rotary_value, rotary_units)
    wob = gen.weight(wob_value, wob_units)
    bit = gen.length(bit_value, bit_units)
    return math.log(rop['ft/hr'] / rpm['rph']) /\
        math.log((12 * (wob['lb']) / 1000) / (bit['in'] * 1000))


def d_exponent_corrected(d_comp, mud_value, mud_units):
    mud_weight = dri.mud_weight(mud_value, mud_units)
    return d_comp * (9.0 / mud_weight['ppg'])


def drilling_cost(fixed_cost, hourly_cost, rotating_hrs, tripping_hrs,
                  drilled_value, drilled_units):
    drilled = gen.length(drilled_value, drilled_units)
    footage_cost = (fixed_cost + ((rotating_hrs + tripping_hrs) *
                                  hourly_cost)) / drilled['ft']
    return dri.footage_cost(footage_cost, 'cur/ft')


def round_trip_ton_miles(mud_value, mud_units, dp_value, hwdp_value,
                         collar_value, dp_units, depth_value, depth_units,
                         stand_len_value, bha_len_value, hwdp_len_value,
                         collar_len_value, stand_units, block_value,
                         block_units, bha_weight_value, bha_weight_units):
    mud_weight = dri.mud_weight(mud_value, mud_units)
    drillpipe = dri.weight_length(dp_value, dp_units)
    hwdrillpipe = dri.weight_length(hwdp_value, dp_units)
    collar = dri.weight_length(collar_value, dp_units)
    block = gen.weight(block_value, block_units)
    depth = gen.length(depth_value, depth_units)
    stand = gen.length(stand_len_value, stand_units)
    hwdp_len = gen.length(hwdp_len_value, stand_units)
    collar_len = gen.length(collar_len_value, stand_units)
    bha_len = gen.length(bha_len_value, stand_units)
    bha_weight = gen.weight(bha_weight_value, bha_weight_units)
    buoyancy_factor = (65.5 - mud_weight['ppg']) / 65.5
    drillpipe = drillpipe['lb/ft'] * buoyancy_factor
    total_bha_weight = (((collar_len['ft'] * collar['lb/ft']) +
                         (hwdp_len['ft'] * hwdrillpipe['lb/ft']) +
                         bha_weight['lb']) * buoyancy_factor) -\
        ((collar_len['ft'] + hwdp_len['ft'] + bha_len['ft']) * drillpipe)
    return (drillpipe * depth['ft'] * (stand['ft'] + depth['ft']) +
            (2 * depth['ft']) * (2 * block['lb'] +
                                 total_bha_weight)) / 10560000


def drilling_connection_ton_miles(ton_mile_1_value, ton_mile_2_value):
    return 3 * (ton_mile_2_value - ton_mile_1_value)


def coring_ton_miles(ton_mile_1_value, ton_mile_2_value):
    return 2 * (ton_mile_2_value - ton_mile_1_value)


def setting_casing_ton_miles(mud_value, mud_units, casing_value, casing_units,
                             depth_value, depth_units, stand_value,
                             stand_units, block_value, block_units):
    mud_weight = dri.mud_weight(mud_value, mud_units)
    casing = dri.weight_length(casing_value, casing_units)
    depth = gen.length(depth_value, depth_units)
    stand = gen.length(stand_value, stand_units)
    block = gen.weight(block_value, block_units)
    buoyancy_factor = (65.5 - mud_weight['ppg']) / 65.5
    casing = casing['lb/ft'] * buoyancy_factor
    return ((casing * depth['ft'] * (stand['ft'] + depth['ft']) + depth['ft'] *
             block['lb']) * 0.5) / 10560000


def short_trip_ton_miles(ton_mile_1_value, ton_mile_2_value):
    return ton_mile_2_value - ton_mile_1_value


def drill_line_cut_off(ton_mile_value, cut_off_goal):
    line_removed = ton_mile_value / cut_off_goal
    return gen.length(line_removed, 'ft')


def hydrostatic_decrease_dry(stands_value, avg_stand_value, avg_std_units,
                             disp_value, disp_units, mud_value, mud_units,
                             annulus_value, annulus_units):
    avg_stand = gen.length(avg_stand_value, avg_std_units)
    pipe_disp = pro.pipe_capacity(disp_value, disp_units)
    mud_weight = dri.mud_weight(mud_value, mud_units)
    annular_vol = pro.pipe_capacity(annulus_value, annulus_units)
    vol_displaced = stands_value * avg_stand['ft'] * pipe_disp['bbl/ft']
    pressure_dec = (vol_displaced / (annular_vol['bbl/ft'] -
                                     pipe_disp['bbl/ft'])) *\
        0.052 * mud_weight['ppg']
    return gen.pressure(pressure_dec, 'psi')


def hydrostatic_decrease_wet(stands_value, avg_stand_value, avg_std_units,
                             disp_value, disp_units,
                             pipe_capacity_value, pipe_capacity_units,
                             mud_value, mud_units,
                             annulus_value, annulus_units):
    avg_stand = gen.length(avg_stand_value, avg_std_units)
    pipe_disp = pro.pipe_capacity(disp_value, disp_units)
    pipe_capacity = pro.pipe_capacity(pipe_capacity_value, pipe_capacity_units)
    mud_weight = dri.mud_weight(mud_value, mud_units)
    annular_vol = pro.pipe_capacity(annulus_value, annulus_units)
    vol_displaced = stands_value * avg_stand['ft'] *\
        (pipe_disp['bbl/ft'] + pipe_capacity['bbl/ft'])
    pressure_dec = (vol_displaced /
                    (annular_vol['bbl/ft'] - (pipe_disp['bbl/ft'] +
                                              pipe_capacity['bbl/ft']))) *\
        0.052 * mud_weight['ppg']
    return gen.pressure(pressure_dec, 'psi')


def loss_of_overbalance_dry(pressure_value, pressure_units,
                            disp_value, disp_units,
                            annulus_value, annulus_units,
                            mud_value, mud_units):
    pressure = gen.pressure(pressure_value, pressure_units)
    pipe_disp = pro.pipe_capacity(disp_value, disp_units)
    annular_vol = pro.pipe_capacity(annulus_value, annulus_units)
    mud_weight = dri.mud_weight(mud_value, mud_units)
    pulled_pipe = (pressure['psi'] * (annular_vol['bbl/ft'] -
                                      pipe_disp['bbl/ft'])) /\
        (mud_weight['ppg'] * 0.052 * pipe_disp['bbl/ft'])
    return gen.length(pulled_pipe, 'ft')


def loss_of_overbalance_wet(pressure_value, pressure_units,
                            disp_value, disp_units,
                            pipe_capacity_value, pipe_capacity_units,
                            annulus_value, annulus_units,
                            mud_value, mud_units):
    pressure = gen.pressure(pressure_value, pressure_units)
    pipe_disp = pro.pipe_capacity(disp_value, disp_units)
    pipe_capacity = pro.pipe_capacity(pipe_capacity_value, pipe_capacity_units)
    annular_vol = pro.pipe_capacity(annulus_value, annulus_units)
    mud_weight = dri.mud_weight(mud_value, mud_units)
    pulled_pipe = (pressure['psi'] * (annular_vol['bbl/ft'] -
                                      pipe_disp['bbl/ft'] -
                                      pipe_capacity['bbl/ft'])) /\
        (mud_weight['ppg'] * 0.052 *
         (pipe_capacity['bbl/ft'] + pipe_disp['bbl/ft']))
    return gen.length(pulled_pipe, 'ft')


def lost_circulation_mud_weight_at_tvd(volume_added_value, volume_added_units,
                                       riser_dia_value, riser_dia_units,
                                       dp_od_value, dp_units,
                                       mud_value, mud_units,
                                       liquid_value, liquid_units,
                                       depth_value, depth_units):
    liquid_added = gen.volume(volume_added_value, volume_added_units)
    riser_dia = gen.length(riser_dia_value, riser_dia_units)
    pipe_od = gen.length(dp_od_value, dp_units)
    mud_weight = dri.mud_weight(mud_value, mud_units)
    added_liquid = dri.mud_weight(liquid_value, liquid_units)
    depth = gen.length(depth_value, depth_units)
    annulus_filled = liquid_added['bbl'] / (0.000971 *
                                            ((riser_dia['in']**2) -
                                             (pipe_od['in']**2)))
    bottom_hole_pressure = annulus_filled * (mud_weight['ppg'] -
                                             added_liquid['ppg']) * 0.052
    mud_weight_tvd = mud_weight['ppg'] - ((bottom_hole_pressure /
                                           0.052) / depth['ft'])
    return {'annulus_filled': gen.length(annulus_filled, 'ft'),
            'bottom_hole_pressure': gen.pressure(bottom_hole_pressure, 'psi'),
            'tvd_equivalent_mud_weight': dri.mud_weight(mud_weight_tvd, 'ppg')}


def mud_weight_balance_losses(volume_added_value, volume_added_units,
                              annulus_value, annulus_units,
                              gradient_value, gradient_units,
                              depth_value, depth_units,
                              mud_value, mud_units):
    liquid_added = gen.volume(volume_added_value, volume_added_units)
    annular_vol = pro.pipe_capacity(annulus_value, annulus_units)
    liquid_gradient = dri.pressure_grad(gradient_value, gradient_units)
    depth = gen.length(depth_value, depth_units)
    mud_weight = dri.mud_weight(mud_value, mud_units)
    annular_vol = pro.pipe_capacity(annulus_value, annulus_units)
    mud_level = liquid_added['bbl'] / annular_vol['bbl/ft']
    mud_weight_equivalent = ((mud_level * liquid_gradient['psi/ft']) +
                             ((depth['ft'] - mud_level) * mud_weight['ppg'] *
                              0.052)) / (depth['ft'] * 0.052)
    return {'annulus_filled': gen.length(mud_level, 'ft'),
            'mud_weight_equivalent': dri.mud_weight(mud_weight_equivalent,
                                                    'ppg')}


def fluid_level_depth_losses(weight_value, weight_units, dp_value, dp_units,
                             buoyancy):
    weight_increase = gen.weight(weight_value, weight_units)
    pipe_weight = dri.weight_length(dp_value, dp_units)
    fluid_depth = weight_increase['lb'] / (pipe_weight['lb/ft'] *
                                           (1 - buoyancy))
    return gen.length(fluid_depth, 'ft')


def fluid_drop_before_kick(pressure_value, pressure_units,
                           gradient_value, gradient_units,
                           annulus_value, annulus_units):
    pressure = gen.pressure(pressure_value, pressure_units)
    mud_gradient = dri.pressure_grad(gradient_value, gradient_units)
    annular_vol = pro.pipe_capacity(annulus_value, annulus_units)
    fluid_drop_length = pressure['psi'] / mud_gradient['psi/ft']
    mud_loss = fluid_drop_length * annular_vol['bbl/ft']
    return {'fluid_drop_length': gen.length(fluid_drop_length, 'ft'),
            'loss_before_kick': gen.volume(mud_loss, 'bbl')}


def drill_collar_prevent_buckling(wob_value, weight_units,
                                  buoyancy_factor, safety_factor=0, angle=0):
    wob = gen.weight(wob_value, weight_units)
    weight_value = (wob['lb'] * (1 + safety_factor)) /\
        (buoyancy_factor * math.cos(math.radians(angle)))
    return gen.weight(weight_value, 'lb')


def effective_mud_density(mud_value, mud_units, flow_value, flow_units,
                          rop_value, rop_units, hole_value, hole_units):
    mud_weight = dri.mud_weight(mud_value, mud_units)
    flow_rate = dri.flow_rate(flow_value, flow_units)
    rop = dri.drilling_rate(rop_value, rop_units)
    hole_size = gen.length(hole_value, hole_units)
    effective_mud_density = ((mud_weight['ppg'] * flow_rate['gpm']) +
                             (0.01414296 * rop['ft/hr'] *
                              (hole_size['in']**2))) /\
        (flow_rate['gpm'] + (0.00067955 * rop['ft/hr'] * (hole_size['in']**2)))
    return dri.mud_weight(effective_mud_density, 'ppg')


def ecd_yield_below_13(mud_value, mud_units, reading_300, reading_600,
                       hole_id_value, dp_od_value, dp_units):
    mud_weight = dri.mud_weight(mud_value, mud_units)
    hole_id = gen.length(hole_id_value, dp_units)
    dp_od = gen.length(dp_od_value, dp_units)
    yp = reading_300 - (reading_600 - reading_300)
    ecd = mud_weight['ppg'] + ((0.1 * yp) / (hole_id['in'] - dp_od['in']))
    return {'yp': flu.viscosity(yp, 'cp'),
            'ecd': dri.mud_weight(ecd, 'ppg')}


def ecd_yield_above_13(mud_value, mud_units, reading_300, reading_600,
                       hole_id_value, dp_od_value, dp_units,
                       flow_value, flow_units):
    mud_weight = dri.mud_weight(mud_value, mud_units)
    hole_id = gen.length(hole_id_value, dp_units)
    dp_od = gen.length(dp_od_value, dp_units)
    flow_rate = dri.flow_rate(flow_value, flow_units)
    pv = reading_600 - reading_300
    yp = reading_300 - pv
    av = (24.5 * flow_rate['gpm']) / (hole_id['in']**2 - dp_od['in']**2)
    ecd = mud_weight['ppg'] + ((0.1 / (hole_id['in'] - dp_od['in'])) *
                               (yp + ((pv * av) / (300 * (hole_id['in'] -
                                                          dp_od['in'])))))
    return {'av': fap.velocity(av, 'ft/min'),
            'pv': flu.viscosity(pv, 'cp'),
            'yp': flu.viscosity(yp, 'cp'),
            'ecd': dri.mud_weight(ecd, 'ppg')}


def lag_time(flow_value, flow_units, pump_value, pump_units,
             annulus_value, annulus_units):
    flow_rate = dri.flow_rate(flow_value, flow_units)
    pump_output = pro.stroke_volume(pump_value, pump_units)
    annular_volume = gen.volume(annulus_value, annulus_units)
    lag_time = annular_volume['bbl'] / flow_rate['bbl/min']
    lag_strokes = annular_volume['bbl'] / pump_output['bbl/stk']
    return {'lag_time': lag_time,
            'lag_strokes': lag_strokes}


def light_weight_pill_height(mud_value, pill_value, mud_units,
                             pressure_value, pressure_units,
                             annulus_value, annulus_units):
    mud_weight = dri.mud_weight(mud_value, mud_units)
    pill_weight = dri.mud_weight(pill_value, mud_units)
    pressure = gen.pressure(pressure_value, pressure_units)
    annular_volume = pro.pipe_capacity(annulus_value, annulus_units)
    pill_height = pressure['psi'] / ((mud_weight['ppg'] -
                                      pill_weight['ppg']) * 0.052)
    pill_volume = pill_height * annular_volume['bbl/ft']
    return {'pill_height': gen.length(pill_height, 'ft'),
            'pill_volume': gen.volume(pill_volume, 'bbl')}


def maximum_rop_fracturing_formation(mud_value, lot_value, mud_units,
                                     pressure_value, pressure_units,
                                     flow_value, flow_units,
                                     depth_value, depth_units,
                                     hole_value, hole_units):
    mud_weight = dri.mud_weight(mud_value, mud_units)
    lot_test = dri.mud_weight(lot_value, mud_units)
    pressure = gen.pressure(pressure_value, pressure_units)
    flow_rate = dri.flow_rate(flow_value, flow_units)
    depth = gen.length(depth_value, depth_units)
    hole_id = gen.length(hole_value, hole_units)
    annular_pressure_loss = pressure['psi'] / (0.052 * depth['ft'])
    max_rop = (flow_rate['gpm'] * (lot_test['ppg'] - annular_pressure_loss -
                                   mud_weight['ppg'])) /\
        ((hole_id['in']**2) * (0.01414296 -
                               (0.00067995 * (lot_test['ppg'] -
                                              annular_pressure_loss))))
    return dri.drilling_rate(max_rop, 'ft/hr')


def pipe_thermal_expansion(pipe_value, pipe_units, surface_value,
                           bottom_value, temp_units):
    pipe_length = gen.length(pipe_value, pipe_units)
    surface_temp = gen.temperature(surface_value, temp_units)
    bottom_temp = gen.temperature(bottom_value, temp_units)
    average_temp = (bottom_temp['f'] + surface_temp['f']) / 2
    delta_temp = average_temp - surface_temp['f']
    thermal_expansion = (pipe_length['ft'] / 100) * (delta_temp / 100) * 0.83
    return {'average_temp': gen.temperature(average_temp, 'f'),
            'delta_temp': gen.temperature(delta_temp, 'f'),
            'thermal_expansion': gen.length(thermal_expansion, 'in')}


def stuck_pipe(stretch_value, stretch_units, pull_value, pull_units,
               dp_od_value, dp_id_value, dp_units):
    stretch = gen.length(stretch_value, stretch_units)
    pull_force = fap.force(pull_value, pull_units)
    dp_od = gen.length(dp_od_value, dp_units)
    dp_id = gen.length(dp_id_value, dp_units)
    free_point_constant = (((dp_od['in']**2) - (dp_id['in']**2)) *
                           0.7854) * 2500
    stuck_depth = (free_point_constant * stretch['in']) / pull_force['klbs']
    return {'free_point_constant': free_point_constant,
            'stuck_depth': gen.length(stuck_depth, 'ft')}


def annular_pressure_loss(mud_value, mud_units, length_value, length_unit,
                          flow_value, flow_units, hole_value,
                          dp_value, dp_units):
    mud_weight = dri.mud_weight(mud_value, mud_units)
    annular_length = gen.length(length_value, length_unit)
    flow_rate = dri.flow_rate(flow_value, flow_units)
    hole_id = gen.length(hole_value, dp_units)
    pipe_od = gen.length(dp_value, dp_units)
    annular_velocity = (24.5 * flow_rate['gpm']) / ((hole_id['in']**2) -
                                                    (pipe_od['in']**2))
    annular_pressure_loss = (0.00000014327 * mud_weight['ppg'] *
                             annular_length['ft'] *
                             (annular_velocity**2)) / (hole_id['in'] -
                                                       pipe_od['in'])
    return gen.pressure(annular_pressure_loss, 'psi')


def critical_rpm(pipe_length, pipe_units, od_value, id_value, dp_units):
    pipe_length = gen.length(pipe_length, pipe_units)
    pipe_od = gen.length(od_value, dp_units)
    pipe_id = gen.length(id_value, dp_units)
    return (33055 * ((pipe_od['in'])**2 +
                     (pipe_id['in'])**2)**0.5) / (pipe_length['ft'])**2


def laminar_flow(velocity, id_value, od_value, n_value, k_value, length):
    return ((((2.4 * velocity) / (od_value - id_value)) *
             (((2 * n_value) + 1) / (3 * n_value)))**n_value) *\
        ((k_value * length)/(300 * (od_value - id_value)))


def turbulent_flow(mud, flow_rate, pv, length, id_value, od_value):
    return (0.000077 * (mud**0.8) * (flow_rate**1.8) * (pv**0.2) * length) /\
        (((od_value - id_value)**3) * ((od_value + id_value)**1.8))


def ecd_engineering_formula(mud_value, mud_units, reading_300, reading_600,
                            viscosity_value, viscosity_units,
                            flow_value, flow_units,
                            hole_dia_value, collar_dia_value,
                            dp_dia_value, dia_units,
                            hole_len_value, dp_len_value,
                            collar_len_value, len_units):
    mud_weight = dri.mud_weight(mud_value, mud_units)
    viscosity = flu.viscosity(viscosity_value, viscosity_units)
    flow_rate = dri.flow_rate(flow_value, flow_units)
    hole_id = gen.length(hole_dia_value, dia_units)
    pipe_od = gen.length(dp_dia_value, dia_units)
    collar_od = gen.length(collar_dia_value, dia_units)
    hole_tvd = gen.length(hole_len_value, len_units)
    pipe_len = gen.length(dp_len_value, len_units)
    collar_len = gen.length(collar_len_value, len_units)
    n_value = 3.32 * (math.log(reading_600/reading_300, 10))
    k_value = (reading_300 / (511**n_value))
    annular_velocity_pipe = (24.5 * flow_rate['gpm']) /\
        ((hole_id['in'])**2 - (pipe_od['in'])**2)
    annular_velocity_collar = (24.5 * flow_rate['gpm']) /\
        ((hole_id['in'])**2 - (collar_od['in'])**2)
    critical_velocity_pipe = (((3.878e4 * k_value) /
                               mud_weight['ppg'])**(1 / (2 - n_value))) *\
        ((2.4 / (hole_id['in'] - pipe_od['in'])) *
         (((2 * n_value) + 1) / (3 * n_value)))**(n_value / (2 - n_value))
    critical_velocity_collar = (((3.878e4 * k_value) /
                                 mud_weight['ppg'])**(1 / (2 - n_value))) *\
        ((2.4 / (hole_id['in'] - collar_od['in'])) *
         (((2 * n_value) + 1) / (3 * n_value)))**(n_value / (2 - n_value))
    pressure_loss_pipe = 0
    pressure_loss_collar = 0
    if annular_velocity_pipe < critical_velocity_pipe:
        pressure_loss_pipe = laminar_flow(annular_velocity_pipe,
                                          pipe_od['in'], hole_id['in'],
                                          n_value, k_value, pipe_len['ft'])
    elif annular_velocity_pipe > critical_velocity_pipe:
        pressure_loss_pipe = turbulent_flow(mud_weight['ppg'],
                                            flow_rate['gpm'], viscosity['cp'],
                                            pipe_len['ft'], pipe_od['in'],
                                            hole_id['in'])
    if annular_velocity_collar < critical_velocity_collar:
        pressure_loss_collar = laminar_flow(annular_velocity_collar,
                                            collar_od['in'], hole_id['in'],
                                            n_value, k_value, collar_len['ft'])
    elif annular_velocity_collar > critical_velocity_collar:
        pressure_loss_collar = turbulent_flow(mud_weight['ppg'],
                                              flow_rate['gpm'],
                                              viscosity['cp'],
                                              collar_len['ft'],
                                              collar_od['in'], hole_id['in'])
    ecd_value = ((pressure_loss_pipe + pressure_loss_collar) /
                 (0.052 * hole_tvd['ft'])) + mud_weight['ppg']
    return dri.mud_weight(ecd_value, 'ppg')


def bhp_wellhead_pressure(pressure_value, pressure_units,
                          temp_value, temp_units,
                          gas_value, depth_value, depth_units):
    wellhead_pressure = gen.pressure(pressure_value, pressure_units)
    average_temp = gen.temperature(temp_value, temp_units)
    tvd_depth = gen.length(depth_value, depth_units)
    bottom_hole_pressure = wellhead_pressure['psi'] *\
        math.exp(((gas_value / 53.36) * tvd_depth['ft']) /
                 (average_temp['f'] + 460))
    return gen.pressure(bottom_hole_pressure, 'psi')
