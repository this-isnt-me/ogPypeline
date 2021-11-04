Directional Drilling Formulas
==================

This module contains functions, outlined below, for formulas related todirectional drilling. 

Directional Drilling Function
------------

*directional_survey(depth_one, depth_two, depth_unit, inc_one, inc_two, azi_one, azi_two, angle_units, calc_type)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - depth_one
     - survey one depth value (Integer or Float)
   * - depth_two
     - survey two depth value (Integer or Float)
   * - depth_unit
     - depth units (String)
   * - inc_one
     - survey one inclination value (Integer or Float)
   * - inc_two
     - survey two inclination value (Integer or Float)
   * - azi_one
     - survey one azimuth value (Integer or Float)
   * - azi_two
     - survey two azimuth value (Integer or Float)
   * - angle_units
     - angle units (String)
   * - calc_type
     - calculation method (String)

This function calculates the North, East and TVD between surveys. The function takes in six value inputs(Integers or Floats) and three units inputs(Strings). To see the range of depth units that can be input into the function see the Length units section under General Conversions. To see the range of inclination and azimuth units that can be input into the function see the Angle units section under General Conversions. A number of different strings can be passed int as the calc_type input representing the different calulation methods, these are outlined in the table below, the default input is 'roc'.

.. list-table:: calc_type Inputs
   :widths: 70 30
   :header-rows: 1

   * - Calculation Method
     - Input String
   * - Angle Averaging
     - 'aa'
   * - Radius of Curvature
     - 'roc'
   * - Balanced Tangential
     - 'bt'
   * - Minimum Curvature
     - 'mc'
   * - Tangential
     - 'tan'
   * - All methods
     - 'all

The function returns a dictionary with three subdictionaries of different depth units and values, to see the range of depth units returned see the example code below or the Length units section under General Conversions. To see the range of dogleg severity units returned see the example code below or the Dogleg units section under Drilling Conversions.

.. code:: python

   # Example Code
   from ogPypeline import directional_formula as dir_for

   north_east_tvd  = dir_for.directional_survey(7500, 7595, 'ft', 45, 52, 130, 139, 'deg','roc')
   print(north_east_tvd)
   # outputs the following dictionary:
   {
       'dogleg_severity': 
          {
              'deg/100ft': 10.21677767051634,
              'deg/30m': 10.056378347800301
          },
       'radius_of_curvature': 
          {
              'north':  
                 {
                     'cm': -1517.538767738226,
                     'dm': -151.7538767738226,
                     'dam': -1.517538767738226,
                     'fath': -8.298004545308288,
                     'ft': -49.78801731424626,
                     'hm': -0.1517538767738226,
                     'in': -597.4562077709552,
                     'km': -0.01517538767738226,
                     'league': -0.0031416238925289393,
                     'm': -15.175387677382261,
                     'mi': -0.009429850479318241,
                     'mm': -15175.387677382261,
                     'nleague': -0.00273336215055212,
                     'nm': -0.008195107649924933,
                     'yd': -16.596004111814842
                 },
                 'east':  
                 {
                     'cm': 1544.2586691722277,
                     'dm': 154.42586691722278,
                     'dam': 1.5442586691722278,
                     'fath': 8.444110772222011,
                     'ft': 50.66465450040117,
                     'hm': 0.15442586691722276,
                     'in': 607.975854004814,
                     'km': 0.015442586691722276,
                     'league': 0.003196939698975314,
                     'm': 15.442586691722278,
                     'mi': 0.009595885562375981,
                     'mm': 15442.586691722277,
                     'nleague': 0.0027814895320720243,
                     'nm': 0.008339402130766033,
                     'yd': 16.888216477978574
                 },
                 'tvd':  
                 {
                     'cm': 1917.4895532680373,
                     'dm': 191.74895532680372,
                     'dam': 1.9174895532680372,
                     'fath': 10.484962471379855,
                     'ft': 62.90976224632668,
                     'hm': 0.19174895532680372,
                     'in': 754.9171469559201,
                     'km': 0.01917489553268037,
                     'league': 0.003969605997743214,
                     'm': 19.174895532680374,
                     'mi': 0.011915108969454273,
                     'mm': 19174.895532680373,
                     'nleague': 0.0034537459473233346,
                     'nm': 0.010354946865745372,
                     'yd': 20.969918651783484
                 }
          }
      }