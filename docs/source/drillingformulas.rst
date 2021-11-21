Drilling Formulas
==================

This module contains 33 useful drilling and completion functions for formulas related to oil and gas, they are outlined below. 

Controlled Drilling Large Diameter Holes(>14.75 inches) Function
------------

*max_drilling_rate(mud_in_value, mud_out_value, mud_units, circ_value, circ_units, diameter_value, diameter_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - mud_in_value
     - mud weight in value (Integer or Float)
   * - mud_out_value
     - required mud weight out value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - circ_value
     - flow rate values (Integer or Float)
   * - circ_units
     - flow rate units (String)
   * - diameter_value
     - hole diameter value (Integer or Float)
   * - diameter_units
     - hole diameter units (String)

This function calculates the maximum drilling rate to keep the mud at the required rate out. The function takes in four value inputs(Integers or Floats) and three units inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of flow rate units that can be input into the function see the Flow Rate units section under Drilling Conversions. To see the range of hole diameter units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary of different drilling rate units and values, to see the range of drilling rate units returned see the example code below or the Drilling Rate units section under Drilling Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   max_drilling_rate  = dri_for.max_drilling_rate(9,9.7,'ppg',530,'gpm',17.5,'in')
   print(max_drilling_rate)
   # outputs the following dictionary:
   {
       'ft/d': 1947.9771428571407,
       'ft/hr': 81.1657142857142,
       'ft/min': 1.352764610285713,
       'ft/s': 0.022547835428571403,
       'm/d': 593.7434331428565,
       'm/hr': 24.73930971428569,
       'm/min': 0.4123218285714282,
       'm/s': 0.006874735999999992
   }
   # Each key representing a different rate of penetration unit
   print(max_drilling_rate['m/hr'])
   # outputs the following float:
   24.73930971428569 

Effect of Drilling on ROP Function
------------

*mud_on_drilling_rate(pv_1_value, pv_2_value, pv_units, rop_value, rop_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - pv_1_value
     - current plastic viscosity value (Integer or Float)
   * - pv_2_value
     - new plastic viscosity value (Integer or Float)
   * - pv_units
     - viscosity units (String)
   * - rop_value
     - current rop values (Integer or Float)
   * - rop_units
     - rop units (String)

This function calculates the effect of changes in mud viscosity on the rate of penetration. The function takes in three value inputs(Integers or Floats) and two units inputs(Strings). To see the range of plastic viscosity units that can be input into the function see the Viscosity units section under Fluid Conversions. To see the range of rop units that can be input into the function see the Drilling Rate units section under Drilling Conversions. The function returns a dictionary of different drilling rate units and values, to see the range of drilling rate units returned see the example code below or the Drilling Rate units section under Drilling Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   new_drilling_rate  = dri_for.mud_on_drilling_rate(24, 36, 'cp',100,'ft/hr')
   print(new_drilling_rate)
   # outputs the following dictionary:
   {
       'ft/d': 2209.0789722076115,
       'ft/hr': 92.04495717531714,
       'ft/min': 1.534085687753858,
       'ft/s': 0.0255700891033031,
       'm/d': 673.32727072888,
       'm/hr': 28.055302947036665,
       'm/min': 0.4675883824506111,
       'm/s': 0.007796207872749362
   }
   # Each key representing a different rate of penetration unit
   print(new_drilling_rate['ft/hr'])
   # outputs the following float:
   92.04495717531714

"d" Exponent Function
------------

*d_exponent(rop_value, rop_units, rotary_value, rotary_units, wob_value, wob_units, bit_value, bit_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - rop_value
     - rate of penetration value (Integer or Float)
   * - rop_units
     - rate of penetration units (String)
   * - rotary_value
     - rotary value (Integer or Float)
   * - rotary_units
     - rotary units (String)
   * - wob_value
     - weight on bit value (Integer or Float)
   * - wob_units
     - weight on bit units (String)
   * - bit_value
     - bit size value (Integer or Float)
   * - bit_units
     - bit size units (String)

This function calculates the "d" Exponent using rop, rotary speed, wob, and bit size. The function takes in four value inputs(Integers or Floats) and four units inputs(Strings). To see the range of rate of penetration units that can be input into the function see the Drilling Rate units section under Force and Power Conversions. To see the range of weight on bit units that can be input into the function see the Weight units section under General Conversions. To see the range of bit size units that can be input into the function see the Length units section under General Conversions. The function returns the calculated "d" Exponent.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   d_exponent  = dri_for.d_exponent(30, 'ft/hr', 120, 'rpm',35000,'lb',8.5, 'in' )
   print(d_exponent)
   # outputs the following float:
   1.8222833982318458

"d" Exponent Corrected Function
------------

*d_exponent_corrected(d_comp, mud_value, mud_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - d_comp
     - "d" exponent value (Integer or Float)
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)

This function corrects the "d" Exponent based on the mud weight. The function takes in two value inputs(Integers or Floats) and one units input(String). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. The function returns the corrected "d" Exponent.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   d_exponent_corrected  = dri_for.d_exponent_corrected(1.82,12.7,'ppg')
   print(d_exponent_corrected)
   # outputs the following float:
   1.2897637795275592 

Drilling Cost Function
------------

*drilling_cost(fixed_cost, hourly_cost, rotating_hrs, tripping_hrs, drilled_value, drilled_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - fixed_cost
     - fixed cost value (Integer or Float)
   * - hourly_cost
     - hourly cost value (Integer or Float)
   * - rotating_hrs
     - time rotating on bottom value (Integer or Float)
   * - tripping_hrs
     - tripping time values (Integer or Float)
   * - drilled_value
     - depth drilled values (Integer or Float)
   * - drilled_units
     - depth units (String)

This function calculates the footage cost of drilling operations. The function takes in five value inputs(Integers or Floats) and one units input(String). To see the range of depth units that can be input into the function see the Length units section under General Conversions. To see the range of rop units that can be input into the function see the Drilling Rate units section under General Conversions. The function returns a dictionary of different footage cost units and values, to see the range of footage cost units returned see the example code below or the Footage Cost units section under Drilling Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   drilling_cost = dri_for.drilling_cost(2500, 900, 65, 6, 1300,'ft')
   print(drilling_cost)
   # outputs the following dictionary:
   {
       'cur/ft': 51.07692307692308,
       'cur/m': 167.58345612307693,
       'cur/1000ft': 51076.92307692308,
       'cur/1000m': 167583.45612307693
   }
   # Each key representing a different cost per length unit
   print(drilling_cost['cur/ft'])
   # outputs the following float:
   51.07692307692308 

Ton Mile Function
------------

*round_trip_ton_miles(mud_value, mud_units, dp_value, hwdp_value, collar_value, dp_units, depth_value, depth_units, stand_len_value, bha_len_value, hwdp_len_value, collar_len_value, stand_units, block_value,	block_units, bha_weight_value, bha_weight_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - dp_value
     - drillpipe weight per length value (Integer or Float)
   * - hwdp_value
     - heavyweight drillpipe weight per length value (Integer or Float)
   * - collar_value
     - drill collar weight per length value (Integer or Float)
   * - dp_units
     - drillpipe weight per length units (String)
   * - depth_value
     - measured depth value (Integer or Float)
   * - depth_units
     - measured depth units (String)
   * - stand_len_value
     - average stand length value (Integer or Float)
   * - bha_len_value
     - bha total length value (Integer or Float)
   * - hwdp_len_value
     - heavyweight drillpipe total length value (Integer or Float)
   * - collar_len_value
     - drill collar total length value (Integer or Float)
   * - stand_units
     - length units (String)
   * - block_value
     - weight of travelling block value (Integer or Float)
   * - block_units
     - weight of travelling block units (String)
   * - bha_weight_value
     - bha weight values (Integer or Float)
   * - bha_weight_units
     - bha weight units (String)

This function calculates the round trip tons miles for an operation. The function takes in eleven value inputs(Integers or Floats) and six units input(String). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of weight per length units that can be input into the function see the Weight Length units section under Drilling Conversions. To see the range of weight units that can be input into the function see the Weight units section under General Conversions. The function returns a float for the calculated ton-miles.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   ton_miles_round_trip = dri_for.round_trip_ton_miles(10.0, 'ppg', 13.3, 49, 85, 'lb/ft', 5500, 'ft', 94, 94, 450, 120, 'ft', 95000,'lb', 8300, 'lb')
   print(ton_miles_round_trip)
   # outputs the following float:
   258.7468026399491

Drilling or Connection Ton Mile Function
------------

*drilling_connection_ton_miles(ton_mile_1_value, ton_mile_2_value)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - ton_mile_1_value
     - ton miles for round trip of depth where drilling stopped (Integer or Float)
   * - ton_mile_2_value
     - ton miles for round trip of depth before drilling started (Integer or Float)

This function calculates ton-miles of work done during a drilling operation. The function takes in two value inputs(Integers or Floats). The function returns a float for the calculated ton-miles.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   ton_miles_round_trip = dri_for.drilling_connection_ton_miles(195, 230)
   print(ton_miles_round_trip)
   # outputs the following float:
   105

Coring Ton Mile Function
------------

*coring_ton_miles(ton_mile_1_value, ton_mile_2_value)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - ton_mile_1_value
     - ton miles for round trip of depth where coring stopped (Integer or Float)
   * - ton_mile_2_value
     - ton miles for round trip of depth before coring started (Integer or Float)

This function calculates ton-miles of work done during a coring operation. The function takes in two value inputs(Integers or Floats). The function returns a float for the calculated ton-miles.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   ton_miles_round_trip = dri_for.coring_ton_miles(190, 200)
   print(ton_miles_round_trip)
   # outputs the following float:
   20

Ton Mile Setting Casing Function
------------

*setting_casing_ton_miles(mud_value, mud_units, casing_value, casing_units, depth_value, depth_units, stand_value, stand_units, block_value, block_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - casing_value
     - drillpipe weight per length value (Integer or Float)
   * - casing_units
     - drillpipe weight per length units (String)
   * - depth_value
     - measured depth value (Integer or Float)
   * - depth_units
     - measured depth units (String)
   * - stand_len_value
     - average stand length value (Integer or Float)
   * - stand_units
     - length units (String)
   * - block_value
     - weight of travelling block value (Integer or Float)
   * - block_units
     - weight of travelling block units (String)

This function calculates the round trip tons miles for a casing setting operation. The function takes in five value inputs(Integers or Floats) and five units input(String). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of weight per length units that can be input into the function see the Weight Length units section under Drilling Conversions. To see the range of weight units that can be input into the function see the Weight units section under General Conversions. The function returns a float for the calculated ton-miles.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   ton_miles_round_trip = dri_for.setting_casing_ton_miles(10, 'ppg', 25, 'lb/ft', 5200, 'ft', 42, 'ft', 95000,'lb')
   print(ton_miles_round_trip)
   # outputs the following float:
   50.730128093916264

Short Trip Ton Mile Function
------------

*short_trip_ton_miles(ton_mile_1_value, ton_mile_2_value)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - ton_mile_1_value
     - ton miles for round trip of depth where coring stopped (Integer or Float)
   * - ton_mile_2_value
     - ton miles for round trip of depth before coring started (Integer or Float)

This function calculates ton-miles of work done during a short round trip. The function takes in two value inputs(Integers or Floats). The function returns a float for the calculated ton-miles.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   ton_miles_round_trip = dri_for.short_trip_ton_miles(190, 200)
   print(ton_miles_round_trip)
   # outputs the following float:
   10 

Hydrostatic Pressure Decrease POOH Dry Function
------------

*hydrostatic_decrease_dry(stands_value, avg_stand_value, avg_std_units, disp_value, disp_units, mud_value, mud_units, annulus_value, annulus_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - stands_value
     - number of stands value (Integer or Float)
   * - avg_stand_value
     - average stand length value (Integer or Float)
   * - avg_std_units
     - average stand length units (String)
   * - disp_value
     - displacement volume value (Integer or Float)
   * - disp_units
     - displacement volume units (String)
   * - mud_value
     - mud weight values (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - annulus_value
     - annular volume value (Integer or Float)
   * - annulus_units
     - annular volume units (String)

This function calculates the hydrostatic pressure drop when pulling dry pipe out the hole. The function takes in five value inputs(Integers or Floats) and four units input(String). To see the range of average stand length units that can be input into the function see the Length units section under General Conversions. To see the range of displacement volume units that can be input into the function see the Pipe Capacity units section under production Conversions. The function returns a dictionary of different hydrostatic pressure loss units and values, to see the range of hydrostatic pressure loss units returned see the example code below or the Pressure units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   hydrostatic_decrease = dri_for.hydrostatic_decrease_dry(5, 92, 'ft', 0.0075, 'bbl/ft',11.5,'ppg',0.0773, 'bbl/ft')
   print(hydrostatic_decrease)
   # outputs the following dictionary:
   {
       'atm': 2.0112554141627026,
       'bar': 2.037904548005146,
       'cm_Hg': 152.85544892067222,
       'cm_h2o': 2078.090639321246,
       'dyne/cm2': 2038434.9372591635,
       'ft_air': 52743.230889111124,
       'ft_hg': 5.0149405894697,
       'ft_h2o': 68.17861978826689,
       'in_air': 632918.7706693335,
       'in_hg': 60.17928094732341,
       'in_h2o': 818.1432487414745,
       'kg/cm2': 2.0780843130080306,
       'kg/m2': 20781.344716485884,
       'kPa': 203.790508193786,
       'Mpa': 0.20379045522204026,
       'm_Hg': 1.5285541176759885,
       'm_h2o': 20.780843568391674,
       'mbar': 2037.9008666872044,
       'N/cm2': 20.379045199034316,
       'N/m2': 203843.49372591637,
       'N/mm2': 0.20379045522204026,
       'Pa': 203843.49372591637,
       'psf': 4256.279389185224,
       'psi': 29.557306590257873,
       'torr': 1528.5541181527217
   }
   # Each key representing a different pressure unit
   print(hydrostatic_decrease['psi'])
   # outputs the following float:
   29.557306590257873 

Hydrostatic Pressure Decrease POOH Wet Function
------------

*hydrostatic_decrease_wet(stands_value, avg_stand_value, avg_std_units, disp_value, disp_units, pipe_capacity_value, pipe_capacity_units, mud_value, mud_units, annulus_value, annulus_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - stands_value
     - number of stands value (Integer or Float)
   * - avg_stand_value
     - average stand length value (Integer or Float)
   * - avg_std_units
     - average stand length units (String)
   * - disp_value
     - displacement volume value (Integer or Float)
   * - disp_units
     - displacement volume units (String)
   * - pipe_capacity_value
     - pipe capacity value (Integer or Float)
   * - pipe_capacity_units
     - pipe capacity units (String)
   * - mud_value
     - mud weight values (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - annulus_value
     - annular volume value (Integer or Float)
   * - annulus_units
     - annular volume units (String)

This function calculates the hydrostatic pressure drop when pulling wet pipe out the hole. The function takes in five value inputs(Integers or Floats) and four units input(String). To see the range of average stand length units that can be input into the function see the Length units section under General Conversions. To see the range of displacement volume, and pipe capacity units that can be input into the function see the Pipe Capacity units section under production Conversions. The function returns a dictionary of different hydrostatic pressure loss units and values, to see the range of hydrostatic pressure loss units returned see the example code below or the Pressure units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   hydrostatic_decrease = dri_for.hydrostatic_decrease_wet(5, 92, 'ft', 0.0075, 'bbl/ft',  0.01776, 'bbl/ft', 11.5,'ppg',0.0773, 'bbl/ft')
   print(hydrostatic_decrease)
   # outputs the following dictionary:
   {
       'atm': 9.085680145965007,
       'bar': 9.206065406113703,
       'cm_Hg': 690.5118602449027,
       'cm_h2o': 9387.602753107807,
       'dyne/cm2': 9208461.39574333,
       'ft_air': 238263.18743447232,
       'ft_hg': 22.654579734671604,
       'ft_h2o': 307.9912813795625,
       'in_air': 2859158.249213668,
       'in_hg': 271.8549291409465,
       'in_h2o': 3695.8945240380062,
       'kg/cm2': 9.387574174510593,
       'kg/m2': 93878.00762024768,
       'kPa': 920.6067818110621,
       'Mpa': 0.9206065425155777,
       'm_Hg': 6.9051169240896355,
       'm_h2o': 93.87574372514132,
       'mbar': 9206.048776064084,
       'N/cm2': 92.0606527916653,
       'N/m2': 920846.139574333,
       'N/mm2': 0.9206065425155777,
       'Pa': 920846.139574333,
       'psf': 19227.390449610946,
       'psi': 133.52269023827827,
       'torr': 6905.116926243239
   }
   # Each key representing a different pressure unit
   print(hydrostatic_decrease['psi'])
   # outputs the following float:
   133.52269023827827 

Loss of Overbalance POOH Dry Function
------------

*loss_of_overbalance_dry(pressure_value, pressure_units, disp_value, disp_units, annulus_value, annulus_units, mud_value, mud_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - pressure_value
     - overbalance pressure value (Integer or Float)
   * - pressure_units
     - overbalance pressure units (String)
   * - disp_value
     - displacement volume value (Integer or Float)
   * - disp_units
     - displacement volume units (String)
   * - annulus_value
     - annular volume value (Integer or Float)
   * - annulus_units
     - annular volume units (String)
   * - mud_value
     - mud weight values (Integer or Float)
   * - mud_units
     - mud weight units (String)

This function calculates the length of dry pipe that can be pulled out of the hole before the overbalance pressure is lost. The function takes in four value inputs(Integers or Floats) and four units input(String). To see the range of overbalance pressure units that can be input into the function see the Pressure units section under General Conversions. To see the range of displacement volume, and annular units that can be input into the function see the Pipe Capacity units section under Production Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. The function returns a dictionary of different length units and values, to see the range of length units returned see the example code below or the Length units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   max_pipe_pull = dri_for.loss_of_overbalance_dry(150,'psi', 0.0075, 'bbl/ft', 0.0773, 'bbl/ft', 11.5, 'ppg')
   print(max_pipe_pull)
   # outputs the following dictionary:
   {
       'cm': 71153.97993311039,
       'dm': 7115.397993311039,
       'dam': 71.15397993311038,
       'fath': 389.07477123745826,
       'ft': 2334.4481605351175,
       'hm': 7.115397993311038,
       'in': 28013.37792642141,
       'km': 0.7115397993311038,
       'league': 0.14730367892976592,
       'm': 711.5397993311038,
       'mi': 0.44214448160535125,
       'mm': 711539.7993311038,
       'nleague': 0.12816120401337794,
       'nm': 0.38425016722408034,
       'yd': 778.1493090301004
   }
   # Each key representing a different unit
   print(max_pipe_pull['ft'])
   # outputs the following float:
   2334.4481605351175 

Loss of Overbalance POOH Wet Function
------------

*loss_of_overbalance_wet(pressure_value, pressure_units, disp_value, disp_units, pipe_capacity_value, pipe_capacity_units, annulus_value, annulus_units, mud_value, mud_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - pressure_value
     - overbalance pressure value (Integer or Float)
   * - pressure_units
     - overbalance pressure units (String)
   * - disp_value
     - displacement volume value (Integer or Float)
   * - disp_units
     - displacement volume units (String)
   * - pipe_capacity_value
     - pipe capacity value (Integer or Float)
   * - pipe_capacity_units
     - pipe capacity units (String)
   * - annulus_value
     - annular volume value (Integer or Float)
   * - annulus_units
     - annular volume units (String)
   * - mud_value
     - mud weight values (Integer or Float)
   * - mud_units
     - mud weight units (String)

This function calculates the length of wet pipe that can be pulled out of the hole before the overbalance pressure is lost. The function takes in four value inputs(Integers or Floats) and four units input(String). To see the range of overbalance pressure units that can be input into the function see the Pressure units section under General Conversions. To see the range of displacement volume, pipe capacity and annular units that can be input into the function see the Pipe Capacity units section under Production Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. The function returns a dictionary of different length units and values, to see the range of length units returned see the example code below or the Length units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   max_pipe_pull = dri_for.loss_of_overbalance_wet(150,'psi', 0.0075, 'bbl/ft', 0.01776, 'bbl/ft', 0.0773, 'bbl/ft', 11.5, 'ppg')
   print(max_pipe_pull)
   # outputs the following dictionary:
   {
       'cm': 15751.030751753668,
       'dm': 1575.1030751753667,
       'dam': 15.751030751753667,
       'fath': 86.12770068875666,
       'ft': 516.7661007793198,
       'hm': 1.5751030751753667,
       'in': 6201.193209351837,
       'km': 0.15751030751753667,
       'league': 0.03260794095917508,
       'm': 157.5103075175367,
       'mi': 0.09787549948760317,
       'mm': 157510.30751753668,
       'nleague': 0.028370458932784656,
       'nm': 0.08505970018827604,
       'yd': 172.25534970090325
   }
   # Each key representing a different unit
   print(max_pipe_pull['ft'])
   # outputs the following float:
   516.7661007793198 

Lost Circulation Function
------------

*lost_circulation_mud_weight_at_tvd(volume_added_value, volume_added_units, riser_dia_value, riser_dia_units, dp_od_value, dp_id_value, dp_units, mud_value, mud_units, liquid_value, liquid_units, depth_value, depth_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - volume_added_value
     - volume of fluid added value (Integer or Float)
   * - volume_added_units
     - volume of fluid added units (String)
   * - riser_dia_value
     - riser diameter value (Integer or Float)
   * - riser_dia_units
     - riser diameter units (String)
   * - dp_od_value
     - drillpipe outer diameter value (Integer or Float)
   * - dp_id_value
     - drillpipe inner diameter value (Integer or Float)
   * - dp_units
     - drillpipe diameter units (String)
   * - mud_value
     - mud weight values (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - liquid_value
     - liquid added weight value (Integer or Float)
   * - liquid_units
     - liquid added weight units (String)
   * - depth_value
     - total vertical depth value (Integer or Float)
   * - depth_units
     - total vertical depth units (String)

This function calculates data related to lost circulation including annulus filled, reduction in bottom hole pressure, and equivalent mud weight at TVD. The function takes in seven value inputs(Integers or Floats) and six units input(String). To see the range of volume units that can be input into the function see the Volume units section under General Conversions. To see the range of riser diameter, drillpipe diameter and depth units that can be input into the function see the Length units section under General Conversions. To see the range of mud weight and liquid added weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. The function returns a dictionary with three sub-dictionaries:

   * - "annulus_filled" which is a dictionary of different length units and values, to see the range of length units returned see the example code below or the Length units section under General Conversions.
   * - "bottom_hole_pressure" which is a dictionary of different pressure units and values, to see the range of pressure units returned see the example code below or the Pressure units section under General Conversions.
   * - "tvd_equivalent_mud_weight"
     - which is a dictionary of different mud weight units and values, to see the range of mud weight units returned see the example code below or the Mud Weight units section under Drilling Conversions.


.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   lost_circulation_info = dri_for.lost_circulation_mud_weight_at_tvd(325, 'bbl', 18.75, 'in', 6.625, 5.965, 'in', 12.5, 'ppg', 8.55, 'ppg', 10000, 'ft')
   print(lost_circulation_info)
   # outputs the following dictionary:
   {
       'annulus_filled': 
          {
              'cm': 33158.22663027399,
              'dm': 3315.8226630273984,
              'dam': 33.15822663027399,
              'fath': 181.31142422309335,
              'ft': 1087.8683277648945,
              'hm': 3.315822663027398,
              'in': 13054.419933178735,
              'km': 0.33158226630273985,
              'league': 0.06864449148196484,
              'm': 331.58226630273987,
              'mi': 0.206042261278671,
              'mm': 331582.26630273985,
              'nleague': 0.05972397119429271,
              'nm': 0.17906312675010164,
              'yd': 362.6227396593539
          },
       'bottom_hole_pressure':
          {
              'atm': 15.204745033060352,
              'bar': 15.406207901760663,
              'cm_Hg': 1155.5609055851066,
              'cm_h2o': 15710.007840860368,
              'dyne/cm2': 15410217.553304086,
              'ft_air': 398729.7546804234,
              'ft_hg': 37.912088381164594,
              'ft_h2o': 515.4186401621795,
              'in_air': 4784757.0561650805,
              'in_hg': 454.94501426010254,
              'in_h2o': 6185.0222552725845,
              'kg/cm2': 15.709960015020467,
              'kg/m2': 157103.39205716742,
              'kPa': 1540.6211938200154,
              'Mpa': 1.5406207933627278,
              'm_Hg': 11.555606247142615,
              'm_h2o': 157.09960346376323,
              'mbar': 15406.180071630142,
              'N/cm2': 154.06207689316537,
              'N/m2': 1541021.7553304087,
              'N/mm2': 1.5406207933627278,
              'Pa': 1541021.7553304087,
              'psf': 32176.740182436097,
              'psi': 223.44815452290925,
              'torr': 11555.606250746636
          },
       'tvd_equivalent_mud_weight':
          {
              'g/cm3': 1.4463396385709155,
              'g/L': 1446.3396385709157,
              'kg/m3': 1446.3396385709157,
              'kg/L': 1.4463396385709155,
              'kPa/m': 14.190652446351551,
              'lb/ft3': 90.3002830735489,
              'lb/bbl': 506.9522644423804,
              'ppg': 12.070292010532867,
              'psi/ft': 0.6276889813653386,
              'psi/100ft': 62.73159489907531,
              'SG': 1.4463396385709155
          }
      }

Mud Weight to Balance Losses Function
------------

*mud_weight_balance_losses(volume_added_value, volume_added_units, annulus_value, annulus_units, gradient_value, gradient_units, depth_value, depth_units, mud_value, mud_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - volume_added_value
     - volume of fluid added value (Integer or Float)
   * - volume_added_units
     - volume of fluid added units (String)
   * - annulus_value
     - riser diameter value (Integer or Float)
   * - annulus_units
     - riser diameter units (String)
   * - gradient_value
     - drillpipe inner diameter value (Integer or Float)
   * - gradient_units
     - drillpipe diameter units (String)
   * - depth_value
     - total vertical depth value (Integer or Float)
   * - depth_units
     - total vertical depth units (String)
   * - mud_value
     - mud weight values (Integer or Float)
   * - mud_units
     - mud weight units (String)

This function calculates the mud weight required to balance the formation losing fluids. The function takes in five value inputs(Integers or Floats) and five units input(String). To see the range of volume units that can be input into the function see the Volume units section under General Conversions. To see the range of annular volume units that can be input into the function see the Pipe Capacity units section under Production Conversions. To see the range of liquid gradient units that can be input into the function see the Pressure Gradient units section under Drilling Conversions. To see the range of depth units that can be input into the function see the Length units section under General Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. The function returns a dictionary with two sub-dictionaries:

   * - "annulus_filled" which is a dictionary of different length units and values, to see the range of length units returned see the example code below or the Length units section under General Conversions.
   * - "mud_weight_equivalent"
     - which is a dictionary of different mud weight units and values, to see the range of mud weight units returned see the example code below or the Mud Weight units section under Drilling Conversions.


.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   balanced_mud_weight = dri_for.mud_weight_balance_losses(25, 'bbl', 0.0502, 'bbl/ft', 0.433, 'psi/ft', 3500, 'ft', 12.2, 'ppg')
   print(balanced_mud_weight)
   # outputs the following dictionary:
   {
       'annulus_filled': 
          {
              'cm': 15179.282868525896,
              'dm': 1517.9282868525895,
              'dam': 15.179282868525895,
              'fath': 83.00134462151394,
              'ft': 498.00796812749,
              'hm': 1.5179282868525896,
              'in': 5976.09561752988,
              'km': 0.15179282868525895,
              'league': 0.03142430278884462,
              'm': 151.79282868525897,
              'mi': 0.0943227091633466,
              'mm': 151792.82868525895,
              'nleague': 0.027340637450199202,
              'nm': 0.08197211155378485,
              'yd': 166.00263944223107
          },
       'mud_weight_equivalent':
          {
              'g/cm3': 1.3958466695538723,
              'g/L': 1395.8466695538725,
              'kg/m3': 1395.8466695538725,
              'kg/L': 1.3958466695538723,
              'kPa/m': 13.695244483244604,
              'lb/ft3': 87.14782200986122,
              'lb/bbl': 489.25412197364386,
              'ppg': 11.64890766603914,
              'psi/ft': 0.6057758155755002,
              'psi/100ft': 60.541580608408125,
              'SG': 1.3958466695538723
          }
      } 

Depth of Fluid Level with Loss of Circulation Function
------------

*fluid_level_depth_losses(weight_value, weight_units, dp_value, dp_units, buoyancy)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - weight_value
     - string weight increase value (Integer or Float)
   * - weight_units
     - string weight increase units (String)
   * - dp_value
     - drill pipe drill pipe weight per length  value (Integer or Float)
   * - dp_units
     - drill pipe weight per length units (String)
   * - buoyancy
     - pipe capacity value (Integer or Float)

This function calculates the depth of fluid level. The function takes in three value inputs(Integers or Floats) and two units input(String). To see the range of string weight increase units that can be input into the function see the Weight units section under General Conversions. To see the range of drill pipe weight per length units that can be input into the function see the Weight Length units section under Drilling Conversions. The function returns a dictionary of different length units and values, to see the range of length units returned see the example code below or the Length units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   fluid_level = dri_for.fluid_level_depth_losses(5000, 'lb', 20.9, 'lb/ft', 0.8183)
   print(fluid_level)
   # outputs the following dictionary:
   {
       'cm': 40131.34853444213,
       'dm': 4013.134853444213,
       'dam': 40.13134853444213,
       'fath': 219.4409260756334,
       'ft': 1316.6452931247418,
       'hm': 4.013134853444213,
       'in': 15799.743517496901,
       'km': 0.4013134853444213,
       'league': 0.08308031799617122,
       'm': 401.31348534442134,
       'mi': 0.24937261851782608,
       'mm': 401313.4853444213,
       'nleague': 0.07228382659254833,
       'nm': 0.21671981524833248,
       'yd': 438.8817204867375
   }
   # Each key representing a different unit
   print(fluid_level['ft'])
   # outputs the following float:
   1316.6452931247418 

Determine Mud Loss Before Kick Function
------------

*fluid_drop_before_kick(pressure_value, pressure_units, gradient_value, gradient_units, annulus_value, annulus_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - pressure_value
     - overbalance pressure value (Integer or Float)
   * - pressure_units
     - overbalance pressure units (String)
   * - gradient_value
     - pressure gradient value (Integer or Float)
   * - gradient_units
     - pressure gradient units (String)
   * - annulus_value
     - pipe capacity value (Integer or Float)
   * - annulus_units
     - pipe capacity units (String)

This function calculates the amount of fluid that can be lost before taking a kick. The function takes in three value inputs(Integers or Floats) and three units input(String). To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions. To see the range of pressure gradient units that can be input into the function see the Pressure Gradient units section under Drilling Conversions. To see the range of pipe capacity units that can be input into the function see the Pipe Capacity units section under Production Conversions. The function returns a dictionary with two sub-dictionaries:

   * - "fluid_drop_length" which is a dictionary of different length units and values, to see the range of length units returned see the example code below or the Length units section under General Conversions.
   * - "loss_before_kick"
     - which is a dictionary of different volume units and values, to see the range of volume units returned see the example code below or the Volume units section under General Conversions.


.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   fluid_drop = dri_for.fluid_drop_before_kick(250, 'psi', 0.624, 'psi/ft', 0.0489,'bbl/ft')
   print(fluid_drop)
   # outputs the following dictionary:
   {
       'fluid_drop_length': 
          {
              'cm': 12211.538461538461,
              'dm': 1221.1538461538462,
              'dam': 12.211538461538462,
              'fath': 66.77351762820513,
              'ft': 400.64102564102564,
              'hm': 1.221153846153846,
              'in': 4807.692307692308,
              'km': 0.12211538461538461,
              'league': 0.02528044871794872,
              'm': 122.11538461538461,
              'mi': 0.07588141025641025,
              'mm': 122115.38461538462,
              'nleague': 0.021995192307692306,
              'nm': 0.06594551282051282,
              'yd': 133.5469951923077
          },
       'loss_before_kick':
          {
              'bbl': 19.591346153846153,
              'bucket': 164.5673076923077,
              'bu_us': 88.38982192307692,
              'cm3': 3114775.129007872,
              'ft3': 109.99724493990384,
              'in3': 190075.24038461538,
              'm3': 3.1147752283653847,
              'mm3': 3114775129.008617,
              'yd3': 4.073971454326923,
              'C': 13165.384615384615,
              'dr': 842584.6153846154,
              'drum': 14.960665048076923,
              'fl_oz': 105323.07692307692,
              'gal_us': 822.8365384615385,
              'gill': 26330.76923076923,
              'gal_uk': 685.154744639423,
              'kL': 3.1147752283653847,
              'L': 3114.775128449519,
              'ml': 3114775.129007872,
              'Pt': 6582.692307692308,
              'qt_dr': 2828.4742760697113,
              'qt_lq': 3291.346153846154,
              'tbsp': 210646.15384615384,
              'tsp': 631938.4615384615,
              'toe': 2.6715464903846153
          }
      } 

Drill Collar Weight Prevent Drill Pipe Buckling Function
------------

*drill_collar_prevent_buckling(wob_value, weight_units, buoyancy_factor, safety_factor, angle)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - wob_value
     - required wob value (Integer or Float)
   * - weight_units
     - wob units (String)
   * - buoyancy_factor
     - buoyancy factor value (Integer or Float)
   * - safety_factor
     - safety factor length  value (Integer or Float)
   * - angle
     - hole angle value (Integer or Float)

This function calculates the weight required to keep the drill sting in tension and prevent buckling. The function takes in four value inputs(Integers or Floats) and one units input(String). To see the range of string weight increase units that can be input into the function see the Weight units section under General Conversions. The safety factor is a decimal display of the safety factor percentage, i.e. a 20% safety factor is input into the function as 0.2, the default for safety factor is 0.0. The angle is the hole angle, the default hole angle is 0.0 representing a vertical hole. The function returns a dictionary of different weight units and values, to see the range of weight units returned see the example code below or the Weight units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   required_weight = dri_for.drill_collar_prevent_buckling(50000,'lb', 0.817,0.25, 0)
   print(required_weight)
   # outputs the following dictionary:
   {
       'ct': 173497693.5434517,
       'cg': 3469953870.8690333,
       'dg': 346995387.0869034,
       'dram': 19583843.2757038,
       'gr': 535495798.67656064,
       'g': 34699538.70869034,
       'kg': 34699.54100367198,
       'kip': 76.49938800489598,
       't_long': 34.14932680538556,
       't_metric': 34.70012239902081,
       'mg': 34699538708.69033,
       'oz': 1223990.2080783355,
       'lb': 76499.38800489597,
       'slug': 2377.6774785801717,
       't_short': 38.24969400244799,
       'toz': 1115616.07252142,
       'KdaN': 30.870767052514143,
       'daN': 30870.766887730126
   }
   # Each key representing a different unit
   print(required_weight['t_metric'])
   # outputs the following float:
   34.70012239902081 

Effective Mud Density Function
------------

*effective_mud_density(mud_value, mud_units, flow_value, flow_units, rop_value, rop_units, hole_value, hole_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - flow_value
     - mud flow rate value (Integer or Float)
   * - flow_units
     - mud flow rate units (String)
   * - rop_value
     - rate of penetration value (Integer or Float)
   * - rop_units
     - rate of penetration units (String)
   * - hole_value
     - hole diameter value (Integer or Float)
   * - hole_units
     - hole diameter units (String)

This function calculates the effective mud density. The function takes in four value inputs(Integers or Floats) and four units inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions.  To see the range of mud flow rate units that can be input into the function see the Flow Rate units section under Drilling Conversions.  To see the range of rate of penetration units that can be input into the function see the Drilling Rate units section under Drilling Conversions.  To see the range of hole diameter units that can be input into the function see the length units section under General Conversions. The function returns a dictionary of different mud weight units and values, to see the range of weight units returned see the example code below or the Mud Weight units section under Drilling Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   effective_density = dri_for.effective_mud_density(9.2,'ppg',900,'gpm',150,'ft/hr',12.25,'in')
   print(effective_density)
   # outputs the following dictionary:
   {
       'g/cm3': 1.125656566559118,
       'g/L': 1125.6565665591181,
       'kg/m3': 1125.6565665591181,
       'kg/L': 1.125656566559118,
       'kPa/m': 11.044294634541764,
       'lb/ft3': 70.2788638941832,
       'lb/bbl': 394.5505814702182,
       'ppg': 9.394061463576625,
       'psi/ft': 0.48851749947808254,
       'psi/100ft': 48.82271760085507,
       'SG': 1.125656566559118
   }
   # Each key representing a different unit
   print(effective_density['ppg'])
   # outputs the following float:
   9.394061463576625 

ECD from yield point (below 13ppg) Function
------------

*ecd_yield_below_13(mud_value, mud_units, reading_300, reading_600, hole_id_value, dp_od_value, dp_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - reading_300
     - reading at 300 rpm (Integer or Float)
   * - reading_600
     - reading at 600 rpm (Integer or Float)
   * - hole_id_value
     - hole inner diameter value (Integer or Float)
   * - dp_od_value
     - drill pipe outer diameter value (Integer or Float)
   * - dp_units
     - diameter units (String)

This function calculates the Equivalent Circulating Density using the yield point for mud weights of less than or equal to 13 ppg. The function takes in five value inputs(Integers or Floats) and two units inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of diameter units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary with two sub-dictionaries:

   * - "yp" which is a dictionary of different viscosity units and values, to see the range of viscosity units returned see the example code below or the Viscositty units section under Fluids Conversions.
   * - "ecd"
     - which is a dictionary of different mud weight units and values, to see the range of mud weight units returned see the example code below or the Mud Weight units section under Drilling Conversions.


.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   ecd_value = dri_for.ecd_yield_below_13(9.2,'ppg',25,40,6.2,4,'in')
   print(ecd_value)
   # outputs the following dictionary:
   {
       'yp': 
          {
              'cp': 10,
              'g/(cm.s)': 0.1,
              'kg/(m.hr)': 36.0,
              'kg/(m.s)': 0.01,
              'kg-f.s/m2': 0.00102,
              'kPa-s': 9.999999999999999e-06,
              'N.s/m2': 0.01,
              'Pa-s': 0.01,
              'dyne-s/cm2': 0.1,
              'p': 0.1,
              'lbf-s/ft2': 0.00020899999999999998,
              'lbf-s/in2': 1.4503770000000001e-06,
              'lb/(ft.hr)': 24.190883,
              'lb/(ft.s)': 0.006719999999999999,
              'poundal.s/ft2': 0.006719999999999999,
              'reyn': 1.4503770000000001e-06
          },
       'ecd':
          {
              'g/cm3': 1.1568694254545455,
              'g/L': 1156.8694254545455,
              'kg/m3': 1156.8694254545455,
              'kg/L': 1.1568694254545455,
              'kPa/m': 11.350537249090909,
              'lb/ft3': 72.22759704,
              'lb/bbl': 405.4909090909091,
              'ppg': 9.654545454545454,
              'psi/ft': 0.5020633963636364,
              'psi/100ft': 50.176502263636365,
              'SG': 1.1568694254545455
          }
      } 

ECD from yield point (above 13ppg) Function
------------

*ecd_yield_above_13(mud_value, mud_units, reading_300, reading_600, hole_id_value, dp_od_value, dp_units, flow_value, flow_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - reading_300
     - reading at 300 rpm (Integer or Float)
   * - reading_600
     - reading at 600 rpm (Integer or Float)
   * - hole_id_value
     - hole inner diameter value (Integer or Float)
   * - dp_od_value
     - drill pipe outer diameter value (Integer or Float)
   * - dp_units
     - diameter units (String)
   * - flow_value
     - mud flow rate value (Integer or Float)
   * - flow_units
     - mud flow rate units (String)

This function calculates the Equivalent Circulating Density using the yield point for mud weights of less than or equal to 13 ppg. The function takes in five value inputs(Integers or Floats) and two units inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of diameter units that can be input into the function see the Length units section under General Conversions. To see the range of mud flow rate units that can be input into the function see the Flow Rate units section under Drilling Conversions. The function returns a dictionary with two sub-dictionaries:

   * - "av" which is a dictionary of different annular velocity units and values, to see the range of length units returned see the example code below or the Velocity units section under Force and Power Conversions.
   * - "pv" which is a dictionary of different viscosity units and values, to see the range of viscosity units returned see the example code below or the Viscositty units section under Fluids Conversions.
   * - "yp" which is a dictionary of different viscosity units and values, to see the range of viscosity units returned see the example code below or the Viscositty units section under Fluids Conversions.
   * - "ecd"
     - which is a dictionary of different mud weight units and values, to see the range of mud weight units returned see the example code below or the Mud Weight units section under Drilling Conversions.


.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   ecd_value = dri_for.ecd_yield_above_13(13.5,'ppg',25,40,6.2,4,'in', 200, 'gpm')
   print(ecd_value)
   # outputs the following dictionary:
   {
       'av': 
          {
              'ft/d': 314438.5026737967,
              'ft/hr': 13101.604278074863,
              'ft/min': 218.36007130124773,
              'ft/s': 3.6393418003565055,
              'kph': 3.6393418003565055,
              'k/min': 0.0665561497326203,
              'k/sec': 0.0011136363636363635,
              'knot': 2.1562401960784308,
              'mach': 0.003253565062388591,
              'm/d': 95840.85561497323,
              'm/hr': 95840.85561497323,
              'm/min': 66.55614973262031,
              'm/sec': 1.1092691622103386,
              'mph': 2.4813565062388587,
              'mi/min': 0.04135739750445632,
              'mi/sec': 0.0006987522281639927
          },
       'pv': 
          {
              'cp': 15,
              'g/(cm.s)': 0.15,
              'kg/(m.hr)': 54.0,
              'kg/(m.s)': 0.015,
              'kg-f.s/m2': 0.00153,
              'kPa-s': 1.4999999999999999e-05,
              'N.s/m2': 0.015,
              'Pa-s': 0.015,
              'dyne-s/cm2': 0.15,
              'p': 0.15,
              'lbf-s/ft2': 0.0003135,
              'lbf-s/in2': 2.1755655e-06,
              'lb/(ft.hr)': 36.2863245,
              'lb/(ft.s)': 0.010079999999999999,
              'poundal.s/ft2': 0.010079999999999999,
              'reyn': 2.1755655e-06
          },
       'yp': 
          {
              'cp': 10,
              'g/(cm.s)': 0.1,
              'kg/(m.hr)': 36.0,
              'kg/(m.s)': 0.01,
              'kg-f.s/m2': 0.00102,
              'kPa-s': 9.999999999999999e-06,
              'N.s/m2': 0.01,
              'Pa-s': 0.01,
              'dyne-s/cm2': 0.1,
              'p': 0.1,
              'lbf-s/ft2': 0.00020899999999999998,
              'lbf-s/in2': 1.4503770000000001e-06,
              'lb/(ft.hr)': 24.190883,
              'lb/(ft.s)': 0.006719999999999999,
              'poundal.s/ft2': 0.006719999999999999,
              'reyn': 1.4503770000000001e-06
          },
       'ecd':
          {
              'g/cm3': 1.6991532153386073,
              'g/L': 1699.1532153386074,
              'kg/m3': 1699.1532153386074,
              'kg/L': 1.6991532153386073,
              'kPa/m': 16.671113816527452,
              'lb/ft3': 106.08436098868903,
              'lb/bbl': 595.5652097052194,
              'ppg': 14.180124040600463,
              'psi/ft': 0.7374061544585377,
              'psi/100ft': 73.6967917725063,
              'SG': 1.6991532153386073
          }
      } 

Lag Time Function
------------

*lag_time(flow_value, flow_units, pump_value, pump_units, annulus_value, annulus_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - flow_value
     - mud flow rate value (Integer or Float)
   * - flow_units
     - mud flow rate units (String)
   * - pump_value
     - pump stroke volume value (Integer or Float)
   * - pump_units
     - pump stroke volume units (String)
   * - annulus_value
     - annular volume value (Integer or Float)
   * - annulus_units
     - annular volume units (String)

This function calculates the theoretical lag time for drilling operations. The function takes in three value inputs(Integers or Floats) and three units inputs(Strings). To see the range of mud flow rate units that can be input into the function see the Flow Rate units section under Drilling Conversions.  To see the range of pump stroke volume units that can be input into the function see the Stroke Volume units section under Production Conversions.  To see the range of annular volume units that can be input into the function see the Volume units section under General Conversions.  To see the range of hole diameter units that can be input into the function see the length units section under General Conversions.  The function returns a dictionary with the lag time in minutes and the lag strokes.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   lag_time = dri_for.lag_time(300,'gpm',0.102,'bbl/stk', 250,'bbl')
   print(lag_time)
   # outputs the following dictionary:
   {
       'lag_time': 35.000035000035,
       'lag_strokes': 2450.9803921568628
   }
   # Each key representing a different category
   print(lag_time['lag_time'])
   # outputs the following float:
   35.000035000035 

Light Weight Pill to Balance Formation Pressure Function
------------

*light_weight_pill_height(mud_value, pill_value, mud_units, pressure_value, pressure_units, annulus_value, annulus_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - mud_value
     - mud weight value (Integer or Float)
   * - pill_value
     - pill weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - pressure_value
     - overbalance pressure value (Integer or Float)
   * - pressure_units
     - overbalance pressure units (String)
   * - annulus_value
     - annular volume value (Integer or Float)
   * - annulus_units
     - annular volume units (String)

This function calculates the height and volume of a lightweight pill. The function takes in four value inputs(Integers or Floats) and three units inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions.  To see the range of overbalance pressure units that can be input into the function see the Pressure units section under General Conversions.  To see the range of annular volume units that can be input into the function see the Pipe Capacity units section under Production Conversions. The function returns a dictionary with two sub-dictionaries:

   * - "pill_height" which is a dictionary of different height units and values, to see the range of height units returned see the example code below or the Length units section under General Conversions.
   * - "pill_volume"
     - which is a dictionary of different volume units and values, to see the range of volume units returned see the example code below or the Volume units section under General Conversions.


.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   pill_size = dri_for.light_weight_pill_height(13, 8.3,'ppg',300,'psi',0.0459,  'bbl/ft' )
   print(pill_size)
   # outputs the following dictionary:
   {
       'pill_height': 
          {
              'cm': 37414.07528641572,
              'dm': 3741.407528641572,
              'dam': 37.41407528641572,
              'fath': 204.58269230769233,
              'ft': 1227.4959083469723,
              'hm': 3.7414075286415716,
              'in': 14729.950900163669,
              'km': 0.37414075286415716,
              'league': 0.07745499181669396,
              'm': 374.1407528641572,
              'mi': 0.23248772504091655,
              'mm': 374140.7528641572,
              'nleague': 0.06738952536824878,
              'nm': 0.20204582651391162,
              'yd': 409.1652618657938
          },
       'pill_volume':
          {
              'bbl': 56.34206219312603,
              'bucket': 473.2733224222587,
              'bu_us': 254.19717486088385,
              'cm3': 8957672.058778418,
              'ft3': 316.33720147708675,
              'in3': 546630.6873977088,
              'm3': 8.957672344517187,
              'mm3': 8957672058.78056,
              'yd3': 11.716190977905075,
              'C': 37861.86579378069,
              'dr': 2423159.4108019643,
              'drum': 43.024849541734866,
              'fl_oz': 302894.92635024554,
              'gal_us': 2366.3666121112933,
              'gill': 75723.73158756139,
              'gal_uk': 1970.412391841244,
              'kL': 8.957672344517187,
              'L': 8957.67205717267,
              'ml': 8957672.058778418,
              'Pt': 18930.932896890346,
              'qt_dr': 8134.309522303602,
              'qt_lq': 9465.466448445173,
              'tbsp': 605789.8527004911,
              'tsp': 1817369.5581014734,
              'toe': 7.683006432078561
          }
      } 

Max Rop Without Fracturing Formation Function
------------

*maximum_rop_fracturing_formation(mud_value, lot_value, mud_units, pressure_value, pressure_units, flow_value, flow_units, depth_value, depth_units, hole_value, hole_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - mud_value
     - mud weight value (Integer or Float)
   * - lot_value
     - leak off test/fracture gradient value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - pressure_value
     - annular pressure loss value (Integer or Float)
   * - pressure_units
     - annular pressure loss units (String)
   * - flow_value
     - mud flow rate value (Integer or Float)
   * - flow_units
     - mud flow rate units (String)
   * - depth_value
     - depth value (Integer or Float)
   * - depth_units
     - depth units (String)
   * - hole_value
     - hole inner diameter value (Integer or Float)
   * - hole_units
     - hole inner diameter units (String)

This function calculates the maximum rate of penetration before fracturing the formation. The function takes in six value inputs(Integers or Floats) and five units inputs(Strings).  To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions.  To see the range of pressure units that can be input into the function see the Pressure Volume units section under General Conversions. To see the range of mud flow rate units that can be input into the function see the Flow Rate units section under Drilling Conversions. To see the range of depth and diameter units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary of different rate of penetration units and values, to see the range of rate of penetration units returned see the example code below or the Drilling Rate units section under Drilling Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   max_rop = dri_for.maximum_rop_fracturing_formation(10.5,12.5,'ppg',600,'psi',800,'gpm',9500,'ft',12.25,'in')
   print(max_rop)
   # outputs the following dictionary:
   {
       'ft/d': 15533.433432585087,
       'ft/hr': 647.2263930243786,
       'ft/min': 10.78712812461941,
       'ft/s': 0.17979949198217235,
       'm/d': 4734.590510251935,
       'm/hr': 197.2746045938306,
       'm/min': 3.2879100765638434,
       'm/s': 0.054820075489164864
   }
   # Each key representing a different rop unit
   print(max_rop['ft/hr'])
   # outputs the following float:
   647.2263930243786 

Pipe Thermal Expansion Function
------------

*pipe_thermal_expansion(pipe_value, pipe_units, surface_value, bottom_value, temp_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - pipe_value
     - pipe length value (Integer or Float)
   * - pipe_units
     - pipe length units (String)
   * - surface_value
     - surface temperature value (Integer or Float)
   * - bottom_value
     - bottom hole temperature value (Integer or Float)
   * - temp_units
     - temperature units (String)

This function calculates the thermal expansion of pipe due to higher downhole temperatures. The function takes in three value inputs(Integers or Floats) and two units inputs(Strings).  To see the range of length units that can be input into the function see the Length units section under General Conversions.  To see the range of temperature units that can be input into the function see the Temperature units section under General Conversions. The function returns a dictionary with three sub-dictionaries:

   * - "average_temp"
     - which is a dictionary of different temperature units and values, to see the range of temperature units returned see the example code below or the Temperature units section under General Conversions.
   * - "delta_temp"
     - which is a dictionary of different temperature units and values, to see the range of temperature units returned see the example code below or the Temperature units section under General Conversions.
   * - "thermal_expansion"
     - which is a dictionary of different length units and values, to see the range of length units returned see the example code below or the Length units section under General Conversions.


.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   thermal_exp = dri_for.pipe_thermal_expansion(10000,'ft',80,375,'f')
   print(thermal_exp)
   # outputs the following dictionary:
   {
       'average_temp': 
          {
              'c': 108.61111111111111,
              'f': 227.5,
              'k': 381.76111111111106
          },
       'delta_temp':
          {
              'c': 64.16666666666667,
              'f': 147.5,
              'k': 337.31666666666666
          },
       'thermal_expansion':
          {
              'cm': 310.9595,
              'dm': 31.09595,
              'dam': 0.3109595,
              'fath': 1.7003485824999998,
              'ft': 10.202079252499999,
              'hm': 0.031095949999999997,
              'in': 122.425,
              'km': 0.003109595,
              'league': 0.0006488525,
              'm': 3.1095949999999997,
              'mi': 0.001934315,
              'mm': 3109.595,
              'nleague': 0.000563155,
              'nm': 0.0016772224999999999,
              'yd': 3.4006971649999995
          }
      } 

Stuck Pipe Function
------------

*stuck_pipe(stretch_value, stretch_units, pull_value, pull_units, dp_od_value, dp_id_value, dp_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - stretch_value
     - stretch length value (Integer or Float)
   * - stretch_units
     - stretch length units (String)
   * - pull_value
     - pull force value (Integer or Float)
   * - pull_units
     - pull force units (String)
   * - dp_od_value
     - drill pipe outer diameter value (Integer or Float)
   * - dp_id_value
     - drill pipe inner diameter value (Integer or Float)
   * - dp_units
     - drill pipe diameter units (String)

This function calculates the free point constant and the depth of the stuck pipe. The function takes in four value inputs(Integers or Floats) and three units inputs(Strings).  To see the range of stretch length and diameter units that can be input into the function see the Length units section under General Conversions. To see the range of pull force units that can be input into the function see the Force units section under Force and Power Conversions. The function returns a dictionary with two sub-dictionaries:

   * - "free_point_constant"
     - which is a float representing the free point constant.
   * - "stuck_depth"
     - which is a dictionary of different depth units and values, to see the range of depth units returned see the example code below or the Length units section under General Conversions.


.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   stuck_depth = dri_for.stuck_pipe(5,'in',100,'klbs',9.625,8.835,'in')
   print(stuck_depth)
   # outputs the following dictionary:
   {
       'average_temp': 28634.505899999967,,
       'stuck_depth':
          {
              'cm': 43638.98699159995
              'dm': 4363.898699159995
              'dam': 43.63898699159995
              'fath': 238.62093022417622
              'ft': 1431.7252949999984
              'hm': 4.363898699159995
              'in': 17180.70353999998
              'km': 0.4363898699159995
              'league': 0.0903418661144999
              'm': 436.3898699159995
              'mi': 0.2711687708729997
              'mm': 436389.86991599953
              'nleague': 0.07860171869549991
              'nm': 0.23566198355699972
              'yd': 477.24171727582296
          }
      } 

Annular Pressure Loss Function
------------

*annular_pressure_loss(mud_value, mud_units, length_value, length_unit, flow_value, flow_units, hole_value, dp_value, dp_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - length_value
     - annular length value (Integer or Float)
   * - length_unit
     - annular length units (String)
   * - flow_value
     - mud flow rate value (Integer or Float)
   * - flow_units
     - mud flow rate units (String)
   * - depth_value
     - depth value (Integer or Float)
   * - depth_units
     - depth units (String)
   * - hole_value
     - hole inner diameter value (Integer or Float)
   * - dp_value
     - drillpipe outer diameter value (Integer or Float)
   * - dp_units
     - diameter units (String)

This function calculates the annular pressure loss. The function takes in six value inputs(Integers or Floats) and five units inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of length, depth and diameter units that can be input into the function see the Length units section under General Conversions. To see the range of mud flow rate units that can be input into the function see the Flow Rate units section under Drilling Conversions. The function returns a dictionary of different pressure units and values, to see the range of pressure units returned see the example code below or the Pressure units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   pressure_loss = dri_for.annular_pressure_loss(13,'ppg', 8000, 'ft', 320, 'gpm', 6.5, 4, 'in')
   print(pressure_loss)
   # outputs the following dictionary:
   {
       'atm': 36.176327044120114,
       'bar': 36.65566337034605,
       'cm_Hg': 2749.4015288615656,
       'cm_h2o': 37378.488115447515,
       'dyne/cm2': 36665203.449134104,
       'ft_air': 948689.2398509005,
       'ft_hg': 90.20342697101725,
       'ft_h2o': 1226.324627647484,
       'in_air': 11384270.878210807,
       'in_hg': 1082.4410134585933,
       'in_h2o': 14715.892137315675,
       'kg/cm2': 37.378374324442035,
       'kg/m2': 373792.76524815056,
       'kPa': 3665.567297416083,
       'Mpa': 3.6655663446165607,
       'm_Hg': 27.49400860591527,
       'm_h2o': 373.78375112829985,
       'mbar': 36655.59715470736,
       'N/cm2': 366.5566286488224,
       'N/m2': 3666520.344913411,
       'N/mm2': 3.6655663446165607,
       'Pa': 3666520.344913411,
       'psf': 76557.43476937454,
       'psi': 531.6454500124446,
       'torr': 27494.00861449024
   }
   # Each key representing a different pressure unit
   print(pressure_loss['psi'])
   # outputs the following float:
   531.6454500124446 

Critical RPM Estimation Function
------------

*critical_rpm(pipe_length, pipe_units, od_value, id_value, dp_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - pipe_length
     - pipe length value (Integer or Float)
   * - pipe_units
     - pipe length units (String)
   * - id_value
     - drillpipe inner diameter value (Integer or Float)
   * - od_value
     - drillpipe outer diameter value (Integer or Float)
   * - dp_units
     - diameter units (String)

This function provides an estimation of the critical RPM to minimise vibrations. The function takes in three value inputs(Integers or Floats) and two units inputs(Strings). To see the range of length and diameter units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary of different angular velocity units and values, to see the range of angular velocity units returned see the example code below or the Angular Velocity units section under Force and Power Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   critical_rpm = dri_for.critical_rpm(32,'ft',4,3.5,'in')
   print(critical_rpm)
   # outputs the following dictionary:
   {
       'deg/hr': 3705955.345968158,
       'deg/min': 61765.92243280263,
       'deg/sec': 1029.4320405467106,
       'rad/hr': 64681.12398338261,
       'rad/min': 1078.0187279092165,
       'rad/sec': 17.966986233273904,
       'rph': 10294.320405467106,
       'rpm': 171.5720067577851,
       'rps': 2.8595391650299766
   }
   # Each key representing a different angular velocity unit
   print(critical_rpm['rpm'])
   # outputs the following float:
   171.5720067577851 

Equivalent Circulation Density Engineering Function
------------

*ecd_engineering_formula(mud_value, mud_units, reading_300, reading_600, viscosity_value, viscosity_units, flow_value,    flow_units, hole_dia_value, collar_dia_value, dp_dia_value, dia_units, hole_len_value, dp_len_value, collar_len_value, len_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - mud_value
     - mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - reading_300
     - reading at 300 rpm (Integer or Float)
   * - reading_600
     - reading at 600 rpm (Integer or Float)
   * - viscosity_value
     - plastic viscosity value (Integer or Float)
   * - viscosity_units
     - plastic viscosity units (String)
   * - flow_value
     - mud circulating rate value (Integer or Float)
   * - flow_units
     - mud circulating rate units (String)
   * - hole_dia_value
     - hole inner diameter value (Integer or Float)
   * - collar_dia_value
     - drill collar inner diameter  value (Integer or Float)
   * - dp_dia_value
     - drill pipe inner diameter value (Integer or Float)
   * - dia_units
     - diameter units (String)
   * - hole_len_value
     - hole depth value (Integer or Float)
   * - collar_len_value
     - drill collar length value (Integer or Float)
   * - dp_len_value
     - drill pipe length value (Integer or Float)
   * - len_units
     - length/depth units (String)

This function calculates the equivalent circulation density using a more complex and accurate formula. The function takes in ten value inputs(Integers or Floats) and five units inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of plastic viscosity units that can be input into the function see the Viscosity units section under Fluids Conversions. To see the range of mud circulating rate units that can be input into the function see the Flow Rate units section under Drilling Conversions. To see the range of length and diameter units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary of different mud weight units and values, to see the range of mud weight units returned see the example code below or the Mud Weight units section under Drilling Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   ecd = dri_for.ecd_engineering_formula(9.5,'ppg', 40, 60, 20, 'cp', 650, 'gpm', 8.5, 6.75, 5, 'in', 9000, 10000, 600, 'ft')
   print(ecd)
   # outputs the following dictionary:
   {
       'g/cm3': 1.2286752934480278,
       'g/L': 1228.675293448028,
       'kg/m3': 1228.675293448028,
       'kg/L': 1.2286752934480278,
       'kPa/m': 12.055055115524357,
       'lb/ft3': 76.71070047797262,
       'lb/bbl': 430.6593732668024,
       'ppg': 10.253794601590533,
       'psi/ft': 0.5332260299075922,
       'psi/100ft': 53.290913638543,
       'SG': 1.2286752934480278
   }
   # Each key representing a different mud weight unit
   print(ecd['SG'])
   # outputs the following float:
   1.2286752934480278 

Bottom Hole Pressure from Wellhead Pressure Function
------------

*bhp_wellhead_pressure(pressure_value, pressure_units, temp_value, temp_units, gas_value, depth_value, depth_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - pressure_value
     - wellhead pressure value (Integer or Float)
   * - pressure_units
     - wellhead pressure units (String)
   * - temp_value
     - average wellbore temperature value (Integer or Float)
   * - temp_units
     - average wellbore temperature units (String)
   * - gas_value
     - specific gravity of gas value (Integer or Float)
   * - depth_value
     - hole depth value (Integer or Float)
   * - depth_units
     - hole depth units (String)

This function calculates the bottom hole pressure in a dry gas well using wellhead pressure. The function takes in four value inputs(Integers or Floats) and three units inputs(Strings). To see the range of wellhead pressure units that can be input into the function see the Pressure units section under General Conversions. To see the range of wellbore temperature units that can be input into the function see the Temperature units section under General Conversions. To see the range of depth units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary of different bottomhole pressure units and values, to see the range of pressure units returned see the example code below or the Pressure units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   downhole_pressure = dri_for.bhp_wellhead_pressure(2000, 'psi', 160, 'f', 0.75, 9000, 'ft')
   print(downhole_pressure)
   # outputs the following dictionary:
   {
       'atm': 166.89446133187715,
       'bar': 169.1058129117297,
       'cm_Hg': 12683.982168360313,
       'cm_h2o': 172440.4645009841,
       'dyne/cm2': 169149824.74047217,
       'ft_air': 4376646.071978671,
       'ft_hg': 416.1409845796964,
       'ft_h2o': 5657.478380810552,
       'in_air': 52519752.86374405,
       'in_hg': 4993.691306593421,
       'in_h2o': 67889.72490988385,
       'kg/cm2': 172.43993954198143,
       'kg/m2': 1724441.0171812181,
       'kPa': 16910.585721759562,
       'Mpa': 16.910581326151274,
       'm_Hg': 126.83979085389286,
       'm_h2o': 1724.3994317909978,
       'mbar': 169105.50743507541,
       'N/cm2': 1691.0581057984264,
       'N/m2': 16914982.474047218,
       'N/mm2': 16.910581326151274,
       'Pa': 16914982.474047218,
       'psf': 353187.09445551044,
       'psi': 2452.6724587368467,
       'torr': 126839.7908934523
   }
   # Each key representing a different pressure unit
   print(downhole_pressure['psi'])
   # outputs the following float:
   1.2286752934480278 

Loss of Hydrostatic Pressure After Filling Annulus due to Losses Function
------------

*pressure_decrease_annular_filling(mud_value, fluid_value, mud_units, depth_value, depth_units, annular_value, annular_units, volume_value, volume_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - mud_value
     - mud weight value (Integer or Float)
   * - fluid_value
     - fluid weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - depth_value
     - true vertical depth value (Integer or Float)
   * - depth_units
     - depth units (String)
   * - annular_value
     - annular capacity value (Integer or Float)
   * - annular_units
     - annular capacity units (String)
   * - volume_value
     - added fluid volume value (Integer or Float)
   * - volume_units
     - fluid volume units (String)

This function calculates the tensile capacity of the drillpipe. The function takes in five value inputs(Integers or Floats) and four units inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of depth units that can be input into the function see the Length units section under General Conversions. To see the range of annular capacity units that can be input into the function see the Pipe Capacity units section under Production Conversions.  To see the range of volume units that can be input into the function see the Volume units section under General Conversions. The function returns a dictionary with three sub-dictionaries:

   * - "pressure_decrease" which is a dictionary of different pressure units and values, to see the range of pressure units returned see the example code below or the Pressure units section under General Conversions.
   * - "fluid_length" which is a dictionary of different length units and values, to see the range of length units returned see the example code below or the Length units section under General Conversions.
   * - "mud_weight_td" which is a dictionary of different mud weight units and values, to see the range of mud weight units returned see the example code below or the Mud Weight units section under Drilling Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   pressure_decrease = dri_for.pressure_decrease_annular_filling(13, 8.6, 'ppg', 6000, 'ft', 0.1422, 'bbl/ft', 140, 'bbl')
   print(pressure_decrease)
   # outputs the following dictionary:
   {
       'pressure_decrease': 
          {
              'atm': 15.32804720344198,
              'bar': 15.531143825875619,
              'cm_Hg': 1164.9318728296737,
              'cm_h2o': 15837.407416405935,
              'dyne/cm2': 15535185.993501138,
              'ft_air': 401963.23502099665,
              'ft_hg': 38.219534692887244,
              'ft_h2o': 519.5984035747825,
              'in_air': 4823558.82025196,
              'in_hg': 458.63436962519415,
              'in_h2o': 6235.179404654278,
              'kg/cm2': 15.837359202724617,
              'kg/m2': 158377.41468450153,
              'kPa': 1553.1147895048427,
              'Mpa': 1.5531143858000656,
              'm_Hg': 11.649315896811196,
              'm_h2o': 158.37359536767588,
              'mbar': 15531.115770057952,
              'N/cm2': 155.31143611708686,
              'N/m2': 1553518.599350114,
              'N/mm2': 1.5531143858000656,
              'Pa': 1553518.599350114,
              'psf': 32437.675955556493,
              'psi': 225.26019690576652,
              'torr': 11649.315900444444
          },
       'fluid_length':
          {
              'cm': 30008.438818565402,
              'dm': 3000.84388185654,
              'dam': 30.008438818565402,
              'fath': 164.08817158931083,
              'ft': 984.5288326300985,
              'hm': 3.00084388185654,
              'in': 11814.345991561182,
              'km': 0.30008438818565397,
              'league': 0.06212376933895922,
              'm': 300.084388185654,
              'mi': 0.18646976090014064,
              'mm': 300084.388185654,
              'nleague': 0.05405063291139241,
              'nm': 0.1620534458509142,
              'yd': 328.1762447257384
          },
       'mud_weight_td':
          {
              'g/cm3': 1.4712299998124707,
              'g/L': 1471.2299998124706,
              'kg/m3': 1471.2299998124706,
              'kg/L': 1.4712299998124707,
              'kPa/m': 14.434862351289263,
              'lb/ft3': 91.85427952498827,
              'lb/bbl': 515.676511954993,
              'ppg': 12.278012189404594,
              'psi/ft': 0.6384910122831692,
              'psi/100ft': 63.81115603164557,
              'SG': 1.4712299998124707
          }
      } 

Margin of Overpull Function
------------

*overpull_margin(max_value, hook_value, weight_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - max_value
     - maximum allowable weight value (Integer or Float)
   * - hook_value
     - hook load value (Integer or Float)
   * - weight_units
     - weight units (String)

This function calculates the additional tension that can be applied to the drillstring. The function takes in two value inputs(Integers or Floats) and one units input(Strings). To see the range of weight units that can be input into the function see the Weight units section under General Conversions. The function returns a dictionary with one sub-dictionary and a safety factor value:

   * - "margin_of_overpull" which is a dictionary of different weight units and values, to see the range of weight units returned see the example code below or the Weight units section under General Conversions.
   * - "safety_factor" which is a float.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   overpull_margin = dri_for.overpull_margin(300000, 100000, 'lb')
   print(overpull_margin)
   # outputs the following dictionary:
   {
       'margin_of_overpull': 
          {
              'ct': 453592370.0,
              'cg': 9071847400.0,
              'dg': 907184740.0,
              'dram': 51199999.86,
              'gr': 1400000216.06,
              'g': 90718474.0,
              'kg': 90718.48,
              'kip': 200.0,
              't_long': 89.28,
              't_metric': 90.72,
              'mg': 90718474000.0,
              'oz': 3200000.0,
              'lb': 200000,
              'slug': 6216.2,
              't_short': 100.0,
              'toz': 2916666.66,
              'KdaN': 80.70853338209297,
              'daN': 80708.53295128162
          },
       'safety_factor': 3.0
      } 

Pressure Required to Break Circulation in Drill String Function
------------

*break_circ_pipe(gel_value, gel_units, length_value, length_units, diameter_value, diameter_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - gel_value
     - gel strength value (Integer or Float)
   * - gel_units
     - gel strength units (String)
   * - length_value
     - drill string length value (Integer or Float)
   * - length_units
     - drill string length units (String)
   * - diameter_value
     - drill pipe inner diameter value (Integer or Float)
   * - diameter_units
     - drill pipe inner diameter units (String)

This function calculates the pressure required to break circulation in the drill string. The function takes in three value inputs(Integers or Floats) and three units inputs(Strings). To see the range of gel strength units that can be input into the function see the Fluid Yield Point units section under Fluids Conversions. To see the range of diameter and length units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary of different pressure units and values, to see the range of pressure units returned see the example code below or the Pressure units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   required_pressure = dri_for.break_circ_pipe(12, 'lbf/100ft2', 11500, 'ft', 3.32, 'in')
   print(required_pressure)
   # outputs the following dictionary:
   {
       'atm': 9.428055224816099,
       'bar': 9.552976954692294,
       'cm_Hg': 716.5323726117126,
       'cm_h2o': 9741.35516142315,
       'dyne/cm2': 9555463.2322393,
       'ft_air': 247241.64323245877,
       'ft_hg': 23.508270751567146,
       'ft_h2o': 319.5972962902466,
       'in_air': 2966899.7187895053,
       'in_hg': 282.0992203008136,
       'in_h2o': 3835.1666708408843,
       'kg/cm2': 9.741325505900562,
       'kg/m2': 97415.60631896919,
       'kPa': 955.2979457580332,
       'Mpa': 0.955297697445193,
       'm_Hg': 7.1653219845122305,
       'm_h2o': 97.41325711365455,
       'mbar': 9552.959697973625,
       'N/cm2': 95.52976822961381,
       'N/m2': 955546.3232239302,
       'N/mm2': 0.955297697445193,
       'Pa': 955546.3232239302,
       'psf': 19951.93492129916,
       'psi': 138.55421686746988,
       'torr': 7165.321986746987
   }
   # Each key representing a different pressure unit
   print(downhole_pressure['psi'])
   # outputs the following float:
   138.55421686746988 

Pressure Required to Break Circulation in the Annulus Function
------------

*break_circ_annulus(gel_value, gel_units, length_value, length_units, hole_value, pipe_value, diameter_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - gel_value
     - gel strength value (Integer or Float)
   * - gel_units
     - gel strength units (String)
   * - length_value
     - drill string length value (Integer or Float)
   * - length_units
     - drill string length units (String)
   * - hole_value
     - hole inner diameter value (Integer or Float)
   * - pipe_value
     - drill pipe outer diameter value (Integer or Float)
   * - diameter_units
     - drill pipe inner diameter units (String)

This function calculates the pressure required to break circulation in the annulus. The function takes in four value inputs(Integers or Floats) and three units inputs(Strings). To see the range of gel strength units that can be input into the function see the Fluid Yield Point units section under Fluids Conversions. To see the range of diameter and length units that can be input into the function see the Length units section under General Conversions. The function returns a dictionary of different pressure units and values, to see the range of pressure units returned see the example code below or the Pressure units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   required_pressure = dri_for.break_circ_annulus(12, 'lbf/100ft2', 11500, 'ft', 6.5, 4, 'in')
   print(required_pressure)
   # outputs the following dictionary:
   {
       'atm': 12.52045733855578,
       'bar': 12.686353395831368,
       'cm_Hg': 951.5549908283544,
       'cm_h2o': 12936.519654369944,
       'dyne/cm2': 12689655.172413792,
       'ft_air': 328336.90221270523,
       'ft_hg': 31.218983558081174,
       'ft_h2o': 424.42520947344747,
       'in_air': 3940042.8265524628,
       'in_hg': 374.6277645594805,
       'in_h2o': 5093.101338876694,
       'kg/cm2': 12.936480271835947,
       'kg/m2': 129367.92519159109,
       'kPa': 1268.635671966668,
       'Mpa': 1.2686353422072163,
       'm_Hg': 9.515547595432242,
       'm_h2o': 129.36480544693325,
       'mbar': 12686.330478908976,
       'N/cm2': 126.86353220892714,
       'N/m2': 1268965.5172413792,
       'N/mm2': 1.2686353422072163,
       'Pa': 1268965.5172413792,
       'psf': 26496.16957548528,
       'psi': 184.0,
       'torr': 9515.5475984
   }
   # Each key representing a different pressure unit
   print(downhole_pressure['psi'])
   # outputs the following float:
   184.0 

Drillpipe Tensile Capacity Function
------------

*drillpipe_tensile_capacity(od_value, id_value, diameter_units, pressure_value, pressure_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - od_value
     - outer diameter value (Integer or Float)
   * - id_value
     - inner diameter value (Integer or Float)
   * - diameter_units
     - diameter units (String)
   * - pressure_value
     - yield strength value (Integer or Float)
   * - pressure_units
     - yield strength units (String)

This function calculates the tensile capacity of the drillpipe. The function takes in three value inputs(Integers or Floats) and two units inputs(Strings). To see the range of diameter units that can be input into the function see the Length units section under General Conversions. To see the range of yield strength units that can be input into the function see the Pressure units section under General Conversions. The function returns a dictionary with three sub-dictionaries of different drill pipe grades:

   * - "new_pipe" which is a dictionary of different weight units and values, to see the range of weight units returned see the example code below or the Weight units section under General Conversions.
   * - "premium" which is a dictionary of different length units and values, to see the range of length units returned see the example code below or the Length units section under General Conversions.
   * - "class_two" which is a dictionary of different mud weight units and values, to see the range of mud weight units returned see the example code below or the Mud Weight units section under Drilling Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_formulas as dri_for

   tensile_capacity = dri_for.drillpipe_tensile_capacity(5.5, 4.276, 'in', 135000, 'psi')
   print(tensile_capacity)
   # outputs the following dictionary:
   {
       'new_pipe': 
          {
              'ct': 2877411701.8938413,
              'cg': 57548234037.87682,
              'dg': 5754823403.787683,
              'dram': 324792673.9467135,
              'gr': 8881051073.11428,
              'g': 575482340.3787683,
              'kg': 575482.3784404099,
              'kip': 1268.7213860735096,
              't_long': 566.3572267432147,
              't_metric': 575.4920207229441,
              'mg': 575482340378.7683,
              'oz': 20299542.177176155,
              'lb': 1268721.3860735097,
              'slug': 39433.12940055076,
              't_short': 634.3606930367548,
              'toz': 18502186.83794797,
              'KdaN': 511.9832117024456,
              'daN': 511983.2089695478
          },
       'premium':
          {
              'ct': 2244286940.5147786,
              'cg': 44885738810.29557,
              'dg': 4488573881.029557,
              'dram': 253327654.16701454,
              'gr': 6926929131.593034,
              'g': 448857388.10295576,
              'kg': 448857.41778979026,
              'kip': 989.5611517957318,
              't_long': 441.74009816161464,
              't_metric': 448.86493845454396,
              'mg': 448857388102.9557,
              'oz': 15832978.428731708,
              'lb': 989561.1517957317,
              'slug': 30756.55015896314,
              't_short': 494.7805758978659,
              'toz': 14431100.097369049,
              'KdaN': 399.3301462666409,
              'daN': 399330.1441350701
          },
       'class_two':
          {
              'ct': 1938532513.7628002,
              'cg': 38770650275.256004,
              'dg': 3877065027.5256004,
              'dram': 218815110.21285656,
              'gr': 5983226609.625852,
              'g': 387706502.75256,
              'kg': 387706.52839495585,
              'kip': 854.7465266061685,
              't_long': 381.5588494769936,
              't_metric': 387.71302446855805,
              'mg': 387706502752.56,
              'oz': 13675944.425698696,
              'lb': 854746.5266061685,
              'slug': 26566.376793446325,
              't_short': 427.37326330308423,
              'toz': 12465053.484515073,
              'KdaN': 344.92669287910985,
              'daN': 344926.69103793736
          }
      }
