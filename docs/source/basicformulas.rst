Basic Formulas
==================

This module contains 27 basic functions for formulas related to oil and gas, they are outlined below. 

Pressure Gradient Function
------------

pressure_gradient(value, units)

   #. value : mud weight (Integer or Float)
   #. units : mud weight units (String)

The pressure gradient function calculates the pressure gradient from the mud weight. The function takes in a value input(Integer or Float) and a units input(String). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. The function returns a dictionary of different pressure gradient units and values, to see the range of pressure gradient units returned see the example code below or the Pressure Gradients units section under Drilling Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   pressure_gradient  = bas_for.pressure_gradient(9.0, 'ppg')
   print(pressure_gradient)
   # outputs the following dictionary:
   {
	   'psi/ft': 0.46799999999999997,
       'kPa/m': 10.53,
       'Mpa/m': 0.01053,
       'Pa/m': 10530.0
   }
   # Each key representing a different pressure gradient unit
   print(pressure_gradient['psi/ft'])
   # outputs the following float:
   0.46799999999999997

Pressure To Mud Weight Function
------------

pressure_to_mud_weight(pressure_value, pressure_units, depth_value, depth_units)

   #. pressure_value : pressure (Integer or Float)
   #. pressure_units : pressure units (String)
   #. depth_value : depth value (Integer or Float)
   #. depth_units : depth units (String)

The pressure to mud weight function calculates the equivalent mud weight from pressure and depth. The function takes in two value inputs(Integers or Floats) and two units input(Strings). To see the range of pressure units that can be input into the function see the pressure units section under General Conversions. To see the range of depth units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary of different mud weight units and values, to see the range of mud weight units returned see the example code below or the Mud Weight units section under Drilling Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   mud_weight  = bas_for.pressure_to_mud_weight(5000,'psi', 8000,'ft')
   print(mud_weight)
   # outputs the following dictionary:
   {
       'g/cm3': 1.440221153846154,
       'g/L': 1440.221153846154,
       'kg/m3': 1440.221153846154,
       'kg/L': 1.440221153846154,
       'kPa/m': 14.13062139423077,
       'lb/ft3': 89.91828365384616,
       'lb/bbl': 504.8076923076923,
       'ppg': 12.01923076923077,
       'psi/ft': 0.625033653846154,
       'psi/100ft': 62.46621995192309,
       'SG': 1.440221153846154
   }
   # Each key representing a different mud weight unit
   print(mud_weight['ppg'])
   # outputs the following float:
   12.01923076923077

Hydrostatic Pressure Function
------------

hydrostatic_pressure(mud_value, mud_units, depth_value, depth_units)

   #. mud_value : mud weight (Integer or Float)
   #. mud_units : mud weight units (String)
   #. depth_value : true vertical depth value (Integer or Float)
   #. depth_units : true vertical depth units (String)
   
The hydrostatic pressure function calculates the hydrostatic pressure using the mud weight and true vertical depth(TVD). The function takes in two value inputs(Integers or Floats) and two units input(Strings).To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of depth units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary of different pressure units and values, to see the range of pressure units returned see the example code below or the Pressure units section under General Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   hydrostatic_pressure  = bas_for.hydrostatic_pressure(12.0, 'ppg', 10000, 'ft')
   print(hydrostatic_pressure)
   # outputs the following dictionary:
   {
       'atm': 424.6068140901525,
       'bar': 430.2328542934116,
       'cm_Hg': 32270.125775918106,
       'cm_h2o': 438716.7534960242,
       'dyne/cm2': 430344827.58620685,
       'ft_air': 11134903.64025696,
       'ft_hg': 1058.730746752318,
       'ft_h2o': 14393.550582143002,
       'in_air': 133618843.68308353,
       'in_hg': 12704.767667669339,
       'in_h2o': 172722.56714451397,
       'kg/cm2': 438.7154179144365,
       'kg/m2': 4387260.071714828,
       'kPa': 43023.296701478306,
       'Mpa': 43.02328551833168,
       'm_Hg': 322.70117932335427,
       'm_h2o': 4387.154271678606,
       'mbar': 430232.07711082615,
       'N/cm2': 4302.328483607094,
       'N/m2': 43034482.75862069,
       'N/mm2': 43.02328551833168,
       'Pa': 43034482.75862069,
       'psf': 898565.7508208052,
       'psi': 6240.0,
       'torr': 322701.179424
   }
   # Each key representing a different pressure unit
   print(hydrostatic_pressure['psi'])
   # outputs the following float:
   6240.0

Triplex Pump Output Function
------------

triplex_output(diameter_value, diameter_units, length_value, length_units, efficiency)

   #. diameter_value : liner diameter (Integer or Float)
   #. diameter_units : liner diameter units (String)
   #. length_value : stroke length  (Integer or Float)
   #. length_units : stroke length units (String)
   #. efficiency : efficiency (Float between 0.0 and 1.0)

The Triplex Pump Output function calculates pump output. The function takes in two value inputs(Integers or Floats) and two units input(Strings).To see the range of diameter and length units that can be input into the function see the Length units section under General Conversions. Efficiency is input as a float between 0.0 and 1.0, with the default option being 1.0 to represent 100% efficiency. The function returns a dictionary of stroke-volume units and values, to see the range of stroke-volume units returned see the example code below or the Stroke Volume units section under Production Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   triplex_output  = bas_for.triplex_output(152.4, 'mm', 304.8, 'mm', 0.95)
   print(triplex_output)
   # outputs the following dictionary:
   {
       'bbl/stk': 0.09969874073206572,
       'm3/stk': 0.01585545191225856,
       'gal/stk': 4.189023079580242,
       'L/stk': 15.85545191225856
   }
   # Each key representing a different stroke-volume unit
   print(triplex_output['m3/stk'])
   # outputs the following float:
   0.01585545191225856

Duplex Pump Output Function
------------

duplex_output(diameter_value, diameter_units, length_value, length_units, rod_value, rod_units, efficiency=1)

   #. diameter_value : liner diameter (Integer or Float)
   #. diameter_units : liner diameter units (String)
   #. length_value : stroke length (Integer or Float)
   #. length_units : stroke length units (String)
   #. rod_value : rod diameter (Integer or Float)
   #. rod_units : rod diameter units (String)
   #. efficiency : efficiency (Float between 0.0 and 1.0)

The Duplex Pump Output function calculates pump output. The function takes in three value inputs(Integers or Floats) and three units input(Strings).To see the range of liner diameter, rod diameter and length units that can be input into the function see the Length units section under General Conversions. Efficiency is input as a float between 0.0 and 1.0, with the default option being 1.0 to represent 100% efficiency. The function returns a dictionary of stroke-volume units and values, to see the range of stroke-volume units returned see the example code below or the Stroke Volume units section under Production Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   duplex_output  = bas_for.duplex_output(5.5, 'in', 14, 'in', 2, 'in', 0.95)
   print(duplex_output)
   # outputs the following dictionary:
   {
       'bbl/stk': 0.12169912796172896,
       'm3/stk': 0.01935425319309361,
       'gal/stk': 5.113409177017886,
       'L/stk': 19.35425319309361
   }
   # Each key representing a different stroke-volume unit
   print(duplex_output['m3/stk'])
   # outputs the following float:
   0.01935425319309361

Hydraulic Horsepower Function
------------

hydraulic_horsepower(pressure_value, pressure_units, circulating_value, circulating_units)

   #. pressure_value : pressure value (Integer or Float)
   #. pressure_units : pressure units (String)
   #. circulating_value : flow rate (Integer or Float)
   #. circulating_units : flow rate units (String)

The function takes in two value inputs(Integers or Floats) and two units input(Strings). To see the range of pressure units that can be input into the function see the pressure units section under General Conversions. To see the range of flow rate units(circulating_units) that can be input into the function see the flow rate units section under Drilling Conversions. The function returns the hyraulic horsepower as a dictionary with a single entry 'hhp'.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   hydraulic_horsepower  = bas_for.hydraulic_horsepower(3500 , 'psi', 800, 'gpm')
   print(hydraulic_horsepower)
   # outputs the following dictionary:
   {
       'hhp': 1633.6056009334889
   }

Suspended Drill Collar Weight Function
------------

drill_collar_in_air(od_value, id_value, diameter_units, dc_type)

   #. od_value : drill collar outer diameter value (Integer or Float)
   #. id_value : drill collar inner diameter value (Integer or Float)
   #. diameter_units : diameter units (String)
   #. dc_type : drill collar type (String 'reg' or 'spiral')

The function takes in two value inputs(Integers or Floats) and one units input(Strings). To see the range of diameter units that can be input into the function see the pressure units section under General Conversions. To see the range of diameter units that can be input into the function see the Length units section under General Conversions. Drill Collar type(dc_type) is input as a string, either 'reg' or 'spiral', with the default option being 'reg' for regular drill collar. The function returns a dictionary of weight-length units and values, to see the range of weight-length units returned see the example code below or the Weight Length units section under Drilling Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   drill_collar_in_air  = bas_for.drill_collar_in_air(8.0, 2.8125, 'in', dc_type='reg')
   print(drill_collar_in_air)
   # outputs the following dictionary:
   {
       'lb/ft': 149.198984375,
       'kg/m': 222.0319605875
   }
   # Each key representing a different stroke-volume unit
   print(drill_collar_in_air['lb/ft'])
   # outputs the following float:
   149.198984375

Capacity of Hole or Tubular Function
------------

hole_tubular_capacity(diameter_value, diameter_units, washout_value)

   #. diameter_value : inner diameter value of hole or tubular (Integer or Float)
   #. diameter_units : diameter units (string)
   #. washout_value : washout value of hole or tubular (Integer or Float)

The function takes in two value inputs(Integers or Floats) and one units input(Strings). To see the range of diameter units that can be input into the function see the pressure units section under General Conversions. To see the range of diameter units that can be input into the function see the Length units section under General Conversions. The washout is a decimal display of the percentage of washout in the hole, i.e. 20% washout is input into the function as 0.2, the default for washout is 0.0 . The function returns a dictionary containing the capacity in volume by length and in length by volume, To see the range of capacity units that can be returned, see the example code below or review the Pipe Capacity (Volume per Length) and the Pipe Capacity (Length per Volume) units section of Production Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   hole_tubular_capacity  = bas_for.hole_tubular_capacity(2.8125,'in',0.05)
   print(hole_tubular_capacity)
   # outputs the following dictionary:
   {
       'bbl/ft': 0.00847187416516903,
       'm3/m': 0.004419387045757085,
       'bbl/in': 0.0007059895137640856,
       'ft3/ft': 0.04756604348985526,
       'gal(us)/ft': 0.35581871493709927,
       'l/m': 4.419030040979765,
       'dm3/m': 4.419030040979765,
       'in3/ft': 82.19412315046993,
       'm/m3': 226.29400359955125,
       'ft/bbl': 118.03763612440862,
       'ft/ft3': 21.023400868169222,
       'ft/gal(us)': 2.8104199077240137
   }
   # Each key representing a different pipe capacity unit
   print(hole_tubular_capacity['ft/bbl'])
   # outputs the following float:
   118.03763612440862

Tubular Displacement Function
------------

tubular_displacement(od_value, id_value, diameter_units)

   #. od_value : outer diameter value of tubular (Integer or Float)
   #. id_value : inner diameter value of tubular (Integer or Float)
   #. diameter_units : diameter units (string)

The function is for the calculation of plain pipe such as casing or tubing that has no tool joints. It takes in two value inputs(Integers or Floats) and one units input(Strings). To see the range of diameter units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary containing the capacity in volume by length and in length by volume, To see the range of capacity units that can be returned, see the example code below or review the Pipe Capacity (Volume per Length) and the Pipe Capacity (Length per Volume) units section of Production Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   tubular_displacement  = bas_for.tubular_displacement(5, 4.276,'in')
   print(tubular_displacement)
   # outputs the following dictionary:
   {
       'bbl/ft': 0.006524017874489995,
       'm3/m': 0.0034032800202992036,
       'bbl/in': 0.0005436681562074994,
       'ft3/ft': 0.03662964202448027,
       'gal(us)/ft': 0.2740087507285798,
       'l/m': 3.403005098185973,
       'dm3/m': 3.403005098185973,
       'in3/ft': 63.29602141830193,
       'm/m3': 293.8579200287023,
       'ft/bbl': 153.27977624190268,
       'ft/ft3': 27.300294098743297,
       'ft/gal(us)': 3.6495184819500626
   }
   # Each key representing a different pipe capacity unit
   print(tubular_displacement['l/m'])
   # outputs the following float:
   3.403005098185973

Annular Capacity Function
------------

annular_capacity(od_value, id_value, diameter_units)

   #. od_value : outer diameter value of annulus (Integer or Float)
   #. id_value : inner diameter value of annulus (Integer or Float)
   #. diameter_units : diameter units (string)

The function is for the calculation of fluid in the annulus between two tubulars. It takes in two value inputs(Integers or Floats) and one units input(Strings). To see the range of diameter units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary containing the capacity in volume by length and in length by volume, To see the range of capacity units that can be returned, see the example code below or review the Pipe Capacity (Volume per Length) and the Pipe Capacity (Length per Volume) units section of Production Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   annular_capacity  = bas_for.annular_capacity(6.125, 3.5,'in')
   print(annular_capacity)
   # outputs the following dictionary:
   {
       'bbl/ft': 0.02454403050320575,
       'm3/m': 0.012803491688119291,
       'bbl/in': 0.002045335875267145,
       'ft3/ft': 0.13780450459612387,
       'gal(us)/ft': 1.0308492811346415,
       'l/m': 12.802457402673886,
       'dm3/m': 12.802457402673886,
       'in3/ft': 238.1261839421022,
       'm/m3': 78.11000408336783,
       'ft/bbl': 40.74310451453309,
       'ft/ft3': 7.256656833757274,
       'ft/gal(us)': 0.9700739170126922
   }
   # Each key representing a different pipe capacity unit
   print(annular_capacity['bbl/ft'])
   # outputs the following float:
   0.02454403050320575

Annular Capacity Multiple Tubulars Function
------------

annular_capacity_multiple_tubulars(od_value, id_array, diameter_units)

   #. od_value : outer diameter value of annulus (Integer or Float)
   #. id_array : a list of inner diameter value of annulus (list of Integers or Floats)
   #. diameter_units : diameter units (string)

The function is for the calculation of fluid in the annulus between tubulars. It takes in one value input(Integer or Float), a list of values(Integers or Floats) and one units input(Strings). To see the range of diameter units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary containing the capacity in volume by length and in length by volume, To see the range of capacity units that can be returned, see the example code below or review the Pipe Capacity (Volume per Length) and the Pipe Capacity (Length per Volume) units section of Production Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   annular_capacity  = bas_for.annular_capacity_multiple_tubulars(8.681, [2.125,3.5,5.5],'in')
   print(annular_capacity)
   # outputs the following dictionary:
   {
       'bbl/ft': 0.027534618224208267,
       'm3/m': 0.014363543735131138,
       'bbl/in': 0.0022945515186840212,
       'ft3/ft': 0.1545954085713359,
       'gal(us)/ft': 1.1564539654167472,
       'l/m': 14.36238342631917,
       'dm3/m': 14.36238342631917,
       'in3/ft': 267.1408660112686,
       'm/m3': 69.6263266560265,
       'ft/bbl': 36.31791775201757,
       'ft/ft3': 6.468497410377888,
       'ft/gal(us)': 0.8647123274289895
   }
   # Each key representing a different pipe capacity unit
   print(annular_capacity['bbl/ft'])
   # outputs the following float:
   0.027534618224208267

Cuttings Drilled Function
------------

cuttings_drilled(diameter_value, diameter_units, washout_value, porosity)

   #. diameter_value : outer diameter value of annulus (Integer or Float)
   #. diameter_units : a list of inner diameter value of annulus (list of Integers or Floats)
   #. washout_value : diameter units (string)
   #. porosity : porosity (Float between 0.0 and 1.0)

This function is for the calculation of the volume of cuttings produced while drilling. It takes in three value inputs(Integers or Floats) and one unit input(String). To see the range of diameter units that can be input into the function see the Length units section under General Conversions. The washout and porosity values are a decimal display of the percentage i.e. 20% is input into the function as 0.2. The function returns a dictionary containing the capacity in volume by length. To see the range of capacity units that can be returned, see the example code below or review the Pipe Capacity (Volume per Length) units section of Production Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   cuttings_drilled  = bas_for.cuttings_drilled(12.25,'in',0.1,0.2)
   print(cuttings_drilled)
   # outputs the following dictionary:
   {
       'bbl/ft': 0.14111181270643094,
       'm3/m': 0.07361154154556052,
       'bbl/in': 0.011759317725535907,
       'ft3/ft': 0.7922840317579817,
       'gal(us)/ft': 5.9266961336701,
       'l/m': 73.60559509377308,
       'dm3/m': 73.60559509377308,
       'in3/ft': 1369.066806877793
   }
   # Each key representing a different volume per length unit
   print(cuttings_drilled['ft3/ft'])
   # outputs the following float:
   0.7922840317579817

Annular Velocity from Annular Capacity Function
------------

annular_velocity_annular_capcity(output_value, output_units, annulus_value, annulus_units)

   #. output_value : pump output / flow rate value (Integer or Float)
   #. output_units : pump output / flow rate units (string)
   #. annulus_value : annular capacity value value (Integer or Float)
   #. annulus_units : annular capacity value units (string)

This function is for the calculation of annular velocity from the annular capacity and flow rate. It takes in two value inputs(Integers or Floats) and two unit inputs(Strings). To see the range of flow rate units that can be input into the function see the Flow Rate units section under Drilling Conversions. To see the range of annular capacity units that can be input into the function see the Annular Capacity units section under Production Conversions. The function returns a dictionary containing the annular velocity with different units. To see the range of velocity units that can be returned, see the example code below or review the Velocity units section of Force and Power Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   annular_velocity  = bas_for.annular_velocity_annular_capcity(12.6,'bbl/min',0.1261,'bbl/ft')
   print(annular_velocity)
   # outputs the following dictionary:
   {
       'ft/d': 143885.80491673274,
       'ft/hr': 5995.241871530531,
       'ft/min': 99.92069785884219,
       'ft/s': 1.665348295003965,
       'kph': 1.665348295003965,
       'k/min': 0.030455828707375097,
       'k/sec': 0.0005095955590800952,
       'knot': 0.986686915146709,
       'mach': 0.0014888183980967485,
       'm/d': 43856.39333862014,
       'm/hr': 43856.39333862014,
       'm/min': 30.4558287073751,
       'm/sec': 0.5075971451229183,
       'mph': 1.135458842188739,
       'mi/min': 0.01892498017446471,
       'mi/sec': 0.000319746233148295
   }
   # Each key representing a different velocity unit
   print(annular_velocity['ft/min'])
   # outputs the following float:
   99.92069785884219

Annular Velocity from Annulus Diameter Function
------------

annular_velocity_flow_rate(hole_id_value, pipe_od_value, dia_units, flow_value, flow_units)

   #. hole_id_value : hole inner diameter value (Integer or Float)
   #. pipe_od_value : pipe outer diameter value (Integer or Float)
   #. dia_unit : diameter units (string)
   #. flow_value : pump output / flow rate value (Integer or Float)
   #. flow_units : pump output / flow rate units (string)

This function is for the calculation of annular velocity from the annular diameter and flow rate. It takes in three value inputs(Integers or Floats) and two unit inputs(Strings). To see the range of flow rate units that can be input into the function see the Flow Rate units section under Drilling Conversions. To see the range of Diameter units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary containing the annular velocity with different units and values. To see the range of velocity units that can be returned, see the example code below or review the Velocity units section of Force and Power Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   annular_velocity  = bas_for.annular_velocity_flow_rate(12.25,4.5,'in',120,'ft3/min')
   print(annular_velocity)
   # outputs the following dictionary:
   {
       'ft/d': 243963.61949118917, 
       'ft/hr': 10165.150812132882, 
       'ft/min': 169.4191802022147, 
       'ft/s': 2.8236586506762515, 
       'kph': 2.8236586506762515, 
       'k/min': 0.05163896612563504, 
       'k/sec': 0.000864037819031295, 
       'knot': 1.6729635787428097, 
       'mach': 0.002524345785012999, 
       'm/d': 74360.11122091446, 
       'm/hr': 74360.11122091446, 
       'm/min': 51.638966125635044, 
       'm/sec': 0.8606494354272507, 
       'mph': 1.925211796145887, 
       'mi/min': 0.03208799273029946, 
       'mi/sec': 0.000542141376647087
   }
   # Each key representing a different velocity unit
   print(annular_velocity['ft/min'])
   # outputs the following float:
   169.4191802022147

Flow Rate from Required Annular Velocity Function
------------

pump_output_flow_rate(od_value, id_value, diameter_units, velocity_value, velocity_units)

   #. od_value : hole inner diameter value (Integer or Float)
   #. id_value : pipe outer diameter units (Integer or Float)
   #. diameter_units : diameter units (string)
   #. velocity_value : required annular velocity value (Integer or Float)
   #. velocity_units : required annular velocity units (string)

This function is for the calculation of the flow rate from the required annular velocity. It takes in three value inputs(Integers or Floats) and two unit inputs(Strings). To see the range of Diameter units that can be input into the function see the Length units section under General Conversions. To see the range of annular velocity units that can be input into the function see the Velocity units section under Force and Power Conversions. The function returns a dictionary containing the flow rate with different units and values. To see the range of velocity units that can be returned, see the example code below or review the Flow Rate units section of Drilling Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   pump_output  = bas_for.pump_output_flow_rate(10, 5.0, 'in', 120, 'ft/min')
   print(pump_output)
   # outputs the following dictionary:
   {
       'bbl/hr': 524.7813306122449,
       'bbl/min': 8.74634693877551,
       'ft3/min': 49.10715918367347,
       'm3/hr': 83.43356326530612,
       'm3/min': 1.3905551020408162,
       'gal/hr': 22040.81632653061,
       'gpm': 367.3469387755102,
       'L/hr': 83433.56583673469,
       'L/min': 1390.5594367346937
   }
   # Each key representing a different flow rate unit
   print(pump_output['gpm'])
   # outputs the following float:
   367.3469387755102

Stroke Rate from Required Annular Velocity Function
------------

pump_output_spm(velocity_value, velocity_units, stroke_value, stroke_units, annulus_value, annulus_units)

   #. velocity_value : required annular velocity value (Integer or Float)
   #. velocity_units : required annular velocity units (string)
   #. stroke_value : pump output value (Integer or Float)
   #. stroke_units : pump output units (string)
   #. annulus_value : annular capacity value (Integer or Float)
   #. annulus_units : annular capacity units (string)

This function is for the calculation of the required Strokes per Minute from the required annular velocity, pump output and annular capacity. It takes in three value inputs(Integers or Floats) and three unit inputs(Strings).To see the range of annular velocity units that can be input into the function see the Velocity units section under Force and Power Conversions.  To see the range of Pump Output units that can be input into the function see the Stroke Volume units section under Production Conversions.  To see the range of Annular Capacity units that can be input into the function see the Pipe Capacity units section under Production Conversions. The function returns a float giving the required strokes per minute.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   spm_output  = bas_for.pump_output_spm(120,'ft/min',0.136,'bbl/stk',0.1261,'bbl/ft')
   print(spm_output)
   # outputs the following float:
   111.26470588235291

Stroke Pressure Factor Function
------------

stroke_pressure_factor(old_spm, new_spm, pressure_old_value, pressure_new_value, pressure_units)

   #. old_spm : old strokes per minute value (Integer or Float)
   #. new_spm : new strokes per minute value (Integer or Float)
   #. pressure_old_value : old pressure value (Integer or Float)
   #. pressure_new_value : new pressure value (Integer or Float)
   #. pressure_units : pressure units (string)

This function is for the calculation of the relationship factor between pump pressure and pump stroke output. It takes in four value inputs(Integers or Floats) and one unit input(String).To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions. The function returns a float giving the stroke pressure factor.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   factor  = bas_for.stroke_pressure_factor(120, 315, 450, 2500, 'psi')
   print(factor)
   # outputs the following float:
   1.7768442367078825

New Pressure from Stroke Pressure Factor Function
------------

stroke_pressure_relationship(old_spm, new_spm, pressure_value, pressure_units, factor)

   #. old_spm : old strokes per minute value (Integer or Float)
   #. new_spm : new strokes per minute value (Integer or Float)
   #. pressure_value : old pressure value (Integer or Float)
   #. pressure_units : pressure units (string)
   #. factor : stroke pressure factor (Integer or Float)

This function is for the calculation of the new pump pressure from the pump stroke output and stroke pressure factor. It takes in four value inputs(Integers or Floats) and one unit input(String). The default input for factor is 2. To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions. The function returns a dictionary of the new pressure with the different pressure units and values. To see the range of pressure units that can be returned, see the example code below or review the Pressure units section of General Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   new_pressure  = bas_for.stroke_pressure_relationship(60, 30, 1800, 'psi', 1.7768)
   print(new_pressure)
   # outputs the following dictionary:
   {
       'atm': 35.744133919186226,
       'bar': 36.21774368659171,
       'cm_Hg': 2716.554843320286,
       'cm_h2o': 36931.93295344288,
       'dyne/cm2': 36227169.791496836,
       'ft_air': 937355.392535161,
       'ft_hg': 89.12578022885893,
       'ft_h2o': 1211.673912212499,
       'in_air': 11248264.710421933,
       'in_hg': 1069.50925386916,
       'in_h2o': 14540.083592648887,
       'kg/cm2': 36.93182052188139,
       'kg/m2': 369327.11943802587,
       'kPa': 3621.7753175671164,
       'Mpa': 3.6217743761505465,
       'm_Hg': 27.16554183033969,
       'm_h2o': 369.3182130085059,
       'mbar': 36217.678262021276,
       'N/cm2': 362.17743187166604,
       'N/m2': 3622716.979149684,
       'N/mm2': 3.6217743761505465,
       'Pa': 3622716.979149684,
       'psf': 75642.81463865908,
       'psi': 525.2939619767042,
       'torr': 27165.541838812216
   }
   # Each key representing a different pressure unit
   print(new_pressure['psi'])
   # outputs the following float:
   525.2939619767042

Buoyancy Factor Function
------------

buoyancy_factor(value, units)

   #. value : mud weight value (Integer or Float)
   #. units : mud weight units (string)

This function is used to calculate the buoyancy factor to compensate for weight loss due to the buoyancy in drilling fluid. It takes in one value input(Integer or Float) and one unit input(String).To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. The function returns a float giving the buoyancy factor.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   buoyancy_factor  = bas_for.buoyancy_factor(120, 'lb/ft3')
   print(buoyancy_factor)
   # outputs the following float:
   0.7551113282442748

Formation Temperature Function
------------

formation_temp(depth_value, depth_units, gradient_value, gradient_units, temp_value, temp_units)

   #. depth_value : depth value (Integer or Float)
   #. depth_units : depth units (string)
   #. gradient_value : geothermal gradient value (Integer or Float)
   #. gradient_units : geothermal gradient units (string)
   #. temp_value : surface temperature value (Integer or Float)
   #. temp_units : surface temperature units (string)

This function is for the calculation of formation temperature using the geothermal gradient and total vertical depth. It takes in three value inputs(Integers or Floats) and three unit inputs(Strings). To see the range of depth units that can be input into the function see the Length units section under General Conversions. To see the range of geothermal gradient units that can be input into the function see the Geothermal Gradient units section under Drilling Conversions. To see the range of temperature units that can be input into the function see the Temperature units section under General Conversions. The function returns a dictionary of formation temperatures with the different temperature units and values. To see the range of temperature units that can be returned, see the example code below or review the Temperature units section of General Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   formation_temp = basFor.formation_temp(12000, 'ft', 0.15, 'f/100ft', 90, 'f')
   print(formation_temp)
   # outputs the following dictionary:
   {
       'c': 42.22222222222222,
       'f': 108.0,
       'k': 315.3722222222222
   }
   # Each key representing a different temperature unit
   print(formation_temp['f'])
   # outputs the following float:
   108.0

Surface Accumulator Capacity Function
------------

accumulator_capacity_surface(volume_value, volume_units, pre_charge_value, operating_value, minimum_value, pressure_units)

   #. volume_value : volume per bottle value (Integer or Float)
   #. volume_units : volume units (string)
   #. pre_charge_value : pre-charge pressure value (Integer or Float)
   #. operating_value : operating pressure value (Integer or Float)
   #. minimum_value : minimum system pressure value (Integer or Float)
   #. pressure_units : pressure units (string)

This function is used to calculate the usable volume of hydraulic fluid per bottle. It takes in four value inputs(Integers or Floats) and two unit inputs(Strings). To see the range of volume units that can be input into the function see the Volume units section under General Conversions. To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions. The function returns a dictionary of accumulator volume with the different volume units and values. To see the range of temperature units that can be returned, see the example code below or review the  Volume units section under General Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   accumulator_capacity = basFor.accumulator_capacity_surface(10,'gal_us',1000,3000,1200,'psi' )
   print(accumulator_capacity)
   # outputs the following dictionary:
   {
       'bbl': 0.11904761904761904,
       'bucket': 1.0,
       'bu_us': 0.5371043789851466,
       'cm3': 18925.056775170324,
       'ft3': 0.6684027760371456,
       'in3': 1155.0011550011548,
       'm3': 0.01892705891700147,
       'mm3': 18927062.67128992,
       'yd3': 0.024755658433030393,
       'C': 80.0,
       'dr': 5119.803399549457,
       'drum': 0.09090909090909091,
       'fl_oz': 640.0,
       'gal_us': 5.0,
       'gill': 160.0,
       'gal_uk': 4.163371,
       'kL': 0.018927,
       'L': 18.927059,
       'ml': 18927.05892,
       'Pt': 40.0,
       'qt_dr': 17.18734,
       'qt_lq': 20.0,
       'tbsp': 1280.0,
       'tsp': 3840.0,
       'toe': 0.016234000000000002
   }
   # Each key representing a different volume unit
   print(accumulator_capacity['gal_us'])
   # outputs the following float:
   5.0

Subsea Accumulator Capacity Function
------------

accumulator_capacity_subsea(volume_value, volume_units, pre_charge_value, operating_value, minimum_value, pressure_units, pres_grad_value, pres_grad_units, depth_value, depth_units)

   #. volume_value : volume per bottle value (Integer or Float)
   #. volume_units : volume units (string)
   #. pre_charge_value : pre-charge pressure value (Integer or Float)
   #. operating_value : operating pressure value (Integer or Float)
   #. minimum_value : minimum system pressure value (Integer or Float)
   #. pressure_units : pressure units (string)
   #. pres_grad_value : pressure gradient value (Integer or Float)
   #. pres_grad_units : pressure gradient units (string)
   #. depth_value : water depth value (Integer or Float)
   #. depth_units : water depth units (string)

This function is used to calculate the usable volume of hydraulic fluid per bottle for a subsea BOP. It takes in six value inputs(Integers or Floats) and four unit inputs(Strings). To see the range of volume units that can be input into the function see the Volume units section under General Conversions. To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions.To see the range of pressure gradient units that can be input into the function see the Pressure Gradient units section under Drilling Conversions.To see the range of depth units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary of accumulator volumes with the different volume units and values. To see the range of temperature units that can be returned, see the example code below or review the  Volume units section under General Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   accumulator_capacity = basFor.accumulator_capacity_subsea(10,'gal_us',1000,3000,1200,'psi', 0.445, 'psi/ft', 1500, 'ft' )
   print(accumulator_capacity)
   # outputs the following dictionary:
   {
       'bbl': 0.10434179995862304,
       'bucket': 0.8764711196524337,
       'bu_us': 0.4707564764193365,
       'cm3': 16587.26570121941,
       'ft3': 0.5858357294920719,
       'in3': 1012.3251555237163,
       'm3': 0.01658902052071186,
       'mm3': 16589023.811237257,
       'yd3': 0.02169761966453136,
       'C': 70.11768957219469,
       'dr': 4487.359818003449,
       'drum': 0.07967919269567578,
       'fl_oz': 560.9415165775575,
       'gal_us': 4.382355598262168,
       'gill': 140.23537914438938,
       'gal_uk': 3.6490744418984726,
       'kL': 0.01658896888166161,
       'L': 16.589020593457672,
       'ml': 16589.020523339983,
       'Pt': 35.058844786097346,
       'qt_dr': 15.06420713364706,
       'qt_lq': 17.529422393048673,
       'tbsp': 1121.883033155115,
       'tsp': 3365.649099465345,
       'toe': 0.014228632156437609
   }
   # Each key representing a different volume unit
   print(accumulator_capacity['gal_us'])
   # outputs the following float:
   4.382355598262168

Depth of Washout Plugging Function
------------

washout_depth_plug(pipe_value, pipe_units, pump_value, pump_units, strokes)

   #. pipe_value : pipe capacity value (Integer or Float)
   #. pipe_units : pipe capacity units (string)
   #. pump_value : stroke volume value (Integer or Float)
   #. pump_units : stroke volume units (string)
   #. strokes : number of strokes until pressure increase is seen value (Integer or Float)

This function is for the calculation of washout depth by pumping material to plug the hole and using the number of strokes when a pressure increase is seen. It takes in three value inputs(Integers or Floats) and two unit inputs(Strings). To see the range of pipe capacity units that can be input into the function see the Pipe Capacity units section under Production Conversions. To see the range of stroke volume units that can be input into the function see the Stroke Volume units section under Production Conversions. The function returns a dictionary of the washout depth with the different depth units. To see the range of depth units that can be returned and values, see the example code below or review the Length units section of General Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   washout_depth = basFor.washout_depth_plug(0.00742,'bbl/ft', 0.0855 ,'bbl/stk', 400)
   print(washout_depth)
   # outputs the following dictionary:
   {
       'cm': 140487.33153638814,
       'dm': 14048.733153638816,
       'dam': 140.48733153638815,
       'fath': 768.1942237196766,
       'ft': 4609.1644204851755,
       'hm': 14.048733153638814,
       'in': 55309.9730458221,
       'km': 1.4048733153638815,
       'league': 0.2908382749326146,
       'm': 1404.8733153638816,
       'mi': 0.8729757412398922,
       'mm': 1404873.3153638816,
       'nleague': 0.25304312668463613,
       'nm': 0.7586684636118598,
       'yd': 1536.3879865229112
   }
   # Each key representing a different depth unit
   print(washout_depth['ft'])
   # outputs the following float:
   4609.1644204851755

Depth of Washout Passing Function
------------

washout_depth_pass(pipe_value, pipe_units, pump_value, pump_units, strokes, annular_value, annular_units)

   #. pipe_value : pipe capacity value (Integer or Float)
   #. pipe_units : pipe capacity units (string)
   #. pump_value : stroke volume value (Integer or Float)
   #. pump_units : stroke volume units (string)
   #. strokes : number of strokes until passing material is seen at shakers (Integer or Float)
   #. annular_value : annular capacity value (Integer or Float)
   #. annular_units : annular capacity units (string)

This function is for the calculation of washout depth by pumping material that will pass through the hole and using the number of strokes when material is seen at the shakers. It takes in four value inputs(Integers or Floats) and three unit inputs(Strings). To see the range of pipe capacity units that can be input into the function see the Pipe Capacity units section under Production Conversions. To see the range of stroke volume units that can be input into the function see the Stroke Volume units section under Production Conversions. To see the range of annular capacity units that can be input into the function see the Pipe Capacity units section under Production Conversions.The function returns a dictionary of the washout depth with the different depth units and values. To see the range of depth units that can be returned, see the example code below or review the Length units section of General Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   washout_depth = basFor.washout_depth_pass(0.00742,'bbl/ft', 0.0855 ,'bbl/stk', 2500, 0.0455, 'bbl/ft')
   print(washout_depth)
   # outputs the following dictionary:
   {
       'cm': 123112.24489795919,
       'dm': 12311.224489795919,
       'dam': 123.11224489795919,
       'fath': 673.1860756802721,
       'ft': 4039.1156462585036,
       'hm': 12.311224489795919,
       'in': 48469.38775510204,
       'km': 1.2311224489795918,
       'league': 0.2548681972789116,
       'm': 1231.122448979592,
       'mi': 0.7650085034013606,
       'mm': 1231122.448979592,
       'nleague': 0.22174744897959184,
       'nm': 0.6648384353741497,
       'yd': 1346.3717474489797
   }
   # Each key representing a different depth unit
   print(washout_depth['ft'])
   # outputs the following float:
   4039.1156462585036

Basic Equivalent Circulating Density Function
------------

ecd(pres_value, pres_units, mud_value, mud_units, depth_value, depth_units)

   #. pres_value : annular pressure loss value (Integer or Float)
   #. pres_units : annular pressure loss units (string)
   #. mud_value : mud weight value (Integer or Float)
   #. mud_units : mud weight units (string)
   #. depth_value : true vertical depth value (Integer or Float)
   #. depth_units : true vertical depth units (String)

This is a simple version of the calculation, this function uses annular pressure loss, mud weight and depth to caculate the ECD. It takes in three value inputs(Integers or Floats) and three unit inputs(Strings). To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of depth units that can be input into the function see the Length units section under General Conversions.The function returns a dictionary of the ECD with the mud weight units. To see the range of mud weight units that can be returned, see the example code below or review the Mud Weight units section of Drilling Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   ecd = basFor.ecd(400,'psi',10,'ppg',8000,'ft')
   print(ecd)
   # outputs the following dictionary:
   {
       'g/cm3': 1.3134816923076924, 
       'g/L': 1313.4816923076924, 
       'kg/m3': 1313.4816923076924, 
       'kg/L': 1.3134816923076924, 
       'kPa/m': 12.887126711538462, 
       'lb/ft3': 82.0054746923077, 
       'lb/bbl': 460.3846153846154, 
       'ppg': 10.961538461538462, 
       'psi/ft': 0.5700306923076923, 
       'psi/100ft': 56.96919259615385, 
       'SG': 1.3134816923076924
   }
   # Each key representing a different pressure unit
   print(ecd['SG'])
   # outputs the following float:
   1.3134816923076924

Formation Integrity Test Function
------------

fit_test(fit_value, mud_value, mud_units, depth_value, depth_units)

   #. fit_value : required FIT value (Integer or Float)
   #. mud_value : mud weight value (Integer or Float)
   #. mud_units : mud weight units (string)
   #. depth_value : true vertical depth of shoe value (Integer or Float)
   #. depth_units : true vertical depth units (String)

This function uses requried FIT value, mud weight and depth to caculate the required FIT pressure. It takes in three value inputs(Integers or Floats) and two unit inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of depth units that can be input into the function see the Length units section under General Conversions.The function returns a dictionary of the FIT with the pressure units. To see the range of pressure units that can be returned, see the example code below or review the Pressure units section under General Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   fit_pressure = basFor.fit_test(14.5, 9.2,'ppg',4000,'ft')
   print(fit_pressure)
   # outputs the following dictionary:
   {
       'atm': 75.01387048926028,
       'bar': 76.00780425850273,
       'cm_Hg': 5701.055553745532,
       'cm_h2o': 77506.62645096428,
       'dyne/cm2': 76027586.20689656,
       'ft_air': 1967166.3097787297,
       'ft_hg': 187.04243192624287,
       'ft_h2o': 2542.8606028452637,
       'in_air': 23605995.717344757,
       'in_hg': 2244.5089546215836,
       'in_h2o': 30514.320195530807,
       'kg/cm2': 77.50639049821712,
       'kg/m2': 775082.6126696197,
       'kPa': 7600.782417261168,
       'Mpa': 7.600780441571932,
       'm_Hg': 57.01054168045926,
       'm_h2o': 775.0639213298871,
       'mbar': 76007.66695624596,
       'N/cm2': 760.07803210392,
       'N/m2': 7602758.620689656,
       'N/mm2': 7.600780441571932,
       'Pa': 7602758.620689656,
       'psf': 158746.61597834228,
       'psi': 1102.4,
       'torr': 57010.54169824
   }
   # Each key representing a different pressure unit
   print(fit_pressure['bar'])
   # outputs the following float:
   76.00780425850273

Leak Off Test Function
------------

lot_test(pres_value, pres_units, mud_value, mud_units, depth_value, depth_units)

   #. pres_value : lot pressure value (Integer or Float)
   #. pres_units : lot pressure loss units (string)
   #. mud_value : mud weight value (Integer or Float)
   #. mud_units : mud weight units (string)
   #. depth_value : true vertical depth of shoe value (Integer or Float)
   #. depth_units : true vertical depth units (String)

This function uses LOT pressure value, mud weight and depth to caculate the LOT equivelent mud weight. It takes in three value inputs(Integers or Floats) and three unit inputs(Strings). To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of depth units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary of the LOT with the pressure units. To see the range of pressure units that can be returned, see the example code below or review the Pressure units section under General Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   lot_mud_weight = basFor.lot_test(1600,'psi', 9.2,'ppg',4000,'ft')
   print(lot_mud_weight)
   # outputs the following dictionary:
   {
       'g/cm3': 2.0241444184615385, 
       'g/L': 2024.1444184615386, 
       'kg/m3': 2024.1444184615386, 
       'kg/L': 2.0241444184615385, 
       'kPa/m': 19.859740532307693, 
       'lb/ft3': 126.37475257846154, 
       'lb/bbl': 709.4769230769231, 
       'ppg': 16.892307692307693, 
       'psi/ft': 0.8784472984615385, 
       'psi/100ft': 87.79252416923077, 
       'SG': 2.0241444184615385
   }
   # Each key representing a pressure unit
   print(lot_mud_weight['SG'])
   # outputs the following float:
   2.0241444184615385

Mud Motor Bit Revolutions Function
------------

bit_revolutions_mud_motor(bit_rotation_value, bit_rotation_units, flow_value, flow_units, rev_value, rev_units)

   #. bit_rotation_value : bit rotation value (Integer or Float)
   #. bit_rotation_units : bit rotation units (string)
   #. flow_value : mud flow rate value (Integer or Float)
   #. flow_units : mud flow rate units (string)
   #. rev_value : mud motor data flow on revolutions value (Integer or Float)
   #. rev_units : mud motor data flow on revolutions units (String)

This function calculates the total bit rotations when using a mud motor. It takes in three value inputs(Integers or Floats) and three unit inputs(Strings). To see the range of bit rotation units that can be input into the function see the Angular Elocity units section under Force and Power Conversions. To see the range ofmud flow rate units that can be input into the function see the Flow Rate units section under Drilling Conversions. To see the range of flow on revolutions units that can be input into the function see the Volume units section under General Conversions. The function returns a dictionary of the total bit revolutions with the angualr velocity units and values. To see the range of angualr velocity units that can be returned, see the example code below or review the Angular Elocity units section under Force and Power Conversions.

.. code-block:: python

   # Example Code
   from ogPypeline import basic_formulas as bas_for

   total_bit_revs = basFor.bit_revolutions_mud_motor(200,'rpm', 300,'gpm',0.2,'gal_us')
   print(total_bit_revs)
   # outputs the following dictionary:
   {
       'deg/hr': 5616000.0,
       'deg/min': 93600.0,
       'deg/sec': 1560.0,
       'rad/hr': 98017.692708,
       'rad/min': 1633.6282039999999,
       'rad/sec': 27.227148,
       'rph': 15600.0,
       'rpm': 260.0,
       'rps': 4.333342
   }
   # Each key representing a different annular velocity unit
   print(total_bit_revs['rpm'])
   # outputs the following float:
   260.0

