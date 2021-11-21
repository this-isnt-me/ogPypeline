Hydraulic Formulas
==================

This module contains functions for formulas related to hydraulics, they are outlined below. 

Bit Nozzle Velocity(Flow Rate) Function
------------

*bit_nozzle_velocity_flow(flow_value, flow_units, area_value, area_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - flow_value
     - flow rate value (Integer or Float)
   * - flow_units
     - flow rate units (String)
   * - area_value
     - area value (Integer or Float)
   * - area_units
     - area units (String)

This function calculates the bit nozzle velocity from the flow rate. The function takes in two value inputs(Integer or Float) and two units inputs(String). To see the range of flow rate units that can be input into the function see the Flow Rate units section under Drilling Conversions. To see the range of area units that can be input into the function see the Area units section under General Conversions. The function returns a dictionary of different velocity units and values, to see the range of velocity units returned see the example code below or the Velocity units section under Force and Power Conversions.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   nozzle_velocity  = hydro.bit_nozzle_velocity_flow(800, 'gpm', 1.00,'in2')
   print(nozzle_velocity)
   # outputs the following dictionary:
   {
       'ft/d': 22187520.0,
       'ft/hr': 924480.0,
       'ft/min': 15408.0,
       'ft/s': 256.8,
       'kph': 281.78150400000004,
       'k/min': 4.6963584,
       'k/sec': 0.07827264,
       'knot': 152.14983984,
       'mach': 0.23001576,
       'm/d': 6762756.096000001,
       'm/hr': 281781.504,
       'm/min': 4696.3584,
       'm/sec': 78.27264000000001,
       'mph': 175.09091376,
       'mi/min': 2.91817248,
       'mi/sec': 0.04863792
   }
   # Each key representing a different unit
   print(nozzle_velocity['ft/s'])
   # outputs the following float:
   256.8

Bit Nozzle Velocity(Pressure Drop) Function
------------

*bit_nozzle_velocity_pressure_drop(mud_value, mud_units, pressure_value, pressure_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - pressure_value
     - pressure drop value (Integer or Float)
   * - pressure_units
     - pressure drop units (String)
   
This function calculates nozzle velocity using the pressure drop. The function takes in two value inputs(Integers or Floats) and two units input(Strings).To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions. The function returns a dictionary of different velocity units and values, to see the range of velocity units returned see the example code below or the Velocity units section under Force and Power Conversions.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   nozzle_velocity  = hydro.bit_nozzle_velocity_pressure_drop(12, 'ppg', 450,'psi')
   print(nozzle_velocity)
   # outputs the following dictionary:
   {
       'ft/d': 22187520.0,
       'ft/hr': 924480.0,
       'ft/min': 15408.0,
       'ft/s': 256.8,
       'kph': 281.78150400000004,
       'k/min': 4.6963584,
       'k/sec': 0.07827264,
       'knot': 152.14983984,
       'mach': 0.23001576,
       'm/d': 6762756.096000001,
       'm/hr': 281781.504,
       'm/min': 4696.3584,
       'm/sec': 78.27264000000001,
       'mph': 175.09091376,
       'mi/min': 2.91817248,
       'mi/sec': 0.04863792
   }
   # Each key representing a different unit
   print(nozzle_velocity['ft/s'])
   # outputs the following float:
   256.8

Bit Aggressiveness Function
------------

*bit_aggressiveness(torque_value, torque_units, wob_value, wob_units, bit_value, bit_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - torque_value
     - torque value (Integer or Float)
   * - torque_units
     - torque units (String)
   * - wob_value
     - weight on bit length (Integer or Float)
   * - wob_units
     - weight on bit units (String)
   * - bit_value
     - bit diammeter value (Integer or Float)
   * - bit_units
     - bit diammeter units (String)

The Bit Aggressiveness function calculates bit aggressiveness/coefficient of friction. The function takes in three value inputs(Integers or Floats) and three units input(Strings). To see the range of torque units that can be input into the function see the Torque units section under General Conversions. To see the range of weight on bit units that can be input into the function see the Weight units section under General Conversions. To see the range of diameter units that can be input into the function see the Length units section under General Conversions. The function returns a float.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   aggressiveness  = hydro.bit_aggressiveness(16000, 'ft-lb', 15000,'lb', 12.25,'in')
   print(aggressiveness)
   # outputs the following float:
   3.1346938775510202

Bit Hydraulic Horsepower Function
------------

*bit_hhp(flow_value, flow_units, pressure_value, pressure_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - flow_value
     - flow rate value (Integer or Float)
   * - flow_units
     - flow rate units (String)
   * - pressure_value
     - pressure drop value (Integer or Float)
   * - pressure_units
     - pressure drop units (String)

The Bit Hydraulic Horsepower function calculates hydraulic horsepower from the flow rate and pressure drop. The function takes in two value inputs(Integers or Floats) and two units input(Strings). To see the range of flow rate units that can be input into the function see the Flow Rate units section under Drilling Conversions. To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions. The function returns a float of the hydraulic horsepower.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   bit_hhp  = hydro.bit_hhp(800, 'gpm', 500,'psi')
   print(bit_hhp)
   # outputs the following float:
   229.88505747126436

Bit Hydraulic Horse Power by Bit Area Function
------------

*bit_hhp_area(bit_hhp_value, diameter_value, diameter_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - bit_hhp_value
     - Bit Hydraulic Horsepower value (Integer or Float)
   * - diameter_value
     - bit diameter rate (Integer or Float)
   * - diameter_units
     - bit diameter units (String)

The function takes in two value inputs(Integers or Floats) and one units input(Strings). To see the range of diameter units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary of hydraulic horsepower by area.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   hhp  = hydro.bit_hhp_area(450, 8.625,'in')
   print(hhp)
   # outputs the following dictionary:
   {
       'in2': 7.700567107750471,
       'cm2': 1.1935879017013231,
       'mm2': 0.01193587901701323
   }
   # Each key representing a different unit
   print(hhp['in2'])
   # outputs the following float:
   7.700567107750471

Critical Flow Rate Function
------------

*critical_flow(n_constant, k_constant, mud_value, mud_units, hole_id_value, pipe_od_value, dia_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - n_constant
     - flow behavior index value (Integer or Float)
   * - k_constant
     - consistency factor value (Integer or Float)
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - hole_id_value
     - hole inner diameter value (Integer or Float)
   * - pipe_od_value
     - drill pipe outer diameter value (Integer or Float)
   * - dia_units
     - diameter units (String)

The function takes in two value inputs(Integers or Floats) and one units input(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of diameter units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary with two sub-dictionaries:

   * - "critical_velocity" which is a dictionary of different velocity units and values, to see the range of velocity units returned see the example code below or the Velocity units section under Force and Power Conversions.
   * - "critical_flow" which is a dictionary of different flow rate units and values, to see the range of flow rate units returned see the example code below or the Flow Rate units section under Drilling Conversions.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   critical_flow = hydro.critical_flow(0.51, 6.63, 10, 'ppg', 12.25, 5, 'in')
   print(critical_flow)
   # outputs the following dictionary:
   {
       'critical_velocity': 
          {
              'ft/d': 320361.2658860939,
              'ft/hr': 13348.386078587246,
              'ft/min': 222.47310130978744,
              'ft/s': 3.7078850218297905,
              'kph': 4.068588076753393,
              'k/min': 0.0678098012792232,
              'k/sec': 0.00113016335465372,
              'knot': 2.196861807696797,
              'mach': 0.0033211526140529434,
              'm/d': 97646.11384208142,
              'm/hr': 4068.588076753392,
              'm/min': 67.80980127922321,
              'm/sec': 1.1301633546537202,
              'mph': 2.5281034913909486,
              'mi/min': 0.04213492223406501,
              'mi/sec': 0.0007022734231345623
          },
       'critical_flow':
          {
              'bbl/hr': 1623.010764438843,
              'bbl/min': 27.0501528981377,
              'ft3/min': 151.87553999516103,
              'm3/hr': 258.0380882397218,
              'm3/min': 4.300621549407188,
              'gal/hr': 68166.45346976047,
              'gpm': 1136.1075578293412,
              'L/hr': 258038.09619247468,
              'L/min': 4300.63495547637
          }
      }

Cross Flow Velocity Under Bit Function
------------

*cross_flow_velocity(flow_value, flow_units, velocity_value, velocity_units, bit_value, bit_units, nozzles)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - flow_units
     - flow rate value (Integer or Float)
   * - flow_value
     - flow rate units (String)
   * - velocity_value
     - nozzle velocity value (Integer or Float)
   * - velocity_units
     - nozzle velocity units (String)
   * - bit_units
     - bit diameter rate (Integer or Float)
   * - bit_value
     - bit diameter units (String)
   * - nozzles
     - number of nozzles value (Integer or Float)

The function takes in four value inputs(Integers or Floats) and three units inputs(Strings). To see the range of flow rate units that can be input into the function see the Flow Rate units section under Drilling Conversions. To see the range of velocity units that can be input into the function see the Velocity units section under Force and Power Conversions. To see the range of diameter units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary of different velocity units and values, to see the range of velocity units returned see the example code below or the Velocity units section under Force and Power Conversions.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   cross_flow_velocity  = hydro.cross_flow_velocity(800, 'gpm', 350, 'ft/s', 12.25, 'in', 8)
   print(cross_flow_velocity)
   # outputs the following dictionary:
   {
       'ft/d': 48105484.09485139,
       'ft/hr': 2004395.1706188081,
       'ft/min': 33406.586176980134,
       'ft/s': 556.7764362830022,
       'kph': 610.9396480046126,
       'k/min': 10.182327466743544,
       'k/sec': 0.16970545777905907,
       'knot': 329.88101871941103,
       'mach': 0.49870465397868513,
       'm/d': 14662551.552110706,
       'm/hr': 610939.6480046127,
       'm/min': 10182.327466743545,
       'm/sec': 169.7054577790591,
       'mph': 379.6203075888913,
       'mi/min': 6.326984711345524,
       'mi/sec': 0.10545345703200062
   }
   # Each key representing a different unit
   print(cross_flow_velocity['ft/s'])
   # outputs the following float:
   556.7764362830022

Cutting Carrying Index Function
------------

*cutting_carrying_index(mud_value, mud_units, velocity_value, velocity_units, viscosity_value, viscosity_units, yield_value, yield_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (string)
   * - velocity_value
     - velocity value (Integer or Float)
   * - velocity_units
     - velocity units (string)
   * - viscosity_value
     - plastic viscosity value (Integer or Float)
   * - viscosity_units
     - plastic viscosity units (string)
   * - yield_value
     - yield point value (Integer or Float)
   * - yield_units
     - yield point units (string)

This function calculates the cutting carrying index. The function takes in four value inputs(Integers or Floats) and four units inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of velocity units that can be input into the function see the Velocity units section under Force and Power Conversions. To see the range of viscosity units that can be input into the function see the Viscosity units section under Fluids Conversions. To see the range of yield point units that can be input into the function see the Fluid Yield Point units section under Fluids Conversions. The function returns a dictionary containing flow behaviour index (n) consistency factor (K) the cuttings carrying index (cci) and hole cleaning performance.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   cci  = hydro.cutting_carrying_index(10.3, 'ppg', 120, 'ft/min', 17, 'cp', 15, 'lbf/100ft2')
   print(cci)
   # outputs the following dictionary:
   {
       'n': 0.6147231498759947,
       'K': 353.7055313846302,
       'cci': 1.0929500919785073,
       'hole_cleaning': 'Good Hole Cleaning'
   }

Cutting Slip Velocity(One) Function
------------

*cutting_slip_velocity_one(flow_value, flow_units, hole_diameter, pipe_diameter, diameter_units, viscosity_value, viscosity_units, mud_value, mud_units, cutting_dia, dia_units, cutting_density, density_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - flow_value
     - flow rate value (Integer or Float)
   * - flow_units
     - flow rate units (string)
   * - hole_diameter
     - inner diameter value of hole value (Integer or Float)
   * - pipe_diameter
     - outer diameter value of tubular value (Integer or Float)
   * - diameter_units
     - diameter units (string)
   * - viscosity_value
     - plastic viscosity value (Integer or Float)
   * - viscosity_units
     - plastic viscosity units (string)
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (string)
   * - cutting_dia
     - cutting diameter value (Integer or Float)
   * - diameter_units
     - cutting diameter units (string)
   * - cutting_density
     - cutting density value (Integer or Float)
   * - density_units
     - cutting density units (string)

The function is for the calculation of cuttings movement. It takes in seven value inputs(Integers or Floats) and six units input(Strings). To see the range of flow rate units that can be input into the function see the Flow Rate units section under Drilling Conversions. To see the range of diameter units that can be input into the function see the Length units section under General Conversions. To see the range of plastic viscosity units that can be input into the function see the Viscosity units section under Fluids Conversions. To see the range of mud weight and cutting density units that can be input into the function see the Mud Weight units section under Drilling Conversions. The function returns a dictionary with three sub-dictionaries and a string indicating cutting movement:

   * - "annular_velocity" which is a dictionary of different velocity units and values, to see the range of velocity units returned see the example code below or the Velocity units section under Force and Power Conversions.
   * - "cutting_slip_velocity" which is a dictionary of different flow rate units and values, to see the range of flow rate units returned see the example code below or the Flow Rate units section under Drilling Conversions.
   * - "net_rise_velocity" which is a dictionary of different flow rate units and values, to see the range of flow rate units returned see the example code below or the Flow Rate units section under Drilling Conversions.
   * - "net_rise" which is a string indicating cutting movement.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   cutting_slip = hydro.cutting_slip_velocity_one(600, 'gpm', 11.5, 5, 'in', 17, 'cp', 9.2, 'ppg', 0.75, 'in', 21.5, 'ppg')
   print(cutting_slip)
   # outputs the following dictionary:
   {
       'annular_velocity': 
          {
              'ft/d': 197370.62937062938,
              'ft/hr': 8223.776223776224,
              'ft/min': 137.06293706293707,
              'ft/s': 2.284386853146853,
              'kph': 2.284386853146853,
              'k/min': 0.041776783216783214,
              'k/sec': 0.000699020979020979,
              'knot': 1.3534553846153847,
              'mach': 0.002042237762237762,
              'm/d': 60158.56783216783,
              'm/hr': 60158.56783216783,
              'm/min': 41.77678321678322,
              'm/sec': 0.6962797202797203,
              'mph': 1.5575283916083915,
              'mi/min': 0.02595972027972028,
              'mi/sec': 0.0004386013986013986
          },
       'cutting_slip_velocity':
          {
              'ft/d': 122890.45140128904,
              'ft/hr': 5120.43547505371,
              'ft/min': 85.34059125089517,
              'ft/s': 1.4223460322012946,
              'kph': 1.4223460322012946,
              'k/min': 0.026011812213272846,
              'k/sec': 0.0004352370153795654,
              'knot': 0.8427127364252146,
              'mach': 0.001271574809638338,
              'm/d': 37457.0095871129,
              'm/hr': 37457.0095871129,
              'm/min': 26.01181221327285,
              'm/sec': 0.4335302035545475,
              'mph': 0.9697763427386724,
              'mi/min': 0.016163507982919545,
              'mi/sec': 0.00027308989200286454
          },
       'net_rise_velocity':
          {
              'ft/d': 74480.17796934032,
              'ft/hr': 3103.3407487225136,
              'ft/min': 51.722345812041894,
              'ft/s': 0.8620408209455586,
              'kph': 0.8620408209455586,
              'k/min': 0.015764971003510368,
              'k/sec': 0.0002637839636414137,
              'knot': 0.5107426481901701,
              'mach': 0.0007706629525994242,
              'm/d': 22701.55824505493,
              'm/hr': 22701.55824505493,
              'm/min': 15.76497100351037,
              'm/sec': 0.2627495167251728,
              'mph': 0.5877520488697192,
              'mi/min': 0.009796212296800735,
              'mi/sec': 0.00016551150659853406
          },
       'net_rise': 'positive'
      }

Cutting Slip Velocity(Two) Function
------------

*cutting_slip_velocity_two(reading_300, reading_600, flow_value, flow_units, hole_diameter, pipe_diameter, diameter_units, cutting_dia, dia_units, cutting_density, density_units, mud_value, mud_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - reading_600
     - 600 rpm sheer stress value (Integer or Float)
   * - reading_300
     - 300 rpm sheer stress value (Integer or Float)
   * - flow_value
     - flow rate value (Integer or Float)
   * - flow_units
     - flow rate units (string)
   * - hole_diameter
     - inner diameter value of hole value (Integer or Float)
   * - pipe_diameter
     - outer diameter value of tubular value (Integer or Float)
   * - diameter_units
     - diameter units (string)
   * - cutting_dia
     - cutting diameter value (Integer or Float)
   * - diameter_units
     - cutting diameter units (string)
   * - cutting_density
     - cutting density value (Integer or Float)
   * - density_units
     - cutting density units (string)
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (string)

The function is for the calculation of cuttings movement. It takes in eight value inputs(Integers or Floats) and five units input(Strings). To see the range of flow rate units that can be input into the function see the Flow Rate units section under Drilling Conversions. To see the range of diameter units that can be input into the function see the Length units section under General Conversions. To see the range of mud weight and cutting density units that can be input into the function see the Mud Weight units section under Drilling Conversions. The function returns a dictionary with four sub-dictionaries and a string indicating cutting movement, floats of flow behaviour index (n) and consistency factor (K):

   * - "n" flow behavior index (n).
   * - "K" consistency factor (K).
   * - "viscosity" which is a dictionary of different viscosity units and values, to see the range of viscosity units returned see the example code below or the Viscosity units section under Fluids Conversions.
   * - "annular_velocity" which is a dictionary of different velocity units and values, to see the range of velocity units returned see the example code below or the Velocity units section under Force and Power Conversions.
   * - "cutting_slip_velocity" which is a dictionary of different flow rate units and values, to see the range of flow rate units returned see the example code below or the Flow Rate units section under Drilling Conversions.
   * - "net_rise_velocity" which is a dictionary of different flow rate units and values, to see the range of flow rate units returned see the example code below or the Flow Rate units section under Drilling Conversions.
   * - "net_rise" which is a string indicating cutting movement.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   cutting_slip = hydro.cutting_slip_velocity_two(32, 49, 200, 'gpm', 11.5, 5, 'in', 0.75, 'in', 21.5, 'ppg', 9.2, 'ppg')
   print(cutting_slip)
   # outputs the following dictionary:
   {
       'n': 0.6143530576725775,
       'K': 0.6937824614629686,
       'viscosity':
          {
              'cp': 125.87251643085676,
              'g/(cm.s)': 1.2587251643085677,
              'kg/(m.hr)': 453.14105915108433,
              'kg/(m.s)': 0.12587251643085676,
              'kg-f.s/m2': 0.01283899667594739,
              'kPa-s': 0.00012587251643085675,
              'N.s/m2': 0.12587251643085676,
              'Pa-s': 0.12587251643085676,
              'dyne-s/cm2': 1.2587251643085677,
              'p': 1.2587251643085677,
              'lbf-s/ft2': 0.0026307355934049063,
              'lbf-s/in2': 1.8256260276343673e-05,
              'lb/(ft.hr)': 304.49673178944334,
              'lb/(ft.s)': 0.08458633104153573,
              'poundal.s/ft2': 0.08458633104153573,
              'reyn': 1.8256260276343673e-05
          },
       'annular_velocity':
          {
              'ft/d': 65790.20979020979,
              'ft/hr': 2741.258741258741,
              'ft/min': 45.687645687645684,
              'ft/s': 0.7614622843822844,
              'kph': 0.7614622843822844,
              'k/min': 0.013925594405594403,
              'k/sec': 0.000233006993006993,
              'knot': 0.45115179487179485,
              'mach': 0.0006807459207459207,
              'm/d': 20052.85594405594,
              'm/hr': 20052.85594405594,
              'm/min': 13.925594405594405,
              'm/sec': 0.2320932400932401,
              'mph': 0.5191761305361304,
              'mi/min': 0.008653240093240092,
              'mi/sec': 0.00014620046620046617
          },
       'cutting_slip_velocity':
          {
              'ft/d': 96207.77535303852,
              'ft/hr': 4008.657306376605,
              'ft/min': 66.81095510627675,
              'ft/s': 1.1135181454697827,
              'kph': 1.1135181454697827,
              'k/min': 0.020363979116393153,
              'k/sec': 0.00034073587104201146,
              'knot': 0.659738138387951,
              'mach': 0.0009954832310835235,
              'm/d': 29324.12992760614,
              'm/hr': 29324.12992760614,
              'm/min': 20.363979116393153,
              'm/sec': 0.3393996519398859,
              'mph': 0.7592129694456865,
              'mi/min': 0.012653994897128816,
              'mi/sec': 0.0002137950563400856
          },
       'net_rise_velocity':
          {
              'ft/d': -30417.565562828735,
              'ft/hr': -1267.398565117864,
              'ft/min': -21.123309418631067,
              'ft/s': -0.35205586108749837,
              'kph': -0.35205586108749837,
              'k/min': -0.006438384710798749,
              'k/sec': -0.00010772887803501844,
              'knot': -0.2085863435161562,
              'mach': -0.0003147373103376029,
              'm/d': -9271.273983550198,
              'm/hr': -9271.273983550198,
              'm/min': -6.43838471079875,
              'm/sec': -0.10730641184664583,
              'mph': -0.240036838909556,
              'mi/min': -0.004000754803888724,
              'mi/sec': -6.759459013961941e-05
          },
       'net_rise': 'negative'
      }

Effective Viscosity Function
------------

*effective_viscosity(consistency_factor_value, consistency_factor_units, power_law_value, hole_id_value, pipe_od_value, dia_units, flow_value, flow_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - consistency_factor_value
     - consistency factor value (Integer or Float)
   * - consistency_factor_units
     - consistency factor units (string)
   * - power_law_value
     - drilling mud power law constant value (Integer or Float)
   * - hole_id_value
     - inner diameter hole value (Integer or Float)
   * - pipe_od_value
     - outer diameter drill pipe value (Integer or Float)
   * - dia_units
     - diameter units (string)
   * - flow_value
     - flow rate value (Integer or Float)
   * - flow_units
     - flow rate units (string)

The function is for the calculation of fluid in the annulus between two tubular. It takes in five value inputs(Integers or Floats) and three units inputs(Strings). To see the range of consistency factor units that can be input into the function see the Viscosity units section under Fluids Conversions. To see the range of diameter units that can be input into the function see the Diameter units section under General Conversions. To see the range of flow rate factor units that can be input into the function see the Flow Rate units section under Drilling Conversions. The function returns a dictionary of different viscosity units and values, to see the range of viscosity units returned see the example code below or the Viscosity units section under Fluid Conversions.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   effective_viscosity  = hydro.effective_viscosity(663, 'cp', 0.514, 8.5, 5, 'in', 800, 'gpm')
   print(effective_viscosity)
   # outputs the following dictionary:
   {
       'cp': 42.54717845581881,
       'g/(cm.s)': 0.4254717845581881,
       'kg/(m.hr)': 153.16984244094772,
       'kg/(m.s)': 0.04254717845581881,
       'kg-f.s/m2': 0.004339812202493519,
       'kPa-s': 4.2547178455818805e-05,
       'N.s/m2': 0.04254717845581881,
       'Pa-s': 0.04254717845581881,
       'dyne-s/cm2': 0.4254717845581881,
       'p': 0.4254717845581881,
       'lbf-s/ft2': 0.000889236029726613,
       'lbf-s/in2': 6.170944904721512e-06,
       'lb/(ft.hr)': 102.92538160048335,
       'lb/(ft.s)': 0.028591703922310238,
       'poundal.s/ft2': 0.028591703922310238,
       'reyn': 6.170944904721512e-06
   }
   # Each key representing a different unit
   print(effective_viscosity['cp'])
   # outputs the following float:
   42.54717845581881

Impact Force Jet Nozzle(Velocity) Function
------------

*impact_force_jet_nozzle_velocity(flow_value, flow_units, mud_value, mud_units, velocity_value, velocity_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - flow_value
     - flow rate value (Integer or Float)
   * - flow_units
     - flow rate units (string)
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (string)
   * - velocity_value
     - nozzle velocity value (Integer or Float)
   * - velocity_units
     - nozzle velocity units (string)

The function is for the calculation of jet impact force using nozzle velocity. It takes in three value inputs(Integer or Float) and three units inputs(Strings). To see the range of flow rate units that can be input into the function see the Flow Rate units section under Drilling Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of nozzle velocity units that can be input into the function see the Velocity units section under Force and Power Conversions. The function returns a dictionary of different impact force units and values, to see the range of impact force units returned see the example code below or the Force units section under Force and Power Conversions.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   impact_force  = hydro.impact_force_jet_nozzle_velocity(800, 'gpm', 12, 'ppg', 350, 'ft/s')
   print(impact_force)
   # outputs the following dictionary:
   {
       'daN': 766.0103626943005,
       'dyn': 774405418.4455959,
       'gf': 789669.6373056994,
       'kgf': 783.419689119171,
       'kN': 7.747150259067357,
       'kip': 1.7409326424870468,
       'klbs': 1.7409326424870468,
       'MN': 0.007747150259067357,
       'N': 7747.150259067358,
       'ozf': 27854.922279792747,
       'lbf': 1740.9326424870467,
       'pdl': 56005.80310880829,
       'sn': 7.747150259067357,
       'tf-metric': 0.7903834196891192,
       'tf-long': 0.7764559585492228,
       'tf-short': 0.8704663212435234,
       'hN': 77.47150259067358,
       'J/m': 7747.150259067358,
       'mN': 7747150.2590673575
   }
   # Each key representing a different unit
   print(impact_force['lbf'])
   # outputs the following float:
   1740.9326424870467

Impact Force Jet Nozzle(Pressure) Function
------------

*impact_force_jet_nozzle_pressure(flow_value, flow_units, mud_value, mud_units, pressure_value, pressure_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - flow_value
     - flow rate value (Integer or Float)
   * - flow_units
     - flow rate units (string)
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (string)
   * - pressure_value
     - pressure drop value (Integer or Float)
   * - pressure_units
     - pressure drop units (string)

The function is for the calculation of jet impact force using nozzle velocity. It takes in three value inputs(Integer or Float) and three units inputs(Strings). To see the range of flow rate units that can be input into the function see the Flow Rate units section under Drilling Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of pressure drop units that can be input into the function see the Pressure units section under General Conversions. The function returns a dictionary of different impact force units and values, to see the range of impact force units returned see the example code below or the Force units section under Force and Power Conversions.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   impact_force  = hydro.impact_force_jet_nozzle_pressure(800, 'gpm', 12, 'ppg', 450, 'psi')
   print(impact_force)
   # outputs the following dictionary:
   {
       'daN': 447.4923821295733,
       'dyn': 452396654.55095947,
       'gf': 461313.7945685298,
       'kgf': 457.66266354160905,
       'kN': 4.525775228355911,
       'kip': 1.0170281412035755,
       'klbs': 1.0170281412035755,
       'MN': 0.0045257752283559115,
       'N': 4525.775228355912,
       'ozf': 16272.45025925721,
       'lbf': 1017.0281412035756,
       'pdl': 32717.79530251903,
       'sn': 4.525775228355911,
       'tf-metric': 0.4617307761064233,
       'tf-long': 0.45359455097679474,
       'tf-short': 0.5085140706017878,
       'hN': 45.25775228355912,
       'J/m': 4525.775228355912,
       'mN': 4525775.228355912
   }
   # Each key representing a different unit
   print(impact_force['lbf'])
   # outputs the following float:
   1017.0281412035756

Mechanical Specific Energy(Friction) Function
------------

*specific_energy_friction(wob_value, wob_units, coef_value, rotary_value, rotary_units, rop_value, rop_units, bit_value, dia_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - wob_value
     - weight on bit value (Integer or Float)
   * - wob_units
     - weight on bit units (String)
   * - coef_value
     - coefficient of friction value (Integer or Float)
   * - rotary_value
     - rotary speed value (Integer or Float)
   * - rotary_units
     - rotary speed units (String)
   * - rop_value
     - rate of penetration value (Integer or Float)
   * - rop_units
     - rate of penetration units (String)
   * - bit_value
     - bit diameter value (Integer or Float)
   * - dia_units
     - bit diameter units (String)

This function is for the calculation of mechanical specific energy using the coefficient of friction. It takes in five value inputs(Integers or Floats) and four units inputs(String). To see the range of weight on bit units that can be input into the function see the Weight units section under General Conversions. To see the range of rotary speed units that can be input into the function see the Angular Velocity units section under Force and Power Conversions. To see the range of rate of penetration units that can be input into the function see the Drilling Rate units section under Drilling Conversions. To see the range of bit diameter units that can be input into the function see the Length units section under General Conversions.  The function returns a dictionary containing pressure units to see the range of Pressure units that will be returned see the example code below or the Pressure units section of General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   specific_energy  = hydro.specific_energy_friction(15000, 'lb', 3.1, 100, 'rpm', 140, 'ft/hr', 12.25, 'in')
   print(specific_energy)
   # outputs the following dictionary:
   {
       'atm': 2468.0211553569884,
       'bar': 2500.722435180501,
       'cm_Hg': 187569.65375521942,
       'cm_h2o': 2550034.980380302,
       'dyne/cm2': 2501373278.375389,
       'ft_air': 64721471.33555166,
       'ft_hg': 6153.857625697069,
       'ft_h2o': 83662.31101012773,
       'in_air': 776657656.0266199,
       'in_hg': 73846.28399073682,
       'in_h2o': 1003947.5005451043,
       'kg/cm2': 2550.0272173310436,
       'kg/m2': 25500887.672392003,
       'kPa': 250072.30903718926,
       'Mpa': 250.07224403530628,
       'm_Hg': 1875.6960816450505,
       'm_h2o': 25500.272711164416,
       'mbar': 2500717.9178176164,
       'N/cm2': 25007.224006967528,
       'N/m2': 250137327.83753893,
       'N/mm2': 250.07224403530628,
       'Pa': 250137327.83753893,
       'psf': 5222900.831813136,
       'psi': 36269.912536443146,
       'torr': 1875696.0822300522
   }
   # Each key representing a different unit
   print(specific_energy['psi'])
   # outputs the following float:
   36269.912536443146

Mechanical Specific Energy(Torque) Function
------------

*specific_energy_torque(wob_value, wob_units, torque_value, torque_units, rotary_value, rotary_units, rop_value, rop_units, bit_value, dia_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - wob_value
     - weight on bit value (Integer or Float)
   * - wob_units
     - weight on bit units (String)
   * - torque_value
     - drilling torque value (Integer or Float)
   * - torque_units
     - drilling torque units (String)
   * - rotary_value
     - rotary speed value (Integer or Float)
   * - rotary_units
     - rotary speed units (String)
   * - rop_value
     - rate of penetration value (Integer or Float)
   * - rop_units
     - rate of penetration units (String)
   * - bit_value
     - bit diameter value (Integer or Float)
   * - dia_units
     - bit diameter units (String)

This function is for the calculation of mechanical specific energy using the coefficient of friction. It takes in five value inputs(Integers or Floats) and five units inputs(String). To see the range of weight on bit units that can be input into the function see the Weight units section under General Conversions. To see the range of drilling torque units that can be input into the function see the Torque units section under General Conversions. To see the range of rotary speed units that can be input into the function see the Angular Velocity units section under Force and Power Conversions. To see the range of rate of penetration units that can be input into the function see the Drilling Rate units section under Drilling Conversions. To see the range of bit diameter units that can be input into the function see the Length units section under General Conversions.  The function returns a dictionary containing pressure units to see the range of Pressure units that will be returned see the example code below or the Pressure units section of General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   specific_energy  = hydro.specific_energy_torque(15000, 'lb', 16000, 'ft-lb', 100, 'rpm', 140, 'ft/hr', 12.25, 'in')
   print(specific_energy)
   # outputs the following dictionary:
   {
       'atm': 2496.167090724209,
       'bar': 2529.241304185807,
       'cm_Hg': 189708.7453671318,
       'cm_h2o': 2579116.2220812286,
       'dyne/cm2': 2529899569.760547,
       'ft_air': 65459571.308936365,
       'ft_hg': 6224.037769257021,
       'ft_h2o': 84616.4170935591,
       'in_air': 785514855.7072364,
       'in_hg': 74688.44562772331,
       'in_h2o': 1015396.7709053247,
       'kg/cm2': 2579.1083705002,
       'kg/m2': 25791706.22339024,
       'kPa': 252924.19668491668,
       'Mpa': 252.92413094173583,
       'm_Hg': 1897.0869925648944,
       'm_h2o': 25791.084248989802,
       'mbar': 2529236.7353057778,
       'N/cm2': 25292.412693087976,
       'N/m2': 252989956.97605473,
       'N/mm2': 252.92413094173583,
       'Pa': 252989956.97605473,
       'psf': 5282464.109430323,
       'psi': 36683.54376152794,
       'torr': 1897086.9931565677
   }
   # Each key representing a different unit
   print(specific_energy['psi'])
   # outputs the following float:
   36683.54376152794

Minimum Flow PDC Bit Function
------------

*pdc_minimum_flow(bit_value, dia_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - bit_value
     - bit diameter value (Integer or Float)
   * - dia_units
     - bit diameter units (string)

This function is for the calculation of the minimum flow rate for a PDC bit. It takes in one value input(Integers or Floats) and one unit input(Strings). To see the range of dimeter units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary containing the flow rate with different units. To see the range of flow rate units that can be returned, see the example code below or review the Flow Rate units section of Drilling Conversions.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   min_flow  = hydro.pdc_minimum_flow(12.25, 'in')
   print(min_flow)
   # outputs the following dictionary:
   {
       'bbl/hr': 722.685120438183,
       'bbl/min': 12.044740203445848,
       'ft3/min': 67.62628771039977,
       'm3/hr': 114.89775111974537,
       'm3/min': 1.914956616733821,
       'gal/hr': 30352.7756654592,
       'gpm': 505.87959442432003,
       'L/hr': 114897.75466090252,
       'L/min': 1914.9625861130353
   }
   # Each key representing a different unit
   print(min_flow['gpm'])
   # outputs the following float:
   505.87959442432003

Power Law Constant Function
------------

*power_law_constants(reading_300, reading_3)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - reading_600
     - 600 rpm sheer stress value (Integer or Float)
   * - reading_300
     - 300 rpm sheer stress value (Integer or Float)

This function is for the calculation of flow behaviour index (n) and the consistency factor (K). It takes in two value inputs(Integers or Floats). The function returns a dictionary containing a float and a subdictionary. The flow behaviour index (n) is returned as a float, while the subdictionary contains the consistency factor (K) data with different viscosity units. To see the range of viscosity units that can be returned, see the example code below or review the Viscosity units section of Fluids Conversions.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   constants  = hydro.power_law_constants(32, 3)
   print(constants)
   # outputs the following dictionary:
   {
       'power_law_n': 0.5140143618001217,
       'power_law_k':
          {
              'cp': 662.8322609796006,
              'g/(cm.s)': 6.628322609796006,
              'kg/(m.hr)': 2386.196139526562,
              'kg/(m.s)': 0.6628322609796007,
              'kg-f.s/m2': 0.06760889061991926,
              'kPa-s': 0.0006628322609796006,
              'N.s/m2': 0.6628322609796007,
              'Pa-s': 0.6628322609796007,
              'dyne-s/cm2': 6.628322609796006,
              'p': 6.628322609796006,
              'lbf-s/ft2': 0.013853194254473653,
              'lbf-s/in2': 9.613566661828102e-05,
              'lb/(ft.hr)': 1603.4497673982983,
              'lb/(ft.s)': 0.44542327937829157,
              'poundal.s/ft2': 0.44542327937829157,
              'reyn': 9.613566661828102e-05,
              'poise': 6.628322609796006
          }
      }

Pressure Drop Across Bit (Flow Rate) Function
------------

*pressure_drop_across_bit_flow_rate(mud_value, mud_units, flow_value, flow_units, nozzle_value, nozzle_unit)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (string)
   * - flow_value
     - pump output / flow rate value (Integer or Float)
   * - flow_units
     - pump output / flow rate units (string)
   * - nozzle_value
     - nozzle area value (Integer or Float)
   * - nozzle_unit
     - nozzle area units (string)

This function is for the calculation of pressure drop across bit using flow rate. It takes in three value inputs(Integers or Floats) and three units inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of flow rate units that can be input into the function see the Flow Rate units section under Drilling Conversions. To see the range of nozzle area units that can be input into the function see the Area units section under General Conversions. The function returns a dictionary containing the pressure drop with different units and values. To see the range of pressure units that can be returned, see the example code below or review the Pressure units section of General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   annular_velocity  = hydro.annular_velocity_flow_rate(12.25,4.5,'in',120,'ft3/min')
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
   # Each key representing a different unit
   print(annular_velocity['ft/min'])
   # outputs the following float:
   169.4191802022147

Pressure Drop Across Bit (Velocity) Function
------------

*pressure_drop_across_bit_velocity(mud_value, mud_units, nozzle_value, nozzle_unit)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (string)
   * - nozzle_value
     - nozzle velocity value (Integer or Float)
   * - nozzle_unit
     - nozzle velocity units (string)

This function is for the calculation of pressure drop across bit using flow rate. It takes in two value inputs(Integers or Floats) and two units inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of nozzle velocity units that can be input into the function see the Velocity units section under Force and Power Conversions. The function returns a dictionary containing the pressure drop with different units and values. To see the range of pressure units that can be returned, see the example code below or review the Pressure units section of General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   annular_velocity  = hydro.bit_nozzle_velocity_pressure_drop(12, 'ppg', 450,'psi')
   print(annular_velocity)
   # outputs the following dictionary:
   {
       'ft/d': 18623659.79070709,
       'ft/hr': 775985.8246127954,
       'ft/min': 12933.097076879923,
       'ft/s': 215.55161794799872,
       'kph': 236.52047934198004,
       'k/min': 3.942007989033,
       'k/sec': 0.06570013315055001,
       'knot': 127.71084169797848,
       'mach': 0.19306958419602246,
       'm/d': 5676491.504207521,
       'm/hr': 236520.47934198004,
       'm/min': 3942.0079890330007,
       'm/sec': 65.70013315055002,
       'mph': 146.9670161563922,
       'mi/min': 2.449442365713878,
       'mi/sec': 0.04082547643935096
   }
   # Each key representing a different unit
   print(annular_velocity['ft/min'])
   # outputs the following float:
   215.55161794799872

Pressure Loss Annulus Function
------------

*pressure_loss_annulus(string_value, string_units, hole_id_value, pipe_od_value, dia_units, mud_value, mud_units, viscosity_value, viscosity_units, flow_value, flow_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - string_value
     - drill string length value (Integer or Float)
   * - string_units
     - drill string length units (String)
   * - hole_id_value
     - hole inner diameter value (Integer or Float)
   * - pipe_od_value
     - drill string outer diameter value (Integer or Float)
   * - dia_units
     - diameter units (String)
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - viscosity_value
     - plastic viscosity value (Integer or Float)
   * - viscosity_units
     - plastic viscosity units (String)
   * - flow_value
     - flow rate value (Integer or Float)
   * - flow_units
     - flow rate units (String)

This function is for the calculation of the general coefficient and pressure loss in the annulus. It takes in six value inputs(Integers or Floats) and five units inputs(Strings). To see the range of drill string length and diameter units that can be input into the function see the Length units section under General Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of plastic viscosity units that can be input into the function see the Viscosity units section under Fluids Conversions. To see the range of flow rate units that can be input into the function see the Flow Rate units section under Drilling Conversions. The function returns a dictionary containing a string and a subdictionary. The general coefficient is returned as a string, while the subdictionary contains the pressure loss data with different pressure units. To see the range of pressure units that can be returned, see the example code below or review the Pressure units section of General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   pressure_loss  = hydro.pressure_loss_annulus(2500, 'ft', 8.835, 5, 'in', 9.5, 'ppg', 12, 'cp', 600, 'gpm')
   print(pressure_loss)
   # outputs the following dictionary:
   {
       'coefficient': 0.0019118563645424322,
       'power_law_k':
          {
              'atm': 4.693389963484698,
              'bar': 4.755577379578617,
              'cm_Hg': 356.6977246034627,
              'cm_h2o': 4849.354130321725,
              'dyne/cm2': 4756815.075986551,
              'ft_air': 123079.61920379192,
              'ft_hg': 11.702676678629475,
              'ft_h2o': 159.09906200138397,
              'in_air': 1476955.4304455032,
              'in_hg': 140.43210584742022,
              'in_h2o': 1909.1883036320178,
              'kg/cm2': 4.849339367475226,
              'kg/m2': 48494.56415791675,
              'kPa': 475.557862554391,
              'Mpa': 0.47555773894151815,
              'm_Hg': 3.5669763790444846,
              'm_h2o': 48.49339469757918,
              'mbar': 4755.568788993573,
              'N/cm2': 47.55577314001514,
              'N/m2': 475681.5075986551,
              'N/mm2': 0.47555773894151815,
              'Pa': 475681.5075986551,
              'psf': 9932.29344533797,
              'psi': 68.973818601805,
              'torr': 3566.976380156971
          }
      }

Pressure Loss Annulus(Tooljoint Corrected) Function
------------

*pressure_loss_annulus_corrected(pipe_value, collar_value, length_units, pipe_od_value, tj_od_value, collar_od_value, hole_id_value, dia_units, mud_value, mud_units, viscosity_value, viscosity_units, flow_value, flow_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - pipe_value
     - drill pipe length value (Integer or Float)
   * - collar_value
     - collar length value (Integer or Float)
   * - length_units
     - drill string length units (String)
   * - pipe_od_value
     - drill pipe outer diameter value (Integer or Float)
   * - tj_od_value
     - tool joint outer diameter value (Integer or Float)
   * - collar_od_value
     - collar outer diameter value (Integer or Float)
   * - hole_id_value
     - hole inner diameter value (Integer or Float)
   * - dia_units
     - diameter units (String)
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - viscosity_value
     - plastic viscosity value (Integer or Float)
   * - viscosity_units
     - plastic viscosity units (String)
   * - flow_value
     - flow rate value (Integer or Float)
   * - flow_units
     - flow rate units (String)

This function is for the calculation of the pressure loss in the annulus correcting for tooljoints. It takes in nine value inputs(Integers or Floats) and five units inputs(Strings). To see the range of drill string length and diameter units that can be input into the function see the Length units section under General Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of plastic viscosity units that can be input into the function see the Viscosity units section under Fluids Conversions. To see the range of flow rate units that can be input into the function see the Flow Rate units section under Drilling Conversions. The function returns a dictionary containing three subdictionaries. The subdictionaries, 'pressure_loss_pipe';  'pressure_loss_collar';  'total_pressure_loss', each contain the pressure loss data with different pressure units. To see the range of pressure units that can be returned, see the example code below or review the Pressure units section of General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   pressure_loss  = hydro.pressure_loss_annulus_corrected(2500, 500, 'ft', 5, 6, 5, 9, 'in', 9.5, 'ppg', 12, 'cp', 600, 'gpm')
   print(pressure_loss)
   # outputs the following dictionary:
   {
       'pressure_loss_pipe':
          {
              'atm': 4.254353028355916,
              'bar': 4.31072320514565,
              'cm_Hg': 323.3309093599577,
              'cm_h2o': 4395.727734199763,
              'dyne/cm2': 4311845.122885758,
              'ft_air': 111566.29957502408,
              'ft_hg': 10.60796532036556,
              'ft_h2o': 144.21635140064586,
              'in_air': 1338795.594900289,
              'in_hg': 127.29557088556606,
              'in_h2o': 1730.5958176183522,
              'kg/cm2': 4.395714352324147,
              'kg/m2': 43958.204515111785,
              'kPa': 431.0724334558773,
              'Mpa': 0.4310723214062066,
              'm_Hg': 3.233308307710877,
              'm_h2o': 43.9571444503894,
              'mbar': 4310.715418155482,
              'N/cm2': 43.107231457028696,
              'N/m2': 431184.5122885758,
              'N/mm2': 0.4310723214062066,
              'Pa': 431184.5122885758,
              'psf': 9003.190237002978,
              'psi': 62.52175428184349,
              'torr': 3233.3083087192977
          },
       'pressure_loss_collar':
          {
              'atm': 0.8078579858328871,
              'bar': 0.8185621039864285,
              'cm_Hg': 61.39722196349874,
              'cm_h2o': 834.703591815629,
              'dyne/cm2': 818775.1446531886,
              'ft_air': 21185.295498699565,
              'ft_hg': 2.0143437651687757,
              'ft_h2o': 27.385205315628735,
              'in_air': 254223.5459843948,
              'in_hg': 24.17212272127824,
              'in_h2o': 328.6223879855742,
              'kg/cm2': 0.8347010507347619,
              'kg/m2': 8347.211978816871,
              'kPa': 81.85623184503916,
              'Mpa': 0.08185621056795644,
              'm_Hg': 0.6139720704027873,
              'm_h2o': 8.347010683403498,
              'mbar': 818.5606253168987,
              'N/cm2': 8.185620926988545,
              'N/m2': 81877.51446531886,
              'N/mm2': 0.08185621056795644,
              'Pa': 81877.51446531886,
              'psf': 1709.6134435618967,
              'psi': 11.872239597471236,
              'torr': 613.972070594276
          },
       'total_pressure_loss':
          {
              'atm': 5.0622110141888035,
              'bar': 5.1292853091320785,
              'cm_Hg': 384.72813132345647,
              'cm_h2o': 5230.431326015393,
              'dyne/cm2': 5130620.267538947,
              'ft_air': 132751.59507372367,
              'ft_hg': 12.622309085534338,
              'ft_h2o': 171.6015567162746,
              'in_air': 1593019.140884684,
              'in_hg': 151.4676936068443,
              'in_h2o': 2059.2182056039264,
              'kg/cm2': 5.23041540305891,
              'kg/m2': 52305.41649392866,
              'kPa': 512.9286653009165,
              'Mpa': 0.5129285319741631,
              'm_Hg': 3.8472803781136644,
              'm_h2o': 52.304155133792904,
              'mbar': 5129.276043472382,
              'N/cm2': 51.292852384017245,
              'N/m2': 513062.02675389475,
              'N/mm2': 0.5129285319741631,
              'Pa': 513062.02675389475,
              'psf': 10712.803680564877,
              'psi': 74.39399387931473,
              'torr': 3847.280379313574
          }   
      }

Pressure Loss Drillstring Function
------------

*pressure_loss_drillstring(pipe_value, collar_value, length_units, pipe_id_value, collar_id_value, dia_units, mud_value, mud_units, viscosity_value, viscosity_units, flow_value, flow_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - pipe_value
     - drill pipe length value (Integer or Float)
   * - collar_value
     - collar length value (Integer or Float)
   * - length_units
     - drill string length units (String)
   * - pipe_id_value
     - drill pipe inner diameter value (Integer or Float)
   * - collar_id_value
     - drill collar inner diameter value (Integer or Float)
   * - dia_units
     - diameter units (String)
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - viscosity_value
     - plastic viscosity value (Integer or Float)
   * - viscosity_units
     - plastic viscosity units (String)
   * - flow_value
     - flow rate value (Integer or Float)
   * - flow_units
     - flow rate units (String)

This function is for the calculation of the pressure loss in the drill string. It takes in six value inputs(Integers or Floats) and five units inputs(Strings). To see the range of drill string length and diameter units that can be input into the function see the Length units section under General Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of plastic viscosity units that can be input into the function see the Viscosity units section under Fluids Conversions. To see the range of flow rate units that can be input into the function see the Flow Rate units section under Drilling Conversions. The function returns a dictionary containing three subdictionaries. The subdictionaries, 'pressure_loss_pipe'; 'pressure_loss_collar'; 'total_pressure_loss', each contain the pressure loss data with different pressure units. To see the range of pressure units that can be returned, see the example code below or review the Pressure units section of General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   pressure_loss  = hydro.pressure_loss_drillstring(5000, 500, 'ft', 3.34, 2.8,'in', 9.5, 'ppg', 12, 'cp', 600, 'gpm')
   print(pressure_loss)
   # outputs the following dictionary:
   {
       'pressure_loss_pipe':
          {
              'atm': 85.30674695698707,
              'bar': 86.43706133740433,
              'cm_Hg': 6483.314356919163,
              'cm_h2o': 88141.54138451962,
              'dyne/cm2': 86459557.62582329,
              'ft_air': 2237087.0549151283,
              'ft_hg': 212.70708079029055,
              'ft_h2o': 2891.7740756340436,
              'in_air': 26845044.65898154,
              'in_hg': 2552.484709637906,
              'in_h2o': 34701.28090320721,
              'kg/cm2': 88.14127305599365,
              'kg/m2': 881434.005184868,
              'kPa': 8643.708398398747,
              'Mpa': 8.643706151619309,
              'm_Hg': 64.83312781083589,
              'm_h2o': 881.4127491507712,
              'mbar': 86436.9051954962,
              'N/cm2': 864.3706014547922,
              'N/m2': 8645955.76258233,
              'N/mm2': 8.643706151619309,
              'Pa': 8645955.76258233,
              'psf': 180528.71170647396,
              'psi': 1253.6635855744378,
              'torr': 64833.12783105638
          },
       'pressure_loss_collar':
          {
              'atm': 20.100329533641922,
              'bar': 20.366658896012954,
              'cm_Hg': 1527.625418772264,
              'cm_h2o': 20768.27555416321,
              'dyne/cm2': 20371959.56479514,
              'ft_air': 527111.7303524796,
              'ft_hg': 50.11892459314616,
              'ft_h2o': 681.3718015339963,
              'in_air': 6325340.764229756,
              'in_hg': 601.4270338918603,
              'in_h2o': 8176.459732377719,
              'kg/cm2': 20.76821232948301,
              'kg/m2': 207687.13611019443,
              'kPa': 2036.6664232094797,
              'Mpa': 2.03666589381399,
              'm_Hg': 15.276250474673503,
              'm_h2o': 207.68212767527967,
              'mbar': 20366.62210520895,
              'N/cm2': 203.66658615166614,
              'N/m2': 2037195.9564795143,
              'N/mm2': 2.03666589381399,
              'Pa': 2037195.9564795143,
              'psf': 42536.923807604624,
              'psi': 295.39341368952955,
              'torr': 15276.250479437937              
          },
       'total_pressure_loss':
          {
              'atm': 105.40707649062898,
              'bar': 106.80372023341728,
              'cm_Hg': 8010.939775691428,
              'cm_h2o': 108909.81693868282,
              'dyne/cm2': 106831517.19061843,
              'ft_air': 2764198.785267608,
              'ft_hg': 262.8260053834367,
              'ft_h2o': 3573.14587716804,
              'in_air': 33170385.423211295,
              'in_hg': 3153.9117435297658,
              'in_h2o': 42877.74063558492,
              'kg/cm2': 108.90948538547666,
              'kg/m2': 1089121.1412950624,
              'kPa': 10680.374821608226,
              'Mpa': 10.680372045433298,
              'm_Hg': 80.1093782855094,
              'm_h2o': 1089.094876826051,
              'mbar': 106803.52730070514,
              'N/cm2': 1068.0371876064582,
              'N/m2': 10683151.719061844,
              'N/mm2': 10.680372045433298,
              'Pa': 10683151.719061844,
              'psf': 223065.63551407857,
              'psi': 1549.0569992639673,
              'torr': 80109.37831049431
          }   
      }

Pressure Loss Drillstring(Tooljoint Corrected) Function
------------

*pressure_loss_drillstring_corrected(pipe_value, collar_value, length_units, pipe_id_value, tj_id_value, collar_id_value, dia_units, mud_value, mud_units, viscosity_value, viscosity_units, flow_value, flow_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - pipe_value
     - drill pipe length value (Integer or Float)
   * - collar_value
     - collar length value (Integer or Float)
   * - length_units
     - drill string length units (String)
   * - pipe_id_value
     - drill pipe inner diameter value (Integer or Float)
   * - tj_id_value
     - tool joint inner diameter value (Integer or Float)
   * - collar_id_value
     - collar inner diameter value (Integer or Float)
   * - hole_id_value
     - hole inner diameter value (Integer or Float)
   * - dia_units
     - diameter units (String)
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - viscosity_value
     - plastic viscosity value (Integer or Float)
   * - viscosity_units
     - plastic viscosity units (String)
   * - flow_value
     - flow rate value (Integer or Float)
   * - flow_units
     - flow rate units (String)

This function is for the calculation of the pressure loss in the drill string correcting for tooljoints. It takes in eight value inputs(Integers or Floats) and five units inputs(Strings). To see the range of drill string length and diameter units that can be input into the function see the Length units section under General Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of plastic viscosity units that can be input into the function see the Viscosity units section under Fluids Conversions. To see the range of flow rate units that can be input into the function see the Flow Rate units section under Drilling Conversions. The function returns a dictionary containing three subdictionaries. The subdictionaries, 'pressure_loss_pipe'; 'pressure_loss_collar'; 'total_pressure_loss', each contain the pressure loss data with different pressure units. To see the range of pressure units that can be returned, see the example code below or review the Pressure units section of General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   pressure_loss  = hydro.pressure_loss_drillstring_corrected(5000, 500, 'ft', 3.34, 2.563, 2.8,'in', 9.5, 'ppg', 12, 'cp', 600, 'gpm')
   print(pressure_loss)
   # outputs the following dictionary:
   {
       'pressure_loss_pipe':
          {
              'atm': 100.1979319418396,
              'bar': 101.52555452038004,
              'cm_Hg': 7615.044693002809,
              'cm_h2o': 103527.56938847943,
              'dyne/cm2': 101551977.77125236,
              'ft_air': 2627594.000148393,
              'ft_hg': 249.83732664567722,
              'ft_h2o': 3396.563488321178,
              'in_air': 31531128.00178072,
              'in_hg': 2998.0476145437815,
              'in_h2o': 40758.75245820084,
              'kg/cm2': 103.52725422040255,
              'kg/m2': 1035297.5305372701,
              'kPa': 10152.558112016113,
              'Mpa': 10.152555473037824,
              'm_Hg': 76.15042842088653,
              'm_h2o': 1035.272564040085,
              'mbar': 101525.3711222686,
              'N/cm2': 1015.2555312039193,
              'N/m2': 10155197.777125238,
              'N/mm2': 10.152555473037824,
              'Pa': 10155197.777125238,
              'psf': 212041.88665444954,
              'psi': 1472.5036776831594,
              'torr': 76150.42844463671
          },
       'pressure_loss_collar':
          {
              'atm': 23.72497912167571,
              'bar': 24.039335090375946,
              'cm_Hg': 1803.0988549443118,
              'cm_h2o': 24513.374424586083,
              'dyne/cm2': 24045591.617463116,
              'ft_air': 622164.6653340743,
              'ft_hg': 59.156763454205304,
              'ft_h2o': 804.2421264007825,
              'in_air': 7465975.984008892,
              'in_hg': 709.8810891838352,
              'in_h2o': 9650.90329067534,
              'kg/cm2': 24.513299798734046,
              'kg/m2': 245138.9147530164,
              'kPa': 2403.9341388702055,
              'Mpa': 2.4039335140099554,
              'm_Hg': 18.030984166827743,
              'm_h2o': 245.13300315770718,
              'mbar': 24039.291665164663,
              'N/cm2': 240.39334758885184,
              'N/m2': 2404559.161746312,
              'N/mm2': 2.4039335140099554,
              'Pa': 2404559.161746312,
              'psf': 50207.51662536939,
              'psi': 348.6610784532152,
              'torr': 18030.984172451335              
          },
       'total_pressure_loss':
          {
              'atm': 123.9229110635153,
              'bar': 125.56488961075598,
              'cm_Hg': 9418.14354794712,
              'cm_h2o': 128040.9438130655,
              'dyne/cm2': 125597569.38871548,
              'ft_air': 3249758.6654824675,
              'ft_hg': 308.99409009988256,
              'ft_h2o': 4200.80561472196,
              'in_air': 38997103.98578961,
              'in_hg': 3707.9287037276167,
              'in_h2o': 50409.65574887618,
              'kg/cm2': 128.0405540191366,
              'kg/m2': 1280436.4452902866,
              'kPa': 12556.492250886318,
              'Mpa': 12.556488987047778,
              'm_Hg': 94.18141258771426,
              'm_h2o': 1280.405567197792,
              'mbar': 125564.66278743326,
              'N/cm2': 1255.648878792771,
              'N/m2': 12559756.93887155,
              'N/mm2': 12.556488987047778,
              'Pa': 12559756.93887155,
              'psf': 262249.4032798189,
              'psi': 1821.1647561363745,
              'torr': 94181.41261708803
          }   
      }

Pressure Loss Surface Equipment Function
------------

*pressure_loss_surface_equipment(coefficient, mud_value, mud_units, viscosity_value, viscosity_units, flow_value, flow_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - coefficient
     - general coefficent for surface equipment (Integer or Float)
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - viscosity_value
     - plastic viscosity value (Integer or Float)
   * - viscosity_units
     - plastic viscosity units (String)
   * - flow_value
     - flow rate value (Integer or Float)
   * - flow_units
     - flow rate units (String)

This function is for the calculation of the pressure loss in the surface equipment. It takes in four value inputs(Integers or Floats) and three units inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of plastic viscosity units that can be input into the function see the Viscosity units section under Fluids Conversions. To see the range of flow rate units that can be input into the function see the Flow Rate units section under Drilling Conversions. The function returns a dictionary containing pressure loss data with different pressure units. To see the range of pressure units that can be returned, see the example code below or review the Pressure units section of General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   pressure_loss  = hydro.pressure_loss_surface_equipment(8, 9.5, 'ppg', 12, 'cp', 600, 'gpm')
   print(pressure_loss)
   # outputs the following dictionary:
   {
       'atm': 10.54430561116125,
       'bar': 10.684017658437174,
       'cm_Hg': 801.367422755602,
       'cm_h2o': 10894.699218407713,
       'dyne/cm2': 10686798.30297782,
       'ft_air': 276514.23160809855,
       'ft_hg': 26.291571833604994,
       'ft_h2o': 357.43655337476497,
       'in_air': 3318170.779297183,
       'in_hg': 315.49882988515304,
       'in_h2o': 4289.237651116425,
       'kg/cm2': 10.89466605176987,
       'kg/m2': 108949.290159023,
       'kPa': 1068.402045765883,
       'Mpa': 1.0684017680536284,
       'm_Hg': 8.013672279750896,
       'm_h2o': 108.94666281561122,
       'mbar': 10683.9983585804,
       'N/cm2': 106.84017511109758,
       'N/m2': 1068679.8302977823,
       'N/mm2': 1.0684017680536284,
       'Pa': 1068679.8302977823,
       'psf': 22314.17766735476,
       'psi': 154.95857539317842,
       'torr': 8013.67228225024   
      }

Optimum Flow Rate Function
------------

*optimum_flow_rate(coefficient, depth_value, collar_value, depth_units, hole_id_dia, pipe_od_dia, pipe_id_dia, tj_od_dia, tj_id_dia, collar_od_dia, collar_id_dia, dia_units, mud_value, mud_units, viscosity_value, viscosity_units, yield_value, yield_units, reading_3, reading_300, reading_600, pressure_value, pressure_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - coefficient
     - general coefficent (Integer or Float)
   * - depth_value
     - tvd depth value (Integer or Float)
   * - collar_value
     - collar length value (Integer or Float)
   * - depth_units
     - length/depth units (String)
   * - hole_id_dia
     - hole inner diameter value (Integer or Float)
   * - pipe_od_value
     - drill pipe outer diameter value (Integer or Float)
   * - pipe_id_value
     - drill pipe inner diameter value (Integer or Float)
   * - tj_od_value
     - tool joint outer diameter value (Integer or Float)
   * - tj_id_value
     - tool joint inner diameter value (Integer or Float)
   * - collar_od_value
     - collar outer diameter value (Integer or Float)
   * - collar_id_value
     - collar inner diameter value (Integer or Float)
   * - dia_units
     - diameter units (String)
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - viscosity_value
     - plastic viscosity value (Integer or Float)
   * - viscosity_units
     - plastic viscosity units (String)
   * - yield_value
     - yield point value (Integer or Float)
   * - yield_units
     - yield point units (string)
   * - reading_3
     - 3 rpm sheer stress value (Integer or Float)
   * - reading_300
     - 300 rpm sheer stress value (Integer or Float)
   * - reading_600
     - 600 rpm sheer stress value (Integer or Float)
   * - pressure_value
     - pressure value (Integer or Float)
   * - pressure_units
     - pressure units (String)

This function is for the calculation of the flow rate to optimise the hydraulic horse power, and the flow rate to optimise the pressure loss. It takes in seventeen value inputs(Integers or Floats) and six units inputs(Strings). To see the range of drill string length and diameter units that can be input into the function see the Length units section under General Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of plastic viscosity units that can be input into the function see the Viscosity units section under Fluids Conversions. To see the range of yield point units that can be input into the function see the Fluid Yield Point units section under Fluids Conversions. To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions. The function returns a dictionary containing two subdictionaries. The subdictionaries, 'max_hydraulic_horsepower'; 'pressure_loss', each contain the the flow rate, to optimise pressure loss or hydraulic horsepower, with different flow rate units. To see the range of flow rate units that can be returned, see the example code below or review the Flow Rate units section of Drilling Conversions.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   optimum_flow  = hydro.optimum_flow_rate(5, 6000, 800, 'ft', 8.5, 5, 4.2, 6.5, 3.5, 6.75, 3.5, 'in',9.5, 'ppg', 14, 'cp', 11, 'lbf/100ft2', 3, 30, 33, 4500, 'psi')
   print(optimum_flow)
   # outputs the following dictionary:
   {
       'max_hydraulic_horsepower':
          {
              'bbl/hr': 1002.5075218346743,
              'bbl/min': 16.70844232295472,
              'ft3/min': 93.811066792582,
              'm3/hr': 159.38595728882984,
              'm3/min': 2.656424434335572,
              'gal/hr': 42105.316759162655,
              'gpm': 701.7552793193776,
              'L/hr': 159385.96220111678,
              'L/min': 2656.4327150478675
          },
       'pressure_loss':
          {
              'bbl/hr': 1240.2977983170197,
              'bbl/min': 20.671609713752552,
              'ft3/min': 116.06263002164134,
              'm3/hr': 197.19158969122134,
              'm3/min': 3.2865163657547996,
              'gal/hr': 52092.508571165,
              'gpm': 868.2084761860833,
              'L/hr': 197191.59576868065,
              'L/min': 3286.5266106148188              
          }   
      }

Reynold Number Function
------------

*reynold_number(annular_value, annular_units, hole_id_value, pipe_od_value, dia_units, mud_value, mud_units, viscosity_value, viscosity_units, power_law_value)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - annular_value
     - annular velocity value (Integer or Float)
   * - annular_units
     - annular velocity units (string)
   * - hole_id_value
     - hole inner diameter value (Integer or Float)
   * - pipe_od_value
     - hole outer diameter value (Integer or Float)
   * - dia_units
     - diameter units (string)
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (string)
   * - viscosity_value
     - effective viscosity value (Integer or Float)
   * - viscosity_units
     - effective viscosity units (string)
   * - power_law_value
     - power law constant value (Integer or Float)

This function is for the calculation of the Reynolds number to indicate the flow regime. It takes in six value inputs(Integers or Floats) and four unit inputs(Strings). To see the range of annular velocity units that can be input into the function see the Velocity units section under Force and Power Conversions. To see the range of diameter units that can be input into the function see the Length units section under General Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of effective viscosity units that can be input into the function see the Viscosity units section under Drilling Conversions. The function returns a dictionary containing a float, Reynolds number, and string, flow regime.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   reynold_number  = hydro.reynold_number(7, 'ft/s', 8.5, 5, 'in', 9.5, 'ppg', 42.53, 'cp', 0.514)
   print(reynold_number)
   # outputs the following dictionary:
   {
       'reynold_number': 4411.484164391324,
       'flow_regime': 'Turbulent Flow'
      }

Surge Swab Pressure(One) Function
------------

*surge_swab_one(reading_300, reading_600, hole_id_value, collar_od_value, collar_id_value, pipe_od_value, pipe_id_value, dia_units, pipe_speed, speed_units, pipe_value, collar_value, tvd_value, length_units, mud_value, mud_units, pipe_state)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - reading_300
     - 300 rpm sheer stress value (Integer or Float)
   * - reading_600
     - 600 rpm sheer stress value (Integer or Float)
   * - hole_id_dia
     - hole inner diameter value (Integer or Float)
   * - pipe_od_value
     - drill pipe outer diameter value (Integer or Float)
   * - pipe_id_value
     - drill pipe inner diameter value (Integer or Float)
   * - collar_od_value
     - collar outer diameter value (Integer or Float)
   * - collar_id_value
     - collar inner diameter value (Integer or Float)
   * - dia_units
     - diameter units (String)
   * - pipe_speed
     - pipe running speed average value (Integer or Float)
   * - speed_units
     - pipe running speed units (String)
   * - pipe_value
     - drill pipe length value (Integer or Float)
   * - collar_value
     - drill collar length value (Integer or Float)
   * - tvd_value
     - true vertical depth value (Integer or Float)
   * - length_units
     - length/depth units (String)
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - pipe_state
     - pipe state open ended('open') or closed ended('closed') (String)

This function is for the calculation of the surge and swab pressures when running drill pipe. It takes in twelve value inputs(Integers or Floats), one string input(String) and four units inputs(Strings). To see the range of length and diameter units that can be input into the function see the Length units section under General Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of velocity units that can be input into the function see the Velocity units section under Force and Power Conversions. The function returns a dictionary containing four subdictionaries. Two subdictionaries, 'surge_bhp'; 'swab_bhp', each contains the pressure with different pressure units. The other two subdictionaries, 'surge_bhp_mud_weight'; 'swab_bhp_mud_weight', each contains the mud weight with different mud weight units. To see the range of pressure units and mud weight that can be returned, see the example code below or review the Pressure units section of General Conversions and the Mud Weight units section of Drilling Conversions.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   surge_swab  = hydro.surge_swab_one(47, 80, 6.35, 5, 2.25, 4, 3.34, 'in', 20, 'ft/min', 12270, 100, 9972, 'ft', 13.2, 'ppg', 'open')
   print(surge_swab)
   # outputs the following dictionary:
   {
       'surge_bhp':
          {
              'atm': 470.5571158500806,
              'bar': 476.7919975426295,
              'cm_Hg': 35762.349565146884,
              'cm_h2o': 486194.0113762948,
              'dyne/cm2': 476916088.414376,
              'ft_air': 12339905.927923722,
              'ft_hg': 1173.3049732635625,
              'ft_h2o': 15951.19867138406,
              'in_air': 148078871.13508466,
              'in_hg': 14079.658245838991,
              'in_h2o': 191414.33990385258,
              'kg/cm2': 486.1925312601049,
              'kg/m2': 4862042.664703968,
              'kPa': 47679.212246253584,
              'Mpa': 47.67919985288389,
              'm_Hg': 357.6234087274365,
              'm_h2o': 4861.925415149204,
              'mbar': 476791.13625453005,
              'N/cm2': 4767.9199096789935,
              'N/m2': 47691608.84143761,
              'N/mm2': 47.67919985288389,
              'Pa': 47691608.84143761,
              'psf': 995807.1657750781,
              'psi': 6915.283282008453,
              'torr': 357623.4088389739
          },
       'surge_bhp_mud_weight':
          {
              'g/cm3': 1.5980003638326887,
              'g/L': 1598.000363832689,
              'kg/m3': 1598.000363832689,
              'kg/L': 1.5980003638326887,
              'kPa/m': 15.678660231354195,
              'lb/ft3': 99.76901784169054,
              'lb/bbl': 560.11042041631,
              'ppg': 13.335962390864523,
              'psi/ft': 0.6935073850196497,
              'psi/100ft': 69.309523710196,
              'SG': 1.5980003638326887              
          },
       'swab_bhp':
          {
              'atm': 460.9622971734595,
              'bar': 467.07004752042855,
              'cm_Hg': 35033.143167093294,
              'cm_h2o': 476280.3511134228,
              'dyne/cm2': 467191608.13734794,
              'ft_air': 12088291.074217606,
              'ft_hg': 1149.3808881915427,
              'ft_h2o': 15625.94833774454,
              'in_air': 145059492.8906113,
              'in_hg': 13792.56925420071,
              'in_h2o': 187511.33680046795,
              'kg/cm2': 476.2789011773024,
              'kg/m2': 4762903.97102689,
              'kPa': 46707.01698931758,
              'Mpa': 46.707004848652886,
              'm_Hg': 350.331346519311,
              'm_h2o': 4762.789112230188,
              'mbar': 467069.20379428467,
              'N/cm2': 4670.700410797594,
              'N/m2': 46719160.8137348,
              'N/mm2': 46.707004848652886,
              'Pa': 46719160.8137348,
              'psf': 975502.321005637,
              'psi': 6774.278317991546,
              'torr': 350331.34662857413             
          },
       'swab_bhp_mud_weight':
          {
              'g/cm3': 1.5654165961673112,
              'g/L': 1565.4165961673111,
              'kg/m3': 1565.4165961673111,
              'kg/L': 1.5654165961673112,
              'kPa/m': 15.358967048645804,
              'lb/ft3': 97.73469383830945,
              'lb/bbl': 548.6895795836899,
              'ppg': 13.064037609135475,
              'psi/ft': 0.6793665349803503,
              'psi/100ft': 67.896279089804,
              'SG': 1.5654165961673112             
          }   
      }

Surge Swab Pressure(Two) Function
------------

*surge_swab_two(reading_300, reading_600, hole_id_value, collar_od_value, pipe_od_value, dia_units, pipe_speed, speed_units, pipe_value, collar_value, tvd_value, length_units, mud_value, mud_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - reading_300
     - 300 rpm sheer stress value (Integer or Float)
   * - reading_600
     - 600 rpm sheer stress value (Integer or Float)
   * - hole_id_dia
     - hole inner diameter value (Integer or Float)
   * - pipe_od_value
     - drill pipe outer diameter value (Integer or Float)
   * - collar_od_value
     - collar outer diameter value (Integer or Float)
   * - dia_units
     - diameter units (String)
   * - pipe_speed
     - pipe running speed average value (Integer or Float)
   * - speed_units
     - pipe running speed units (String)
   * - pipe_value
     - drill pipe length value (Integer or Float)
   * - collar_value
     - drill collar length value (Integer or Float)
   * - tvd_value
     - true vertical depth value (Integer or Float)
   * - length_units
     - length/depth units (String)
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)

This function is for the calculation of the surge and swab pressures when running drill pipe. It takes in ten value inputs(Integers or Floats) and four units inputs(Strings). To see the range of length and diameter units that can be input into the function see the Length units section under General Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of velocity units that can be input into the function see the Velocity units section under Force and Power Conversions. The function returns a dictionary containing four subdictionaries. Two subdictionaries, 'surge_bhp'; 'swab_bhp', each contains the pressure with different pressure units. The other two subdictionaries, 'surge_bhp_mud_weight'; 'swab_bhp_mud_weight', each contains the mud weight with different mud weight units. To see the range of pressure units and mud weight that can be returned, see the example code below or review the Pressure units section of General Conversions and the Mud Weight units section of Drilling Conversions.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   surge_swab = hydro.surge_swab_two(85, 130, 9, 6.25, 5, 'in', 250, 'ft/min', 12000, 800, 9000, 'ft', 12.5, 'ppg')
   print(surge_swab)
   # outputs the following dictionary:
   {
       'surge_bhp':
          {
              'atm': 435.64540182640684,
              'bar': 441.41770331500226,
              'cm_Hg': 33109.05864938302,
              'cm_h2o': 450122.16013135505,
              'dyne/cm2': 441532587.5997449,
              'ft_air': 11424379.94324822,
              'ft_hg': 1086.2547803977466,
              'ft_h2o': 14767.742577336621,
              'in_air': 137092559.31897864,
              'in_hg': 13035.056037790784,
              'in_h2o': 177212.87005107777,
              'kg/cm2': 450.1207898283874,
              'kg/m2': 4501316.543764537,
              'kPa': 44141.78189668136,
              'Mpa': 44.14177042280426,
              'm_Hg': 331.0905060188917,
              'm_h2o': 4501.207993223747,
              'mbar': 441416.9059278466,
              'N/cm2': 4414.176972280664,
              'N/m2': 44153258.759974495,
              'N/mm2': 44.14177042280426,
              'Pa': 44153258.759974495,
              'psf': 921925.9432343041,
              'psi': 6402.222520196302,
              'torr': 331090.5061221539
          },
       'surge_bhp_mud_weight':
          {
              'g/cm3': 1.6392206764830133,
              'g/L': 1639.2206764830134,
              'kg/m3': 1639.2206764830134,
              'kg/L': 1.6392206764830133,
              'kPa/m': 16.083090224802117,
              'lb/ft3': 102.34255299307607,
              'lb/bbl': 574.5584312996682,
              'ppg': 13.679962649992099,
              'psi/ft': 0.7113963616950092,
              'psi/100ft': 71.09735824493112,
              'SG': 1.6392206764830133              
          },
       'swab_bhp':
          {
              'atm': 360.49237459262906,
              'bar': 365.2688984851445,
              'cm_Hg': 27397.427180463426,
              'cm_h2o': 372471.75267369027,
              'dyne/cm2': 365363964.1243929,
              'ft_air': 9453564.38223358,
              'ft_hg': 898.8653697628498,
              'ft_h2o': 12220.164764181507,
              'in_air': 113442772.58680297,
              'in_hg': 10786.383339089227,
              'in_h2o': 146641.94334488595,
              'kg/cm2': 372.470618761181,
              'kg/m2': 3724796.0907007647,
              'kPa': 36526.89941859047,
              'Mpa': 36.52688992406765,
              'm_Hg': 273.97420521239764,
              'm_h2o': 3724.70626617364,
              'mbar': 365268.2386549524,
              'N/cm2': 3652.6889344826373,
              'N/m2': 36536396.412439294,
              'N/mm2': 36.52688992406765,
              'Pa': 36536396.412439294,
              'psf': 762884.8395547057,
              'psi': 5297.777479803698,
              'torr': 273974.2052978461             
          },
       'swab_bhp_mud_weight':
          {
              'g/cm3': 1.3564393235169867,
              'g/L': 1356.4393235169869,
              'kg/m3': 1356.4393235169869,
              'kg/L': 1.3564393235169867,
              'kPa/m': 13.308602275197885,
              'lb/ft3': 84.68747700692393,
              'lb/bbl': 475.44156870033186,
              'ppg': 11.320037350007901,
              'psi/ft': 0.5886736383049909,
              'psi/100ft': 58.83237925506889,
              'SG': 1.3564393235169867             
          }   
      }

Total Flow Area Function
------------

*tfa_table(nozzle_size, nozzle_count)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - nozzle_size
     - nozzle size in /32 of an inch value (Integer or Float)
   * - nozzle_count
     - number of nozzles on bit value (Integer or Float)

This function is for the calculation of the total flow area of the bit nozzles. It takes in two value inputs(Integers or Floats). The function returns a dictionary containing the total flow area. To see the range of area units that can be returned, see the example code below or review the Area units section of General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import hydraulic_formulas as hydro

   tfa  = hydro.tfa_table(7, 9)
   print(tfa)
   # outputs the following dictionary:
   {
       'acre': 5.3773800000000005e-08,
       'ha': 2.18139e-08,
       'cm2': 2.18139,
       'dm2': 0.0218193112,
       'ft2': 0.003382,
       'in2': 0.3382,
       'km2': 2.1813900000000003e-10,
       'm2': 0.00021983,
       'mi2': 8.42118e-11,
       'mm2': 218.19311199999999,
       'yd2': 0.000260414
   }
       
