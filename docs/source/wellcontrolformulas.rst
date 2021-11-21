Well Control Formulas
==================

This module contains functions, outlined below, for formulas related to well control. 

Gas Migration Rate Function
------------

*gas_migration_rate(pressure_value, pressure_units, mud_value, mud_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - pressure_value
     - shut in casing pressure increase value (Integer or Float)
   * - pressure_units
     - pressure units (String)
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)

This function calculates the gas migration rate of a shut-in well. The function takes in two value inputs(Integers or Floats) and two units inputs(Strings). To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. The function returns a dictionary of different velocity units and values, to see the range of velocity units returned see the example code below or the Velocity units section under Force and Power Conversions.

.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   gas_migration = wcf.gas_migration_rate(pressure_value, pressure_units, mud_value, mud_units)
   print(gas_migration)
   # outputs the following dictionary:
   {
       'ft/d': 6293.706293706294,
       'ft/hr': 262.23776223776224,
       'ft/min': 4.370638111888112,
       'ft/s': 0.07284965034965034,
       'kph': 0.07993006993006993,
       'k/min': 0.0013374125874125876,
       'k/sec': 2.229020979020979e-05,
       'knot': 0.04316433566433566,
       'mach': 6.51215034965035e-05,
       'm/d': 1918.3216783216783,
       'm/hr': 79.93006993006993,
       'm/min': 1.3321678321678323,
       'm/sec': 0.022211538461538463,
       'mph': 0.04966783216783217,
       'mi/min': 0.0008391608391608392,
       'mi/sec': 1.3977272727272728e-05
   }
   # Each key representing a different unit
   print(gas_migration['ft/hr'])
   # outputs the following float:
   262.23776223776224 

Max Shut-in Casing Pressure Function
------------

*max_shutin_casing_pressure(pressure_value, pressure_units, tvd_value, depth_units, original_mud_value, current_mud_value, mud_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - pressure_value
     - lot pressure value (Integer or Float)
   * - pressure_units
     - pressure units (String)
   * - tvd_value
     - true vertical depth value (Integer or Float)
   * - depth_units
     - depth units (String)
   * - original_mud_value
     - original mud weight value (Integer or Float)
   * - current_mud_value
     - current mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)

This function calculates the gas migration rate of a shut-in well. The function takes in four value inputs(Integers or Floats) and three units inputs(Strings). To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions. To see the range of depths units that can be input into the function see the Length units section under General Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. The function returns a dictionary of different pressure units and values, to see the range of pressure units returned see the example code below or the Pressure units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   shutin_pressure = wcf.max_shutin_casing_pressure(pressure_value, pressure_units, mud_value, mud_units)
   print(shutin_pressure)
   # outputs the following dictionary:
   {
       'atm': 28.239074975547002,
       'bar': 28.61324271342401,
       'cm_Hg': 2146.170223879169,
       'cm_h2o': 29177.476394366993,
       'dyne/cm2': 28620689.65517241,
       'ft_air': 740542.4696645254,
       'ft_hg': 70.41238139458525,
       'ft_h2o': 957.2633800623952,
       'in_air': 8886509.635974305,
       'in_hg': 844.9484907183935,
       'in_h2o': 11487.157911053413,
       'kg/cm2': 29.17738756962999,
       'kg/m2': 291780.91823103424,
       'kPa': 2861.3250210117785,
       'Mpa': 2.861324277260841,
       'm_Hg': 21.461697022306414,
       'm_h2o': 291.7738818504201,
       'mbar': 28613.191025800134,
       'N/cm2': 286.13242318861285,
       'N/m2': 2862068.9655172415,
       'N/mm2': 2.861324277260841,
       'Pa': 2862068.9655172415,
       'psf': 59760.38246644778,
       'psi': 415.0,
       'torr': 21461.697029
   }
   # Each key representing a different unit
   print(shutin_pressure['Pa'])
   # outputs the following float:
   2862068.9655172415 

Influx Height Function
------------

*influx_height(gain_value, volume_units, annular_value, annular_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - gain_value
     - pit gain volume value (Integer or Float)
   * - volume_units
     - volume units (String)
   * - annular_value
     - annular capacity value (Integer or Float)
   * - annular_units
     - annular capacity units (String)

This function calculates the influx height. The function takes in two value inputs(Integers or Floats) and two units inputs(Strings). To see the range of volume units that can be input into the function see the Volume units section under General Conversions. To see the range of annular capacity units that can be input into the function see the Pipe Capacity units section under Production Conversions. The function returns a dictionary of different depth units and values, to see the range of depth units returned see the example code below or the Length units section under General Conversions.


.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   influx_height = wcf.influx_height(12, 'bbl', 0.0459, 'bbl/ft')
   print(influx_height)
   # outputs the following dictionary:
   {
       'cm': 7968.627450980392,
       'dm': 796.8627450980391,
       'dam': 7.968627450980391,
       'fath': 43.57299346405228,
       'ft': 261.437908496732,
       'hm': 0.7968627450980391,
       'in': 3137.254901960784,
       'km': 0.07968627450980391,
       'league': 0.01649673202614379,
       'm': 79.68627450980392,
       'mi': 0.04951633986928104,
       'mm': 79686.27450980392,
       'nleague': 0.014352941176470587,
       'nm': 0.043032679738562084,
       'yd': 87.14596078431371
   }
   # Each key representing a different unit
   print(influx_height['ft'])
   # outputs the following float:
   261.437908496732 

Gas Migration Estimation Function
------------

*gas_migration_estimation(mud_value, mud_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - mud_value
     - mud weight values (Integer or Float)
   * - mud_units
     - mud weight units (String)

This function estimates the speed of gas migration based on the mud weight. The function takes in one value input(Integers or Floats) and one units input(String). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. The function returns a dictionary of different speed units and values, to see the range of migration speed units returned see the example code below or the Velocity units section under Force and Power Conversions.

.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   gas_migration = wcf.gas_migration_estimation(12, 'ppg')
   print(gas_migration)
   # outputs the following dictionary:
   {
       'ft/d': 12230.029057278429,
       'ft/hr': 509.5845440532679,
       'ft/min': 8.493075734221131,
       'ft/s': 0.14155126223701886,
       'kph': 0.15532136902743607,
       'k/min': 0.002588689483790601,
       'k/sec': 4.314482472984334e-05,
       'knot': 0.08386682974498544,
       'mach': 0.0001267874655856978,
       'm/d': 3727.7128566584656,
       'm/hr': 155.32136902743605,
       'm/min': 2.588689483790601,
       'm/sec': 0.04314482472984335,
       'mph': 0.09651222682617218,
       'mi/min': 0.0016085319235565874,
       'mi/sec': 2.6809809067691373e-05
   }
   # Each key representing a different unit
   print(gas_migration['ft/hr'])
   # outputs the following float:
   509.5845440532679

Influx Type Estimation Function
------------

*influx_type_estimation(casing_pressure, pipe_pressure, pressure_units, influx_height, height_units, mud_value, mud_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - casing_pressure
     - shutin casing pressure value (Integer or Float)
   * - pipe_pressure
     - shutin pipe pressure value (Integer or Float)
   * - pressure_units
     - pressure units (String)
   * - influx_height
     - influx height value (Integer or Float)
   * - height_units
     - height units (String)
   * - mud_value
     - mud weight values (Integer or Float)
   * - mud_units
     - mud weight units (String)

This function calculates estimates the weight and type of influx. The function takes in four value inputs(Integers or Floats) and three units inputs(Strings). To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions. To see the range of height units that can be input into the function see the Length units section under General Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. The function returns a dictionary of one subdictionary of different influx weight units and values, and a string estimating the influx type. To see the range of influx weight units returned see the example code below or the Mud Weight units section under Drilling Conversions.


.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   influx_estimation = wcf.influx_type_estimation(1050, 750, 'psi', 450, 'ft', 14, 'ppg')
   print(influx_estimation)
   # outputs the following dictionary:
   {
       'water_added_per_100': 
          {
              'influx_type': 'Gas Influx',
              'influx_weight': 
              {
                  'g/cm3': 0.1413337025641025,
                  'g/L': 141.3337025641025,
                  'kg/m3': 141.3337025641025,
                  'kg/L': 0.1413337025641025,
                  'kPa/m': 1.3866849794871787,
                  'lb/ft3': 8.823980902564099,
                  'lb/bbl': 49.53846153846151,
                  'ppg': 1.1794871794871788,
                  'psi/ft': 0.06133663589743587,
                  'psi/100ft': 6.130018384615382,
                  'SG': 0.1413337025641025
              }
      } 

Final Circulating Pressure Function
------------

*final_circulating_pressure(pressure_value, pressure_units, kill_mud, original_mud, mud_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - pressure_value
     - slow circulation rate values (Integer or Float)
   * - pressure_units
     - pressure units (String)
   * - kill_mud
     - kill mud weight values (Integer or Float)
   * - original_mud
     - original mud weight values (Integer or Float)
   * - mud_units
     - mud weight units (String)

This function estimates the speed of gas migration based on the mud weight. The function takes in three value inputs (Integers or Floats) and two units input(String). To see the range of SCR pressure units that can be input into the function see the Pressure units section under General Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. The function returns a dictionary of final circulating pressure units and values, to see the range of pressure units returned see the example code below or the Pressure units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   final_pressure = wcf.final_circulating_pressure(450, 'psi', 12, 10, 'ppg')
   print(final_pressure)
   # outputs the following dictionary:
   {
       'atm': 36.74482045010935,
       'bar': 37.231689313852925,
       'cm_Hg': 2792.6070383006054,
       'cm_h2o': 37965.8728986944,
       'dyne/cm2': 37241379.31034482,
       'ft_air': 963597.4304068523,
       'ft_hg': 91.62093000741214,
       'ft_h2o': 1245.595723454683,
       'in_air': 11563169.164882228,
       'in_hg': 1099.4510481636928,
       'in_h2o': 14947.145233659863,
       'kg/cm2': 37.965757319518545,
       'kg/m2': 379666.73697532166,
       'kPa': 3723.1699068586995,
       'Mpa': 3.723168939086396,
       'm_Hg': 27.926063595290277,
       'm_h2o': 379.6575812029563,
       'mbar': 37231.62205766764,
       'N/cm2': 372.31688800446005,
       'N/m2': 3724137.931034483,
       'N/mm2': 3.723168939086396,
       'Pa': 3724137.931034483,
       'psf': 77760.49766718506,
       'psi': 540.0,
       'torr': 27926.063604
   }
   # Each key representing a different unit
   print(final_pressure['psi'])
   # outputs the following float:
   540.0 

Initial Circulating Pressure Function
------------

*inital_circulating_pressure(scr_value, sidpp_value, pressure_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - scr_value
     - slow circulation pressure values (Integer or Float)
   * - sidpp_value
     - shutin drillpipe pressure values (Integer or Float)
   * - pressure_units
     - pressure units (String)

This function estimates the speed of gas migration based on the mud weight. The function takes in two value inputs (Integers or Floats) and one units input(String). To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions. The function returns a dictionary of initial circulating pressure units and values, to see the range of pressure units returned see the example code below or the Pressure units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   inital_pressure = wcf.inital_circulating_pressure(400, 500, 'psi')
   print(inital_pressure)
   # outputs the following dictionary:
   {
       'atm': 61.24136741684892,
       'bar': 62.05281552308821,
       'cm_Hg': 4654.345063834342,
       'cm_h2o': 63276.45483115733,
       'dyne/cm2': 62068965.51724137,
       'ft_air': 1605995.717344754,
       'ft_hg': 152.70155001235355,
       'ft_h2o': 2075.9928724244714,
       'in_air': 19271948.60813705,
       'in_hg': 1832.4184136061547,
       'in_h2o': 24911.90872276644,
       'kg/cm2': 63.27626219919757,
       'kg/m2': 632777.8949588694,
       'kPa': 6205.283178097833,
       'Mpa': 6.205281565143993,
       'm_Hg': 46.543439325483796,
       'm_h2o': 632.7626353382605,
       'mbar': 62052.703429446075,
       'N/cm2': 620.5281466741001,
       'N/m2': 6206896.551724138,
       'N/mm2': 6.205281565143993,
       'Pa': 6206896.551724138,
       'psf': 129600.82944530844,
       'psi': 900,
       'torr': 46543.43934
   }
   # Each key representing a different unit
   print(inital_pressure['psi'])
   # outputs the following float:
   900 

Formation Pressure Kick Analysis Function
------------

*formation_pressure_kick_analysis(sidpp_value, pressure_units, tvd_value, depth_units, mud_value, mud_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - sidpp_value
     - shutin drillpipe pressure values (Integer or Float)
   * - pressure_units
     - pressure units (String)
   * - tvd_value
     - true vertical depth value (Integer or Float)
   * - depth_units
     - depth units (String)
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)

This function calculates the formation pressure using shut-in drillpipe pressure. The function takes in three value inputs(Integers or Floats) and three units inputs(Strings). To see the range of SIDPP pressure units that can be input into the function see the Pressure units section under General Conversions. To see the range of depth units that can be input into the function see the Length units section under General Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. The function returns a dictionary of different pressure units and values, to see the range of pressure units returned see the example code below or the Pressure units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   formation_pressure = wcf.formation_pressure_kick_analysis(550, 'psi', 6000, 'ft', 10.2, 'ppg')
   print(formation_pressure)
   # outputs the following dictionary:
   {
       'atm': 253.9747552740521,
       'bar': 257.3399207315271,
       'cm_Hg': 19302.086129172552,
       'cm_h2o': 262414.4889020129,
       'dyne/cm2': 257406896.55172408,
       'ft_air': 6660242.683797288,
       'ft_hg': 633.2702947401204,
       'ft_h2o': 8609.373107818996,
       'in_air': 79922912.20556745,
       'in_hg': 7599.242763270679,
       'in_h2o': 103312.4534631705,
       'kg/cm2': 262.4136900358722,
       'kg/m2': 2624200.2390494267,
       'kPa': 25733.998815480387,
       'Mpa': 25.733992126381597,
       'm_Hg': 193.02081437603965,
       'm_h2o': 2624.136955707248,
       'mbar': 257339.45586673834,
       'N/cm2': 2573.3991718293455,
       'N/m2': 25740689.65517241,
       'N/mm2': 25.733992126381597,
       'Pa': 25740689.65517241,
       'psf': 537469.0398018546,
       'psi': 3732.3999999999996,
       'torr': 193020.81443623998
   }
   # Each key representing a different unit
   print(formation_pressure['psi'])
   # outputs the following float:
   3732.3999999999996

Pressure Loss due to Gas Cut Function
------------

*pressure_loss_gas_cut(mud_value, mud_units, annular_value, annular_units, gain_value, gain_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - annular_value
     - annular capacity value (Integer or Float)
   * - annular_units
     - annular capacity units (String)
   * - gain_value
     - pit gain value (Integer or Float)
   * - gain_units
     - volume units (String)

This function calculates the formation pressure loss due to gas cut. The function takes in three value inputs(Integers or Floats) and three units inputs(Strings).  To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of annular capacity units that can be input into the function see the Pipe Capacity units section under Production Conversions. To see the range of gain volume units that can be input into the function see the Volume units section under General Conversions. The function returns a dictionary of different pressure units and values, to see the range of pressure units returned see the example code below or the Pressure units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   pressure_loss = wcf.pressure_loss_gas_cut(12, 'ppg', 0.0352, 'bbl/ft', 15, 'bbl')
   print(pressure_loss)
   # outputs the following dictionary:
   {
       'atm': 18.094040373159906,
       'bar': 18.33378640454879,
       'cm_Hg': 1375.1474052237827,
       'cm_h2o': 18695.316200114663,
       'dyne/cm2': 18338557.993730403,
       'ft_air': 474498.73467004084,
       'ft_hg': 45.116367049104454,
       'ft_h2o': 613.3615304890483,
       'in_air': 5693984.816040491,
       'in_hg': 541.3963494745457,
       'in_h2o': 7360.336668090084,
       'kg/cm2': 18.695259286126554,
       'kg/m2': 186957.10532875685,
       'kPa': 1833.379120801632,
       'Mpa': 1.8333786442470887,
       'm_Hg': 13.751470709802028,
       'm_h2o': 186.95259680448603,
       'mbar': 18333.753285972703,
       'N/cm2': 183.33786151734773,
       'N/m2': 1833855.7993730407,
       'N/mm2': 1.8333786442470887,
       'Pa': 1833855.7993730407,
       'psf': 38291.15415429567,
       'psi': 265.9090909090909,
       'torr': 13751.470714090907
   }
   # Each key representing a different unit
   print(pressure_loss['psi'])
   # outputs the following float:
   265.9090909090909 

Casing Pressure Increase due to Kick Penetration Function
------------

*kick_penetration_pressure_increase(gain_value, gain_units, mud_value, kick_value, mud_units, hole_id_value, bha_od_value, pipe_od_value, dia_value, bha_length, length_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - gain_value
     - pit gain value (Integer or Float)
   * - gain_units
     - volume units (String)
   * - mud_value
     - mud weight value (Integer or Float)
   * - kick_value
     - kick density value (Integer or Float)
   * - mud_units
     - mud/kick weight units (String)
   * - hole_id_value
     - hole inner diameter value (Integer or Float)
   * - bha_od_value
     - bha outer diameter value (Integer or Float)
   * - pipe_od_value
     - pipe outer diameter value (Integer or Float)
   * - dia_value
     - diameter units (String)
   * - bha_length
     - bha length value (Integer or Float)
   * - length_units
     - length units (String)

This function calculates the increase in casing pressure due to kick penetration. The function takes in seven value inputs(Integers or Floats) and four units inputs(Strings). To see the range of pit gain volume units that can be input into the function see the Volume units section under General Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of diameter and depth units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary of different pressure units and values, to see the range of pressure units returned see the example code below or the Pressure units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   pressure_increase = wcf.kick_penetration_pressure_increase(30, 'bbl', 11, 2, 'ppg', 12.25, 6.5, 5, 'in', 800, 'ft')
   print(pressure_increase)
   # outputs the following dictionary:
   {
       'atm': 2.56826043053855,
       'bar': 2.6022898807385215,
       'cm_Hg': 195.18784053521082,
       'cm_h2o': 2653.605266869186,
       'dyne/cm2': 2602967.15808693,
       'ft_air': 67350.14952223499,
       'ft_hg': 6.403798039145906,
       'ft_h2o': 87.06027597386668,
       'in_air': 808201.79426682,
       'in_hg': 76.84556864679257,
       'in_h2o': 1044.7230707044391,
       'kg/cm2': 2.6535971885218075,
       'kg/m2': 26536.612382943462,
       'kPa': 260.22905625406696,
       'Mpa': 0.2602289886121168,
       'm_Hg': 1.9518779309281857,
       'm_h2o': 26.535972444917125,
       'mbar': 2602.2851799018526,
       'N/cm2': 26.022898448542072,
       'N/m2': 260296.71580869303,
       'N/mm2': 0.2602289886121168,
       'Pa': 260296.71580869303,
       'psf': 5435.0302102788555,
       'psi': 37.74302379226049,
       'torr': 1951.8779315369475
   }
   # Each key representing a different unit
   print(pressure_increase['psi'])
   # outputs the following float:
   37.74302379226049 

Kick Tolerance Factor Function
------------

*kick_tolerance_factor(shoe_value, tvd_value, depth_units, max_mud_value, mud_value, mud_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - shoe_value
     - shoe depth value (Integer or Float)
   * - tvd_value
     - true vertical depth value (Integer or Float)
   * - depth_units
     - depth units (String)
   * - max_mud_value
     - maximum allowable mud weight value (Integer or Float)
   * - mud_value
     - current mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)

This function calculates the kick tolerance factor. The function takes in four value inputs(Integers or Floats) and two units inputs(Strings). To see the range of depth units that can be input into the function see the Length units section under General Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions.  The function returns a dictionary of different mud weight units and values, to see the range of mud weight units returned see the example code below or the Mud Weight units section under Drilling Conversions.

.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   kick_tolerance = wcf.kick_tolerance_factor(4000, 10000, 'ft', 14.2, 10, 'ppg')
   print(kick_tolerance)
   # outputs the following dictionary:
   {
       'g/cm3': 0.20130835199999997,
       'g/L': 201.30835199999999,
       'kg/m3': 201.30835199999999,
       'kg/L': 0.20130835199999997,
       'kPa/m': 1.9751217359999997,
       'lb/ft3': 12.568418015999997,
       'lb/bbl': 70.55999999999999,
       'ppg': 1.6799999999999997,
       'psi/ft': 0.08736470399999999,
       'psi/100ft': 8.73127836,
       'SG': 0.20130835199999997
   }
   # Each key representing a different unit
   print(kick_tolerance['ppg'])
   # outputs the following float:
   1.6799999999999997 

Required Kill Mud Weight Function
------------

*kill_mud_weight(pressure_value, pressure_units, mud_value, mud_units, tvd_value, depth_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1
   
   * - mud_value
     - current mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - pressure_units
     - shutin drillpipe pressure value (Integer or Float)
   * - pressure_units
     - pressure units (String)
   * - tvd_value
     - true vertical depth value (Integer or Float)
   * - depth_units
     - depth units (String)

This function calculates the mud weight required for kill mud. The function takes in three value inputs(Integers or Floats) and three units inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions. To see the range of depth units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary of different mud weight units and values, to see the range of mud weight units returned see the example code below or the Mud Weight units section under Drilling Conversions.

.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   kill_mud = wcf.kill_mud_weight(500, 'psi', 9.5, 'ppg', 9000, 'ft')
   print(kill_mud)
   # outputs the following dictionary:
   {
       'g/cm3': 1.266370458119658,
       'g/L': 1266.3704581196582,
       'kg/m3': 1266.3704581196582,
       'kg/L': 1.266370458119658,
       'kPa/m': 12.424898385042734,
       'lb/ft3': 79.06414772478632,
       'lb/bbl': 443.87179487179486,
       'ppg': 10.568376068376068,
       'psi/ft': 0.549585147008547,
       'psi/100ft': 54.92585313461539,
       'SG': 1.266370458119658
   }
   # Each key representing a different unit
   print(kill_mud['ppg'])
   # outputs the following float:
   10.568376068376068 

Fluid Increment(Lube or Mud) Function
------------

*fluid_increment(pressure_value, pressure_units, casing_id_value, pipe_od_value, dia_units, mud_value, mud_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - pressure_units
     - pressure increment value (Integer or Float)
   * - pressure_units
     - pressure units (String)
   * - casing_id_value
     - casing inner diameter value (Integer or Float)
   * - pipe_od_value
     - pipe outer diameter value (Integer or Float)
   * - dia_value
     - diameter units (String)
   * - mud_value
     - mud volume value (Integer or Float)
   * - mud_units
     - volume units (String)

This function calculates the fluid increment volume. The function takes in four value inputs(Integers or Floats) and three units inputs(Strings). To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions. To see the range of diameter units that can be input into the function see the Length units section under General Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under General Conversions. The function returns a dictionary with two sub-dictionaries:

   * - "annular_capacity" which is a dictionary of different annular capacity units and values, to see the range of annular capacity units returned see the example code below or the Pipe Capacity units section under Production Conversions.
   * - "lube_increment" which is a dictionary of different volume units and values, to see the range of volume units returned see the example code below or the Volume units section under General Conversions.


.. code:: python

   # Example Code
   from ogPypeline import drilling_fluid_formulas as dff

   fluid_added = dff.fluid_increment(100, 'psi', 12.5, 5, 'in', 11, 'ppg')
   print(fluid_added)
   # outputs the following dictionary:
   {
       'annular_capacity': 
          {
              'bbl/ft': 0.1275014571595104,
              'm3/m': 0.06651164513308723,
              'bbl/in': 0.010625121429959195,
              'ft3/ft': 0.7158675563435006,
              'gal(us)/ft': 5.355061200699437,
              'l/m': 66.50627222168252,
              'dm3/m': 66.50627222168252,
              'in3/ft': 1237.0191373615698
          },
       'lube_increment':
          {
              'bbl': 22.290464538375943,
              'bucket': 187.23990212235793,
              'bu_us': 100.56737171901345,
              'cm3': 3543900.6596560464,
              'ft3': 125.15166994640776,
              'in3': 216262.0869513234,
              'm3': 3.5439007727021377,
              'mm3': 3543900659.6568937,
              'yd3': 4.635246374593931,
              'C': 14979.192169788634,
              'dr': 958668.2988664726,
              'drum': 17.021810094413066,
              'fl_oz': 119833.53735830907,
              'gal_us': 936.1995106117896,
              'gill': 29958.384339577267,
              'gal_uk': 779.5491651647847,
              'kL': 3.5439007727021377,
              'L': 3543.900659020768,
              'ml': 3543900.6596560464,
              'Pt': 7489.596084894317,
              'qt_dr': 3218.1558660308265,
              'qt_lq': 3744.7980424471584,
              'tbsp': 239667.07471661814,
              'tsp': 719001.2241498544,
              'toe': 3.039607990125282
          }
      } 

Maximum Formation Pressure for Shutin Well Function
------------

*max_formation_pressure(kick_factor, mud_value, mud_units, tvd_value, depth_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - kick_factor
     - kick factor value (Integer or Float)
   * - mud_value
     - fluid weight value (Integer or Float)
   * - mud_units
     - mud weight and kick factor units (String)
   * - tvd_value
     - true vertical depth value (Integer or Float)
   * - depth_units
     - depth units (String)

This function calculates the maximum formation pressure that can be withstood when the well is shut-in. The function takes in three value inputs(Integers or Floats) and two units inputs(Strings). To see the range of mud weight/kick factor units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of depth units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary of different pressure units and values, to see the range of pressure units returned see the example code below or the Pressure units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   formation_pressure = wcf.max_formation_pressure(1.68, 10, 'ppg', 10000, 'ft')
   print(formation_pressure)
   # outputs the following dictionary:
   {
       'atm': 413.2839657144151,
       'bar': 418.7599781789207,
       'cm_Hg': 31409.589088560293,
       'cm_h2o': 427017.6400694635,
       'dyne/cm2': 418868965.51724136,
       'ft_air': 10837972.876516774,
       'ft_hg': 1030.497926838923,
       'ft_h2o': 14009.72256661919,
       'in_air': 130055674.5182013,
       'in_hg': 12365.973863198158,
       'in_h2o': 168116.6320206603,
       'kg/cm2': 427.0163401033849,
       'kg/m2': 4270266.469802433,
       'kPa': 41876.008789438885,
       'Mpa': 41.87599790450951,
       'm_Hg': 314.09581454139817,
       'm_h2o': 4270.16349110051,
       'mbar': 418759.2217212041,
       'N/cm2': 4187.599724044238,
       'N/m2': 41886896.55172414,
       'N/mm2': 41.87599790450951,
       'Pa': 41886896.55172414,
       'psf': 874603.9974655837,
       'psi': 6073.6,
       'torr': 314095.81463936
      } 
   # Each key representing a different unit
   print(formation_pressure['psi'])
   # outputs the following float:
   6073.6 

Maximum Influx Height Function
------------

*max_influx_height(casing_pressure, pressure_units, mud_value, influx_value, gradient_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - casing_pressure
     - maximum allowable shut in casing pressure value (Integer or Float)
   * - pressure_units
     - pressure units (String)
   * - mud_value
     - mud gradient value (Integer or Float)
   * - influx_value
     - influx gradient value (Integer or Float)
   * - gradient_units
     - gradient units (String)

This function calculates the maximum controllable influx height based on the maximum allowable shut-in casing pressure. The function takes in three value inputs(Integers or Floats) and two units inputs(Strings). To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions. To see the range of pressure gradient units that can be input into the function see the Pressure Gradient units section under Drilling Conversions. The function returns a dictionary of different height units and values, to see the range of depth units returned see the example code below or the Length units section under General Conversions.
.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   max_height = wcf.max_influx_height(874, 'psi', 0.52, 0.12, 'psi/ft')
   print(max_height)
   # outputs the following dictionary:
   {
       'cm': 66598.8,
       'dm': 6659.88,
       'dam': 66.5988,
       'fath': 364.1667395,
       'ft': 2185.0,
       'hm': 6.65988,
       'in': 26220.0,
       'km': 0.6659879999999999,
       'league': 0.1378735,
       'm': 665.988,
       'mi': 0.413839,
       'mm': 665988.0,
       'nleague': 0.1199565,
       'nm': 0.359651,
       'yd': 728.3332605
      } 
   # Each key representing a different unit
   print(max_height['m'])
   # outputs the following float:
   665.988 

Maximum Initial Shut-in Casing Pressure Function
------------

*misicp(lot_value, mud_value, mud_units, tvd_value, depth_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - lot_value
     - leak off test value (Integer or Float)
   * - mud_value
     - current mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - tvd_value
     - true vertical depth value (Integer or Float)
   * - depth_units
     - depth units (String)

This function calculates the maximum initial/allowable shut-in casing pressure using the leak-off test results. The function takes in three value inputs(Integers or Floats) and two units inputs(Strings). The function returns a dictionary of different pressure units and values, to see the range of pressure units returned see the example code below or the Pressure units section under General Conversions.


.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   misicp = wcf.misicp(15, 12.2, 'ppg', 4000, 'ft')
   print(misicp)
   # outputs the following dictionary:
   {
       'atm': 39.629969315080906,
       'bar': 40.155066400718425,
       'cm_Hg': 3011.878405752357,
       'cm_h2o': 40946.89699296226,
       'dyne/cm2': 40165517.24137931,
       'ft_air': 1039257.6730906498,
       'ft_hg': 98.81486969688304,
       'ft_h2o': 1343.398054333347,
       'in_air': 12471092.077087797,
       'in_hg': 1185.7783156491384,
       'in_h2o': 16120.772933487973,
       'kg/cm2': 40.946772338680745,
       'kg/m2': 409477.606693384,
       'kPa': 4015.507692137976,
       'Mpa': 4.015506648377625,
       'm_Hg': 30.118776736846407,
       'm_h2o': 409.4677320233366,
       'mbar': 40154.99386367711,
       'N/cm2': 401.55065846999554,
       'N/m2': 4016551.7241379316,
       'N/mm2': 4.015506648377625,
       'Pa': 4016551.7241379316,
       'psf': 83866.13674327517,
       'psi': 582.4000000000001,
       'torr': 30118.776746240004
      } 
   # Each key representing a different unit
   print(misicp['psi'])
   # outputs the following float:
   582.4000000000001 

Max Pit Gain from Gas Kick(Water-Based Mud) Function
------------

*max_pit_gain_gas_kick_wbm(pressure_value, pressure_units, pit_gain, volume_units, mud_value, mud_units, annular_value, annular_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - pressure_value
     - formation pressure value (Integer or Float)
   * - pressure_units
     - pressure units (String)
   * - pit_gain
     - pit gain volume value (Integer or Float)
   * - vol_units
     - volume units (String)
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - kill mud weight units (String)
   * - annular_value
     - annular value (Integer or Float)
   * - annular_units
     - annular capcity units (String)

This function calculates the required volume of fluid required to reduce the mud weight. The function takes in four value inputs(Integers or Floats) and four units inputs(Strings). To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions. To see the range of volume units that can be input into the function see the Volume units section under General Conversions. To see the range of annular capacity units that can be input into the function see the Pipe Capacity units section under Production Conversions. The function returns a dictionary of different volume units and values, to see the range of volume units returned see the example code below or the Volume units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   pit_gain = wcf.max_pit_gain_gas_kick_wbm(3620, 'psi', 20, 'bbl', 14.5, 'ppg', 0.1215, 'bbl/ft')
   print(pit_gain)
   # outputs the following dictionary:
   {
       'bbl': 98.52204374376466,
       'bucket': 827.5851674476231,
       'bu_us': 444.49961904732817,
       'cm3': 15663753.225648489,
       'ft3': 553.1602214856105,
       'in3': 955860.8684020047,
       'm3': 15.663753725303033,
       'mm3': 15663753225.652233,
       'yd3': 20.4874126914065,
       'C': 66206.81339580985,
       'dr': 4237236.05733183,
       'drum': 75.23501880513096,
       'fl_oz': 529654.5071664788,
       'gal_us': 4137.9258372381155,
       'gill': 132413.6267916197,
       'gal_uk': 3445.5440270683516,
       'kL': 15.663753725303033,
       'L': 15663.75322284061,
       'ml': 15663753.225648489,
       'Pt': 33103.406697904924,
       'qt_dr': 14223.987681435843,
       'qt_lq': 16551.703348952462,
       'tbsp': 1059309.0143329576,
       'tsp': 3177927.0429988727,
       'toe': 13.434820564257226
   }
   # Each key representing a different unit
   print(pit_gain['bbl'])
   # outputs the following float:
   98.52204374376466 

Maximum Surface Pressure from Gas Kick(Water-Based Mud) Function
------------

*def max_surface_pressure_gas_influx_wbm(pressure_value, pressure_units, pit_gain, volume_units, mud_value, mud_units, annular_value, annular_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - pressure_value
     - formation pressure value (Integer or Float)
   * - pressure_units
     - pressure units (String)
   * - pit_gain
     - pit gain volume value (Integer or Float)
   * - vol_units
     - volume units (String)
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - kill mud weight units (String)
   * - annular_value
     - annular value (Integer or Float)
   * - annular_units
     - annular capcity units (String)

This function calculates the required volume of fluid required to reduce the mud weight. The function takes in four value inputs(Integers or Floats) and four units inputs(Strings). To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions. To see the range of volume units that can be input into the function see the Volume units section under General Conversions. To see the range of annular capacity units that can be input into the function see the Pipe Capacity units section under Production Conversions. The function returns a dictionary of different pressure units and values, to see the range of pressure units returned see the example code below or the Pressure units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   surface_pressure = wcf.max_surface_pressure_gas_influx_wbm(6378, 'psi', 25, 'bbl', 13, 'ppg', 0.0459, 'bbl/ft')
   print(surface_pressure)
   # outputs the following dictionary:
   {
       'atm': 91.45552783224052,
       'bar': 92.66731355804666,
       'cm_Hg': 6950.621817912618,
       'cm_h2o': 94494.64994056104,
       'dyne/cm2': 92691431.34479874,
       'ft_air': 2398332.8952526446,
       'ft_hg': 228.0386844095657,
       'ft_h2o': 3100.208762995616,
       'in_air': 28779994.743031733,
       'in_hg': 2736.463934339932,
       'in_h2o': 37202.49657460098,
       'kg/cm2': 94.49436227132209,
       'kg/m2': 944966.4307808351,
       'kPa': 9266.733783696114,
       'Mpa': 9.266731374972224,
       'm_Hg': 69.50620128493206,
       'm_h2o': 944.9436426440548,
       'mbar': 92667.14616166672,
       'N/cm2': 926.673122802094,
       'N/m2': 9269143.134479875,
       'N/mm2': 9.266731374972224,
       'Pa': 9269143.134479875,
       'psf': 193540.94731000255,
       'psi': 1344.0257544995818,
       'torr': 69506.20130661002
   }
   # Each key representing a different unit
   print(surface_pressure['psi'])
   # outputs the following float:
   1344.0257544995818 

Maximum Surface Pressure from Kick Tolerance Data Function
------------

*max_surface_pressure_kick_tolerance(mud_value, mud_units, tvd_value, depth_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - mud_value
     - kick tolerance factor value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - tvd_value
     - true vertical depth value (Integer or Float)
   * - depth_units
     - depth units (String)

This function calculates the maximum surface pressure from the kick tolerance factor. The function takes in two value inputs(Integers or Floats) and two units inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of depth units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary of different pressure units and values, to see the range of pressure units returned see the example code below or the Pressure units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   surface_pressure = wcf.max_surface_pressure_kick_tolerance(1.68, 'ppg', 10000, 'ft')
   print(surface_pressure)
   # outputs the following dictionary:
   {
       'atm': 59.44495397262134,
       'bar': 60.23259960107762,
       'cm_Hg': 4517.817608628534,
       'cm_h2o': 61420.345489443374,
       'dyne/cm2': 60248275.86206895,
       'ft_air': 1558886.5096359742,
       'ft_hg': 148.2223045453245,
       'ft_h2o': 2015.09708150002,
       'in_air': 18706638.115631692,
       'in_hg': 1778.6674734737073,
       'in_h2o': 24181.159400231954,
       'kg/cm2': 61.4201585080211,
       'kg/m2': 614216.4100400759,
       'kPa': 6023.2615382069625,
       'Mpa': 6.023259972566436,
       'm_Hg': 45.1781651052696,
       'm_h2o': 614.2015980350047,
       'mbar': 60232.49079551565,
       'N/cm2': 602.3259877049932,
       'N/m2': 6024827.586206896,
       'N/mm2': 6.023259972566436,
       'Pa': 6024827.586206896,
       'psf': 125799.20511491272,
       'psi': 873.5999999999999,
       'torr': 45178.16511935999
      }
   # Each key representing a different unit
   print(surface_pressure['psi'])
   # outputs the following float:
   873.5999999999999

Pressure Loss at New Mud Weight Function
------------

*new_mud_pressure_loss(pressure_value, pressure_units, old_value, new_value, mud_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - pressure_value
     - pressure loss value (Integer or Float)
   * - pressure_units
     - pressure units (String)
   * - old_value
     - old mud weight value (Integer or Float)
   * - new_value
     - new mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)

This function calculates the new pressure loss when the mud weight changes. The function takes in three value inputs(Integers or Floats) and two units inputs(Strings). To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. The function returns a dictionary of different pressure units and values representing the new pressure loss, to see the range of pressure units returned see the example code below or the Pressure units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   pressure_loss = wcf.new_mud_pressure_loss(1400, 'psi', 11.5, 12.5, 'ppg')
   print(pressure_loss)
   # outputs the following dictionary:
   {
       'atm': 103.54820577728077,
       'bar': 104.92021948348248,
       'cm_Hg': 7869.66556686966,
       'cm_h2o': 106989.17483529016,
       'dyne/cm2': 104947526.23688154,
       'ft_air': 2715451.695993545,
       'ft_hg': 258.19102659093596,
       'ft_h2o': 3510.132876080024,
       'in_air': 32585420.35192254,
       'in_hg': 3098.2920036819037,
       'in_h2o': 42121.58479694808,
       'kg/cm2': 106.988849129078,
       'kg/m2': 1069914.3151478467,
       'kPa': 10492.024697266866,
       'Mpa': 10.49202197005023,
       'm_Hg': 78.69663654067307,
       'm_h2o': 1069.8885138569622,
       'mbar': 104920.02995316968,
       'N/cm2': 1049.2021803668358,
       'N/m2': 10494752.623688156,
       'N/mm2': 10.49202197005023,
       'Pa': 10494752.623688156,
       'psf': 219131.83722636692,
       'psi': 1521.7391304347825,
       'torr': 78696.63656521738
      }
   # Each key representing a different unit
   print(pressure_loss['psi'])
   # outputs the following float:
   1521.7391304347825

Pressure at New Pump Strokes Function
------------

*new_strokes_pump_pressure(pressure_value, pressure_units, old_stokes, new_stokes)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - pressure_value
     - curent pressure value (Integer or Float)
   * - pressure_units
     - pressure units (String)
   * - old_stokes
     - old pump strokes value (Integer or Float)
   * - new_stokes
     - new pump strokes value (Integer or Float)

This function calculates the new pump pressure loss when the stroke rate changes. The function takes in three value inputs(Integers or Floats) and one units input(Strings). To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions. The function returns a dictionary of different pressure units and values representing the new pump pressure, to see the range of pressure units returned see the example code below or the Pressure units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   new_pressure = wcf.new_strokes_pump_pressure(1600, 'psi', 70, 110)
   print(new_pressure)
   # outputs the following dictionary:
   {
       'atm': 268.85099165310544,
       'bar': 272.4132672396798,
       'cm_Hg': 20432.680370937156,
       'cm_h2o': 277785.0715490263,
       'dyne/cm2': 272484166.08022517,
       'ft_air': 7050357.616279917,
       'ft_hg': 670.3632671744137,
       'ft_h2o': 9113.655784611738,
       'in_air': 84604291.39535901,
       'in_hg': 8044.358387168969,
       'in_h2o': 109363.84418883407,
       'kg/cm2': 277.78422589035483,
       'kg/m2': 2777909.3075745376,
       'kPa': 27241.3338612186,
       'Mpa': 27.241326780314672,
       'm_Hg': 204.32675404566126,
       'm_h2o': 2777.8423174940413,
       'mbar': 272412.775146049,
       'N/cm2': 2724.1326348323305,
       'N/m2': 27248416.60802252,
       'N/mm2': 27.241326780314672,
       'Pa': 27248416.60802252,
       'psf': 568950.5800592225,
       'psi': 3951.020408163265,
       'torr': 204326.75410938772
      }
   # Each key representing a different unit
   print(new_pressure['psi'])
   # outputs the following float:
   3951.020408163265

Riser Margin Function
------------

*riser_margin(air_gap, water_depth, tvd_value, depth_units, mud_value, water_value, mud_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - air_gap
     - air gap value (Integer or Float)
   * - water_depth
     - water depth value (Integer or Float)
   * - tvd_value
     - true vertical depth value (Integer or Float)
   * - depth_units
     - depth units (String)
   * - mud_value
     - mud weight equivelant to formation pressure value (Integer or Float)
   * - water_value
     - sea water density value (Integer or Float)
   * - mud_units
     - mud weight units (String)

This function calculates the new pump pressure loss when the stroke rate changes. The function takes in five value inputs(Integers or Floats) and two units inputs(Strings). To see the range of depth units that can be input into the function see the Length units section under General Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. The function returns a dictionary of different mud weight units and values representing the riser margin, to see the range of mud weight units returned see the example code below or the Mud Weight units section under Drilling Conversions.

.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   riser_margin = wcf.riser_margin(60, 1600, 3000, 'ft', 9.3, 8.6, 'ppg')
   print(riser_margin)
   # outputs the following dictionary:
   {
       'g/cm3': 0.15005126805970165,
       'g/L': 150.05126805970167,
       'kg/m3': 150.05126805970167,
       'kg/L': 0.15005126805970165,
       'kPa/m': 1.4722167168656732,
       'lb/ft3': 9.368250457910458,
       'lb/bbl': 52.594029850746324,
       'ppg': 1.2522388059701506,
       'psi/ft': 0.06511992417910455,
       'psi/100ft': 6.508122373880604,
       'SG': 0.15005126805970165
      }
   # Each key representing a different unit
   print(riser_margin['ppg'])
   # outputs the following float:
   1.2522388059701506

Time to Penetrate Kick Function
------------

*time_penetrate_kick(kick_depth, bit_depth, depth_units, migration_value, stripping_value, velocity_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - kick_depth
     - top of kick depth value (Integer or Float)
   * - bit_depth
     - bit depth value (Integer or Float)
   * - depth_units
     - depth units (String)
   * - migration_value
     - mud weight equivelant to formation pressure value (Integer or Float)
   * - stripping_value
     - sea water density value (Integer or Float)
   * - velocity_units
     - mud weight units (String)

This function calculates the time to penetrate a kick. The function takes in four value inputs(Integers or Floats) and two units inputs(Strings). To see the range of depth units that can be input into the function see the Length units section under General Conversions. To see the range of velocity units that can be input into the function see the Velocity units section under Force and Power Conversions. The function returns a dictionary of different time units and values, to see the range of time units returned see the example code below or the Time units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   penetration_time = wcf.time_penetrate_kick(8974, 6500, 'ft', 262, 200, 'ft/hr')
   print(penetration_time)
   # outputs the following dictionary:
   {
       'day': 0.22312427662337664,
       'decade': 6.104675324675324e-05,
       'hr': 5.354978354978355,
       'minute': 321.2987012987013,
       'sec': 19277.922077922078,
       'yr': 0.0006115385281385281
      }
   # Each key representing a different unit
   print(penetration_time['minute'])
   # outputs the following float:
   321.2987012987013

Trip Margin Calculation Function
------------

*trip_margin(yield_value, yield_units, hole_id, pipe_od, dia_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - yield_value
     - mud yield point value (Integer or Float)
   * - yield_units
     - mud yield point units (String)
   * - hole_id
     - hole inner diameter value (Integer or Float)
   * - pipe_od
     - pipe outer diameter value (Integer or Float)
   * - dia_units
     - diameter units (String)

This function calculates the trip margin to compensate for the effect of swabbing during pull out of hole. The function takes in three value inputs(Integers or Floats) and two units inputs(Strings). To see the range of yield point units that can be input into the function see the Fluid Yield Point units section under Fluids Conversions. To see the range of diameter units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary of different mud weight units and values, to see the range of mud weight units returned see the example code below or the Mud Weight units section under Drilling Conversions.

.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   trip_margin = wcf.trip_margin(10, 'lbf/100ft2', 8.5, 4.5, 'in')
   print(trip_margin)
   # outputs the following dictionary:
   {
       'g/cm3': 0.025603931623931625,
       'g/L': 25.60393162393163,
       'kg/m3': 25.60393162393163,
       'kg/L': 0.025603931623931625,
       'kPa/m': 0.251211047008547,
       'lb/ft3': 1.5985472649572652,
       'lb/bbl': 8.974358974358974,
       'ppg': 0.2136752136752137,
       'psi/ft': 0.011111709401709403,
       'psi/100ft': 1.1105105769230772,
       'SG': 0.025603931623931625
      }
   # Each key representing a different unit
   print(trip_margin['ppg'])
   # outputs the following float:
   0.2136752136752137

Bottle Capacity Required in Accumulator Function
------------

*accumulator_bottle_capacity_required(volume_value, volume_units, pre_charge_value, minimum_value, operating_value, pressure_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - volume_value
     - usable fluid volume required value (Integer or Float)
   * - volume_units
     - volume units (String)
   * - pre_charge_value
     - pre-charge pressure value (Integer or Float)
   * - minimum_value
     - minimum system pressure value (Integer or Float)
   * - operating_value
     - operating pressure value (Integer or Float)
   * - pressure_units
     - pressure units (String)

This function calculates the required bottle volume for the accumulator. The function takes in four value inputs(Integers or Floats) and two units inputs(Strings). To see the range of volume point units that can be input into the function see the Volume units section under General Conversions. To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions. The function returns a dictionary of different pressure units and values, to see the range of pressure units returned see the example code below or the Pressure units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import well_control_formulas as wcf

   bottle_capacity = wcf.accumulator_bottle_capacity_required(5, 'gal_us', 1000, 1200, 3000, 'psi')
   print(bottle_capacity)
   # outputs the following dictionary:
   {
       'bbl': 0.23809523809523808,
       'bucket': 2.0,
       'bu_us': 1.0742087579702932,
       'cm3': 37850.11355034065,
       'ft3': 1.3368055520742912,
       'in3': 2310.0023100023095,
       'm3': 0.03785411783400294,
       'mm3': 37854125.34257984,
       'yd3': 0.049511316866060785,
       'C': 160.0,
       'dr': 10239.606799098914,
       'drum': 0.18181818181818182,
       'fl_oz': 1280.0,
       'gal_us': 10.0,
       'gill': 320.0,
       'gal_uk': 8.326742,
       'kL': 0.037854,
       'L': 37.854118,
       'ml': 37854.11784,
       'Pt': 80.0,
       'qt_dr': 34.37468,
       'qt_lq': 40.0,
       'tbsp': 2560.0,
       'tsp': 7680.0,
       'toe': 0.032468000000000004
      }
   # Each key representing a different unit
   print(bottle_capacity['gal_us'])
   # outputs the following float:
   10.0
