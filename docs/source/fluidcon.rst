Fluid Conversions
==================
   
Example Code
------------

.. code:: python

   # Example Code
   from ogPypeline import fluid as flu

   converted_fluid_yield_point  = flu.fluid_yield_point(2.1, 'deg/100ft')
   print(converted_fluid_yield_point)
   # outputs the following dictionary:
   {
       'dyne/cm2': 67.0600854,
       'kPa': 6.7032378,
       'Mpa': 0.0067031999999999994, 
       'lbf/100ft2': 14
   }
   # Each key representing a different fluid yield point unit
   print(converted_fluid_yield_point['dyne/cm2'])
   # outputs the following float:
   67.0600854

Fluid Consistency units
------------
The fluid_consistency(value, units) function converts between different Fluid Consistency units. The input units are as per the table below:

.. list-table:: Fluid Consistency units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - dyne-s^n/cm2
     - 'dyne-s^n/cm2'
   * - eq.cp
     - 'eq.cp'
   * - lbf-s^n/100ft2
     - 'lbf-s^n/100ft2'
   * - lbf-s^n/ft2
     - 'lbf-s^n/ft2'
   * - Pa-s^n
     - 'Pa-s^n'

Fluid Yield Point units
------------
The fluid_yield_point(value, units) function converts between different Fluid Yield Point units. The input units are as per the table below:

.. list-table:: Fluid Yield Point units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Dyne per Square Centimeter
     - 'dyne/cm2'
   * - KiloPascal
     - 'kPa'
   * - MegaPascal
     - 'Mpa'
   * - Pound Force per Hundred Square Feet
     - 'lbf/100ft2'

Liquid Production Rate units
------------
The liquid_production_rates(value, units) function converts between different Liquid Production Rate units. The input units are as per the table below:

.. list-table:: Liquid Production Rate units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Barrels per Day
     - 'BPD'
   * - Barrels per Hour
     - 'BPH'
   * - Barrels per Minute
     - 'BPM'
   * - Barrels per Second
     - 'BPS'
   * - Cubic Feet per Day
     - 'ft3/day'
   * - Cubic Feet per Hour
     - 'ft3/hr'
   * - Cubic Feet per Minute
     - 'ft3/min'
   * - Cubic Feet per Second	: 'ft3/sec'
   * - Cubic Feet per Day
     - 'm3/day'
   * - Cubic Meter per Hour
     - 'm3/hr'
   * - Cubic Meter per Minute
     - 'm3/min'
   * - Cubic Meter per Second
     - 'm3/sec'
   * - US Gallons per Day
     - 'gal/day'
   * - US Gallons per Hour
     - 'gph'
   * - US Gallons per Minute
     - 'gpm'
   * - US Gallons per Second Feet
     - 'gal/sec'
   * - UK Gallons per Day
     - 'UK gal/day'
   * - UK Gallons per Hour
     - 'UK gph'
   * - UK Gallons per Minute
     - 'UK gpm'
   * - UK Gallons per Second
     - 'UK gal/sec'

Viscosity units
------------
The viscosity(value, units) function converts between different Viscosity units. The input units are as per the table below:

.. list-table:: Viscosity units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Centipoise
     - 'cp'
   * - Gram per Centimeter Second
     - 'g/(cm.s)'
   * - Kilogram per Meter Hour
     - 'kg/(m.hr)'
   * - Kilogram per Meter Second
     - 'kg/(m.s)'
   * - Kilogram-force Second per Square Meter
     - 'kg-f.s/m2'
   * - KiloPascal Second
     - 'kPa-s'
   * - Newton Second per Square Meter
     - 'N.s/m2'
   * - Pascal Second
     - 'Pa-s'
   * - Poise
     - 'p'
   * - Dyne Second per Square Centimeter
     - 'dyne-s/cm2'
   * - Pound Force-Second per Square Foot
     - 'lbf-s/ft2'
   * - Pound Force-Second per Square Inch
     - 'lbf-s/in2'
   * - Pound per Foot Hour
     - 'lb/(ft.hr)'
   * - Pound per Foot Second
     - 'lb/(ft.s)'
   * - Poundal Second per Square Foot
     - 'poundal.s/ft2'
   * - Reyn
     - 'reyn'

Oil Volume units
------------
The oil_volume(value, units) function converts between different Oil Volume units. The input units are as per the table below:

.. list-table:: Oil Volume units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Barrel
     - 'bbl'
   * - Barrel of Oil Equivalent
     - 'BOE'
   * - US Gallons
     - 'gal'
   * - Kiloliters
     - 'kL'
   * - Millions of Barrels of Oil Equivalent
     - 'MMBOE'
   * - Thousands  of Barrels of Oil Equivalent
     - 'KBOE'
   * - Tonnes of Oil Equivalent
     - 'toe'
