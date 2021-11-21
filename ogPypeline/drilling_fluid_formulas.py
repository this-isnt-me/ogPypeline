import drilling as dri
import fluid as flu
import general as gen


def bulk_density_cuttings(rw_value):
    mud_weight = 1 / (2 - (0.12 * rw_value))
    return dri.mud_weight(mud_weight, 'SG')


def decrease_oil_water_ratio(oil_vol, water_vol, mud_value, mud_units,
                             new_oil, new_water):
    mud_volume = gen.volume(mud_value, mud_units)
    original_oil = (oil_vol / (oil_vol + water_vol)) * 100
    original_water = (water_vol / (oil_vol + water_vol)) * 100
    water_added_per_100 = ((oil_vol * 100 / new_oil) - (oil_vol + water_vol))
    water_added_total = water_added_per_100 * mud_volume['bbl'] / 100
    return {'water_added_per_100': gen.volume(water_added_per_100, 'bbl'),
            'water_added_total': gen.volume(water_added_total, 'bbl')}


def retort_oil_water_ratio(oil_vol, water_vol):
    oil_percent = (oil_vol / (oil_vol + water_vol)) * 100
    water_percent = (water_vol / (oil_vol + water_vol)) * 100
    return {'oil_percent': oil_percent,
            'water_percent': water_percent}


def oil_water_density(oil_vol, water_vol,
                      oil_weight, water_weight, weight_units):
    oil_weight = dri.mud_weight(oil_weight, weight_units)
    water_weight = dri.mud_weight(water_weight, weight_units)
    final_density = (((oil_weight['ppg'] * oil_vol / 100) +
                      (water_weight['ppg'] * water_vol / 100)) /
                     ((water_vol + oil_vol) / 100))
    return dri.mud_weight(final_density, 'ppg')


def barite_increase(current_mud, new_mud, mud_units, mud_vol, vol_units):
    current_mud = dri.mud_weight(current_mud, mud_units)
    new_mud = dri.mud_weight(new_mud, mud_units)
    mud_volume = gen.volume(mud_vol, vol_units)
    sacks_per_100 = (1470 * (new_mud['ppg'] - current_mud['ppg']) /
                     (35 - new_mud['ppg']))
    total_sacks_wt = sacks_per_100 * (mud_volume['bbl'] / 100)
    volume_per_100 = (100 * (new_mud['ppg'] - current_mud['ppg']) /
                      (35 - new_mud['ppg']))
    total_sacks_vol = volume_per_100 * (mud_volume['bbl'] / 100)
    return {
        'per_100_bbl_mud': {
                            'weight_required':
                            gen.weight(sacks_per_100 * 100, 'lb'),
                            'volume_required':
                            flu.additive_volume(sacks_per_100, 'sack'),
                            'volume_increase':
                            gen.volume(volume_per_100, 'bbl')
                            },
        'total_mud': {
                            'weight_required':
                            gen.weight(total_sacks_wt * 100, 'lb'),
                            'volume_required':
                            flu.additive_volume(total_sacks_wt, 'sack'),
                            'volume_increase':
                            gen.volume(total_sacks_vol, 'bbl')
                            },
    }


def barite_starting_vol(current_mud, new_mud, mud_units, mud_vol, vol_units):
    current_mud = dri.mud_weight(current_mud, mud_units)
    new_mud = dri.mud_weight(new_mud, mud_units)
    final_volume = gen.volume(mud_vol, vol_units)
    starting_vol = (final_volume['bbl'] * (35 - new_mud['ppg']) /
                    (35 - current_mud['ppg']))
    return gen.volume(starting_vol, 'bbl')


def calcium_carbonate_increase(current_mud, new_mud, mud_units,
                               mud_vol, vol_units):
    current_mud = dri.mud_weight(current_mud, mud_units)
    new_mud = dri.mud_weight(new_mud, mud_units)
    mud_volume = gen.volume(mud_vol, vol_units)
    sacks_per_100 = (945 * (new_mud['ppg'] - current_mud['ppg']) /
                     (22.5 - new_mud['ppg']))
    total_sacks_wt = sacks_per_100 * (mud_volume['bbl'] / 100)
    volume_per_100 = (100 * (new_mud['ppg'] - current_mud['ppg']) /
                      (22.5 - new_mud['ppg']))
    total_sacks_vol = volume_per_100 * (mud_volume['bbl'] / 100)
    return {
        'per_100_bbl_mud': {
                            'weight_required':
                            gen.weight(sacks_per_100 * 100, 'lb'),
                            'volume_required':
                            flu.additive_volume(sacks_per_100, 'sack'),
                            'volume_increase':
                            gen.volume(volume_per_100, 'bbl')
                            },
        'total_mud': {
                            'weight_required':
                            gen.weight(total_sacks_wt * 100, 'lb'),
                            'volume_required':
                            flu.additive_volume(total_sacks_wt, 'sack'),
                            'volume_increase':
                            gen.volume(total_sacks_vol, 'bbl')
                            },
    }


def calcium_carbonate_starting_vol(current_mud, new_mud, mud_units,
                                   mud_vol, vol_units):
    current_mud = dri.mud_weight(current_mud, mud_units)
    new_mud = dri.mud_weight(new_mud, mud_units)
    final_volume = gen.volume(mud_vol, vol_units)
    starting_vol = (final_volume['bbl'] * (22.5 - new_mud['ppg']) /
                    (22.5 - current_mud['ppg']))
    return gen.volume(starting_vol, 'bbl')


def hematite_increase(current_mud, new_mud, mud_units, mud_vol, vol_units):
    current_mud = dri.mud_weight(current_mud, mud_units)
    new_mud = dri.mud_weight(new_mud, mud_units)
    mud_volume = gen.volume(mud_vol, vol_units)
    sacks_per_100 = (1680 * (new_mud['ppg'] - current_mud['ppg']) /
                     (40 - new_mud['ppg']))
    total_sacks_wt = sacks_per_100 * (mud_volume['bbl'] / 100)
    volume_per_100 = (100 * (new_mud['ppg'] - current_mud['ppg']) /
                      (40 - new_mud['ppg']))
    total_sacks_vol = volume_per_100 * (mud_volume['bbl'] / 100)
    return {
        'per_100_bbl_mud': {
                            'weight_required':
                            gen.weight(sacks_per_100 * 100, 'lb'),
                            'volume_required':
                            flu.additive_volume(sacks_per_100, 'sack'),
                            'volume_increase':
                            gen.volume(volume_per_100, 'bbl')
                            },
        'total_mud': {
                            'weight_required':
                            gen.weight(total_sacks_wt * 100, 'lb'),
                            'volume_required':
                            flu.additive_volume(total_sacks_wt, 'sack'),
                            'volume_increase':
                            gen.volume(total_sacks_vol, 'bbl')
                            },
    }


def hematite_starting_vol(current_mud, new_mud, mud_units, mud_vol, vol_units):
    current_mud = dri.mud_weight(current_mud, mud_units)
    new_mud = dri.mud_weight(new_mud, mud_units)
    final_volume = gen.volume(mud_vol, vol_units)
    starting_vol = (final_volume['bbl'] * (40 - new_mud['ppg']) /
                    (40 - current_mud['ppg']))
    return gen.volume(starting_vol, 'bbl')


def increase_oil_water_ratio(oil_vol, water_vol, mud_value, mud_units,
                             new_oil, new_water):
    mud_volume = gen.volume(mud_value, mud_units)
    original_oil = (oil_vol / (oil_vol + water_vol)) * 100
    original_water = (water_vol / (oil_vol + water_vol)) * 100
    oil_added_per_100 = (water_vol * 100 / new_water) - (oil_vol + water_vol)
    oil_added_total = oil_added_per_100 * mud_volume['bbl'] / 100
    return {'oil_added_per_100': gen.volume(oil_added_per_100, 'bbl'),
            'oil_added_total': gen.volume(oil_added_total, 'bbl')}


def fluid_mixing_limited_space(mud_one_value, mud_two_value, new_mud_value,
                               mud_units, mud_vol, vol_units):
    mud_one = dri.mud_weight(mud_one_value, mud_units)
    mud_two = dri.mud_weight(mud_two_value, mud_units)
    new_mud = dri.mud_weight(new_mud_value, mud_units)
    mud_vol = gen.volume(mud_vol, vol_units)
    mud_two_volume = (mud_vol['bbl'] / ((mud_two['ppg'] - new_mud['ppg']) /
                                        (new_mud['ppg'] - mud_one['ppg']) + 1))
    mud_one_volume = mud_vol['bbl'] - mud_two_volume
    return {'mud_one_volume': gen.volume(mud_one_volume, 'bbl'),
            'mud_two_volume': gen.volume(mud_two_volume, 'bbl')}


def fluid_mixing_unlimited_space(mud_one_value, mud_two_value, mud_units,
                                 mud_one_vol, mud_two_vol, vol_units):
    mud_one = dri.mud_weight(mud_one_value, mud_units)
    mud_two = dri.mud_weight(mud_two_value, mud_units)
    mud_one_vol = gen.volume(mud_one_vol, vol_units)
    mud_two_vol = gen.volume(mud_two_vol, vol_units)
    total_volume = mud_one_vol['bbl'] + mud_two_vol['bbl']
    final_mud_weight = ((mud_one['ppg'] * mud_one_vol['bbl'] + mud_two['ppg'] *
                         mud_two_vol['bbl']) / total_volume)
    return {'total_mud_volume': gen.volume(total_volume, 'bbl'),
            'final_mud_weight': dri.mud_weight(final_mud_weight, 'ppg')}


def plastic_viscosity_yield_point(reading_600, reading_300):
    plastic_viscosity = reading_600 - reading_300
    yield_point = reading_300 - plastic_viscosity
    return {'plastic_viscosity': flu.viscosity(plastic_viscosity, 'cp'),
            'yield_point': flu.fluid_yield_point(yield_point, 'lbf/100ft2')}


def mud_weight_reduction(mud_vol, vol_units, mud_one_value, mud_two_value,
                         mud_final_value, mud_units):
    mud_one = dri.mud_weight(mud_one_value, mud_units)
    mud_two = dri.mud_weight(mud_two_value, mud_units)
    mud_final = dri.mud_weight(mud_final_value, mud_units)
    mud_vol = gen.volume(mud_vol, vol_units)
    required_volume = (mud_vol['bbl'] * (mud_one['ppg'] - mud_final['ppg']) /
                       (mud_final['ppg'] - mud_two['ppg']))
    return gen.volume(required_volume, 'bbl')


def solids_density_retort(mud_density, water_density, oil_density,
                          density_units, water_volume,
                          oil_volume, solids_volume):
    mud = dri.mud_weight(mud_density, density_units)
    water = dri.mud_weight(water_density, density_units)
    oil = dri.mud_weight(oil_density, density_units)
    solids_density = (((100 * mud['ppg']) -
                       (water_volume * water['ppg'] +
                        oil_volume * oil['ppg'])) / solids_volume)
    return dri.mud_weight(solids_density, 'ppg')


# New
def squeeze_below_balance_above(casing_value, od_value, id_value,
                                diameter_units, depth_value, depth_units,
                                volume_beneath, volume_above,
                                line_volume, volume_units):
    casing_value = gen.length(casing_value, diameter_units)
    od_value = gen.length(od_value, diameter_units)
    id_value = gen.length(id_value, diameter_units)
    retainer_depth = gen.length(depth_value, depth_units)
    volume_beneath = gen.volume(volume_beneath, volume_units)
    volume_above = gen.volume(volume_above, volume_units)
    line_volume = gen.volume(line_volume, volume_units)
    stringer_volume = retainer_depth['ft'] * id_value['in']**2 / 1029.4
    toc_stinger = ((retainer_depth['ft'] -
                    (volume_above['bbl'] * 1029.4) /
                    (casing_value['in']**2 - od_value['in']**2 +
                     id_value['in']**2)))
    toc_without = ((retainer_depth['ft'] -
                    (volume_above['bbl'] * 1029.4) /
                    (casing_value['in']**2)))
    displace_balance = (toc_stinger * id_value['in']**2 / 1029.4)
    data = {'stringer_volume': gen.volume(stringer_volume, 'bbl'),
            'toc_with_stinger': gen.length(toc_stinger, 'ft'),
            'toc_without_stinger': gen.length(toc_without, 'ft'),
            'displace_balance': gen.volume(displace_balance, 'bbl')}
    steps = {}
    if stringer_volume > volume_above['bbl']:
        steps['steps'] = ('Step One: Pump Cement', 'Step Two: Displace',
                          'Step Three: Sting Out',
                          'Step Four: Displace to Balance Plug')
        steps['step_one'] = gen.volume(volume_above['bbl'] +
                                       volume_beneath['bbl'], 'bbl')
        steps['step_two'] = gen.volume(stringer_volume - volume_above['bbl'] +
                                       line_volume['bbl'], 'bbl')
        steps['step_three'] = 'Sting Out'
        steps['step_four'] = gen.volume(displace_balance -
                                        (stringer_volume -
                                         volume_above['bbl'] +
                                         line_volume['bbl']), 'bbl')
    elif stringer_volume < volume_above['bbl']:
        steps['steps'] = ('Step One: Pump Cement', 'Step Two: Sting Out',
                          'Step Three: Pump Cement',
                          'Step Four: Displace to Balance Plug')
        steps['step_one'] = gen.volume(stringer_volume +
                                       volume_beneath['bbl'], 'bbl')
        steps['step_two'] = 'Sting Out'
        steps['step_three'] = gen.volume(volume_above['bbl'] -
                                         stringer_volume, 'bbl')
        steps['step_four'] = gen.volume(displace_balance +
                                        line_volume['bbl'], 'bbl')
    return {'data': data,
            'pumping_steps': steps}


def cement_plug_balance_above(casing_value, od_value, id_value, diameter_units,
                              depth_value, depth_units, volume_above,
                              line_volume, volume_units):
    casing_value = gen.length(casing_value, diameter_units)
    od_value = gen.length(od_value, diameter_units)
    id_value = gen.length(id_value, diameter_units)
    retainer_depth = gen.length(depth_value, depth_units)
    volume_above = gen.volume(volume_above, volume_units)
    line_volume = gen.volume(line_volume, volume_units)
    stringer_volume = retainer_depth['ft'] * id_value['in']**2 / 1029.4
    toc_stinger = ((retainer_depth['ft'] - (volume_above['bbl'] * 1029.4) /
                    (casing_value['in']**2 - od_value['in']**2 +
                     id_value['in']**2)))
    toc_without = ((retainer_depth['ft'] - (volume_above['bbl'] * 1029.4) /
                    (casing_value['in']**2)))
    displace_balance = (toc_stinger * id_value['in']**2 / 1029.4)
    data = {'stringer_volume': gen.volume(stringer_volume, 'bbl'),
            'toc_with_stinger': gen.length(toc_stinger, 'ft'),
            'toc_without_stinger': gen.length(toc_without, 'ft'),
            'displace_balance': gen.volume(displace_balance, 'bbl')}
    steps = {
             'steps': ('Step One: Pump Cement', 'Step Two: Displace'),
             'step_one': gen.volume(volume_above['bbl'], 'bbl'),
             'step_two': gen.volume(displace_balance +
                                    line_volume['bbl'], 'bbl')}
    return {'data': data,
            'pumping_steps': steps}
