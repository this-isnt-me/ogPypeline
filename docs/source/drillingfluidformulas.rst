Fluids Formulas
==================

This module contains functions, outlined below, for formulas related to fluids. 

Bulk Density of Cuttings Function
------------

*bulk_density_cuttings(rw_value)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - rw_value
     - weight with cuttings plus water in ppg (Integer or Float)

This function calculates the bulk density of cuttings using a mud balance. The function takes in one value input(Integers or Floats). The function returns a dictionary of different mud weight units and values, to see the range of mud weight units returned see the example code below or the Mud Weight units section under Drilling Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_fluid_formulas as dff

   rw = dir_for.bulk_density_cuttings(14)
   print(rw)
   # outputs the following dictionary:
   {
       'g/cm3': 3.1249999999999996,
       'g/L': 3124.9999999999995,
       'kg/m3': 3124.9999999999995,
       'kg/L': 3.1249999999999996,
       'kPa/m': 30.660701249999995,
       'lb/ft3': 195.10520062499998,
       'lb/bbl': 1095.3345840624997,
       'ppg': 26.079394999999995,
       'psi/ft': 1.3562009374999997,
       'psi/100ft': 135.53955593749998,
       'SG': 3.1249999999999996
   }
   # Each key representing a different unit
   print(rw['SG'])
   # outputs the following float:
   3.1249999999999996 

Decrease Oil-Water Ratio Function
------------

*decrease_oil_water_ratio(oil_vol, water_vol, mud_value, mud_units, new_oil, new_water)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - oil_vol
     - oil percentage value (Integer or Float)
   * - water_vol
     - water percentage value (Integer or Float)
   * - mud_value
     - mud volume value (Integer or Float)
   * - mud_units
     - volume units (String)
   * - new_oil
     - new oil percentage value (Integer or Float)
   * - new_water
     - new water percentage value (Integer or Float)

This function calculates the volume of liquid to add to decrease the oil-water ratio. The function takes in five value inputs(Integers or Floats) and one units input(Strings). To see the range of volume units that can be input into the function see the Volume units section under General Conversions. The function returns a dictionary with two sub-dictionaries:

   * - "water_added_per_100" which is a dictionary of different volume units and values representing the volume added per 100 barrels, to see the range of volume units returned see the example code below or the Volume units section under General Conversions.
   * - "water_added_total" which is a dictionary of different volume units and values representing the total volume added, to see the range of volume units returned see the example code below or the Volume units section under General Conversions.


.. code:: python

   # Example Code
   from ogPypeline import drilling_fluid_formulas as dff

   water_added = dff.decrease_oil_water_ratio(56, 14, 300, 'bbl', 70, 30)
   print(water_added)
   # outputs the following dictionary:
   {
       'water_added_per_100': 
          {
              'bbl': 10.0,
              'bucket': 84.0,
              'bu_us': 45.116768,
              'cm3': 1589872.9492849999,
              'ft3': 56.145832999999996,
              'in3': 97020.0,
              'm3': 1.5898729999999999,
              'mm3': 1589872949.28538,
              'yd3': 2.079475,
              'C': 6720.0,
              'dr': 430080.0,
              'drum': 7.636364,
              'fl_oz': 53760.0,
              'gal_us': 420.0,
              'gill': 13440.0,
              'gal_uk': 349.72315799999996,
              'kL': 1.5898729999999999,
              'L': 1589.872949,
              'ml': 1589872.9492849999,
              'Pt': 3360.0,
              'qt_dr': 1443.736563,
              'qt_lq': 1680.0,
              'tbsp': 107520.0,
              'tsp': 322560.0,
              'toe': 1.363636
          },
       'water_added_total':
          {
              'bbl': 30.0,
              'bucket': 252.0,
              'bu_us': 135.350304,
              'cm3': 4769618.847855,
              'ft3': 168.437499,
              'in3': 291060.0,
              'm3': 4.769619,
              'mm3': 4769618847.85614,
              'yd3': 6.238425,
              'C': 20160.0,
              'dr': 1290240.0,
              'drum': 22.909092,
              'fl_oz': 161280.0,
              'gal_us': 1260.0,
              'gill': 40320.0,
              'gal_uk': 1049.1694739999998,
              'kL': 4.769619,
              'L': 4769.618847,
              'ml': 4769618.847855,
              'Pt': 10080.0,
              'qt_dr': 4331.209688999999,
              'qt_lq': 5040.0,
              'tbsp': 322560.0,
              'tsp': 967680.0,
              'toe': 4.090908
          }
      } 

Oil-Water Ratio from Retort Data Function
------------

*retort_oil_water_ratio(oil_vol, water_vol)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - oil_vol
     - oil percentage value (Integer or Float)
   * - water_vol
     - water percentage value (Integer or Float)

This function calculates the oil water ratio. The function takes in two value inputs(Integers or Floats). The function returns a dictionary with two values representing the percentage of oil and water.


.. code:: python

   # Example Code
   from ogPypeline import drilling_fluid_formulas as dff

   ratios = dff.retort_oil_water_ratio(56, 14)
   print(ratios)
   # outputs the following dictionary:
   {
       'oil_percent': 80.0,
       'water_added_total': 20.0
      } 

Oil Water Density Function
------------

*oil_water_density(oil_vol, water_vol, oil_weight, water_weight, weight_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - oil_vol
     - oil percentage value (Integer or Float)
   * - water_vol
     - water percentage value (Integer or Float)
   * - oil_weight
     - mud weight values (Integer or Float)
   * - water_weight
     - mud weight values (Integer or Float)
   * - weight_units
     - fluid weight units (String)

This function calculates the density of an oil and water mixture. The function takes in four value inputs(Integers or Floats) and one units input(String). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. The function returns a dictionary of different mud weight units and values, to see the range of mud weight units returned see the example code below or the Mud Weight units section under Drilling Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_fluid_formulas as dff

   oil_water_density = dir_for.oil_water_density(80, 20, 7, 8.33, 'ppg')
   print(oil_water_density)
   # outputs the following dictionary:
   {
       'g/cm3': 0.8706586224,
       'g/L': 870.6586224,
       'kg/m3': 870.6586224,
       'kg/L': 0.8706586224,
       'kPa/m': 8.5424015082,
       'lb/ft3': 54.3584079192,
       'lb/bbl': 305.172,
       'ppg': 7.266,
       'psi/ft': 0.3778523448,
       'psi/100ft': 37.762778907000005,
       'SG': 0.8706586224
   }
   # Each key representing a different unit
   print(oil_water_density['ppg'])
   # outputs the following float:
   7.266 

Weighting Up with Barite Function
------------

*barite_increase(current_mud, new_mud, mud_units, mud_vol, vol_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - current_mud
     - current mud weight value (Integer or Float)
   * - new_mud
     - new mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - mud_vol
     - current mud volume value (Integer or Float)
   * - vol_units
     - volume units (String)

This function calculates the volume of barite required to increase the mud weight using barite. The function takes in three value inputs(Integers or Floats) and two units inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of volume units that can be input into the function see the Volume units section under General Conversions. The function returns a dictionary with two sub-dictionaries that each contains 3 sub dictionaries:

   * - "per_100_bbl_mud" which is a dictionary of different volume units and values representing the volume required, the weight required, and volume increase per 100 barrels. The three subdictionaries are 'weight_required'; to see the range of weight units returned see the example code below or the Weight units section under General Conversions, 'volume_required'; to see the range of volume units returned see the example code below or the Additive Volume units section under Fluids Conversions, 'volume_increase'; to see the range of volume units returned see the example code below or the Volume units section under General Conversions.
   * - "water_added_total" which is a dictionary of different volume units and values representing the volume required, the weight required, and volume increase for the total volume of mud. The three subdictionaries are 'weight_required'; to see the range of weight units returned see the example code below or the Weight units section under General Conversions, 'volume_required'; to see the range of volume units returned see the example code below or the Additive Volume units section under Fluids Conversions, 'volume_increase'; to see the range of volume units returned see the example code below or the Volume units section under General Conversions.


.. code:: python

   # Example Code
   from ogPypeline import drilling_fluid_formulas as dff

   barite_increase = dff.barite_increase(10.1, 11.1, 'ppg', 1000, 'bbl')
   print(barite_increase)
   # outputs the following dictionary:
   {
       'water_added_per_100': 
          {
              'weight_required': 
              {
                  'ct': 13949388.78451883,
                  'cg': 278987775.6903766,
                  'dg': 27898777.56903766,
                  'dram': 1574560.6651506277,
                  'gr': 43054399.94996234,
                  'g': 2789877.7569037657,
                  'kg': 2789.877941422594,
                  'kip': 6.150627615062762,
                  't_long': 2.7456401673640167,
                  't_metric': 2.7899246861924687,
                  'mg': 2789877756.9037657,
                  'oz': 98410.04184100419,
                  'lb': 6150.627615062762,
                  'slug': 191.1676569037657,
                  't_short': 3.075313807531381,
                  'toz': 89696.65251464436,
                  'KdaN': 2.482040670955579,
                  'daN': 2482.0406577067783
              },
              'volume_required': 
              {
                  'sack': 61.50627615062762,
                  'ft3': 229.62556659693442,
                  'm3': 6.502271942926393,
                  'bbl': 54.53074679852935
              },
              'volume_increase': 
              {
                  'bbl': 4.184100418410042,
                  'bucket': 35.14644351464435,
                  'bu_us': 18.87730878661088,
                  'cm3': 665218.8072322175,
                  'ft3': 23.49198033472803,
                  'in3': 40594.14225941423,
                  'm3': 0.6652188284518828,
                  'mm3': 665218807.2323766,
                  'yd3': 0.8700732217573222,
                  'C': 2811.715481171548,
                  'dr': 179949.79079497908,
                  'drum': 3.195131380753138,
                  'fl_oz': 22493.723849372385,
                  'gal_us': 175.73221757322176,
                  'gill': 5623.430962343096,
                  'gal_uk': 146.3276811715481,
                  'kL': 0.6652188284518828,
                  'L': 665.2188071129707,
                  'ml': 665218.8072322175,
                  'Pt': 1405.857740585774,
                  'qt_dr': 604.0738757322175,
                  'qt_lq': 702.928870292887,
                  'tbsp': 44987.44769874477,
                  'tsp': 134962.3430962343,
                  'toe': 0.5705589958158995
              }
          },
       'water_added_total': 
          {
              'weight_required': 
              {
                  'ct': 139493887.8451883,
                  'cg': 2789877756.9037657,
                  'dg': 278987775.6903766,
                  'dram': 15745606.651506277,
                  'gr': 430543999.4996234,
                  'g': 27898777.569037657,
                  'kg': 27898.77941422594,
                  'kip': 61.50627615062761,
                  't_long': 27.45640167364017,
                  't_metric': 27.899246861924688,
                  'mg': 27898777569.037655,
                  'oz': 984100.4184100418,
                  'lb': 61506.276150627615,
                  'slug': 1911.676569037657,
                  't_short': 30.753138075313807,
                  'toz': 896966.5251464435,
                  'KdaN': 24.820406709555787,
                  'daN': 24820.40657706778
              },
              'volume_required': 
              {
                  'sack': 615.0627615062762,
                  'ft3': 2296.255665969344,
                  'm3': 65.02271942926393,
                  'bbl': 545.3074679852934
              },
              'volume_increase': 
              {
                  'bbl': 41.84100418410041,
                  'bucket': 351.46443514644346,
                  'bu_us': 188.77308786610877,
                  'cm3': 6652188.072322175,
                  'ft3': 234.9198033472803,
                  'in3': 405941.4225941422,
                  'm3': 6.652188284518828,
                  'mm3': 6652188072.323765,
                  'yd3': 8.70073221757322,
                  'C': 28117.154811715478,
                  'dr': 1799497.9079497906,
                  'drum': 31.951313807531378,
                  'fl_oz': 224937.23849372382,
                  'gal_us': 1757.3221757322174,
                  'gill': 56234.309623430956,
                  'gal_uk': 1463.2768117154808,
                  'kL': 6.652188284518828,
                  'L': 6652.188071129706,
                  'ml': 6652188.072322175,
                  'Pt': 14058.577405857739,
                  'qt_dr': 6040.738757322175,
                  'qt_lq': 7029.2887029288695,
                  'tbsp': 449874.47698744765,
                  'tsp': 1349623.430962343,
                  'toe': 5.7055899581589955
              }
      } 

Starting Mud Volume to Achieve A Required Mud Weight and Volume Using Barite Function
------------

*barite_starting_vol(current_mud, new_mud, mud_units, mud_vol, vol_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - current_mud
     - current mud weight value (Integer or Float)
   * - new_mud
     - new mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - mud_vol
     - required mud volume value (Integer or Float)
   * - vol_units
     - volume units (String)

This function calculates the volume of barite required to increase the mud weight using barite. The function takes in three value inputs(Integers or Floats) and two units inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of volume units that can be input into the function see the Volume units section under General Conversions. The function returns a dictionary of different volume units and values, to see the range of volume units returned see the example code below or the Volume units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_fluid_formulas as dff

   barite_starting_vol = dir_for.barite_starting_vol(10, 13, 'ppg', 100, 'bbl')
   print(barite_starting_vol)
   # outputs the following dictionary:
   {
       'bbl': 88.0,
       'bucket': 739.2,
       'bu_us': 397.0275584,
       'cm3': 13990881.953707999,
       'ft3': 494.08333039999997,
       'in3': 853776.0,
       'm3': 13.9908824,
       'mm3': 13990881953.711344,
       'yd3': 18.29938,
       'C': 59136.0,
       'dr': 3784704.0,
       'drum': 67.2000032,
       'fl_oz': 473088.0,
       'gal_us': 3696.0,
       'gill': 118272.0,
       'gal_uk': 3077.5637903999996,
       'kL': 13.9908824,
       'L': 13990.8819512,
       'ml': 13990881.953707999,
       'Pt': 29568.0,
       'qt_dr': 12704.8817544,
       'qt_lq': 14784.0,
       'tbsp': 946176.0,
       'tsp': 2838528.0,
       'toe': 11.9999968
   }
   # Each key representing a different unit
   print(barite_starting_vol['bbl'])
   # outputs the following float:
   88.0

Weighting Up with Calcium Carbonate Function
------------

*calcium_carbonate_increase(current_mud, new_mud, mud_units, mud_vol, vol_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - current_mud
     - current mud weight value (Integer or Float)
   * - new_mud
     - new mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - mud_vol
     - current mud volume value (Integer or Float)
   * - vol_units
     - volume units (String)

This function calculates the volume of Calcium Carbonate required to increase the mud weight using Calcium Carbonate. The function takes in three value inputs(Integers or Floats) and two units inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of volume units that can be input into the function see the Volume units section under General Conversions. The function returns a dictionary with two sub-dictionaries that each contains 3 sub dictionaries:

   * - "per_100_bbl_mud" which is a dictionary of different volume units and values representing the volume required, the weight required, and volume increase per 100 barrels. The three subdictionaries are 'weight_required'; to see the range of weight units returned see the example code below or the Weight units section under General Conversions, 'volume_required'; to see the range of volume units returned see the example code below or the Additive Volume units section under Fluids Conversions, 'volume_increase'; to see the range of volume units returned see the example code below or the Volume units section under General Conversions.
   * - "water_added_total" which is a dictionary of different volume units and values representing the volume required, the weight required, and volume increase for the total volume of mud. The three subdictionaries are 'weight_required'; to see the range of weight units returned see the example code below or the Weight units section under General Conversions, 'volume_required'; to see the range of volume units returned see the example code below or the Additive Volume units section under Fluids Conversions, 'volume_increase'; to see the range of volume units returned see the example code below or the Volume units section under General Conversions.


.. code:: python

   # Example Code
   from ogPypeline import drilling_fluid_formulas as dff

   calcium_carbonate_increase = dff.calcium_carbonate_increase(10, 13, 'ppg', 500, 'bbl')
   print(calcium_carbonate_increase)
   # outputs the following dictionary:
   {
       'water_added_per_100': 
          {
              'weight_required': 
              {
                  'ct': 67680756.26052633,
                  'cg': 1353615125.2105265,
                  'dg': 135361512.52105266,
                  'dram': 7639578.926478948,
                  'gr': 208894769.08053157,
                  'g': 13536151.252105264,
                  'kg': 13536.152147368422,
                  'kip': 29.842105263157897,
                  't_long': 13.321515789473686,
                  't_metric': 13.536378947368423,
                  'mg': 13536151252.105265,
                  'oz': 477473.68421052635,
                  'lb': 29842.105263157897,
                  'slug': 927.5224736842106,
                  't_short': 14.921052631578949,
                  'toz': 435197.3674263158,
                  'KdaN': 12.042562744117557,
                  'daN': 12042.56267983597
              },
              'volume_required': 
              {
                  'sack': 298.42105263157896,
                  'ft3': 1114.1156250000133,
                  'm3': 31.5482412388752,
                  'bbl': 264.57662337662396
              },
              'volume_increase': 
              {
                  'bbl': 31.57894736842105,
                  'bucket': 265.2631578947368,
                  'bu_us': 142.47400421052632,
                  'cm3': 5020651.418794736,
                  'ft3': 177.30263052631577,
                  'in3': 306378.94736842107,
                  'm3': 5.020651578947368,
                  'mm3': 5020651418.795937,
                  'yd3': 6.566763157894737,
                  'C': 21221.052631578947,
                  'dr': 1358147.3684210526,
                  'drum': 24.114833684210524,
                  'fl_oz': 169768.42105263157,
                  'gal_us': 1326.3157894736842,
                  'gill': 42442.10526315789,
                  'gal_uk': 1104.3889199999999,
                  'kL': 5.020651578947368,
                  'L': 5020.651417894736,
                  'ml': 5020651.418794736,
                  'Pt': 10610.526315789473,
                  'qt_dr': 4559.16809368421,
                  'qt_lq': 5305.263157894737,
                  'tbsp': 339536.84210526315,
                  'tsp': 1018610.5263157894,
                  'toe': 4.3062189473684205
              }
          },
       'water_added_total': 
          {
              'weight_required': 
              {
                  'ct': 338403781.30263156,
                  'cg': 6768075626.052631,
                  'dg': 676807562.6052631,
                  'dram': 38197894.63239474,
                  'gr': 1044473845.4026577,
                  'g': 67680756.26052631,
                  'kg': 67680.7607368421,
                  'kip': 149.21052631578948,
                  't_long': 66.60757894736842,
                  't_metric': 67.68189473684211,
                  'mg': 67680756260.52631,
                  'oz': 2387368.4210526315,
                  'lb': 149210.52631578947,
                  'slug': 4637.612368421052,
                  't_short': 74.60526315789474,
                  'toz': 2175986.837131579,
                  'KdaN': 60.212813720587775,
                  'daN': 60212.813399179846
              },
              'volume_required': 
              {
                  'sack': 1492.1052631578948,
                  'ft3': 5570.578125000066,
                  'm3': 157.741206194376,
                  'bbl': 1322.88311688312
              },
              'volume_increase': 
              {
                  'bbl': 157.89473684210526,
                  'bucket': 1326.3157894736842,
                  'bu_us': 712.3700210526316,
                  'cm3': 25103257.09397368,
                  'ft3': 886.5131526315789,
                  'in3': 1531894.7368421052,
                  'm3': 25.103257894736842,
                  'mm3': 25103257093.979683,
                  'yd3': 32.83381578947368,
                  'C': 106105.26315789473,
                  'dr': 6790736.842105263,
                  'drum': 120.57416842105263,
                  'fl_oz': 848842.1052631579,
                  'gal_us': 6631.578947368421,
                  'gill': 212210.52631578947,
                  'gal_uk': 5521.9446,
                  'kL': 25.103257894736842,
                  'L': 25103.257089473682,
                  'ml': 25103257.09397368,
                  'Pt': 53052.63157894737,
                  'qt_dr': 22795.84046842105,
                  'qt_lq': 26526.315789473683,
                  'tbsp': 1697684.2105263157,
                  'tsp': 5093052.631578947,
                  'toe': 21.531094736842107
              }
      } 

Starting Mud Volume to Achieve A Required Mud Weight and Volume Using Calcium Carbonate Function
------------

*barite_starting_vol(current_mud, new_mud, mud_units, mud_vol, vol_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - current_mud
     - current mud weight value (Integer or Float)
   * - new_mud
     - new mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - mud_vol
     - required mud volume value (Integer or Float)
   * - vol_units
     - volume units (String)

This function calculates the volume of calcium carbonate required to increase the mud weight using calcium carbonate. The function takes in three value inputs(Integers or Floats) and two units inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of volume units that can be input into the function see the Volume units section under General Conversions. The function returns a dictionary of different volume units and values, to see the range of volume units returned see the example code below or the Volume units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_fluid_formulas as dff

   calcium_carbonate_starting_vol = dir_for.calcium_carbonate_starting_vol(10, 13, 'ppg', 100, 'bbl')
   print(calcium_carbonate_starting_vol)
   # outputs the following dictionary:
   {
       'bbl': 76.0,
       'bucket': 638.4,
       'bu_us': 342.8874368,
       'cm3': 12083034.414565999,
       'ft3': 426.7083308,
       'in3': 737352.0,
       'm3': 12.0830348,
       'mm3': 12083034414.568888,
       'yd3': 15.80401,
       'C': 51072.0,
       'dr': 3268608.0,
       'drum': 58.0363664,
       'fl_oz': 408576.0,
       'gal_us': 3192.0,
       'gill': 102144.0,
       'gal_uk': 2657.8960008,
       'kL': 12.0830348,
       'L': 12083.0344124,
       'ml': 12083034.414565999,
       'Pt': 25536.0,
       'qt_dr': 10972.397878799999,
       'qt_lq': 12768.0,
       'tbsp': 817152.0,
       'tsp': 2451456.0,
       'toe': 10.3636336
   }
   # Each key representing a different unit
   print(calcium_carbonate_starting_vol['bbl'])
   # outputs the following float:
   76.0 

Weighting Up with Hematite Function
------------

*hematite_increase(current_mud, new_mud, mud_units, mud_vol, vol_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - current_mud
     - current mud weight value (Integer or Float)
   * - new_mud
     - new mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - mud_vol
     - current mud volume value (Integer or Float)
   * - vol_units
     - volume units (String)

This function calculates the volume of Hematite required to increase the mud weight using Hematite. The function takes in three value inputs(Integers or Floats) and two units inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of volume units that can be input into the function see the Volume units section under General Conversions. The function returns a dictionary with two sub-dictionaries that each contains 3 sub dictionaries:

   * - "per_100_bbl_mud" which is a dictionary of different volume units and values representing the volume required, the weight required, and volume increase per 100 barrels. The three subdictionaries are 'weight_required'; to see the range of weight units returned see the example code below or the Weight units section under General Conversions, 'volume_required'; to see the range of volume units returned see the example code below or the Additive Volume units section under Fluids Conversions, 'volume_increase'; to see the range of volume units returned see the example code below or the Volume units section under General Conversions.
   * - "water_added_total" which is a dictionary of different volume units and values representing the volume required, the weight required, and volume increase for the total volume of mud. The three subdictionaries are 'weight_required'; to see the range of weight units returned see the example code below or the Weight units section under General Conversions, 'volume_required'; to see the range of volume units returned see the example code below or the Additive Volume units section under Fluids Conversions, 'volume_increase'; to see the range of volume units returned see the example code below or the Volume units section under General Conversions.


.. code:: python

   # Example Code
   from ogPypeline import drilling_fluid_formulas as dff

   hematite_increase = dff.hematite_increase(10, 13, 'ppg', 500, 'bbl')
   print(hematite_increase)
   # outputs the following dictionary:
   {
       'water_added_per_100': 
          {
              'weight_required': 
              {
                  'ct': 42335287.86666667,
                  'cg': 846705757.3333333,
                  'dg': 84670575.73333333,
                  'dram': 4778666.6536,
                  'gr': 130666686.83226664,
                  'g': 8467057.573333332,
                  'kg': 8467.058133333332,
                  'kip': 18.666666666666664,
                  't_long': 8.332799999999999,
                  't_metric': 8.4672,
                  'mg': 8467057573.333332,
                  'oz': 298666.6666666666,
                  'lb': 18666.666666666664,
                  'slug': 580.1786666666666,
                  't_short': 9.333333333333332,
                  'toz': 272222.22159999993,
                  'KdaN': 7.5327964489953425,
                  'daN': 7532.796408786285
              },
              'volume_required': 
              {
                  'sack': 186.66666666666666,
                  'ft3': 696.8953703703787,
                  'm3': 19.733879293452798,
                  'bbl': 165.49648869648905
              },
              'volume_increase': 
              {
                  'bbl': 11.11111111111111,
                  'bucket': 93.33333333333333,
                  'bu_us': 50.12974222222222,
                  'cm3': 1766525.4992055553,
                  'ft3': 62.38425888888888,
                  'in3': 107800.0,
                  'm3': 1.7665255555555555,
                  'mm3': 1766525499.2059777,
                  'yd3': 2.3105277777777777,
                  'C': 7466.666666666666,
                  'dr': 477866.6666666666,
                  'drum': 8.484848888888889,
                  'fl_oz': 59733.33333333333,
                  'gal_us': 466.66666666666663,
                  'gill': 14933.333333333332,
                  'gal_uk': 388.58128666666664,
                  'kL': 1.7665255555555555,
                  'L': 1766.5254988888887,
                  'ml': 1766525.4992055553,
                  'Pt': 3733.333333333333,
                  'qt_dr': 1604.1517366666665,
                  'qt_lq': 1866.6666666666665,
                  'tbsp': 119466.66666666666,
                  'tsp': 358400.0,
                  'toe': 1.5151511111111111
              }
          },
       'water_added_total': 
          {
              'weight_required': 
              {
                  'weight_required': {'ct': 211676439.33333334,
                  'cg': 4233528786.6666665,
                  'dg': 423352878.6666667,
                  'dram': 23893333.268,
                  'gr': 653333434.1613332,
                  'g': 42335287.86666667,
                  'kg': 42335.29066666667,
                  'kip': 93.33333333333333,
                  't_long': 41.664,
                  't_metric': 42.336,
                  'mg': 42335287866.666664,
                  'oz': 1493333.3333333333,
                  'lb': 93333.33333333333,
                  'slug': 2900.8933333333334,
                  't_short': 46.666666666666664,
                  'toz': 1361111.108,
                  'KdaN': 37.663982244976715,
                  'daN': 37663.98204393143
              },
              'volume_required': 
              {
                  'sack': 933.3333333333333,
                  'ft3': 3484.476851851893,
                  'm3': 98.66939646726398,
                  'bbl': 827.4824434824453
              },
              'volume_increase': 
              {
                  'bbl': 55.55555555555556,
                  'bucket': 466.6666666666667,
                  'bu_us': 250.6487111111111,
                  'cm3': 8832627.496027777,
                  'ft3': 311.9212944444444,
                  'in3': 539000.0,
                  'm3': 8.832627777777779,
                  'mm3': 8832627496.029888,
                  'yd3': 11.55263888888889,
                  'C': 37333.333333333336,
                  'dr': 2389333.3333333335,
                  'drum': 42.42424444444445,
                  'fl_oz': 298666.6666666667,
                  'gal_us': 2333.3333333333335,
                  'gill': 74666.66666666667,
                  'gal_uk': 1942.9064333333333,
                  'kL': 8.832627777777779,
                  'L': 8832.627494444445,
                  'ml': 8832627.496027777,
                  'Pt': 18666.666666666668,
                  'qt_dr': 8020.7586833333335,
                  'qt_lq': 9333.333333333334,
                  'tbsp': 597333.3333333334,
                  'tsp': 1792000.0,
                  'toe': 7.575755555555556
              }
      } 

Starting Mud Volume to Achieve A Required Mud Weight and Volume Using Hematite Function
------------

*barite_starting_vol(current_mud, new_mud, mud_units, mud_vol, vol_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - current_mud
     - current mud weight value (Integer or Float)
   * - new_mud
     - new mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - mud_vol
     - required mud volume value (Integer or Float)
   * - vol_units
     - volume units (String)

This function calculates the volume of hematite required to increase the mud weight using hematite. The function takes in three value inputs(Integers or Floats) and two units inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of volume units that can be input into the function see the Volume units section under General Conversions. The function returns a dictionary of different volume units and values, to see the range of volume units returned see the example code below or the Volume units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_fluid_formulas as dff

   hematite_starting_vol = dir_for.hematite_starting_vol(10, 13, 'ppg', 100, 'bbl')
   print(hematite_starting_vol)
   # outputs the following dictionary:
   {
       'bbl': 90.0,
       'bucket': 756.0,
       'bu_us': 406.050912,
       'cm3': 14308856.543565,
       'ft3': 505.31249699999995,
       'in3': 873180.0,
       'm3': 14.308857,
       'mm3': 14308856543.56842,
       'yd3': 18.715275000000002,
       'C': 60480.0,
       'dr': 3870720.0,
       'drum': 68.727276,
       'fl_oz': 483840.0,
       'gal_us': 3780.0,
       'gill': 120960.0,
       'gal_uk': 3147.508422,
       'kL': 14.308857,
       'L': 14308.856541,
       'ml': 14308856.543565,
       'Pt': 30240.0,
       'qt_dr': 12993.629067,
       'qt_lq': 15120.0,
       'tbsp': 967680.0,
       'tsp': 2903040.0,
       'toe': 12.272724
   }
   # Each key representing a different unit
   print(hematite_starting_vol['bbl'])
   # outputs the following float:
   90.0 

Increase Oil-Water Ratio Function
------------

*increase_oil_water_ratio(oil_vol, water_vol, mud_value, mud_units, new_oil, new_water)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - oil_vol
     - oil percentage value (Integer or Float)
   * - water_vol
     - water percentage value (Integer or Float)
   * - mud_value
     - mud volume value (Integer or Float)
   * - mud_units
     - volume units (String)
   * - new_oil
     - new oil percentage value (Integer or Float)
   * - new_water
     - new water percentage value (Integer or Float)

This function calculates the volume of liquid to add to increase the oil water ratio. The function takes in five value inputs(Integers or Floats) and one units input(Strings). To see the range of volume units that can be input into the function see the Volume units section under General Conversions. The function returns a dictionary with two sub-dictionaries:

   * - "oil_added_per_100" which is a dictionary of different volume units and values representing the volume of oil added per 100 barrels, to see the range of volume units returned see the example code below or the Volume units section under General Conversions.
   * - "oil_added_total" which is a dictionary of different volume units and values representing the total volume of oil added, to see the range of volume units returned see the example code below or the Volume units section under General Conversions.


.. code:: python

   # Example Code
   from ogPypeline import drilling_fluid_formulas as dff

   oil_added = dff.increase_oil_water_ratio(56, 14, 300, 'bbl', 70, 30)
   print(oil_added)
   # outputs the following dictionary:
   {
       'oil_added_per_100': 
          {
              'bbl': 17.0,
              'bucket': 142.8,
              'bu_us': 76.6985056,
              'cm3': 2702784.0137845,
              'ft3': 95.44791609999999,
              'in3': 164934.0,
              'm3': 2.7027841,
              'mm3': 2702784013.7851458,
              'yd3': 3.5351075,
              'C': 11424.0,
              'dr': 731136.0,
              'drum': 12.9818188,
              'fl_oz': 91392.0,
              'gal_us': 714.0,
              'gill': 22848.0,
              'gal_uk': 594.5293686,
              'kL': 2.7027841,
              'L': 2702.7840133,
              'ml': 2702784.0137845,
              'Pt': 5712.0,
              'qt_dr': 2454.3521571,
              'qt_lq': 2856.0,
              'tbsp': 182784.0,
              'tsp': 548352.0,
              'toe': 2.3181812
          },
       'oil_added_total':
          {
              'bbl': 51.0,
              'bucket': 428.40000000000003,
              'bu_us': 230.0955168,
              'cm3': 8108352.0413534995,
              'ft3': 286.34374829999996,
              'in3': 494802.0,
              'm3': 8.1083523,
              'mm3': 8108352041.355437,
              'yd3': 10.6053225,
              'C': 34272.0,
              'dr': 2193408.0,
              'drum': 38.9454564,
              'fl_oz': 274176.0,
              'gal_us': 2142.0,
              'gill': 68544.0,
              'gal_uk': 1783.5881057999998,
              'kL': 8.1083523,
              'L': 8108.3520399,
              'ml': 8108352.0413534995,
              'Pt': 17136.0,
              'qt_dr': 7363.056471299999,
              'qt_lq': 8568.0,
              'tbsp': 548352.0,
              'tsp': 1645056.0,
              'toe': 6.9545436
          }
      } 

Mixing Fluids with Different Densities - Limited Space Function
------------

*fluid_mixing_limited_space(mud_one_value, mud_two_value, new_mud_value, mud_units, mud_vol, vol_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - mud_one_value
     - fluid one weight value (Integer or Float)
   * - mud_two_value
     - fluid two weight value (Integer or Float)
   * - new_mud_value
     - final fluid required weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - mud_vol
     - required volume of mud value (Integer or Float)
   * - vol_units
     - volume units (String)

This function calculates the volume of liquid to add to increase the oil water ratio. The function takes in four value inputs(Integers or Floats) and two units inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of volume units that can be input into the function see the Volume units section under General Conversions. The function returns a dictionary with two sub-dictionaries:

   * - "mud_one_volume" which is a dictionary of different volume units and values, to see the range of volume units returned see the example code below or the Volume units section under General Conversions.
   * - "mud_two_volume" which is a dictionary of different volume units and values representing the total volume added, to see the range of volume units returned see the example code below or the Volume units section under General Conversions.


.. code:: python

   # Example Code
   from ogPypeline import drilling_fluid_formulas as dff

   mixed_fluid = dff.fluid_mixing_limited_space(11, 14, 12, 'ppg', 300, 'bbl')
   print(mixed_fluid)
   # outputs the following dictionary:
   {
       'oil_added_per_100': 
          {
              'bbl': 200.0,
              'bucket': 1680.0,
              'bu_us': 902.33536,
              'cm3': 31797458.9857,
              'ft3': 1122.9166599999999,
              'in3': 1940400.0,
              'm3': 31.79746,
              'mm3': 31797458985.7076,
              'yd3': 41.5895,
              'C': 134400.0,
              'dr': 8601600.0,
              'drum': 152.72728,
              'fl_oz': 1075200.0,
              'gal_us': 8400.0,
              'gill': 268800.0,
              'gal_uk': 6994.463159999999,
              'kL': 31.79746,
              'L': 31797.45898,
              'ml': 31797458.9857,
              'Pt': 67200.0,
              'qt_dr': 28874.73126,
              'qt_lq': 33600.0,
              'tbsp': 2150400.0,
              'tsp': 6451200.0,
              'toe': 27.27272
          },
       'oil_added_total':
          {
              'bbl': 100.0,
              'bucket': 840.0,
              'bu_us': 451.16768,
              'cm3': 15898729.49285,
              'ft3': 561.4583299999999,
              'in3': 970200.0,
              'm3': 15.89873,
              'mm3': 15898729492.8538,
              'yd3': 20.79475,
              'C': 67200.0,
              'dr': 4300800.0,
              'drum': 76.36364,
              'fl_oz': 537600.0,
              'gal_us': 4200.0,
              'gill': 134400.0,
              'gal_uk': 3497.2315799999997,
              'kL': 15.89873,
              'L': 15898.72949,
              'ml': 15898729.49285,
              'Pt': 33600.0,
              'qt_dr': 14437.36563,
              'qt_lq': 16800.0,
              'tbsp': 1075200.0,
              'tsp': 3225600.0,
              'toe': 13.63636
          }
      } 

Mixing Fluids with Different Densities Function
------------

*fluid_mixing_unlimited_space(mud_one_value, mud_two_value, mud_units, mud_one_vol, mud_two_vol, vol_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - mud_one_value
     - fluid one weight value (Integer or Float)
   * - mud_two_value
     - fluid two weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)
   * - mud_one_vol
     - mud one volume value (Integer or Float)
   * - vol_units
   * - mud_two_vol
     - mud two volume value (Integer or Float)
   * - vol_units
     - volume units (String)

This function calculates the volume of liquid to add to increase the oil water ratio. The function takes in four value inputs(Integers or Floats) and two units inputs(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. To see the range of volume units that can be input into the function see the Volume units section under General Conversions. The function returns a dictionary with two sub-dictionaries:

   * - "total_mud_volume" which is a dictionary of different volume units and values, to see the range of volume units returned see the example code below or the Volume units section under General Conversions.
   * - "final_mud_weight" which is a dictionary of different mud weight units and values representing the new mud weight, to see the range of mud weight units returned see the example code below or the Mud Weight units section under Drilling Conversions.


.. code:: python

   # Example Code
   from ogPypeline import drilling_fluid_formulas as dff

   mixed_fluid = dff.fluid_mixing_unlimited_space(10, 14, 'ppg', 200, 300, 'bbl')
   print(mixed_fluid)
   # outputs the following dictionary:
   {
       'total_mud_volume': 
          {
              'bbl': 500,
              'bucket': 4200.0,
              'bu_us': 2255.8384,
              'cm3': 79493647.46425,
              'ft3': 2807.2916499999997,
              'in3': 4851000.0,
              'm3': 79.49365,
              'mm3': 79493647464.269,
              'yd3': 103.97375000000001,
              'C': 336000.0,
              'dr': 21504000.0,
              'drum': 381.8182,
              'fl_oz': 2688000.0,
              'gal_us': 21000.0,
              'gill': 672000.0,
              'gal_uk': 17486.1579,
              'kL': 79.49365,
              'L': 79493.64745,
              'ml': 79493647.46425,
              'Pt': 168000.0,
              'qt_dr': 72186.82815,
              'qt_lq': 84000.0,
              'tbsp': 5376000.0,
              'tsp': 16128000.0,
              'toe': 68.1818
          },
       'final_mud_weight':
          {
              'g/cm3': 1.48584736,
              'g/L': 1485.8473600000002,
              'kg/m3': 1485.8473600000002,
              'kg/L': 1.48584736,
              'kPa/m': 14.57827948,
              'lb/ft3': 92.76689488000001,
              'lb/bbl': 520.8000000000001,
              'ppg': 12.4,
              'psi/ft': 0.6448347200000001,
              'psi/100ft': 64.44514980000001,
              'SG': 1.48584736
          }
      } 

Plastic Viscosity and Yield Point Function
------------

*plastic_viscosity_yield_point(reading_600, reading_300)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - reading_600
     - 600 rpm sheer stress value (Integer or Float)
   * - reading_300
     - 300 rpm sheer stress value (Integer or Float)

This function calculates the plastic viscosity and yield point from the 600 and 300 shear stress values. The function takes in two value inputs(Integers or Floats). The function returns a dictionary with two sub-dictionaries:

   * - "plastic_viscosity" which is a dictionary of different viscosity units and values, to see the range of viscosity units returned see the example code below or the Viscosity units section under Fluid Conversions.
   * - "yield_point" which is a dictionary of different yield point units and values, to see the range of yield point units returned see the example code below or the Fluid Yield Point units section under Fluid Conversions.


.. code:: python

   # Example Code
   from ogPypeline import drilling_fluid_formulas as dff

   viscosity_yield = dff.plastic_viscosity_yield_point(56, 35)
   print(viscosity_yield)
   # outputs the following dictionary:
   {
       'plastic_viscosity': 
          {
              'cp': 21,
              'g/(cm.s)': 0.21,
              'kg/(m.hr)': 75.60000000000001,
              'kg/(m.s)': 0.021,
              'kg-f.s/m2': 0.002142,
              'kPa-s': 2.1e-05,
              'N.s/m2': 0.021,
              'Pa-s': 0.021,
              'dyne-s/cm2': 0.21,
              'p': 0.21,
              'lbf-s/ft2': 0.0004389,
              'lbf-s/in2': 3.0457917e-06,
              'lb/(ft.hr)': 50.8008543,
              'lb/(ft.s)': 0.014112,
              'poundal.s/ft2': 0.014112,
              'reyn': 3.0457917e-06
          },
       'yield_point':
          {
              'dyne/cm2': 67.0600854,
              'kPa': 6.7032378,
              'Mpa': 0.0067031999999999994,
              'lbf/100ft2': 14
          }
      } 

Mud Weight Reduction Function
------------

*mud_weight_reduction(mud_vol, vol_units, mud_one_value, mud_two_value, mud_final_value, mud_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - mud_vol
     - current mud volume value (Integer or Float)
   * - vol_units
     - current mud volume units (String)
   * - mud_one_value
     - mud one mud weight value (Integer or Float)
   * - mud_two_value
     - added fluid mud weight value (Integer or Float)
   * - mud_final_value
     - required mud weight value (Integer or Float)
   * - mud_units
     - mud weight units (String)

This function calculates the required volume of fluid required to reduce the mud weight. The function takes in four value inputs(Integers or Floats) and two units inputs(Strings). To see the range of volume units that can be input into the function see the Volume units section under General Conversions. To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. The function returns a dictionary of different volume units and values, to see the range of volume units returned see the example code below or the Volume units section under General Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_fluid_formulas as dff

   mud_weight = dir_for.mud_weight_reduction(200, 'bbl', 13.8, 7.2, 10, 'ppg')
   print(mud_weight)
   # outputs the following dictionary:
   {
       'bbl': 271.4285714285715,
       'bucket': 2280.000000000001,
       'bu_us': 1224.597988571429,
       'cm3': 43153694.33773573,
       'ft3': 1523.9583242857145,
       'in3': 2633400.000000001,
       'm3': 43.153695714285725,
       'mm3': 43153694337.74604,
       'yd3': 56.44289285714287,
       'C': 182400.00000000006,
       'dr': 11673600.000000004,
       'drum': 207.2727371428572,
       'fl_oz': 1459200.0000000005,
       'gal_us': 11400.000000000004,
       'gill': 364800.0000000001,
       'gal_uk': 9492.48571714286,
       'kL': 43.153695714285725,
       'L': 43153.69433000001,
       'ml': 43153694.33773573,
       'Pt': 91200.00000000003,
       'qt_dr': 39187.13528142858,
       'qt_lq': 45600.000000000015,
       'tbsp': 2918400.000000001,
       'tsp': 8755200.000000002,
       'toe': 37.01297714285715
   }
   # Each key representing a different unit
   print(mud_weight['bbl'])
   # outputs the following float:
   271.4285714285715 

Solids Density from Retort Data Function
------------

*solids_density_retort(mud_density, water_density, oil_density, density_units, water_volume, oil_volume, solids_volume)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - mud_density
     - mud weight value (Integer or Float)
   * - water_density
     - water weight value (Integer or Float)
   * - oil_density
     - oil weight value (Integer or Float)
   * - density_units
     - mud volume units (String)
   * - water_volume
     - water volume percentage value (Integer or Float)
   * - oil_volume
     - oil volume percentage value (Integer or Float)
   * - solids_volume
     - solids volume percentage value (Integer or Float)

This function calculates the required volume of fluid required to reduce the mud weight. The function takes in six value inputs(Integers or Floats) and one units input(Strings). To see the range of mud weight units that can be input into the function see the Mud Weight units section under Drilling Conversions. The function returns a dictionary of different mud weight units and values, to see the range of mud weight units returned see the example code below or the Mud Weight units section under Drilling Conversions.

.. code:: python

   # Example Code
   from ogPypeline import drilling_fluid_formulas as dff

   solids_density = dir_for.solids_density_retort(12, 8.6, 7, 'ppg', 5, 60, 35)
   print(solids_density)
   # outputs the following dictionary:
   {
       'g/cm3': 2.523201622857143,
       'g/L': 2523.201622857143,
       'kg/m3': 2523.201622857143,
       'kg/L': 2.523201622857143,
       'kPa/m': 24.75620271142857,
       'lb/ft3': 157.53272241142858,
       'lb/bbl': 884.4,
       'ppg': 21.057142857142857,
       'psi/ft': 1.0950303885714285,
       'psi/100ft': 109.43796175714286,
       'SG': 2.523201622857143
   }
   # Each key representing a different unit
   print(solids_density['ppg'])
   # outputs the following float:
   21.057142857142857 

Squeeze Below and Balance Cement Plug Function
------------

*squeeze_below_balance_above(casing_value, od_value, id_value, diameter_units, depth_value, depth_units, volume_beneath, volume_above, line_volume, volume_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - casing_value
     - casing id value (Integer or Float)
   * - od_value
     - drill pipe od value (Integer or Float)
   * - id_value
     - drill pipe id value (Integer or Float)
   * - diameter_units
     - diameter units (String)
   * - depth_value
     - Retainer Depth value (Integer or Float)
   * - depth_units
     - depth units (String)
   * - volume_beneath
     - volume of squeeze under retainer value (Integer or Float)
   * - volume_above
     - volume of depth on top of retainer value (Integer or Float)
   * - line_volume
     - line volume value (Integer or Float)
   * - volume_units
     - volume units (String)

This function calculates the required data and steps for performing a cement squeeze below a retainer and balancing a cement plug above the retainer. The function takes in seven value inputs(Integers or Floats) and three units inputs(Strings). To see the range of diameter and depth units that can be input into the function see the Length units section under General Conversions. To see the range of volume units that can be input into the function see the Volume units section under General Conversions. The function returns a dictionary with two sub-dictionaries one has four sub dictionaries and the other has four and a tuple:

   * - "data" which is a dictionary of different units and values representing the volume required, the weight required, and volume increase per 100 barrels. The four subdictionaries are 'stringer_volume'; to see the range of volume units returned see the example code below or the Volume units section under General Conversions, 'toc_with_stinger'; to see the range of depth units returned see the example code below or the Length units section under General Conversions, 'toc_without_stinger'; to see the range of depth units returned see the example code below or the Length units section under General Conversions, 'displace_balance'; to see the range of volume units returned see the example code below or the Volume units section under General Conversions.
   * - "pumping_steps" which is a dictionary of different units and values representing the steps to be followed during the process, plus any data related to the different volumes pumped at each stage. The tuple, 'steps', contains the process order while the four subdictionaries are 'step_one'; to see the range of volume units returned see the example code below or the Volume units section under General Conversions, 'step_two'; to see the range of volume units returned see the example code below or the Volume units section under General Conversions, 'step_three'; to see the range of volume units returned see the example code below or the Volume units section under General Conversions, 'step_four'; to see the range of volume units returned see the example code below or the Volume units section under General Conversions.


.. code:: python

   # Example Code
   from ogPypeline import drilling_fluid_formulas as dff

   squeeze_balance = dff.squeeze_below_balance_above(8.835, 4, 3.34, 'in', 1000, 'ft', 30, 12, 0.5, 'bbl')
   print(squeeze_balance)
   # outputs the following dictionary:
   {
       'data': 
          {
              'stringer_volume': 
              {
                  'bbl': 10.836992422770546,
                  'bucket': 91.0307363512726,
                  'bu_us': 48.89300729558966,
                  'cm3': 1722944.1104569405,
                  'ft3': 60.845196679114046,
                  'in3': 105140.50048571984,
                  'm3': 1.7229441654167477,
                  'mm3': 1722944110.4573524,
                  'yd3': 2.253525481834078,
                  'C': 7282.458908101807,
                  'dr': 466077.3701185156,
                  'drum': 8.275521880551779,
                  'fl_oz': 58259.67126481445,
                  'gal_us': 455.1536817563629,
                  'gill': 14564.917816203613,
                  'gal_uk': 378.9947213313386,
                  'kL': 1.7229441654167477,
                  'L': 1722.9441101480863,
                  'ml': 1722944.1104569405,
                  'Pt': 3641.2294540509033,
                  'qt_dr': 1564.576219370779,
                  'qt_lq': 1820.6147270254517,
                  'tbsp': 116519.3425296289,
                  'tsp': 349558.02758888673,
                  'toe': 1.4777712999417136
              },
              'toc_with_stinger': 
              {
                  'cm': 25337.27611248439,
                  'dm': 2533.727611248439,
                  'dam': 25.33727611248439,
                  'fath': 138.54593821051844,
                  'ft': 831.275463008018,
                  'hm': 2.533727611248439,
                  'in': 9975.305556096217,
                  'km': 0.25337276112484386,
                  'league': 0.05245348171580594,
                  'm': 253.37276112484392,
                  'mi': 0.15744357269371861,
                  'mm': 253372.7611248439,
                  'nleague': 0.045637022919140194,
                  'nm': 0.13682794121111977,
                  'yd': 277.0917932934906
              },
              'toc_without_stinger': 
              {
                  'cm': 25656.444666076713,
                  'dm': 2565.6444666076713,
                  'dam': 25.656444666076716,
                  'fath': 140.2911734326643,
                  'ft': 841.7468722466114,
                  'hm': 2.5656444666076714,
                  'in': 10100.962466959336,
                  'km': 0.2565644466607671,
                  'league': 0.053114227638761176,
                  'm': 256.56444666076715,
                  'mi': 0.1594268576035082,
                  'mm': 256564.44666076716,
                  'nleague': 0.046211903286338965,
                  'nm': 0.13855153517179222,
                  'yd': 280.58226269064136
              },
              'displace_balance': 
              {
                  'bbl': 9.008525893852969,
                  'bucket': 75.67161750836495,
                  'bu_us': 40.6435572774957,
                  'cm3': 1432241.163157031,
                  'ft3': 50.57911904124445,
                  'in3': 87400.71822216151,
                  'm3': 1.4322412088437702,
                  'mm3': 1432241163.1573734,
                  'yd3': 1.8733004383119904,
                  'C': 6053.7294006691955,
                  'dr': 387438.6816428285,
                  'drum': 6.879238282888664,
                  'fl_oz': 48429.835205353564,
                  'gal_us': 378.3580875418247,
                  'gill': 12107.458801338391,
                  'gal_uk': 315.04901245230326,
                  'kL': 1.4322412088437702,
                  'L': 1432.2411629002881,
                  'ml': 1432241.163157031,
                  'Pt': 3026.8647003345977,
                  'qt_dr': 1300.5938211687787,
                  'qt_lq': 1513.4323501672989,
                  'tbsp': 96859.67041070713,
                  'tsp': 290579.0112321214,
                  'toe': 1.2284350215790087
              }
          },
       'pumping_steps': 
          {
              'steps': ('Step One: Pump Cement', 'Step Two: Sting Out', 'Step Three: Pump Cement', 'Step Four: Displace to Balance Plug'),
              'step_one': 
              {
                  'bbl': 40.83699242277055,
                  'bucket': 343.03073635127265,
                  'bu_us': 184.24331129558968,
                  'cm3': 6492562.958311941,
                  'ft3': 229.28269567911406,
                  'in3': 396200.5004857199,
                  'm3': 6.492563165416748,
                  'mm3': 6492562958.313493,
                  'yd3': 8.49195048183408,
                  'C': 27442.45890810181,
                  'dr': 1756317.3701185158,
                  'drum': 31.18461388055178,
                  'fl_oz': 219539.67126481447,
                  'gal_us': 1715.153681756363,
                  'gill': 54884.91781620362,
                  'gal_uk': 1428.1641953313388,
                  'kL': 6.492563165416748,
                  'L': 6492.562957148087,
                  'ml': 6492562.958311941,
                  'Pt': 13721.229454050905,
                  'qt_dr': 5895.785908370779,
                  'qt_lq': 6860.614727025452,
                  'tbsp': 439079.34252962895,
                  'tsp': 1317238.027588887,
                  'toe': 5.5686792999417145
              },
              'step_two': Sting Out',
              'step_three': 
              {
                  'bbl': 1.163007577229454,
                  'bucket': 9.769263648727414,
                  'bu_us': 5.247114304410336,
                  'cm3': 184903.42868505942,
                  'ft3': 6.529802920885952,
                  'in3': 11283.499514280162,
                  'm3': 0.18490343458325237,
                  'mm3': 184903428.68510363,
                  'yd3': 0.24184451816592187,
                  'C': 781.541091898193,
                  'dr': 50018.629881484354,
                  'drum': 0.8881149194482222,
                  'fl_oz': 6252.328735185544,
                  'gal_us': 48.846318243637064,
                  'gill': 1563.082183796386,
                  'gal_uk': 40.673068268661346,
                  'kL': 0.18490343458325237,
                  'L': 184.9034286519137,
                  'ml': 184903.42868505942,
                  'Pt': 390.7705459490965,
                  'qt_dr': 167.9076562292209,
                  'qt_lq': 195.38527297454826,
                  'tbsp': 12504.657470371088,
                  'tsp': 37513.97241111327,
                  'toe': 0.15859190005828636
              },
              'step_four': 
              {
                  'bbl': 9.508525893852969,
                  'bucket': 79.87161750836495,
                  'bu_us': 42.899395677495704,
                  'cm3': 1511734.810621281,
                  'ft3': 53.38641069124445,
                  'in3': 92251.71822216151,
                  'm3': 1.5117348588437702,
                  'mm3': 1511734810.6216424,
                  'yd3': 1.9772741883119904,
                  'C': 6389.7294006691955,
                  'dr': 408942.6816428285,
                  'drum': 7.261056482888663,
                  'fl_oz': 51117.835205353564,
                  'gal_us': 399.3580875418247,
                  'gill': 12779.458801338391,
                  'gal_uk': 332.5351703523033,
                  'kL': 1.5117348588437702,
                  'L': 1511.734810350288,
                  'ml': 1511734.810621281,
                  'Pt': 3194.8647003345977,
                  'qt_dr': 1372.7806493187788,
                  'qt_lq': 1597.4323501672989,
                  'tbsp': 102235.67041070713,
                  'tsp': 306707.0112321214,
                  'toe': 1.2966168215790088
              }
      }

Balance Cement Plug Function
------------

*cement_plug_balance_above(casing_value, od_value, id_value, diameter_units, depth_value, depth_units, volume_above, line_volume, volume_units)*

.. list-table:: Function Inputs
   :widths: 30 70
   :header-rows: 1

   * - Input Name
     - Input Description
   * - casing_value
     - casing id value (Integer or Float)
   * - od_value
     - drill pipe od value (Integer or Float)
   * - id_value
     - drill pipe id value (Integer or Float)
   * - diameter_units
     - diameter units (String)
   * - depth_value
     - Retainer Depth value (Integer or Float)
   * - depth_units
     - depth units (String)
   * - line_volume
     - line volume value (Integer or Float)
   * - volume_units
     - volume units (String)

This function calculates the required data and steps for balancing a cement plug above the retainer. The function takes in six value inputs(Integers or Floats) and three units inputs(Strings). To see the range of diameter and depth units that can be input into the function see the Length units section under General Conversions. To see the range of volume units that can be input into the function see the Volume units section under General Conversions. The function returns a dictionary with two sub-dictionaries one has four sub dictionaries and the other has two and a tuple:

   * - "data" which is a dictionary of different units and values representing the volume required, the weight required, and volume increase per 100 barrels. The four subdictionaries are 'stringer_volume'; to see the range of volume units returned see the example code below or the Volume units section under General Conversions, 'toc_with_stinger'; to see the range of depth units returned see the example code below or the Length units section under General Conversions, 'toc_without_stinger'; to see the range of depth units returned see the example code below or the Length units section under General Conversions, 'displace_balance'; to see the range of volume units returned see the example code below or the Volume units section under General Conversions.
   * - "pumping_steps" which is a dictionary of different units and values representing the steps to be followed during the process, plus any data related to the different volumes pumped at each stage. The tuple, 'steps', contains the process order while the four subdictionaries are 'step_one'; to see the range of volume units returned see the example code below or the Volume units section under General Conversions, 'step_two'; to see the range of volume units returned see the example code below or the Volume units section under General Conversions.


.. code:: python

   # Example Code
   from ogPypeline import drilling_fluid_formulas as dff

   plug_balance = dff.cement_plug_balance_above(6.33, 4, 3.34, 'in', 7600, 'ft',10, 0.5, 'bbl')
   print(plug_balance)
   # outputs the following dictionary:
   {
       'data': 
          {
              'stringer_volume': 
              {
                  'bbl': 82.36114241305614,
                  'bucket': 691.8335962696716,
                  'bu_us': 371.5868554464814,
                  'cm3': 13094375.239472747,
                  'ft3': 462.4234947612667,
                  'in3': 799067.8036914706,
                  'm3': 13.09437565716728,
                  'mm3': 13094375239.475876,
                  'yd3': 17.126793661938994,
                  'C': 55346.68770157373,
                  'dr': 3542188.0129007185,
                  'drum': 62.893966292193504,
                  'fl_oz': 442773.5016125898,
                  'gal_us': 3459.167981348358,
                  'gill': 110693.37540314745,
                  'gal_uk': 2880.359882118173,
                  'kL': 13.09437565716728,
                  'L': 13094.375237125454,
                  'ml': 13094375.239472747,
                  'Pt': 27673.343850786863,
                  'qt_dr': 11890.77926721792,
                  'qt_lq': 13836.671925393432,
                  'tbsp': 885547.0032251796,
                  'tsp': 2656641.009675539,
                  'toe': 11.231061879557023
              },
              'toc_with_stinger': 
              {
                  'cm': 222740.53161861774,
                  'dm': 22274.053161861775,
                  'dam': 222.74053161861772,
                  'fath': 1217.9602808766626,
                  'ft': 7307.760223707931,
                  'hm': 22.274053161861772,
                  'in': 87693.12268449517,
                  'km': 2.2274053161861773,
                  'league': 0.46111967011597044,
                  'm': 2227.4053161861775,
                  'mi': 1.3840897863702821,
                  'mm': 2227405.3161861775,
                  'nleague': 0.4011960362815654,
                  'nm': 1.2028573328223253,
                  'yd': 2435.919830977303
              },
              'toc_without_stinger': 
              {
                  'cm': 223817.46010496918,
                  'dm': 22381.746010496918,
                  'dam': 223.81746010496917,
                  'fath': 1223.848998624569,
                  'ft': 7343.09252312891,
                  'hm': 22.38174601049692,
                  'in': 88117.11027754692,
                  'km': 2.2381746010496917,
                  'league': 0.46334913820943424,
                  'm': 2238.174601049692,
                  'mi': 1.3907817238806155,
                  'mm': 2238174.601049692,
                  'nleague': 0.4031357795197772,
                  'nm': 1.2086730293070185,
                  'yd': 2447.697262939886
              },
              'displace_balance': 
              {
                  'bbl': 79.19414217174683,
                  'bucket': 665.2307942426734,
                  'bu_us': 357.2983739321718,
                  'cm3': 12590862.438069073,
                  'ft3': 444.64210809531545,
                  'in3': 768341.5673502878,
                  'm3': 12.590862839702165,
                  'mm3': 12590862438.072083,
                  'yd3': 16.468223879259327,
                  'C': 53218.463539413875,
                  'dr': 3405981.666522488,
                  'drum': 60.475529629120935,
                  'fl_oz': 425747.708315311,
                  'gal_us': 3326.153971213367,
                  'gill': 106436.92707882775,
                  'gal_uk': 2769.602549540428,
                  'kL': 12.590862839702165,
                  'L': 12590.86243581204,
                  'ml': 12590862.438069073,
                  'Pt': 26609.231769706937,
                  'qt_dr': 11433.547862877112,
                  'qt_lq': 13304.615884853469,
                  'tbsp': 851495.416630622,
                  'tsp': 2554486.249891866,
                  'toe': 10.799198325451217
              }
          },
       'pumping_steps': 
          {
              'steps': ('Step One: Pump Cement', 'Step Two: Displace'),
              'step_one': 
              {
                  'bbl': 10,
                  'bucket': 84.0,
                  'bu_us': 45.116768,
                  'cm3': 1589872.9492849999,
                  'ft3': 56.145832999999996,
                  'in3': 97020.0,
                  'm3': 1.5898729999999999,
                  'mm3': 1589872949.28538,
                  'yd3': 2.079475,
                  'C': 6720.0,
                  'dr': 430080.0,
                  'drum': 7.636364,
                  'fl_oz': 53760.0,
                  'gal_us': 420.0,
                  'gill': 13440.0,
                  'gal_uk': 349.72315799999996,
                  'kL': 1.5898729999999999,
                  'L': 1589.872949,
                  'ml': 1589872.9492849999,
                  'Pt': 3360.0,
                  'qt_dr': 1443.736563,
                  'qt_lq': 1680.0,
                  'tbsp': 107520.0,
                  'tsp': 322560.0,
                  'toe': 1.363636
              },
              'step_two': 
              {
                  'bbl': 79.69414217174683,
                  'bucket': 669.4307942426734,
                  'bu_us': 359.5542123321718,
                  'cm3': 12670356.085533323,
                  'ft3': 447.4493997453155,
                  'in3': 773192.5673502878,
                  'm3': 12.670356489702165,
                  'mm3': 12670356085.53635,
                  'yd3': 16.572197629259325,
                  'C': 53554.463539413875,
                  'dr': 3427485.666522488,
                  'drum': 60.85734782912093,
                  'fl_oz': 428435.708315311,
                  'gal_us': 3347.153971213367,
                  'gill': 107108.92707882775,
                  'gal_uk': 2787.0887074404277,
                  'kL': 12.670356489702165,
                  'L': 12670.35608326204,
                  'ml': 12670356.085533323,
                  'Pt': 26777.231769706937,
                  'qt_dr': 11505.734691027112,
                  'qt_lq': 13388.615884853469,
                  'tbsp': 856871.416630622,
                  'tsp': 2570614.249891866,
                  'toe': 10.867380125451216
              }
      }
