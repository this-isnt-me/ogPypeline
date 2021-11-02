Gas Conversions
==================

List Legend
------------

   #. "Unit Description" : 'Function Input String'
   
Example Code
------------

.. code-block:: python

   from ogPypeline import gas as gas

   converted_gas_injection_rate  = gas.gas_injection_rate(5506, 'm3/min')
   print(converted_gas_injection_rate)
   # outputs the following dictionary:
   {
	   'm3/min': 5506,
       'scfm': 194558.303634
   }
   # Each key representing a different gas injection rate unit
   print(converted_gas_injection_rate['scfm'])
   # outputs the following float:
   194558.303634

Gas Injection Rate units
------------
The gas_injection_rate(value, units) function converts between different Gas Injection Rate units. The input units are as per the list below:

   #. Cubic Meter per Minute : 'm3/min'
   #. Standard Cubic Feet per Minute : 'scfm'

Gas Production Index units
------------
The gas_production_index(value, units) function converts between different Gas Production Index units. The input units are as per the list below:

   #. Cubic Meter per Day - MegaPascal : 'm3/d-MPa'
   #. Cubic Meter per Day - KiloPascal : 'm3/d-kPa'
   #. Cubic Meter per Hour - KiloPascal : 'm3/hr-kPa'
   #. Million Standard Cubic Feet per Day per Pounds per Square Inch : 'MMSCFD/psi'
   #. Thousand Standard Cubic Feet per Hour per Pounds per Square Inch : 'MSCF/hr-psi'
   #. Thousand Standard Cubic Feet per Day per Pounds per Square Inch : 'MSCFD/psi'
   #. Standard Cubic Feet per Hour per Pounds per Square Inch : 'SCF/hr-psi'
   #. Standard Cubic Feet per Day per Pounds per Square Inch : 'SCFD/psi'

Gas Production Rate units
------------
The gas_production_rate(value, units) function converts between different Gas Production Rate units. The input units are as per the list below:

   #. Cubic Meters per Minute : 'm3/min'
   #. Million Barrels : 'MM'
   #. Mega Standard Cubic Metres per Day : 'MMM3/d'
   #. Standard Cubic Feet per Minute : 'scfm'

Gas Volume units
------------
The gas_volume(value, units) function converts between different Gas Volume units. The input units are as per the list below:

   #. Barrels of Oil Equivalent : 'BOE'
   #. Cubic Meters : 'm3'
   #. Million Standard Cubic Feet : 'MMscf'
   #. Standard Cubic Feet per Minute : 'MMsm3'
   #. Thousand Barrels of Oil Equivalent : 'KBOE'
   #. Thousand Cubic Meter : 'dam3'
   #. Thousand Standard Cubic Feet : 'Mscf'
   #. Ton Liquefied Natural Gas : 'ton_LNG'

LNG Volume units
------------
The lng_volume(value, units) function converts between different LNG Volume units. The input units are as per the list below:

   #. Barrels of Oil Equivalent : 'BOE'
   #. Million Barrels of Oil Equivalent : 'MMBOE'
   #. Million Cubic Feet : 'MMCF'
   #. Thousand Barrels of Oil Equivalent : 'KBOE'
   #. Ton Liquefied Natural Gas : 'ton_LNG'

Specific Volume units
------------
The specific_volume(value, units) function converts between different Specific Volume units. The input units are as per the list below:

   #. Barrels per Ton (U.K.) : 'bbl/UK ton'
   #. Barrels per Ton (U.S.) : 'bbl/US ton'
   #. Cubic Foot per Pound : 'ft3/lb'
   #. Cubic Inch per Pound : 'in3/lb'
   #. Cubic Meter per Kilogram : 'm3/kg'
   #. Gallons (U.K.) per Pound : 'UK gal/lb'
   #. Gallons (U.S.) per Pound : 'US gal/lb'
   #. Liters per Gram : 'l/g'
   #. Liters per Kilogram : 'l/kg'

Volume units
------------
The volume_gas(value, units) function converts between different Volume units. The input units are as per the list below:

   #. Barrels : 'bbl'
   #. Cubic Centimeter : 'cm3'
   #. Cubic Decimeter : 'dm3'
   #. Cubic Foot : 'ft3'
   #. Cubic Inch : 'in3'
   #. Cubic Meter : 'm3'
   #. Cubic Yard : 'yd3'
   #. Fluid Ounce : 'fl_oz'
   #. Gallon : 'gal'
   #. Liter : 'L'
   #. Quart - Liquid : 'qt'
