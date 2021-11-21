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

The function returns a dictionary with the dogleg severity and three subdictionaries of different depth units and values realting to the position of the survey. to see the range of depth units returned see the example code below or the Length units section under General Conversions. To see the range of dogleg severity units returned see the example code below or the Dogleg units section under Drilling Conversions.

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

Calculate Deviation from Vertical Function
------------

*departure_vertical(depth_value, depth_unit, angle_value, angle_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - depth_value
     - measured depth from kickoff point to tvd value (Integer or Float)
   * - depth_unit
     - depth units (String)
   * - angle_value
     - hole angle value (Integer or Float)
   * - angle_units
     - hole angle units (String)

This function calculates the horizontal deviation from the vertical. The function takes in two value inputs(Integers or Floats) and two units inputs(Strings). To see the range of depth units that can be input into the function see the Length units section under General Conversions. To see the range of angle units that can be input into the function see the Angle units section under General Conversions. The function returns a dictionary of different distance units and values, to see the range of distance units returned see the example code below or the Length units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   departure  = dir_for.departure_vertical(6000, 'ft', 20, 'deg')
   print(departure)
   # outputs the following dictionary:
   {
       'cm': 62548.66952050007, 
       'dm': 6254.866952050007, 
       'dam': 62.54866952050007, 
       'fath': 342.02035230880347, 
       'ft': 2052.12170342848, 
       'hm': 6.254866952050007, 
       'in': 24625.46044114176, 
       'km': 0.6254866952050007, 
       'league': 0.12948887948633708, 
       'm': 625.4866952050007, 
       'mi': 0.3886718506293541, 
       'mm': 625486.6952050007, 
       'nleague': 0.11266148151822356, 
       'nm': 0.3377792323843278, 
       'yd': 684.0404994054365
   }
   # Each key representing a different rate of penetration unit
   print(departure['ft'])
   # outputs the following float:
   2052.12170342848 

Calculate True Vertical Depth Increase Function
------------

*new_tvd(tvd, depth_one, depth_two, depth_unit, angle_value, angle_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - tvd
     - survey one tvd value (Integer or Float)
   * - depth_one
     - survey one measured depth value (Integer or Float)
   * - depth_two
     - survey two measured depth value (Integer or Float)
   * - depth_unit
     - depth units (String)
   * - angle_value
     - hole angle value (Integer or Float)
   * - angle_units
     - hole angle units (String)

This function calculates the new true vertical depth between surveys. The function takes in four value inputs(Integers or Floats) and two units inputs(Strings). To see the range of depth units that can be input into the function see the Length units section under General Conversions. To see the range of angle units that can be input into the function see the Angle units section under General Conversions. The function returns a dictionary of different depth units and values, to see the range of depth units returned see the example code below or the Length units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   new_tvd  = dir_for.new_tvd(8500, 8500, 8530, 'ft', 40, 'deg')
   print(new_tvd)
   # outputs the following dictionary:
   {
       'cm': 259780.47086292735,
       'dm': 25978.047086292736,
       'dam': 259.78047086292736,
       'fath': 1420.4971720200215,
       'ft': 8522.981327523863,
       'hm': 25.978047086292733,
       'in': 102275.77593028636,
       'km': 2.5978047086292735,
       'league': 0.5378001217667557,
       'm': 2597.8047086292736,
       'mi': 1.6142526634330197,
       'mm': 2597804.7086292733,
       'nleague': 0.46791167488106006,
       'nm': 1.4028827265104278,
       'yd': 2840.99349174191
   }
   # Each key representing a different rate of penetration unit
   print(new_tvd['ft'])
   # outputs the following float:
   8522.981327523863 

Calculate Available Weight On Bit Function
------------

*directional_available_wob(weight, weight_unit, angle_value, angle_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - weight
     - drill collar weight value (Integer or Float)
   * - weight_unit
     - weight units (String)
   * - angle_value
     - hole angle value (Integer or Float)
   * - angle_units
     - hole angle units (String)

This function calculates the available weight that can be trandfered to the bit in a directional well. The function takes in two value inputs(Integers or Floats) and two units inputs(Strings). To see the range of weight units that can be input into the function see the Weight units section under General Conversions. To see the range of angle units that can be input into the function see the Angle units section under General Conversions. The function returns a dictionary of different depth units and values, to see the range of depth units returned see the example code below or the Length units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   available_wob  = dir_for.directional_available_wob(45000, 'lb', 25, 'deg')
   print(available_wob)
   # outputs the following dictionary:
   {
       'ct': 92496208.77537753,
       'cg': 1849924175.5075502,
       'dg': 184992417.55075505,
       'dram': 10440664.767685268,
       'gr': 285486972.0808121,
       'g': 18499241.755075503,
       'kg': 18499.242978590908,
       'kip': 40.783846860288904,
       't_long': 18.205909238432966,
       't_metric': 18.499552935827047,
       'mg': 18499241755.075504,
       'oz': 652541.5497646225,
       'lb': 40783.846860288904,
       'slug': 1267.6027442646396,
       't_short': 20.391923430144452,
       'toz': 594764.4320197516,
       'KdaN': 16.458022328868974,
       'daN': 16458.022241018254
   }
   # Each key representing a different rate of penetration unit
   print(available_wob['lb'])
   # outputs the following float:
   40783.846860288904