Production Conversions
==================

List Legend
------------

   #. "Unit Description" : 'Function Input String'
   
Example Code
------------

.. code-block:: console

   from ogPypeline import production as pro

   converted_permeability  = pro.permeability(100000, 'md')
   print(converted_permeability)
   # outputs the following dictionary:
   {
	   'darcy': 100.0,
       'md': 100000,
       'ud': 100000000,
       'm2': 9.869e-11,
       'ft2': 1.06235016146393e-09
   }
   # Each key representing a different permeability unit
   print(converted_permeability['darcy'])
   # outputs the following float:
   100.0

Nozzle Size units
------------
The nozzle_size(value, units) function converts between different Nozzle Size units. The input units are as per the list below

   #. Millimetres: 'mm'
   #. Eighth of an Inch : '1/8in'
   #. Sixteenth of an Inch : '1/16in'
   #. Thirty Seconds of an Inch : '1/32in'
   #. Sixty Fourths of an Inch : '1/64in'

Nozzle Speed units
------------
The nozzle_speed(value, units) function converts between different Nozzle Speed units. The input units are as per the list below

   #. Feet per Second : 'ft/s'
   #. Meters per Second : 'm/s'

Oil Production Index units
------------
The oil_production_index(value, units) function converts between different Oil Production Index units. The input units are as per the list below

   #. Barrels per Day - Pounds Per Square Inch : 'bbl/d-psi'
   #. Barrels per Hour - Pounds Per Square Inch : 'bbl/hr-psi'
   #. Barrels per Minute - Pounds Per Square Inch : 'bbl/min-psi'
   #. Cubic Feet per Day - Pounds Per Square Inch : 'ft3/d-psi'
   #. Cubic Meter per Day - KiloPascal : 'm3/d-kPa'
   #. Cubic Meter per Day - MegaPascal : 'm3/d-MPa'
   #. Cubic Meter per Hour - KiloPascal : 'm3/hr-kPa'
   #. Gallons per Day - Pounds Per Square Inch : 'gal/d-psi'
   #. Litres per Hour - KiloPascal : 'l/hr-kPa'

Permeability units
------------
The permeability(value, units) function converts between different Permeability units. The input units are as per the list below

   #. Darcy : 'darcy'
   #. MilliDarcy : 'md'
   #. MicroDarcy : 'ud'
   #. Square Metres : 'm2'
   #. Square Feet : 'ft2'

Pipe Capacity (Volume per Length) units
------------
The pipe_capacity(value, units) function converts between different Pipe Capacity units in volume per length. The input units are as per the list below

   #. Barrels per Foot : 'bbl/ft'
   #. Cubic Meters per Meter : 'm3/m'
   #. Barrels per Inch : 'bbl/in'
   #. Cubic Feet per Foot : 'ft3/ft'
   #. US Gallons per Foot : 'gal(us)/ft'
   #. Litres per Meter : 'l/m'
   #. Cubic Decimeter per Meter : 'dm3/m'
   #. Square Feet : 'in3/ft'

Pipe Capacity (Length per Volume) units
------------
The pipe_cap_length_vol(value, units) function converts between different Pipe Capacity units in length per volume. The input units are as per the list below

   #. Meters per Cubic Meter : 'm/m3'
   #. Feet per Barrel : 'ft/bbl'
   #. Feet per Cubic Foot : 'ft/ft3'
   #. Feet per US Gallon : 'ft/gal(us)'

Production Rate units
------------
The production_rate(value, units) function converts between different Production Rate units. The input units are as per the list below

   #. Cubic Meter per Day : 'm3/d'
   #. Stock Tank Barrel per Day : 'stb/d'

Rotation units
------------
The rotation(value, units) function converts between different Rotation units. The input units are as per the list below

   #. Radian per Second : 'rad/sec'
   #. Rotations per Minute : 'rpm'

Section Modulus units
------------
The section_modulus(value, units) function converts between different Section Modulus units. The input units are as per the list below

   #. Cubic Centimeter : 'cm3'
   #. Cubic Inch : 'in3'

Section Modulus - Moment of Section units
------------
The moment_of_section(value, units) function converts between different Section Modulus - Moment of Section units. The input units are as per the list below

   #. Centimetre to the Power of 4 : 'cm4'
   #. Foot to the Power of 4 : 'ft4'
   #. Inch to the Power of 4 : 'in4'
   #. Meter to the Power of 4 : 'm4'

Stress Elastic Modulus units
------------
The stress_elastic_modulus(value, units) function converts between different Stress Elastic Modulus units. The input units are as per the list below

   #. Kilogram per Square Centimeter : 'kg/cm2'
   #. KiloPascal	: 'kPa'
   #. MegaPascal : 'Mpa'
   #. Pascal : 'Pa'
   #. Pounds per Square Inch : 'psi'

Stroke Rate units
------------
The stroke_rate(value, units) function converts between different Stroke Rate units. The input units are as per the list below

   #. Strokes per Hour : 'stk/hr'
   #. Strokes per Minute : 'stk/min'

Stroke Volume units
------------
The stroke_volume(value, units) function converts between different Stroke Volume units. The input units are as per the list below

   #. Barrels per Stroke : 'bbl/stk'
   #. Cubic Meters per Stroke : 'm3/stk'
   #. US Gallons per Stroke : 'gal/stk'
   #. Litres per Stroke : 'L/stk'
