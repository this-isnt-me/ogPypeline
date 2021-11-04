import drilling as dri
import general as gen
import math


def angle_averaging(depth, inc_one, inc_two, azi_one, azi_two):
    north = (depth * (math.sin(math.radians(inc_one + inc_two) / 2)) *
             (math.cos(math.radians(azi_one + azi_two) / 2)))
    east = (depth * (math.sin(math.radians(inc_one + inc_two) / 2)) *
            (math.sin(math.radians(azi_one + azi_two) / 2)))
    tvd = (depth * (math.cos(math.radians(inc_one + inc_two) / 2)))
    return {
        'north': gen.length(north, 'ft'),
        'east': gen.length(east, 'ft'),
        'tvd': gen.length(tvd, 'ft')
    }


def radius_of_curvature(depth, inc_one, inc_two, azi_one, azi_two):
    north = (((depth * (math.cos(math.radians(inc_one)) -
               math.cos(math.radians(inc_two))) *
               (math.sin(math.radians(azi_two)) -
                math.sin(math.radians(azi_one)))) /
              ((inc_two - inc_one) *
               (azi_two - azi_one))) *
             (180 / math.pi)**2)
    east = (((depth * (math.cos(math.radians(inc_one)) -
                       math.cos(math.radians(inc_two))) *
              (math.cos(math.radians(azi_one)) -
               math.cos(math.radians(azi_two)))) /
             ((inc_two - inc_one) * (azi_two - azi_one))) * (180 / math.pi)**2)
    tvd = ((depth * (math.sin(math.radians(inc_two)) -
                     math.sin(math.radians(inc_one))) /
            (inc_two - inc_one)) * (180 / math.pi))
    return {
        'north': gen.length(north, 'ft'),
        'east': gen.length(east, 'ft'),
        'tvd': gen.length(tvd, 'ft')
    }


def balanced_tangential(depth, inc_one, inc_two, azi_one, azi_two):
    north = ((depth / 2) * ((math.sin(math.radians(inc_one)) *
                             math.cos(math.radians(azi_one))) +
                            (math.sin(math.radians(inc_two)) *
                             math.cos(math.radians(azi_two)))))
    east = ((depth / 2) * ((math.sin(math.radians(inc_one)) *
                            math.sin(math.radians(azi_one))) +
                           (math.sin(math.radians(inc_two)) *
                            math.sin(math.radians(azi_two)))))
    tvd = ((depth / 2) * (math.cos(math.radians(inc_one)) +
                          math.cos(math.radians(inc_two))))
    return {
        'north': gen.length(north, 'ft'),
        'east': gen.length(east, 'ft'),
        'tvd': gen.length(tvd, 'ft')
    }


def tangential(depth, inc_one, inc_two, azi_one, azi_two):
    north = (depth * math.sin(math.radians(inc_two)) *
             math.cos(math.radians(azi_two)))
    east = (depth * math.sin(math.radians(inc_two)) *
            math.sin(math.radians(azi_two)))
    tvd = (depth * math.cos(math.radians(inc_two)))
    return {
        'north': gen.length(north, 'ft'),
        'east': gen.length(east, 'ft'),
        'tvd': gen.length(tvd, 'ft')
    }


def minimum_curvature(depth, inc_one, inc_two, azi_one, azi_two):
    dog_leg = math.acos(math.cos(math.radians(inc_two - inc_one)) -
                        math.sin(math.radians(inc_one)) *
                        math.sin(math.radians(inc_two)) *
                        (1 - math.cos(math.radians(azi_two - azi_one))))
    ratio_factor = (2 / dog_leg) * math.tan(dog_leg / 2)
    north = (depth / 2) * ratio_factor * (math.sin(math.radians(inc_one)) *
                                          math.cos(math.radians(azi_one)) +
                                          math.sin(math.radians(inc_two)) *
                                          math.cos(math.radians(azi_two)))
    east = (depth / 2) * ratio_factor * (math.sin(math.radians(inc_one)) *
                                         math.sin(math.radians(azi_one)) +
                                         math.sin(math.radians(inc_two)) *
                                         math.sin(math.radians(azi_two)))
    tvd = (depth / 2) * ratio_factor * (math.cos(math.radians(inc_one)) +
                                        math.cos(math.radians(inc_two)))
    return {
        'dog_leg': gen.angle(dog_leg, 'rad'),
        'ratio_factor': ratio_factor,
        'north': gen.length(north, 'ft'),
        'east': gen.length(east, 'ft'),
        'tvd': gen.length(tvd, 'ft')
    }


def dogleg_severity(depth, inc_one, inc_two, azi_one, azi_two):
    dog_leg = math.degrees(math.acos(
        (math.cos(math.radians(inc_one)) * math.cos(math.radians(inc_two))) +
        ((math.sin(math.radians(inc_one)) * math.sin(math.radians(inc_two))) *
         (math.cos(math.radians(azi_two - azi_one)))))) * (100 / depth)
    return dri.dogleg(dog_leg, 'deg/100ft')


def directional_survey(depth_one, depth_two, depth_unit,
                       inc_one, inc_two, azi_one, azi_two, angle_units,
                       calc_type='roc'):
    depth_one = gen.length(depth_one, depth_unit)
    depth_two = gen.length(depth_two, depth_unit)
    inc_one = gen.angle(inc_one, angle_units)
    inc_two = gen.angle(inc_two, angle_units)
    azi_one = gen.angle(azi_one, angle_units)
    azi_two = gen.angle(azi_two, angle_units)
    inc_one = inc_one['deg']
    inc_two = inc_two['deg']
    azi_one = azi_one['deg']
    azi_two = azi_two['deg']
    delta_depth = depth_two['ft'] - depth_one['ft']
    return_dict = {}
    if calc_type == 'aa':
        return_dict['angle_averaging'] = angle_averaging(delta_depth,
                                                         inc_one,
                                                         inc_two,
                                                         azi_one,
                                                         azi_two)
    elif calc_type == 'roc':
        return_dict['radius_of_curvature'] = radius_of_curvature(delta_depth,
                                                                 inc_one,
                                                                 inc_two,
                                                                 azi_one,
                                                                 azi_two)
    elif calc_type == 'bt':
        return_dict['balanced_tangential'] = balanced_tangential(delta_depth,
                                                                 inc_one,
                                                                 inc_two,
                                                                 azi_one,
                                                                 azi_two)
    elif calc_type == 'mc':
        return_dict['minimum_curvature'] = minimum_curvature(delta_depth,
                                                             inc_one,
                                                             inc_two,
                                                             azi_one,
                                                             azi_two)
    elif calc_type == 'tan':
        return_dict['tangential'] = tangential(delta_depth,
                                               inc_one,
                                               inc_two,
                                               azi_one,
                                               azi_two)
    elif calc_type == 'all':
        return_dict['angle_averaging'] = angle_averaging(delta_depth,
                                                         inc_one,
                                                         inc_two,
                                                         azi_one,
                                                         azi_two)
        return_dict['radius_of_curvature'] = radius_of_curvature(delta_depth,
                                                                 inc_one,
                                                                 inc_two,
                                                                 azi_one,
                                                                 azi_two)
        return_dict['balanced_tangential'] = balanced_tangential(delta_depth,
                                                                 inc_one,
                                                                 inc_two,
                                                                 azi_one,
                                                                 azi_two)
        return_dict['minimum_curvature'] = minimum_curvature(delta_depth,
                                                             inc_one,
                                                             inc_two,
                                                             azi_one,
                                                             azi_two)
        return_dict['tangential'] = tangential(delta_depth,
                                               inc_one,
                                               inc_two,
                                               azi_one,
                                               azi_two)
    return return_dict
