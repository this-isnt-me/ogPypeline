import drilling as dri
import force_and_power as fap
import fluid as flu
import general as gen
import production as pro
import math


def gas_migration_rate(pressure_value, pressure_units, mud_value, mud_units):
    pressure = gen.pressure(pressure_value, pressure_units)
    mud_weight = dri.mud_weight(mud_value, mud_units)
    migration_rate = pressure['psi'] / (mud_weight['ppg'] * 0.052)
    return fap.velocity(migration_rate, 'ft/hr')


def max_shutin_casing_pressure(pressure_value, pressure_units,
                               tvd_value, depth_units,
                               original_mud_value,
                               current_mud_value, mud_units):
    pressure = gen.pressure(pressure_value, pressure_units)
    original_mud = dri.mud_weight(original_mud_value, mud_units)
    current_mud = dri.mud_weight(current_mud_value, mud_units)
    tvd = gen.length(tvd_value, depth_units)
    new_pressure = pressure['psi'] - (tvd['ft'] *
                                      (current_mud['ppg'] -
                                       original_mud['ppg']) * 0.052)
    return gen.pressure(new_pressure, 'psi')


def influx_height(gain_value, volume_units, annular_value, annular_units):
    gain = gen.volume(gain_value, volume_units)
    annular_capacity = pro.pipe_capacity(annular_value, annular_units)
    influx_height = gain['bbl']/annular_capacity['bbl/ft']
    return gen.length(influx_height, 'ft')


def gas_migration_estimation(mud_value, mud_units):
    mud_weight = dri.mud_weight(mud_value, mud_units)
    migration_rate = 12 * math.exp(-0.37 * mud_weight['ppg'])
    return fap.velocity(migration_rate, 'ft/s')


def influx_type_estimation(casing_pressure, pipe_pressure, pressure_units,
                           influx_height, height_units,
                           mud_value, mud_units):
    casing_pressure = gen.pressure(casing_pressure, pressure_units)
    pipe_pressure = gen.pressure(pipe_pressure, pressure_units)
    influx_height = gen.length(influx_height, height_units)
    mud_weight = dri.mud_weight(mud_value, mud_units)
    influx_weight = (mud_weight['ppg'] -
                     ((casing_pressure['psi'] -
                       pipe_pressure['psi']) /
                      (0.052 * influx_height['ft'])))
    influx_type = 'Gas Influx'
    if 3 < influx_weight <= 7:
        influx_type = 'Oil Influx or Combination Oil and Gas kick'
    elif influx_weight > 7:
        influx_type = 'Water Kick'
    return {'influx_weight': dri.mud_weight(influx_weight, 'ppg'),
            'influx_type': influx_type}


def final_circulating_pressure(pressure_value, pressure_units, kill_mud,
                               original_mud, mud_units):
    pressure = gen.pressure(pressure_value, pressure_units)
    kill_mud = dri.mud_weight(kill_mud, mud_units)
    original_mud = dri.mud_weight(original_mud, mud_units)
    circulating_pressure = (pressure['psi'] * kill_mud['ppg'] /
                            original_mud['ppg'])
    return gen.pressure(circulating_pressure, 'psi')


def inital_circulating_pressure(scr_value, sidpp_value, pressure_units):
    scr_pressure = gen.pressure(scr_value, pressure_units)
    sidpp_pressure = gen.pressure(sidpp_value, pressure_units)
    return gen.pressure(scr_pressure['psi'] + sidpp_pressure['psi'], 'psi')


def formation_pressure_kick_analysis(sidpp_value, pressure_units,
                                     tvd_value, depth_units,
                                     mud_value, mud_units):
    sidpp_value = gen.pressure(sidpp_value, pressure_units)
    mud = dri.mud_weight(mud_value, mud_units)
    tvd = gen.length(tvd_value, depth_units)
    formation_pressure = sidpp_value['psi'] + (0.052 * tvd['ft'] * mud['ppg'])
    return gen.pressure(formation_pressure, 'psi')


def pressure_loss_gas_cut(mud_value, mud_units, annular_value, annular_units,
                          gain_value, gain_units):
    mud = dri.mud_weight(mud_value, mud_units)
    annular_capacity = pro.pipe_capacity(annular_value, annular_units)
    pit_gain = gen.volume(gain_value, gain_units)
    pressure_loss = ((mud['ppg'] * 0.052) /
                     annular_capacity['bbl/ft']) * pit_gain['bbl']
    return gen.pressure(pressure_loss, 'psi')


def kick_penetration_pressure_increase(gain_value, gain_units, mud_value,
                                       kick_value, mud_units, hole_id_value,
                                       bha_od_value, pipe_od_value, dia_value,
                                       bha_length, length_units):
    pit_gain = gen.volume(gain_value, gain_units)
    mud = dri.mud_weight(mud_value, mud_units)
    kick = dri.mud_weight(kick_value, mud_units)
    hole_id = gen.length(hole_id_value, dia_value)
    bha_od = gen.length(bha_od_value, dia_value)
    pipe_od = gen.length(pipe_od_value, dia_value)
    bha = gen.length(bha_length, length_units)
    hole_capacity = hole_id['in']**2 / 1029.4
    annular_capacity_bha = (hole_id['in']**2 - bha_od['in']**2)/1029.4
    annular_capacity_pipe = (hole_id['in']**2 - pipe_od['in']**2)/1029.4
    kick_height_hole = pit_gain['bbl'] / hole_capacity
    kick_height_annulus = 0
    if annular_capacity_bha * bha['ft'] > pit_gain['bbl']:
        kick_height_annulus = pit_gain['bbl'] / annular_capacity_bha
    else:
        kick_height_annulus = (bha['ft'] + ((pit_gain['bbl'] -
                                             (annular_capacity_bha *
                                              bha['ft'])) /
                                            annular_capacity_pipe))
    casing_pressure_increase = ((kick_height_annulus - kick_height_hole) *
                                0.052 * (mud['ppg'] - kick['ppg']))
    return gen.pressure(casing_pressure_increase, 'psi')


def kick_tolerance_factor(shoe_value, tvd_value, depth_units,
                          max_mud_value, mud_value, mud_units):
    shoe_value = gen.length(shoe_value, depth_units)
    tvd_value = gen.length(tvd_value, depth_units)
    max_mud = dri.mud_weight(max_mud_value, mud_units)
    mud = dri.mud_weight(mud_value, mud_units)
    ktf = (shoe_value['ft'] / tvd_value['ft']) * (max_mud['ppg'] - mud['ppg'])
    return dri.mud_weight(ktf, 'ppg')


def kill_mud_weight(pressure_value, pressure_units, mud_value, mud_units,
                    tvd_value, depth_units):
    pressure = gen.pressure(pressure_value, pressure_units)
    mud = dri.mud_weight(mud_value, mud_units)
    tvd_value = gen.length(tvd_value, depth_units)
    kill_mud_weight = (mud['ppg'] + (pressure['psi'] /
                                     (0.052 * tvd_value['ft'])))
    return dri.mud_weight(kill_mud_weight, 'ppg')


# lube increment and mud increment
def fluid_increment(pressure_value, pressure_units,
                    casing_id_value, pipe_od_value, dia_units,
                    mud_value, mud_units):
    pressure = gen.pressure(pressure_value, pressure_units)
    casing_id = gen.length(casing_id_value, dia_units)
    pipe_od = gen.length(pipe_od_value, dia_units)
    mud = dri.mud_weight(mud_value, mud_units)
    annular_capacity = (casing_id['in']**2 - pipe_od['in']**2) / 1029.4
    lube_increment = pressure['psi'] * annular_capacity / (0.052 * mud['ppg'])
    return {'annular_capacity': pro.pipe_capacity(annular_capacity, 'bbl/ft'),
            'lube_increment': gen.volume(lube_increment, 'bbl')}


def max_formation_pressure(kick_factor, mud_value, mud_units,
                           tvd_value, depth_units):
    kick_factor = dri.mud_weight(kick_factor, mud_units)
    mud = dri.mud_weight(mud_value, mud_units)
    tvd_value = gen.length(tvd_value, depth_units)
    max_formation_pressure = (0.052 * (kick_factor['ppg'] + mud['ppg']) *
                              tvd_value['ft'])
    return gen.pressure(max_formation_pressure, 'psi')


def max_influx_height(casing_pressure, pressure_units, mud_value,
                      influx_value, gradient_units):
    masicp = gen.pressure(casing_pressure, pressure_units)
    mud = dri.pressure_grad(mud_value, gradient_units)
    influx = dri.pressure_grad(influx_value, gradient_units)
    return gen.length((masicp['psi'] / (mud['psi/ft'] -
                                        influx['psi/ft'])), 'ft')


def misicp(lot_value, mud_value, mud_units, tvd_value, depth_units):
    lot = dri.mud_weight(lot_value, mud_units)
    mud = dri.mud_weight(mud_value, mud_units)
    tvd_value = gen.length(tvd_value, depth_units)
    max_formation_pressure = (0.052 * (lot['ppg'] - mud['ppg']) *
                              tvd_value['ft'])
    return gen.pressure(max_formation_pressure, 'psi')


def max_pit_gain_gas_kick_wbm(pressure_value, pressure_units,
                              pit_gain, volume_units,
                              mud_value, mud_units,
                              annular_value, annular_units):
    formation_pressure = gen.pressure(pressure_value, pressure_units)
    gain = gen.volume(pit_gain, volume_units)
    mud = dri.mud_weight(mud_value, mud_units)
    annular_capacity = pro.pipe_capacity(annular_value, annular_units)
    max_gain = 4 * (((formation_pressure['psi'] * gain['bbl'] *
                      annular_capacity['bbl/ft'] / mud['ppg']))**0.5)
    return gen.volume(max_gain, 'bbl')


def max_surface_pressure_gas_influx_wbm(pressure_value, pressure_units,
                                        pit_gain, volume_units,
                                        mud_value, mud_units,
                                        annular_value, annular_units):
    formation_pressure = gen.pressure(pressure_value, pressure_units)
    gain = gen.volume(pit_gain, volume_units)
    mud = dri.mud_weight(mud_value, mud_units)
    annular_capacity = pro.pipe_capacity(annular_value, annular_units)
    max_pressure = 0.2 * ((formation_pressure['psi'] * gain['bbl'] *
                           mud['ppg'] / annular_capacity['bbl/ft']))**0.5
    return gen.pressure(max_pressure, 'psi')


def max_surface_pressure_kick_tolerance(mud_value, mud_units,
                                        tvd_value, depth_units):
    kick_factor = dri.mud_weight(mud_value, mud_units)
    tvd = gen.length(tvd_value, depth_units)
    return gen.pressure(0.052 * kick_factor['ppg'] * tvd['ft'], 'psi')


def new_mud_pressure_loss(pressure_value, pressure_units, old_value,
                          new_value, mud_units):
    pressure_loss = gen.pressure(pressure_value, pressure_units)
    old_mud = dri.mud_weight(old_value, mud_units)
    new_mud = dri.mud_weight(new_value, mud_units)
    return gen.pressure(pressure_loss['psi'] * new_mud['ppg'] /
                        old_mud['ppg'], 'psi')


def new_strokes_pump_pressure(pressure_value, pressure_units,
                              old_stokes, new_stokes):
    pressure_loss = gen.pressure(pressure_value, pressure_units)
    return gen.pressure(pressure_loss['psi'] * (new_stokes /
                                                old_stokes)**2, 'psi')


def riser_margin(air_gap, water_depth, tvd_value, depth_units,
                 mud_value, water_value, mud_units):
    mud = dri.mud_weight(mud_value, mud_units)
    water = dri.mud_weight(water_value, mud_units)
    air_gap = gen.length(air_gap, depth_units)
    water_depth = gen.length(water_depth, depth_units)
    tvd = gen.length(tvd_value, depth_units)
    return dri.mud_weight(((air_gap['ft'] +
                            water_depth['ft']) *
                           mud['ppg'] -
                           (water_depth['ft'] *
                            water['ppg'])) /
                          (tvd['ft'] -
                           air_gap['ft'] - water_depth['ft']), 'ppg')


def time_penetrate_kick(kick_depth, bit_depth, depth_units,
                        migration_value, stripping_value, velocity_units):
    kick_depth = gen.length(kick_depth, depth_units)
    bit_depth = gen.length(bit_depth, depth_units)
    migration = fap.velocity(migration_value, velocity_units)
    stripping = fap.velocity(stripping_value, velocity_units)
    return gen.time((kick_depth['ft'] - bit_depth['ft']) /
                    (migration['ft/hr'] + stripping['ft/hr']), 'hr')


def trip_margin(yield_value, yield_units, hole_id, pipe_od, dia_units):
    yield_point = flu.fluid_yield_point(yield_value, yield_units)
    hole_id = gen.length(hole_id, dia_units)
    pipe_od = gen.length(pipe_od, dia_units)
    return dri.mud_weight(yield_point['lbf/100ft2'] /
                          ((11.7 * (hole_id['in'] - pipe_od['in']))), 'ppg')


def accumulator_bottle_capacity_required(volume_value, volume_units,
                                         pre_charge_value, minimum_value,
                                         operating_value, pressure_units):
    required_volume = gen.volume(volume_value, volume_units)
    pre_charge = gen.pressure(pre_charge_value, pressure_units)
    operating = gen.pressure(operating_value, pressure_units)
    minimum = gen.pressure(minimum_value, pressure_units)
    usable_volume = (required_volume['gal_us'] /
                     ((pre_charge['psi'] /
                       minimum['psi']) -
                      (pre_charge['psi'] / operating['psi'])))
    return gen.volume(usable_volume, 'gal_us')
