import drilling as dri
import force_and_power as fap
import fluid as flu
import gas as gas
import general as gen


def vooip(area_value, area_units, depth_value, depth_units,
          porosity_value, saturation_value):
    area = gen.area(area_value, area_units)
    depth = gen.length(depth_value, depth_units)
    oil_volume = (7758 * area['acre'] * depth['ft'] *
                  porosity_value * (1 - saturation_value))
    return gen.volume(oil_volume, 'bbl')


def vogip(area_value, area_units, depth_value, depth_units,
          porosity_value, saturation_value):
    area = gen.area(area_value, area_units)
    depth = gen.length(depth_value, depth_units)
    gas_volume = (43560 * area['acre'] * depth['ft'] *
                  porosity_value * (1 - saturation_value))
    return gen.gas_volume(gas_volume, 'ft3')


def stoip(area_value, area_units, depth_value, depth_units, porosity_value,
          saturation_value, formation_factor):
    area = gen.area(area_value, area_units)
    depth = gen.length(depth_value, depth_units)
    oil_volume = (((7758 * area['acre'] * depth['ft'] * porosity_value *
                    (1 - saturation_value)) / formation_factor))
    return gen.volume(oil_volume, 'bbl')


def stgoip(area_value, area_units, depth_value, depth_units, porosity_value,
           saturation_value, formation_factor):
    area = gen.area(area_value, area_units)
    depth = gen.length(depth_value, depth_units)
    gas_volume = (((43560 * area['acre'] * depth['ft'] * porosity_value *
                    (1 - saturation_value)) / formation_factor))
    return gas.gas_volume(gas_volume, 'ft3')


def porosity_pore_vol(pore_vol_value, bulk_vol_value, vol_units):
    pore_vol = gen.volume(pore_vol_value, vol_units)
    bulk_vol = gen.volume(bulk_vol_value, vol_units)
    porosity = (pore_vol['cm3'] / bulk_vol['cm3'])
    return {'decimal': porosity,
            'perc': porosity * 100}


def porosity_matrix_vol(matrix_vol_value, bulk_vol_value, vol_units):
    matrix_vol = gen.volume(matrix_vol_value, vol_units)
    bulk_vol = gen.volume(bulk_vol_value, vol_units)
    porosity = ((bulk_vol['cm3'] - matrix_vol['cm3']) /
                bulk_vol['cm3'])
    return {'decimal': porosity,
            'perc': porosity * 100}


def porosity_matrix_density(bulk_vol_value, vol_units,
                            weight_value, weight_units,
                            density_value, density_units):
    bulk_vol = gen.volume(bulk_vol_value, vol_units)
    weight = gen.weight(weight_value, weight_units)
    density = gen.density(density_value, density_units)
    porosity = (bulk_vol['cm3'] - (weight['g'] /
                                   density['g/cm3'])) / bulk_vol['cm3']
    return {'decimal': porosity,
            'perc': porosity * 100}


# def permeability_flow(permeability_value, permeability_unit,
#                       area_value, area_units,
#                       pressure_in_value, pressure_out_value, pressure_units,
#                       viscosity_value, viscosity_units,
#                       length_value, length_units):
#     perm = pr.permeability(permeability_value, permeability_unit)
#     area = gen.area(area_value, area_units)
#     pressure_in = gen.pressure(pressure_in_value, pressure_units)
#     pressure_out = gen.pressure(pressure_out_value, pressure_units)
#     viscosity = flu.Viscocity(viscosity_value, viscosity_units)
#     length = gen.length(length_value, length_units)
#     perm_flow = ((perm['darcy'] * area['cm2'] *
#                  (pressure_in['dyne/cm2'] - pressure_out['dyne/cm2'])) /
#                  ((viscosity['cp'] * 100) * length['cm']))
#     return 1


def capillary_number(fluid_value, fluid_units, velocity_value, velocity_units,
                     tension_value, tension_units):
    viscosity = flu.viscosity(fluid_value, fluid_units)
    velocity = dri.drilling_rate(velocity_value, velocity_units)
    tension = flu.surface_tension(tension_value, tension_units)
    return (viscosity['cp'] * velocity['ft/d']) / tension['dyn/cm']


def capillary_pressure_alpha(height_value, height_units,
                             oil_value, water_value, density_units):
    height = gen.length(height_value, height_units)
    oil_density = gen.density(oil_value, density_units)
    water_density = gen.density(water_value, density_units)
    capillary_pressure = ((water_density['kg/m3'] - oil_density['kg/m3']) *
                          9.81 * height['m'])
    return gen.pressure(capillary_pressure, 'N/m2')


def height_above_fwl(pressure_value, pressure_units,
                     oil_value, water_value, density_units):
    oil_density = gen.density(oil_value, density_units)
    water_density = gen.density(water_value, density_units)
    capillary_pressure = gen.pressure(pressure_value, pressure_units)
    height = ((0.1019367991845056 * capillary_pressure['N/m2']) /
              (water_density['kg/m3'] - oil_density['kg/m3']))
    return gen.length(height, 'm')


def resistivity_to_conductivity(resistivity_value, resistivity_units):
    resistivity = fap.resistivity(resistivity_value, resistivity_units)
    conductivity = 1000 / resistivity['ohm.m']
    return fap.conductivity(conductivity, 'mS/m')


def conductivity_to_resistivity(conductivity_value, conductivity_units):
    conductivity = fap.conductivity(conductivity_value, conductivity_units)
    resistivity = 1000 / conductivity['mS/m']
    return fap.resistivity(resistivity, 'ohm.m')


def archie_one(rock_resistivity, brine_resistivity, resistivity_units):
    rock = fap.resistivity(rock_resistivity, resistivity_units)
    brine = fap.resistivity(brine_resistivity, resistivity_units)
    return rock['ohm.m'] / brine['ohm.m']


def shale_clay_volume_gr(min_value, max_value, input_value):
    result_dict = {}
    dec_vol = (input_value - min_value)/(max_value - min_value)
    young = 0.083 * ((2**(3.71 * dec_vol)) - 1)
    old = 0.33 * ((2**(2 * dec_vol)) - 1)
    steiber = dec_vol / (3 - 2 * dec_vol)
    clavier = 1.7 - ((3.38-(dec_vol + 0.7)**2)**0.5)
    result_dict['linear'] = {'decimal': dec_vol,
                             'perc': dec_vol * 100}
    result_dict['larionov-young'] = {'decimal': young,
                                     'perc': young * 100}
    result_dict['larionov-old'] = {'decimal': old,
                                   'perc': old * 100}
    result_dict['steiber'] = {'decimal': steiber,
                              'perc': steiber * 100}
    result_dict['clavier'] = {'decimal': clavier,
                              'perc': clavier * 100}
    return result_dict


def shale_clay_volume_sp(min_value, max_value, input_value):
    result = (input_value - min_value)/(max_value - min_value)
    return {'decimal': result,
            'perc': result * 100}


def shale_clay_volume_porosity_logs(porosity_neutron, porosity_density,
                                    shale_porosity_neutron,
                                    shale_porosity_density, factor=0):
    result_dict = {}
    result = ((porosity_neutron - porosity_density) /
              (shale_porosity_neutron - shale_porosity_density))
    result_dict['shale'] = {'decimal': result,
                            'perc': result * 100}
    if factor > 0 and factor < 1:
        result = result * factor
        result_dict['clay'] = {'decimal': result,
                               'perc': result * 100}
    return result_dict


def PorosityPoreVol(pore_vol_value, bulk_vol_value, vol_units):
    pore_vol = gen.convertVolume(pore_vol_value, vol_units)
    bulk_vol = gen.convertVolume(bulk_vol_value, vol_units)
    porosity = (pore_vol['cm3'] / bulk_vol['cm3'])
    return {'decimal': porosity,
            'perc': porosity * 100}


def PorosityMatrixVol(matrix_vol_value, bulk_vol_value, vol_units):
    matrix_vol = gen.convertVolume(matrix_vol_value, vol_units)
    bulk_vol = gen.convertVolume(bulk_vol_value, vol_units)
    porosity = ((bulk_vol['cm3'] - matrix_vol['cm3']) / bulk_vol['cm3'])
    return {'decimal': porosity,
            'perc': porosity * 100}


def sonic_porosity(matrix_slowness, fluid_slowness,
                   log_slowness, slowness_units):
    result_dict = {}
    if slowness_units == 'us/m':
        matrix_slowness = matrix_slowness * 0.3048
        fluid_slowness = fluid_slowness * 0.3048
        log_slowness = log_slowness * 0.3048
    print(matrix_slowness, fluid_slowness, log_slowness)
    wyllie = ((log_slowness - matrix_slowness) /
              (fluid_slowness - matrix_slowness))
    alpha = (matrix_slowness / (2 * fluid_slowness)) - 1
    raymer = -alpha-((alpha**2 + (matrix_slowness / log_slowness)-1)**0.5)
    result_dict['wyllie'] = {'decimal': wyllie,
                             'perc': wyllie * 100}
    result_dict['raymer'] = {'decimal': raymer,
                             'perc': raymer * 100}
    return result_dict


def effective_porosity(total_porosity, clay_volume, clay_porosity):
    result = total_porosity - (clay_volume * clay_porosity)
    return {'decimal': result,
            'perc': result * 100}


def total_porosity(effective_porosity, clay_volume, clay_porosity):
    result = effective_porosity + (clay_volume * clay_porosity)
    return {'decimal': result,
            'perc': result * 100}


def shale_porosity(dry_shale_density, wet_shale_density,
                   water_density, density_units):
    dry = gen.density(dry_shale_density, density_units)
    wet = gen.density(wet_shale_density, density_units)
    water = gen.density(water_density, density_units)
    porosity = ((dry['g/cm3'] - wet['g/cm3']) / water['g/cm3'])
    return {'decimal': porosity,
            'perc': porosity * 100}
