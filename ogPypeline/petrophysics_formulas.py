import gas as gas
import general as gen


def VolumeOfOilInPlace(area_value, area_units, depth_value, depth_units,
                       porosity_value, saturation_value):
    area = gen.convertArea(area_value, area_units)
    depth = gen.convertLength(depth_value, depth_units)
    oil_volume = (7758 * area['acre'] * depth['ft'] * porosity_value *
                  (1 - saturation_value))
    return gen.convertVolume(oil_volume, 'bbl')


def VolumeOfGasInPlace(area_value, area_units, depth_value, depth_units,
                       porosity_value, saturation_value):
    area = gen.convertArea(area_value, area_units)
    depth = gen.convertLength(depth_value, depth_units)
    gas_volume = (43560 * area['acre'] * depth['ft'] * porosity_value *
                  (1 - saturation_value))
    return gen.convertGasVolume(gas_volume, 'ft3')


def STOOIP(area_value, area_units, depth_value, depth_units, porosity_value,
           saturation_value, formation_factor):
    area = gen.convertArea(area_value, area_units)
    depth = gen.convertLength(depth_value, depth_units)
    oil_volume = ((7758 * area['acre'] * depth['ft'] * porosity_value *
                   (1 - saturation_value)) / formation_factor)
    return gen.convertVolume(oil_volume, 'bbl')


def STGOIP(area_value, area_units, depth_value, depth_units, porosity_value,
           saturation_value, formation_factor):
    area = gen.convertArea(area_value, area_units)
    depth = gen.convertLength(depth_value, depth_units)
    gas_volume = ((43560 * area['acre'] * depth['ft'] *
                   porosity_value * (1 - saturation_value)) / formation_factor)
    return gas.convertGasVolume(gas_volume, 'ft3')


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
