Force and Power Conversions
==================
   
Example Code
------------

.. code:: python

   # Example Code
   from ogPypeline import force_and_power as fap

   converted_angular_velocity  = fap.angular_velocity(85, 'rpm')
   print(converted_angular_velocity)
   # outputs the following dictionary:
   {
       'deg/hr': 1836000.0, 
       'deg/min': 30600.0, 
       'deg/sec': 510.0, 
       'rad/hr': 32044.245693, 
       'rad/min': 534.070759, 
       'rad/sec': 8.901183,
       'rph': 5100.0,
       'rpm': 85, 
       'rps': 1.4166695
   }
   # Each key representing a different angular velocity unit
   print(converted_angular_velocity['deg/min'])
   # outputs the following float:
   30600.0

Electric Current units
------------
The electric_current(value, units) function converts between different Electric Current units. The input units are as per the table below:

.. list-table:: Electric Current units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Ampere
     - 'amp'
   * - Abampere / BIOT
     - 'biot'
   * - Centiampere
     - 'camp'
   * - Kiloampere
     - 'kamp'
   * - Milliampere
     - 'mamp'
   * - Gilbert
     - 'gilbert'
   * - Volt/Ohm
     - 'v/ohm'
   * - Watt/volt
     - 'w/v'

Fracture Conductivity units
------------
The fracture_conductivity(value, units) function converts between different Fracture Conductivity units. The input units are as per the table below:

.. list-table:: Fracture Conductivity units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Darcy Inch
     - 'darcy-in'
   * - mu.m2-m
     - 'mu.m2-m'

Heat Capacity units
------------
The heat_capacity(value, units) function converts between different Heat Capacity units. The input units are as per the table below:

.. list-table:: Heat Capacity units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - British Thermal Units per Pound - Degree Fahrenheit
     - 'Btu/lb-F'
   * - Joule per Kilogram Celsius
     - 'J/kg-C'

Power/Area units
------------
The power_area(value, units) function converts between different Power/Area units. The input units are as per the table below:

.. list-table:: Power/Area units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Horsepower per Square Inch
     - 'HP/in2'
   * - Kilowatt per Square Millimeter
     - 'kW/mm2'

Angular Velocity units
------------
The angular_velocity(value, units) function converts between different Angular Velocity units. The input units are as per the table below:

.. list-table:: Angular Velocity units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Degrees per hour
     - 'deg/hr'
   * - Degrees per Minute
     - 'deg/min'
   * - Degrees per Second
     - 'deg/sec'
   * - Radians per hour
     - 'rad/hr'
   * - Radians per Minute
     - 'rad/min'
   * - Radians per Second
     - 'rad/sec'
   * - Revolutions per hour
     - 'rph'
   * - Revolutions per Minute
     - 'rpm'
   * - Revolutions per Second
     - 'rps'

Force units
------------
The force(value, units) function converts between different Force units. The input units are as per the table below:

.. list-table:: Force units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - DekaNewtons
     - 'daN'
   * - Dynes
     - 'dyn'
   * - Gram-force
     - 'gf'
   * - Kilogram-force
     - 'kgf'
   * - KiloNewtons
     - 'kN'
   * - KIPS
     - 'kip'
   * - KiloPounds-force
     - 'klbs'
   * - MegaNewton
     - 'MN'
   * - Newton
     - 'N'
   * - Ounce-force
     - 'ozf'
   * - Pound-force
     - 'lbf'
   * - Poundal
     - 'pdl'
   * - Sthene
     - 'sn'
   * - Ton-force(metric)
     - 'tf-metric'
   * - Ton-force(long)
     - 'tf-long'
   * - Ton-force(short)
     - 'tf-short'
   * - Hectonewton
     - 'hN'
   * - Joules per Meter
     - 'J/m'
   * - MillieNewton
     - 'mN'

Power units
------------
The power(value, units) function converts between different Power units. The input units are as per the table below:

.. list-table:: Power units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - British Thermal Units per Second
     - 'BTU/sec'
   * - British Thermal Units per Minute
     - 'BTU/min'
   * - Calories per Minute
     - 'cal/min'
   * - Calories per Second
     - 'cal/sec'
   * - Foot Pound-force per Minute
     - 'ft-lb/min'
   * - Foot Pound-force per Second
     - 'ft-lb/sec'
   * - Horsepower
     - 'hp'
   * - Electric Horsepower
     - 'hp-elec'
   * - Metric Horsepower
     - 'hp-met'
   * - Joules per Second
     - 'J/s'
   * - Kilocalories per Minute
     - 'kcal/min'
   * - Kilocalories per Second
     - 'kcal/s'
   * - Kilogram Force Meter per Minute
     - 'kg-m/min'
   * - Kilogram Force Meter per Second
     - 'kg-m/sec'
   * - Kilowatt
     - 'kW'
   * - Megawatt
     - 'MW'
   * - Newton Meter per Second
     - 'N-m/s'
   * - Ton of Refrigeration
     - 'ton-ref'
   * - Volt Ampere
     - 'var'
   * - Watt
     - 'W'

Velocity units
------------
The velocity(value, units) function converts between different Velocity units. The input units are as per the table below:

.. list-table:: Velocity units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Feet per Day
     - 'ft/d'
   * - Feet per Hour
     - 'ft/hr'
   * - Feet per Minute
     - 'ft/min'
   * - Feet per Second
     - 'ft/s'
   * - Kilometers per Hour
     - 'kph'
   * - Kilometers per Minute
     - 'k/min'
   * - Kilometers per Second
     - 'k/sec'
   * - Nautical Miles per Hour
     - 'knot'
   * - Mach
     - 'mach'
   * - Meters per Day
     - 'm/d'
   * - Meters per Hour
     - 'm/hour'
   * - Meters per Minute
     - 'm/min'
   * - Meters per Second
     - 'm/sec'
   * - Miles per Hour
     - 'mph'
   * - Miles per Minute
     - 'mi/min'
   * - Miles per Second
     - 'mi/sec'

Electrical Resistivity units
------------
The resistivity(value, units) function converts between different Electrical Resistivity units. The input units are as per the table below:

.. list-table:: Electrical Resistivity units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Ohm-Meter
     - 'ohm.m'
   * - Ohm-Centimeter
     - 'ohm.cm'
   * - Ohm-Inch
     - 'ohm.in'
   * - Microhm-Centimeter
     - 'm-ohm.cm'
   * - Microhm-Inch
     - 'm-ohm.in'
   * - Abohm-Centimeter
     - 'ab-ohm.cm'
   * - Statohm-Centimeter
     - 'stat-ohm.cm'
   * - Circular Mil-Ohm per Foot
     - 'circular_mil-ohm/ft'
   * - Ohm-Square Millimeter per Meter
     - 'ohm.mm2/m'

Electrical Conductivity units
------------
The conductivity(value, units) function converts between different Electrical Conductivity units. The input units are as per the table below:

.. list-table:: Electrical Conductivity units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Siemens per Meter
     - 'S/m'
   * - Picosiemens per Meter
     - 'pS/m'
   * - Mho per Meter
     - 'mho/m'
   * - Mho per Centimeter
     - 'mho/cm'
   * - Abmho per Meter
     - 'abmho/m'
   * - Abmho per Centimeter
     - 'abmho/cm'
   * - Statohm Meter
     - 'stmho/m'
   * - Statohm Centimeter
     - 'stmho/cm'
   * - Siemens per Centimeter
     - 'S/cm'
   * - Millisiemens per Meter
     - 'mS/m'
   * - Millisiemens per Centimeter
     - 'mS/cm'
   * - Microsiemens per Meter
     - 'uS/m'
   * - Microsiemens per Centimeter
     - 'uS/cm'
