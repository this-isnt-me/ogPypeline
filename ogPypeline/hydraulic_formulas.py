import drilling as dri
import force_and_power as fap
import fluid as flu
import general as gen
import math


def bit_nozzle_velocity_flow(flow_value, flow_units,
                             area_value, area_units):
    flow_rate= dri.flow_rate(flow_value, flow_units)
    nozzle_area = gen.area(area_value, area_units)
    velocity = 0.321 * (flow_rate['gpm'] / nozzle_area['in2'])
    return fap.velocity(velocity, 'ft/s')


def bit_nozzle_velocity_pressure_drop(mud_value, mud_units,
                                      pressure_value, pressure_units):
    mud_weight = dri.mud_weight(mud_value, mud_units)
    pressure_drop = gen.pressure(pressure_value, pressure_units)
    velocity = ((1239 * pressure_drop['psi']) / mud_weight['ppg'])**0.5
    return fap.velocity(velocity, 'ft/s')


def bit_aggressiveness(torque_value, torque_units,
                       wob_value, wob_units, bit_value, bit_units):
    torque = gen.torque(torque_value, torque_units)
    wob = gen.weight(wob_value, wob_units)
    bit_dia = gen.length(bit_value, bit_units)
    return (36 * torque['ft-lb']) / (wob['lb'] * bit_dia['in'])


def bit_hhp(flow_value, flow_units, pressure_value, pressure_units):
    flow_rate= dri.flow_rate(flow_value, flow_units)
    pressure_drop = gen.pressure(pressure_value, pressure_units)
    return (flow_rate['gpm'] * pressure_drop['psi']) / 1740


def critical_flow(n_constant, k_constant, mud_value, mud_units,
                  hole_id_value, pipe_od_value, dia_units):
    mud_weight = dri.mud_weight(mud_value, mud_units)
    hole_id = gen.length(hole_id_value, dia_units)
    pipe_od = gen.length(pipe_od_value, dia_units)
    sec_one_t = (3470 - (1370 * n_constant))
    sec_two_t = 100
    sec_three_t = 6.63
    sec_four_t = (((2 * n_constant) + 1) / (3 * n_constant))**n_constant
    top = sec_one_t * sec_two_t * sec_three_t * sec_four_t
    sec_one_b = 958 * mud_weight['ppg']
    sec_two_b = hole_id['in'] - pipe_od['in']
    sec_three_b = (144 / (hole_id['in'] - pipe_od['in']))**(1 - n_constant)
    btm = sec_one_b * sec_two_b * sec_three_b
    factor = 1 / (2 - n_constant)
    final = (top / btm)**factor
    critical_flow_rate = 2.45 * final * (hole_id['in']**2 - pipe_od['in']**2)
    return { 'critical_velocity' : fap.velocity(final, 'ft/s'),
             'critical_flow' : dri.flow_rate(critical_flow_rate, 'gpm')
    }


def cross_flow_velocity(flow_value, flow_units,
                        velocity_value, velocity_units,
                        bit_value, bit_units, nozzles):
    flow_rate = dri.flow_rate(flow_value, flow_units)
    nozzle_velocity = fap.velocity(velocity_value, velocity_units)
    bit_dia = gen.length(bit_value, bit_units)
    cross_flow_velocity = ((108.5 * flow_rate['gpm'] * nozzle_velocity['ft/s'])
                           / (nozzles * bit_dia['in']))**0.5
    return fap.velocity(cross_flow_velocity, 'ft/s')


def effective_viscosity(consistency_factor_value, consistency_factor_units,
                        power_law_value, hole_id_value, pipe_od_value, dia_units,
                        flow_value, flow_units):
    consistency_factor = flu.viscocity(consistency_factor_value, consistency_factor_units)
    hole_id = gen.length(hole_id_value, dia_units)
    pipe_od = gen.length(pipe_od_value, dia_units)
    flow_rate = dri.flow_rate(flow_value, flow_units)
    annular_velocity = ((24.5 * flow_rate['gpm'])
                        / ((hole_id['in'])**2 - (pipe_od['in'])**2))
    effective_viscosity = (consistency_factor['cp'] *
                           (((144 * (annular_velocity /60)) /
                             (hole_id['in'] -
                              pipe_od['in']))**(power_law_value - 1)))
    return flu.viscocity(effective_viscosity, 'cp')


def impact_force_jet_nozzle_velocity(flow_value, flow_units,
                                     mud_value, mud_units,
                                     velocity_value, velocity_units):
    mud_weight = dri.mud_weight(mud_value, mud_units)
    flow_rate = dri.flow_rate(flow_value, flow_units)
    nozzle_velocity = fap.velocity(velocity_value, velocity_units)
    btm_hole_force = ((flow_rate['gpm'] * mud_weight['ppg'] *
                       nozzle_velocity['ft/s']) / 1930)
    return fap.force(btm_hole_force,'lbf')


def impact_force_jet_nozzle_pressure(flow_value, flow_units,
                                     mud_value, mud_units,
                                     pressure_value, pressure_units):
    mud_weight = dri.mud_weight(mud_value, mud_units)
    flow_rate = dri.flow_rate(flow_value, flow_units)
    pressure_drop = gen.pressure(pressure_value, pressure_units)
    btm_hole_force = ((flow_rate['gpm'] * 0.0173) *
                      ((pressure_drop['psi'] * mud_weight['ppg'])**0.5))
    return fap.force(btm_hole_force,'lbf')


def power_law_constants(reading_300, reading_3):
    power_law_n = 0.5 * math.log(reading_300 / reading_3, 10)
    power_law_k = (5.11 * reading_300) / (511**power_law_n)
    power_law_dict = flu.viscocity(power_law_k * 100, 'cp')
    power_law_dict['poise'] = power_law_k
    return { 'power_law_n': power_law_n,
             'power_law_k': power_law_dict
    }


def pressure_drop_across_bit_flow_rate(mud_value, mud_units,
                                       flow_value, flow_units,
                                       nozzle_value, nozzle_unit):
    mud_weight = dri.mud_weight(mud_value, mud_units)
    flow_rate = dri.flow_rate(flow_value, flow_units)
    nozzle_area = gen.area(area_value, area_units)
    pressure_drop = ((mud_weight['ppg'] * (flow_rate['gpm'])**2) /
                     (12032 * (nozzle_area['in2'])**2))
    return gen.pressure(pressure_drop, 'psi')


def pressure_drop_across_bit_velocity(mud_value, mud_units,
                                      nozzle_value, nozzle_unit):
    mud_weight = dri.mud_weight(mud_value, mud_units)
    nozzle_velocity = fap.velocity(nozzle_value, nozzle_unit)
    pressure_drop = (mud_weight['ppg'] * (nozzle_velocity['ft/sec'])**2) / 1239
    return gen.pressure(pressure_drop, 'psi')


def pressure_loss_annulus(string_value, string_units,
                          hole_id_value, pipe_od_value, dia_units,
                          mud_value, mud_units,
                          viscosity_value, viscosity_units,
                          flow_value, flow_units):
    string_length = gen.length(string_value, string_units)
    hole_id = gen.length(hole_id_value, dia_units)
    pipe_od = gen.length(pipe_od_value, dia_units)
    mud_weight = dri.mud_weight(mud_value, mud_units)
    viscocity = flu.viscocity(viscosity_value, viscosity_units)
    flow_rate = dri.flow_rate(flow_value, flow_units)
    b_param = 2.0
    hole = hole_id['in']
    if 5.875 < hole <= 6.75:
        b_param = 2.2
    elif 6.75 < hole <= 7.75:
        b_param = 2.3
    elif 7.75 < hole <= 11:
        b_param = 2.4
    elif hole > 11:
        b_param = 2.5
    coefficient = ((8.6 * b_param) /
                   ((hole_id['in'] - pipe_od['in']) *
                    ((hole_id['in'])**2 - (pipe_od['in'])**2)**2))
    viscosity_cor = (viscocity['cp'] / mud_weight['ppg'])**0.14
    pressure_loss = (0.00001 * coefficient * viscosity_cor *
                     string_length['ft'] *
                     mud_weight['ppg'] *
                     (flow_rate['gpm'])**1.86)
    return {'coefficient': coefficient,
            'pressure_loss' : gen.pressure(pressure_loss, 'psi')}


def reynold_number(annular_value, annular_units,
                   hole_id_value, pipe_od_value, dia_units,
                   mud_value, mud_units,
                   viscosity_value, viscosity_units, power_law_value):
    annular_velocity = fap.velocity(annular_value, annular_units)
    hole_id = gen.length(hole_id_value, dia_units)
    pipe_od = gen.length(pipe_od_value, dia_units)
    mud_weight = dri.mud_weight(mud_value, mud_units)
    viscocity = flu.viscocity(viscosity_value, viscosity_units)
    return ((928 * annular_velocity['ft/s'] *
             (hole_id['in'] - pipe_od['in']) *
             mud_weight['ppg']) /
            (viscocity['cp'] *
             (((2 * power_law_value) + 1) /
              (3 * power_law_value))**power_law_value))