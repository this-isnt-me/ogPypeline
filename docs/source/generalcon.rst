General Conversions
==================
   
Example Code
------------

.. code:: python

   # Example Code
   from ogPypeline import general as gen

   converted_temps  = gen.temperature(37, 'c')
   print(converted_temps)
   # outputs the following dictionary:
   {
	   'c' : 37,
	   'f' : 98.6,
	   'k' : 310.15
   }
   # Each key representing a different temperature unit
   print(converted_temps['k'])
   # outputs the following float:
   310.15

Acceleration units
------------

The acceleration(value, units) function converts between different Acceleration units. The input units are as per the table below:

.. list-table:: Acceleration units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - G-unit
     - 'g'
   * - Centimeter per Square Minute
     - 'cm/min2'
   * - Centimeter per Square Second
     - 'cm/s2'
   * - Feet per Square Minute
     - 'ft/min2'
   * - Galileo
     - 'Gal'
   * - Inch per Square Hour
     - 'in/h2'
   * - Inch per Square Minute
     - 'in/min2'
   * - Inch per Square Second
     - 'in/s2'
   * - Kilometer per Square Hour
     - 'km/hr2'
   * - Kilometer per Square Minute
     - 'km/min2'
   * - Kilometer per Square Second
     - 'km/s2'
   * - Meter per Square Day
     - 'm/d2'
   * - Meter per Square Hour
     - 'm/hr2'
   * - Meter per Square Minute
     - 'm/min2'
   * - Meter per Square Second
     - 'm/s2'
   * - Miles per Square Hour
     - 'mi/hr2'
   * - Miles per Square Minute
     - 'mi/min2'
   * - Miles per Square Second
     - 'mi/s2'
   * - Knot per Second
     - 'knot/s'
   * - Millimeter per Square Second
     - 'mm/s2'

Angle units
------------

The angle(value, units) function converts between different Angle units. The input units are as per the table below:

.. list-table:: Angle units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Degrees
     - 'deg'
   * - Gradian
     - 'gon'
   * - Angular Mils
     - 'mil'
   * - Milliradian
     - 'mrad'
   * - Minutes
     - 'min'
   * - Quadrants
     - 'quad'
   * - Radians
     - 'rad'
   * - Revolutions
     - 'r'
   * - Seconds
     - 'sec'

Area units
------------

The area(value, units) function converts between different Area units. The input units are as per the table below:

.. list-table:: Area units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Acre
     - 'acre'
   * - Hectare
     - 'ha'
   * - Square Centimeters
     - 'cm2'
   * - Square Decimeter
     - 'dm2'
   * - Square Feet
     - 'ft2'
   * - Square Inch
     - 'in2'
   * - Square Kilometer
     - 'km2'
   * - Square Meter
     - 'm2'
   * - Square Mile
     - 'mi2'
   * - Square Millimeter
     - 'mm2'
   * - Square Yard
     - 'yd2'

Density units
------------

The density(value, units) function converts between different Density units. The input units are as per the table below:

.. list-table:: Density units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Gram per Cubic Centimeter
     - 'g/cm3'
   * - Gram per Liter
     - 'g/L'
   * - Kilogram per Cubic Centimeter
     - 'kg/cm3'
   * - Kilogram per Cubic Meter
     - 'kg/m3'
   * - Kilogram per Liter
     - 'kg/L'
   * - Ounce per Cubic Foot
     - 'oz/ft3'
   * - Ounce per Cubic Inch
     - 'oz/in3'
   * - Pound per Cubic Foot
     - 'lb/ft3'
   * - Pound per Cubic Inch
     - 'lb/in3'
   * - Pound per US Gallon
     - 'ppg'
   * - Slug per Cubic Foot
     - 'slug/ft3'
   * - Slug per Cubic Inch
     - 'slug/in3'
   * - Specific Gravity
     - 'SG'

Distributed Force units
------------

The distributed_force(value, units) function converts between different Distributed Force units. The input units are as per the table below:

.. list-table:: Distributed Force units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Deka Newton per Meter
     - 'daN/m'
   * - Kilogram per Meter
     - 'kg/m'
   * - Kilonewton per Centimeter
     - 'kg/cm'
   * - Kilopound per Inch
     - 'klb/in'
   * - Newton per Meter
     - 'N/m'
   * - Poundforce per Feet
     - 'lbf/ft'

Frequency units
------------

The frequency(value, units) function converts between different Frequency units. The input units are as per the table below:

.. list-table:: Frequency units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Gigahertz
     - 'gHz'
   * - Hertz
     - 'Hz'
   * - Kilohertz
     - 'kHz'
   * - Megahertz
     - 'mHz'
   * - Radian per Hour
     - 'rad/hr'
   * - Radian per Minute
     - 'rad/min'
   * - Radian per Second   
     - 'rad/sec'
   * - Revolutions per Hour
     - 'rph'
   * - Revolutions per Minute
     - 'rpm'
   * - Revolutions per Second
     - 'rps'

Length units
------------
The length(value, units) function converts between different Length units. The input units are as per the table below:

.. list-table:: Length units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Centimeter
     - 'cm'
   * - Decimeter
     - 'dm'
   * - Dekameter
     - 'dam'
   * - Fathom 
     - 'fath'
   * - Feet
     - 'ft'
   * - Hectometer
     - 'hm'
   * - Inch
     - 'in'
   * - Kilometer
     - 'km'
   * - League
     - 'league'
   * - Meter
     - 'm'
   * - Miles
     - 'mi'
   * - Millimeter
     - 'mm'
   * - Nautical League
     - 'nleague'
   * - Nautical Mile
     - 'nm'
   * - Yard
     - 'yd'

Pressure units
------------

The pressure(value, units) function converts between different Pressure units. The input units are as per the table below:

.. list-table:: Pressure units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Atmosphere
     - 'atm'
   * - Bar
     - 'bar'
   * - Centimeter of Mercury
     - 'cm_Hg'
   * - Centimeter of Water
     - 'cm_h2o'
   * - Dyne per Square Centimeter
     - 'dyne/cm2'
   * - Foot of Air
     - 'ft_air'
   * - Foot of Mercury
     - 'ft_hg'
   * - Foot of Water
     - 'ft_h2o'
   * - Inch of Air
     - 'in_air'
   * - Inch of Mercury
     - 'in_hg'
   * - Inch of Water
     - 'in_h2o'
   * - Kilogram-force per Square Centimeter
     - 'kg/cm2'
   * - Kilogram-force per Square Meter
     - 'kg/m2'
   * - KiloPascal
     - 'kPa'
   * - MegaPascal
     - 'Mpa'
   * - Millibar
     - 'mbar'
   * - Meter of Water
     - 'm_h2o'
   * - Meter of Mercury
     - 'm_Hg'
   * - Newton per Square Centimeter
     - 'N/cm2'
   * - Newton per Square Meter
     - 'N/m2'
   * - Newton per Square Millimeter
     - 'N/mm2'
   * - Pascal
     - 'Pa'
   * - Pound-force per Square Foot
     - 'psf'
   * - Pound-force per Square Inch
     - 'psi'
   * - Torr
     - 'torr'

Time units
------------

The time(value, units) function converts between different Time units. The input units are as per the table below:

.. list-table:: Time units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Days
     - 'day'
   * - Decades
     - 'decade'
   * - Hours
     - 'hr'
   * - Minutes
     - 'minute'
   * - Seconds
     - 'sec'
   * - Years
     - 'year'

Torque units
------------

The torque(value, units) function converts between different Torque units. The input units are as per the table below:

.. list-table:: Torque units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Foot Ounce-force
     - 'ft-oz'
   * - Foot Pound-force
     - 'ft-lb'
   * - Inch Ounce-force
     - 'in-oz'
   * - Inch Pound-force
     - 'in-lb'
   * - Kilogram-force Centimeter
     - 'kg-cm'
   * - Kilogram-force Meter
     - 'kg-m'
   * - KiloNewton Meter
     - 'kN-m'
   * - Newton Centimeter
     - 'N-cm'
   * - Newton Meter
     - 'N-m'

Volume units
------------

The volume(value, units) function converts between different Volume units. The input units are as per the table below:

.. list-table:: Volume units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Barrel
     - 'bbl'
   * - Bucket
     - 'bucket'
   * - Bushel
     - 'bu_us'
   * - Cubic Centimeter
     - 'cm3'
   * - Cubic Foot
     - 'ft3'
   * - Cubic Inch
     - 'in3'
   * - Cubic Meter
     - 'm3'
   * - Cubic Millimeter
     - 'mm3'
   * - Cubic Yard
     - 'yd3'
   * - Cup
     - 'C'
   * - Dram
     - 'dr'
   * - Drum
     - 'drum'
   * - Fluid Ounce
     - 'fl_oz'
   * - US Gallon
     - 'gal_us'
   * - Gill
     - 'gill'
   * - UK Gallon
     - 'gal_uk'
   * - Kiloliter
     - 'kL'
   * - Liter
     - 'L'
   * - Milliliter
     - 'ml'
   * - Pint
     - 'pt'
   * - Quart - Dry
     - 'qt_dr'
   * - Quart - Liquid
     - 'qt_lq'
   * - Tablespoon
     - 'tbsp'
   * - Teaspoon
     - 'tsp'
   * - Tonne of Oil Equivalent
     - 'toe'

Weight units
------------

The weight(value, units) function converts between different Weight units. The input units are as per the table below:

.. list-table:: Weight units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Carat
     - 'ct'
   * - Centigram
     - 'cg'
   * - Decigram
     - 'dg'
   * - Dram
     - 'dram'
   * - Grain
     - 'gr'
   * - Gram
     - 'g'
   * - Kilogram
     - 'kg'
   * - KIP
     - 'kip'
   * - Ton - Long
     - 't_long'
   * - Ton - Metric
     - 't_metric'
   * - Ton - Short
     - 't_short'
   * - Milligram
     - 'mg'
   * - Ounce
     - 'oz'
   * - Pound
     - 'lb'
   * - Slug
     - 'slug'
   * - Troy Ounce
     - 'toz'
   * - Kilodekanewton
     - 'KdaN'
   * - Dekanewton
     - 'daN'

Flowrate Mass units
------------

The flowrate_mass(value, units) function converts between different Flowrate Mass units. The input units are as per the table below:

.. list-table:: Flowrate Mass units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Grams per Day
     - 'g/day'
   * - Kilograms per Day
     - 'kg/day'
   * - Pounds per Day
     - 'lb/day'
   * - Long Tons per Day
     - 'ton/day(l)'
   * - Metric Tons per Day
     - 'ton/day(m)'
   * - Short Tons per Day
     - 'ton/day(s)'
   * - Grams per Hour
     - 'g/hr'
   * - Kilograms per Hour
     - 'kg/hr'
   * - Pounds per Hour
     - 'lb/hr'
   * - Long Tons per Hour
     - 'ton/hr(l)'
   * - Metric Tons per Hour
     - 'ton/hr(m)'
   * - Short Tons per Hour
     - 'ton/hr(s)'
   * - Grams per Minute
     - 'g/min'
   * - Kilograms per Minute
     - 'kg/min'
   * - Pounds per Minute
     - 'lb/min'
   * - Long Tons per Minute
     - 'ton/min(l)'
   * - Metric Tons per Minute
     - 'ton/min(m)'
   * - Short Tons per Minute
     - 'ton/min(s)'
   * - Grams per Second
     - 'g/sec'
   * - Kilograms per Second
     - 'kg/sec'
   * - Pounds per Second
     - 'lb/sec'
   * - Long Tons per Second
     - 'ton/sec(l)'
   * - Metric Tons per Second
     - 'ton/sec(m)'
   * - Short Tons per Second
     - 'ton/sec(s)'

Flowrate Volume units
------------

The flowrate_vol(value, units) function converts between different Flowrate Volume units. The input units are as per the table below:

.. list-table:: Flowrate Volume units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Barrels per Day
     - 'BPD'
   * - Cubic Feet per Day
     - 'ft3/day'
   * - Cubic Meters per Day
     - 'm3/day'
   * - US Gallons per Day
     - 'gal/day'
   * - Barrels per Hour
     - 'BPH'
   * - Cubic Feet per Hour
     - 'ft3/hr'
   * - Cubic Meters per Hour
     - 'm3/hr'
   * - US Gallons per Hour
     - 'gph'
   * - Barrels per Minute
     - 'BPM'
   * - Cubic Feet per Minute
     - 'ft3/min'
   * - Cubic Meters per Minute
     - 'm3/min'
   * - US Gallons per Minute
     - 'gpm'
   * - Barrels per Second
     - 'BPS'
   * - Cubic Feet per Second
     - 'ft3/sec'
   * - Cubic Meters per Second
     - 'm3/sec'
   * - US Gallons per Second
     - 'gal/sec'

Volumetric Flow Rate units
------------

The volumetric_flow_rate(value, units) function converts between different Volumetric Flow Rate units. The input units are as per the table below:

.. list-table:: Volumetric Flow Rate units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Liters per Hour
     - 'L/hr'
   * - Liters per Minute
     - 'L/min'
   * - Liters per Second
     - 'L/sec'
   * - Milliliters per Hour
     - 'mL/hr'
   * - Milliliters per Minute
     - 'mL/min'
   * - Milliliters Feet per Second
     - 'mL/sec'
   * - Cubic Meters per Hour
     - 'm3/hr'
   * - Cubic Meters per Minute
     - 'm3/min'
   * - Cubic Meters per Second
     - 'm3/sec'
   * - Cubic Feet per Hour
     - 'ft3/hr'
   * - Cubic Feet per Minute
     - 'ft3/min'
   * - Cubic Feet per Second
     - 'ft3/sec'
   * - US Gallons per Hour
     - 'us_gal/hr'
   * - US Gallons per Minute
     - 'us_gal/min'
   * - US Gallons per Second
     - 'us_gal/sec'
   * - UK Gallons per Hour 
     - 'uk_gal/hr'
   * - UK Gallons per Minute
     - 'uk_gal/min'
   * - UK Gallons per Second
     - 'uk_gal/sec'
   * - Cubic Centimeters per Hour
     - 'cm3/hr'
   * - Cubic Centimeters per Minute
     - 'cm3/min'
   * - Cubic Centimeters per Second
     - 'cm3/sec'

Energy units
------------

The energy(value, units) function converts between different Energy Volume units. The input units are as per the table below:

.. list-table:: Energy units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Barrels of Oil Equivalent
     - 'boe'
   * - British Thermal Units
     - 'BTU'
   * - Calories
     - 'cal'
   * - Cubic Feet of Natural Gas
     - 'nat_gas_ft3'
   * - Foot Pounds
     - 'ft-lb'
   * - Foot Poundals
     - 'ft-pdl'
   * - GigaJoules
     - 'gJ'
   * - Horsepower Hours
     - 'HP-hr'
   * - Joules
     - 'J'
   * - Kilocalories
     - 'kcal'
   * - Kilogram-force Meters
     - 'kg-m'
   * - KiloJoules
     - 'kJ'
   * - Kilowatt Hours
     - 'kW-hr'
   * - Liter Atmospheres
     - 'L-atm'
   * - MegaJoules
     - 'mJ'
   * - Newton Meters
     - 'Nm'
   * - Therms
     - 'therm'
   * - Thermies
     - 'thermie'
   * - Ton of Explosive
     - 'ton-exp'
   * - Tonne of Coal Equivalent
     - 'toc'
   * - Tonne of Oil Equivalent
     - 'toe'
   * - Watthour
     - 'W-hr'

Temperature units
------------

The temperature(value, units) function converts between different Temperature units. The input units are as per the table below:

.. list-table:: Temperature units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Centigrade
     - 'c'
   * - Fahrenheit
     - 'f'
   * - Kelvin
     - 'k'
