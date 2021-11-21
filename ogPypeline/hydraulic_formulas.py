import drilling as dri
import force_and_power as fap
import fluid as flu
import general as gen
import math


def bit_nozzle_velocity_flow(flow_value, flow_units,
                             area_value, area_units):
    flow_rate = dri.flow_rate(flow_value, flow_units)
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
    flow_rate = dri.flow_rate(flow_value, flow_units)
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
    return {'critical_velocity': fap.velocity(final, 'ft/s'),
            'critical_flow': dri.flow_rate(critical_flow_rate, 'gpm')}


def cross_flow_velocity(flow_value, flow_units,
                        velocity_value, velocity_units,
                        bit_value, bit_units, nozzles):
    flow_rate = dri.flow_rate(flow_value, flow_units)
    nozzle_velocity = fap.velocity(velocity_value, velocity_units)
    bit_dia = gen.length(bit_value, bit_units)
    cross_flow_velocity = ((108.5 * flow_rate['gpm'] * nozzle_velocity['ft/s'])
                           / (nozzles * bit_dia['in']))**0.5
    return fap.velocity(cross_flow_velocity, 'ft/s')


def cutting_carrying_index(mud_value, mud_units,
                           velocity_value, velocity_units,
                           viscosity_value, viscosity_units,
                           yield_value, yield_units):
    mud_weight = dri.mud_weight(mud_value, mud_units)
    annular_velocity = fap.velocity(velocity_value, velocity_units)
    plastic_viscosity = flu.viscosity(viscosity_value, viscosity_units)
    yield_point = flu.fluid_yield_point(yield_value, yield_units)
    n = (3.322 * math.log10((2 * plastic_viscosity['cp'] +
                             yield_point['lbf/100ft2']) /
                            (plastic_viscosity['cp'] +
                             yield_point['lbf/100ft2'])))
    K = 511**(1 - n) * (plastic_viscosity['cp'] + yield_point['lbf/100ft2'])
    cci = K * annular_velocity['ft/min'] * mud_weight['ppg'] / 400000
    hole_cleaning = 'Good Hole Cleaning'
    if cci < 1:
        hole_cleaning = 'Poor Hole Cleaning'
    return {'n': n,
            'K': K,
            'cci': cci,
            'hole_cleaning': hole_cleaning}


def cutting_slip_velocity_one(flow_value, flow_units,
                              hole_diameter, pipe_diameter, diameter_units,
                              viscosity_value, viscosity_units,
                              mud_value, mud_units,
                              cutting_dia, dia_units,
                              cutting_density, density_units):
    flow = dri.flow_rate(flow_value, flow_units)
    hole_dia = gen.length(hole_diameter, diameter_units)
    pipe_dia = gen.length(pipe_diameter, diameter_units)
    pv = flu.viscosity(viscosity_value, viscosity_units)
    mud_weight = dri.mud_weight(mud_value, mud_units)
    cutting_dia = gen.length(cutting_dia, dia_units)
    cutting_weight = dri.mud_weight(cutting_density, density_units)
    annular_velocity = ((24.5 * flow['gpm']) /
                        (hole_dia['in']**2 - pipe_dia['in']**2))
    cutting_slip_velocity =\
        (0.45 * (pv['cp'] /
                 (mud_weight['ppg'] *
                 cutting_dia['in'])) *
         (((36800 / ((pv['cp'] /
                      (mud_weight['ppg'] *
                       cutting_dia['in']))**2) *
            cutting_dia['in'] *
            ((cutting_weight['ppg'] /
              mud_weight['ppg']) - 1) + 1))**0.5 - 1))
    net_rise_velocity = annular_velocity - cutting_slip_velocity
    net_rise = 'positive'
    if net_rise_velocity < 0:
        net_rise = 'negative'
    return {'annular_velocity':
            fap.velocity(annular_velocity, 'ft/min'),
            'cutting_slip_velocity':
            fap.velocity(cutting_slip_velocity, 'ft/min'),
            'net_rise_velocity':
            fap.velocity(net_rise_velocity, 'ft/min'),
            'net_rise': net_rise}


def cutting_slip_velocity_two(reading_300, reading_600, flow_value, flow_units,
                              hole_diameter, pipe_diameter, diameter_units,
                              cutting_dia, dia_units, cutting_density,
                              density_units, mud_value, mud_units):
    flow = dri.flow_rate(flow_value, flow_units)
    hole_dia = gen.length(hole_diameter, diameter_units)
    pipe_dia = gen.length(pipe_diameter, diameter_units)
    cutting_dia = gen.length(cutting_dia, dia_units)
    cutting_weight = dri.mud_weight(cutting_density, density_units)
    mud_weight = dri.mud_weight(mud_value, mud_units)
    n = 3.32 * math.log10(reading_600 / reading_300)
    K = reading_300 / (511**n)
    annular_velocity = (24.5 * flow['gpm'] /
                        (hole_dia['in']**2 - pipe_dia['in']**2))
    viscosity = (((2.4 * annular_velocity /
                   (hole_dia['in'] - pipe_dia['in'])) *
                  ((2 * n + 1) / (3 * n)))**n *
                 ((200 * K * (hole_dia['in'] -
                              pipe_dia['in'])) / annular_velocity))
    cutting_slip_velocity = ((((cutting_weight['ppg'] -
                                mud_weight['ppg'])**0.667) *
                              175 * cutting_dia['in']) /
                             (mud_weight['ppg']**0.333 * viscosity**0.333))
    net_rise_velocity = annular_velocity - cutting_slip_velocity
    net_rise = 'positive'
    if net_rise_velocity < 0:
        net_rise = 'negative'
    return {'n': n,
            'K': K,
            'viscosity':
            flu.viscosity(viscosity, 'cp'),
            'annular_velocity':
            fap.velocity(annular_velocity, 'ft/min'),
            'cutting_slip_velocity':
            fap.velocity(cutting_slip_velocity, 'ft/min'),
            'net_rise_velocity':
            fap.velocity(net_rise_velocity, 'ft/min'),
            'net_rise': net_rise}


def effective_viscosity(consistency_factor_value, consistency_factor_units,
                        power_law_value, hole_id_value, pipe_od_value,
                        dia_units, flow_value, flow_units):
    consistency_factor = flu.viscocity(consistency_factor_value,
                                       consistency_factor_units)
    hole_id = gen.length(hole_id_value, dia_units)
    pipe_od = gen.length(pipe_od_value, dia_units)
    flow_rate = dri.flow_rate(flow_value, flow_units)
    annular_velocity = ((24.5 * flow_rate['gpm'])
                        / ((hole_id['in'])**2 - (pipe_od['in'])**2))
    effective_viscosity = (consistency_factor['cp'] *
                           (((144 * (annular_velocity / 60)) /
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
    return fap.force(btm_hole_force, 'lbf')


def impact_force_jet_nozzle_pressure(flow_value, flow_units,
                                     mud_value, mud_units,
                                     pressure_value, pressure_units):
    mud_weight = dri.mud_weight(mud_value, mud_units)
    flow_rate = dri.flow_rate(flow_value, flow_units)
    pressure_drop = gen.pressure(pressure_value, pressure_units)
    btm_hole_force = ((flow_rate['gpm'] * 0.0173) *
                      ((pressure_drop['psi'] * mud_weight['ppg'])**0.5))
    return fap.force(btm_hole_force, 'lbf')


def specific_energy_friction(wob_value, wob_units, coef_value,
                             rotary_value, rotary_units,
                             rop_value, rop_units,
                             bit_value, dia_units):
    wob = gen.weight(wob_value, wob_units)
    rotary_speed = fap.angular_velocity(rotary_value, rotary_units)
    rop = dri.drilling_rate(rop_value, rop_units)
    bit_dia = gen.length(bit_value, dia_units)
    mechanical_specific_energy = (wob['lb'] *
                                  ((1.274 / (bit_dia['in']**2)) +
                                   (13.33 * coef_value * rotary_speed['rpm'] /
                                    (rop['ft/hr'] * bit_dia['in']))))
    return gen.pressure(mechanical_specific_energy, 'psi')


def specific_energy_torque(wob_value, wob_units, torque_value, torque_units,
                           rotary_value, rotary_units,
                           rop_value, rop_units,
                           bit_value, dia_units):
    wob = gen.weight(wob_value, wob_units)
    torque = gen.torque(torque_value, torque_units)
    rotary_speed = fap.angular_velocity(rotary_value, rotary_units)
    rop = dri.drilling_rate(rop_value, rop_units)
    bit_dia = gen.length(bit_value, dia_units)
    mechanical_specific_energy = ((480 * torque['ft-lb'] *
                                   rotary_speed['rpm'] /
                                   (rop['ft/hr'] * (bit_dia['in']**2))) +
                                  (1.274 * wob['lb'] / (bit_dia['in']**2)))
    return gen.pressure(mechanical_specific_energy, 'psi')


def pdc_minimum_flow(bit_value, dia_units):
    bit_dia = gen.length(bit_value, dia_units)
    return dri.flow_rate(12.72 * bit_dia['in']**1.47, 'gpm')


def power_law_constants(reading_300, reading_3):
    power_law_n = 0.5 * math.log(reading_300 / reading_3, 10)
    power_law_k = (5.11 * reading_300) / (511**power_law_n)
    power_law_dict = flu.viscocity(power_law_k * 100, 'cp')
    power_law_dict['poise'] = power_law_k
    return {'power_law_n': power_law_n,
            'power_law_k': power_law_dict}


def pressure_drop_across_bit_flow_rate(mud_value, mud_units,
                                       flow_value, flow_units,
                                       nozzle_value, nozzle_unit):
    mud_weight = dri.mud_weight(mud_value, mud_units)
    flow_rate = dri.flow_rate(flow_value, flow_units)
    nozzle_area = gen.area(nozzle_value, nozzle_unit)
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
            'pressure_loss': gen.pressure(pressure_loss, 'psi')}


def pressure_loss_annulus_corrected(pipe_value, collar_value, length_units,
                                    pipe_od_value, tj_od_value,
                                    collar_od_value, hole_id_value,
                                    dia_units, mud_value, mud_units,
                                    viscosity_value, viscosity_units,
                                    flow_value, flow_units):
    pipe = gen.length(pipe_value, length_units)
    collar = gen.length(collar_value, length_units)
    pipe_od = gen.length(pipe_od_value, dia_units)
    tj_od = gen.length(tj_od_value, dia_units)
    collar_od = gen.length(collar_od_value, dia_units)
    hole_id = gen.length(hole_id_value, dia_units)
    mud_weight = dri.mud_weight(mud_value, mud_units)
    viscosity = flu.viscosity(viscosity_value, viscosity_units)
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
    coefficient_pipe = ((8.17 * b_param) /
                        ((hole_id['in'] - pipe_od['in']) *
                         ((hole_id['in']**2 - pipe_od['in']**2)**2)) +
                        (0.43 * b_param) /
                        ((hole_id['in'] - tj_od['in']) *
                         ((hole_id['in']**2 - tj_od['in']**2)**2)))
    coefficient_collar = ((8.6 * b_param) /
                          ((hole_id['in'] - collar_od['in']) *
                           ((hole_id['in']**2 - collar_od['in']**2)**2)))
    pressure_loss_pipe = (0.00001 * pipe['ft'] *
                          coefficient_pipe * mud_weight['ppg'] *
                          ((viscosity['cp'] / mud_weight['ppg'])**0.14) *
                          (flow_rate['gpm']**1.86))
    pressure_loss_collar = (0.00001 * collar['ft'] *
                            coefficient_collar * mud_weight['ppg'] *
                            ((viscosity['cp'] / mud_weight['ppg'])**0.14) *
                            (flow_rate['gpm']**1.86))
    total_pressure_loss = pressure_loss_collar + pressure_loss_pipe
    return {'pressure_loss_pipe':
            gen.pressure(pressure_loss_pipe, 'psi'),
            'pressure_loss_collar':
            gen.pressure(pressure_loss_collar, 'psi'),
            'total_pressure_loss':
            gen.pressure(total_pressure_loss, 'psi')}


def pressure_loss_drillstring(pipe_value, collar_value, length_units,
                              pipe_id_value, collar_id_value, dia_units,
                              mud_value, mud_units, viscosity_value,
                              viscosity_units, flow_value, flow_units):
    pipe = gen.length(pipe_value, length_units)
    collar = gen.length(collar_value, length_units)
    pipe_id = gen.length(pipe_id_value, dia_units)
    collar_id = gen.length(collar_id_value, dia_units)
    mud_weight = dri.mud_weight(mud_value, mud_units)
    viscosity = flu.viscosity(viscosity_value, viscosity_units)
    flow_rate = dri.flow_rate(flow_value, flow_units)
    coefficient_pipe = 6.1 / (pipe_id['in']**4.86)
    coefficient_collar = 6.1 / (collar_id['in']**4.86)
    pressure_loss_pipe = (0.00001 * pipe['ft'] * coefficient_pipe *
                          mud_weight['ppg'] *
                          ((viscosity['cp'] / mud_weight['ppg'])**0.14) *
                          (flow_rate['gpm']**1.86))
    pressure_loss_collar = (0.00001 * collar['ft'] * coefficient_collar *
                            mud_weight['ppg'] *
                            ((viscosity['cp'] / mud_weight['ppg'])**0.14) *
                            (flow_rate['gpm']**1.86))
    total_pressure_loss = pressure_loss_collar + pressure_loss_pipe
    return {'pressure_loss_pipe':
            gen.pressure(pressure_loss_pipe, 'psi'),
            'pressure_loss_collar':
            gen.pressure(pressure_loss_collar, 'psi'),
            'total_pressure_loss':
            gen.pressure(total_pressure_loss, 'psi')}


def pressure_loss_drillstring_corrected(pipe_value, collar_value, length_units,
                                        pipe_id_value, tj_id_value,
                                        collar_id_value, dia_units,
                                        mud_value, mud_units,
                                        viscosity_value, viscosity_units,
                                        flow_value, flow_units):
    pipe = gen.length(pipe_value, length_units)
    collar = gen.length(collar_value, length_units)
    pipe_id = gen.length(pipe_id_value, dia_units)
    tj_id = gen.length(tj_id_value, dia_units)
    collar_id = gen.length(collar_id_value, dia_units)
    mud_weight = dri.mud_weight(mud_value, mud_units)
    viscosity = flu.viscosity(viscosity_value, viscosity_units)
    flow_rate = dri.flow_rate(flow_value, flow_units)
    coefficient_pipe = (5.68 / (pipe_id['in']**4.86) +
                        (0.41 / (tj_id['in']**4.86)))
    coefficient_collar = 7.2 / (collar_id['in']**4.86)
    pressure_loss_pipe = (0.00001 * pipe['ft'] * coefficient_pipe *
                          mud_weight['ppg'] *
                          ((viscosity['cp'] /
                            mud_weight['ppg'])**0.14) *
                          (flow_rate['gpm']**1.86))
    pressure_loss_collar = (0.00001 * collar['ft'] * coefficient_collar *
                            mud_weight['ppg'] *
                            ((viscosity['cp'] / mud_weight['ppg'])**0.14) *
                            (flow_rate['gpm']**1.86))
    total_pressure_loss = pressure_loss_pipe + pressure_loss_collar
    print(pressure_loss_pipe, pressure_loss_collar, total_pressure_loss)
    return {'pressure_loss_pipe':
            gen.pressure(pressure_loss_pipe, 'psi'),
            'pressure_loss_collar':
            gen.pressure(pressure_loss_collar, 'psi'),
            'total_pressure_loss':
            gen.pressure(total_pressure_loss, 'psi')}


def pressure_loss_surface_equipment(coefficient, mud_value, mud_units,
                                    viscosity_value, viscosity_units,
                                    flow_value, flow_units):
    mud_weight = dri.mud_weight(mud_value, mud_units)
    viscosity = flu.viscosity(viscosity_value, viscosity_units)
    flow_rate = dri.flow_rate(flow_value, flow_units)
    pressure_loss = (0.00001 * coefficient * mud_weight['ppg'] *
                     (viscosity['cp'] / mud_weight['ppg'])**1.4 *
                     flow_rate['gpm']**1.86)
    return gen.pressure(pressure_loss, 'psi')


def optimum_flow_rate(coefficient, depth_value, collar_value, depth_units,
                      hole_id_dia, pipe_od_dia, pipe_id_dia, tj_od_dia,
                      tj_id_dia, collar_od_dia, collar_id_dia, dia_units,
                      mud_value, mud_units, viscosity_value, viscosity_units,
                      yield_value, yield_units, reading_3, reading_300,
                      reading_600, pressure_value, pressure_units):
    depth = gen.length(depth_value, depth_units)
    collar = gen.length(collar_value, depth_units)
    hole_id = gen.length(hole_id_dia, dia_units)
    pipe_od = gen.length(pipe_od_dia, dia_units)
    pipe_id = gen.length(pipe_id_dia, dia_units)
    tj_od = gen.length(tj_od_dia, dia_units)
    tj_id = gen.length(tj_id_dia, dia_units)
    collar_od = gen.length(collar_od_dia, dia_units)
    collar_id = gen.length(collar_id_dia, dia_units)
    mud_weight = dri.mud_weight(mud_value, mud_units)
    viscosity = flu.viscosity(viscosity_value, viscosity_units)
    yield_point = flu.fluid_yield_point(yield_value, yield_units)
    pressure = gen.pressure(pressure_value, pressure_units)
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
    cpa = ((8.17 * b_param) / ((hole_id['in'] - pipe_od['in']) *
                               (hole_id['in']**2 - pipe_od['in']**2)**2) +
           (0.43 * b_param) / ((hole_id['in'] - tj_od['in']) *
                               (hole_id['in']**2 - tj_od['in']**2)**2))
    cpb = (5.68 / pipe_id['in']**4.86) + (0.41 / tj_id['in']**4.86)
    cp = cpa + cpb
    ccb = 7.2 / (collar_id['in']**4.86)
    cca = ((8.6 * b_param) / ((hole_id['in'] - collar_od['in']) *
                              (hole_id['in']**2 - collar_od['in']**2)**2))
    cc = cca + ccb
    vf = (viscosity['cp'] / mud_weight['ppg'])**0.14
    max_hydraulic_horsepower = (((0.35 * pressure['psi']) /
                                 (0.00001 *
                                  (coefficient +
                                   ((depth['ft'] - collar['ft']) * cp) +
                                   (collar['ft'] * cc)) * mud_weight['ppg'] *
                                  (vf)))**(1 / 1.86))
    max__impact_force = (((0.52 * pressure['psi']) /
                          (0.00001 *
                           (coefficient +
                            ((depth['ft'] - collar['ft']) * cp) +
                            (collar['ft'] * cc)) *
                           mud_weight['ppg'] * (vf)))**(1 / 1.86))
    return {'max_hydraulic_horsepower':
            dri.flow_rate(max_hydraulic_horsepower, 'gpm'),
            'pressure_loss':
            dri.flow_rate(max__impact_force, 'gpm')}


def reynold_number(annular_value, annular_units,
                   hole_id_value, pipe_od_value, dia_units,
                   mud_value, mud_units,
                   viscosity_value, viscosity_units, power_law_value):
    annular_velocity = fap.velocity(annular_value, annular_units)
    hole_id = gen.length(hole_id_value, dia_units)
    pipe_od = gen.length(pipe_od_value, dia_units)
    mud_weight = dri.mud_weight(mud_value, mud_units)
    viscocity = flu.viscocity(viscosity_value, viscosity_units)
    reynold_number = ((928 * annular_velocity['ft/s'] *
                       (hole_id['in'] - pipe_od['in']) *
                       mud_weight['ppg']) /
                      (viscocity['cp'] *
                       (((2 * power_law_value) + 1) /
                        (3 * power_law_value))**power_law_value))
    flow_regime = 'Laminar Flow'
    if 2100  < reynold_number < 4000:
        flow_regime = 'Transitional Flow'
    elif reynold_number > 4000:
        flow_regime = 'Turbulent Flow'
    return {'reynold_number': reynold_number,
            'flow_regime': flow_regime
    }


def surge_swab_one(reading_300, reading_600, hole_id_value, collar_od_value,
                   collar_id_value, pipe_od_value, pipe_id_value, dia_units,
                   pipe_speed, speed_units, pipe_value, collar_value,
                   tvd_value, length_units, mud_value, mud_units, pipe_state):
    pipe = gen.length(pipe_value, length_units)
    collar = gen.length(collar_value, length_units)
    tvd = gen.length(tvd_value, length_units)
    hole_id = gen.length(hole_id_value, dia_units)
    pipe_od = gen.length(pipe_od_value, dia_units)
    pipe_id = gen.length(pipe_id_value, dia_units)
    collar_od = gen.length(collar_od_value, dia_units)
    collar_id = gen.length(collar_id_value, dia_units)
    mud_weight = dri.mud_weight(mud_value, mud_units)
    pipe_speed = fap.velocity(pipe_speed, speed_units)
    n = 3.32 * math.log10(reading_600 / reading_300)
    K = reading_300 / (511**n)
    fluid_velocity_pipe = 0
    fluid_velocity_collar = 0
    if pipe_state == 'closed':
        fluid_velocity_pipe = ((0.45 +
                                ((pipe_od['in']**2) /
                                 (hole_id['in']**2 -
                                  pipe_od['in']**2))) *
                               pipe_speed['ft/min'])
        fluid_velocity_collar = ((0.45 +
                                  ((collar_od['in']**2) /
                                   (hole_id['in']**2 -
                                    collar_od['in']**2))) *
                                 pipe_speed['ft/min'])
    elif pipe_state == 'open':
        fluid_velocity_pipe = ((0.45 +
                                ((pipe_od['in']**2 - pipe_id['in']**2) /
                                 (hole_id['in']**2 - pipe_od['in']**2 +
                                  pipe_id['in']**2))) * pipe_speed['ft/min'])
        fluid_velocity_collar = ((0.45 +
                                  ((collar_od['in']**2 - collar_id['in']**2) /
                                   (hole_id['in']**2 - collar_od['in']**2 +
                                    collar_id['in']**2))) *
                                 pipe_speed['ft/min'])
    max_pipe_velocity = fluid_velocity_pipe * 1.5
    max_collar_velocity = fluid_velocity_collar * 1.5
    pressure_loss_pipe = (((2.4 * max_pipe_velocity /
                            (hole_id['in'] - pipe_od['in']) *
                            ((2 * n + 1)/(3 * n)))**n) *
                          (K * pipe['ft']/(300 *
                                           (hole_id['in'] - pipe_od['in']))))
    pressure_loss_collar = (((2.4 * max_collar_velocity /
                              (hole_id['in'] - collar_od['in']) *
                              ((2 * n + 1) / (3 * n)))**n) *
                            (K * collar['ft'] /
                             (300 * (hole_id['in'] - collar_od['in']))))
    pressure_loss = pressure_loss_collar + pressure_loss_pipe
    surge_bhp = (0.052 * tvd['ft'] * mud_weight['ppg']) + pressure_loss
    swab_bhp = (0.052 * tvd['ft'] * mud_weight['ppg']) - pressure_loss
    return {'surge_bhp':
            gen.pressure(surge_bhp, 'psi'),
            'surge_bhp_mud_weight':
            dri.mud_weight(surge_bhp / (0.052 * tvd['ft']), 'ppg'),
            'swab_bhp':
            gen.pressure(swab_bhp, 'psi'),
            'swab_bhp_mud_weight':
            dri.mud_weight(swab_bhp / (0.052 * tvd['ft']), 'ppg')}


def surge_swab_two(reading_300, reading_600, hole_id_value, collar_od_value,
                   pipe_od_value, dia_units, pipe_speed, speed_units,
                   pipe_value, collar_value, tvd_value, length_units,
                   mud_value, mud_units):
    pipe = gen.length(pipe_value, length_units)
    collar = gen.length(collar_value, length_units)
    tvd = gen.length(tvd_value, length_units)
    hole_id = gen.length(hole_id_value, dia_units)
    pipe_od = gen.length(pipe_od_value, dia_units)
    collar_od = gen.length(collar_od_value, dia_units)
    mud_weight = dri.mud_weight(mud_value, mud_units)
    pipe_speed = fap.velocity(pipe_speed, speed_units)
    pv = reading_600 - reading_300
    n = 3.32 * math.log10(reading_600 / reading_300)
    K = reading_300 / (511**n)
    fluid_velocity_pipe = ((0.45 +
                            ((pipe_od['in']**2) /
                             (hole_id['in']**2 - pipe_od['in']**2))) *
                           pipe_speed['ft/min'])
    fluid_velocity_collar = ((0.45 +
                              ((collar_od['in']**2) /
                               (hole_id['in']**2 - collar_od['in']**2))) *
                             pipe_speed['ft/min'])
    max_pipe_velocity = fluid_velocity_pipe * 1.5
    max_collar_velocity = fluid_velocity_collar * 1.5
    sheer_rate = (2.4 * max_pipe_velocity) / (hole_id['in'] - pipe_od['in'])
    sheer_stress = K * (sheer_rate)**n
    equivalent_flow = (max_collar_velocity *
                       (hole_id['in']**2 - collar_od['in']**2) / 24.5)
    pressure_loss_pipe = ((3.33 * sheer_stress /
                           (hole_id['in'] - pipe_od['in']) *
                           pipe['ft'] / 1000))
    pressure_loss_collar = ((0.000077 *
                             mud_weight['ppg']**0.8 *
                             equivalent_flow**1.8 * pv**0.2 *
                             collar['ft']) /
                            ((hole_id['in'] - collar_od['in'])**3 *
                             (hole_id['in'] + collar_od['in'])**1.8))
    pressure_loss = pressure_loss_collar + pressure_loss_pipe
    surge_bhp = (0.052 * tvd['ft'] * mud_weight['ppg']) + pressure_loss
    swab_bhp = (0.052 * tvd['ft'] * mud_weight['ppg']) - pressure_loss
    return {'surge_bhp':
            gen.pressure(surge_bhp, 'psi'),
            'surge_bhp_mud_weight':
            dri.mud_weight(surge_bhp / (0.052 * tvd['ft']), 'ppg'),
            'swab_bhp':
            gen.pressure(swab_bhp, 'psi'),
            'swab_bhp_mud_weight':
            dri.mud_weight(swab_bhp / (0.052 * tvd['ft']), 'ppg')}


def tfa_table(nozzle_size, nozzle_count):
    nozzle_matrix = [
        [0.0376, 0.0752, 0.1127, 0.1503,
         0.1879, 0.2255, 0.2631, 0.3007, 0.3382],
        [0.0491, 0.0982, 0.1473, 0.1963, 0.2454,
         0.2945, 0.3436, 0.3927, 0.4418],
        [0.0621, 0.1243, 0.1864, 0.2485, 0.3106,
         0.3728, 0.4349, 0.4970, 0.5591],
        [0.0767, 0.1534, 0.2301, 0.3068, 0.3835,
         0.4602, 0.5369, 0.6136, 0.6903],
        [0.0928, 0.1856, 0.2784, 0.3712, 0.4640,
         0.5568, 0.6496, 0.7424, 0.8353],
        [0.1104, 0.2209, 0.3313, 0.4418, 0.5522,
         0.6627, 0.7731, 0.8836, 0.9940],
        [0.1296, 0.2592, 0.3889, 0.5185, 0.6481,
         0.7777, 0.9073, 1.0370, 1.1666],
        [0.1503, 0.3007, 0.4510, 0.6013, 0.7517,
         0.9020, 1.0523, 1.2026, 1.3530],
        [0.1726, 0.3451, 0.5177, 0.6903, 0.8629,
         1.0354, 1.2080, 1.3806, 1.5532],
        [0.1963, 0.3927, 0.5890, 0.7854, 0.9817,
         1.1781, 1.3744, 1.5708, 1.7671],
        [0.2217, 0.4433, 0.6650, 0.8866, 1.1083,
         1.3300, 1.5516, 1.7733, 1.9949],
        [0.2485, 0.4970, 0.7455, 0.9940, 1.2425,
         1.4910, 1.7395, 1.9880, 2.2365],
        [0.2769, 0.5538, 0.8307, 1.1075, 1.3844,
         1.6613, 1.9382, 2.2151, 2.4920],
        [0.3068, 0.6136, 0.9204, 1.2272, 1.5340,
         1.8408, 2.1476, 2.4544, 2.7612],
        [0.3382, 0.6765, 1.0147, 1.3530,
         1.6912, 2.0295, 2.3677, 2.7059, 3.0442],
        [0.3712, 0.7424, 1.1137, 1.4849,
         1.8561, 2.2273, 2.5986, 2.9698, 3.3410],
        [0.4057, 0.8115, 1.2172, 1.6230,
         2.0287, 2.4344, 2.8402, 3.2459, 3.6516],
        [0.4418, 0.8836, 1.3254, 1.7671,
         2.2089, 2.6507, 3.0925, 3.5343, 3.9761],
        [0.4794, 0.9587, 1.4381, 1.9175,
         2.3968, 2.8762, 3.3556, 3.8350, 4.3143],
        [0.5185, 1.0370, 1.5555, 2.0739,
         2.5924, 3.1109, 3.6294, 4.1479, 4.6664],
        [0.5591, 1.1183, 1.6774, 2.2365,
         2.7957, 3.3548, 3.9140, 4.4731, 5.0322],
        [0.6013, 1.2026, 1.8040, 2.4053,
         3.0066, 3.6079, 4.2092, 4.8106, 5.4119],
        [0.6450, 1.2901, 1.9351, 2.5802,
         3.2252, 3.8702, 4.5153, 5.1603, 5.8054],
        [0.6903, 1.3806, 2.0709, 2.7612,
         3.4515, 4.1417, 4.8320, 5.5223, 6.2126]]
    nozzle_list = nozzle_matrix[nozzle_size - 7]
    tfa = nozzle_list[nozzle_count - 1]
    return gen.area(tfa, 'in2')
