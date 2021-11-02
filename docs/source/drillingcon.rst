Drilling Conversions
==================
   
Example Code
------------

.. code:: python
    :linenos:
    
    # Example Code
    from ogPypeline import drilling as dri
    
    converted_dogleg  = dri.dogleg(2.1, 'deg/100ft')
    print(converted_dogleg)
    # outputs the following dictionary:
    {
	   'deg/100ft' : 2.1,
	   'deg/30m' : 2.06703084
    }
    # Each key representing a different dogleg severity unit
    print(converted_dogleg['deg/30m'])
    # outputs the following float:
    2.06703084

Dogleg units
------------
The dogleg(value, units) function converts degrees per 100ft into degrees per 30m and vice versa. The input units are as per the list below:

.. list-table:: Dogleg units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - degrees per 100ft
     - 'deg/100ft'
   * - degrees per 30m
     - 'deg/30m'

Axial Spring Constant units
------------
The axial_spring_con(value, units) function converts Newtons per Meter into Pounds per Inch and vice versa. The input units are as per the list below:


.. list-table:: Axial Spring Constant units
   :widths: 60 40
   :header-rows: 1

   * - Unit Description
     - Function Input String
   * - Newtons per Meter
     - 'N/m'
   * - Pounds per Inch
     - 'lb/in'


Axial Dampening Coefficient units
------------
The axial_dampening_coef(value, units) function converts Newton Seconds per Meter into Pound Seconds per Inch and vice versa. The input units are as per the list below:

.. list-table:: Axial Dampening Coefficient units
   :widths: 60 40
   :header-rows: 1

   * - Newton Seconds per Meter
     - 'N-s/m'
   * - Pound Seconds per Inch
     - 'lb-s/in'

Torsional Spring Constant units
------------
The torsional_spring_con(value, units) function converts Newton Meter per Radian into Pound Inch per Radian and vice versa. The input units are as per the list below:

.. list-table:: Torsional Spring Constant units
   :widths: 60 40
   :header-rows: 1

   * - Newton Meter per Radian
     - 'N-m/rad'
   * - Pound Inch per Radian
     - 'lb-in/rad'

Torsional Dampening Coefficient units
------------
The torsional_dampening_coef(value, units) function converts Newton Meter Second per Radian into Pound Inch Second per Radian and vice versa. The input units are as per the list below:

.. list-table:: Torsional Dampening Coefficient units
   :widths: 60 40
   :header-rows: 1

   * - Newton Meter Second per Radian
     - 'N-m-s/rad'
   * - Pound Inch Second per Radian
     - 'lb-in-s/rad'

Pressure Gradient units
------------
The pressure_grad(value, units) function converts between different pressure gradient units. The input units are as per the list below:

.. list-table:: Pressure Gradient units
   :widths: 60 40
   :header-rows: 1

   * - pound per square inch per foot
     - 'psi/ft'
   * - KiloPascal per Meter
     - 'kPa/m'
   * - MegaPascal per Meter
     - 'MPa/m'
   * - Pascal per Meter
     - 'Pa/m'

Yield Slurry units
------------
The yield_slurry(value, units) function converts between different Yield Slurry units for cementing. The input units are as per the list below:

.. list-table:: Yield Slurry units
   :widths: 60 40
   :header-rows: 1

   * - Cubic Feet per Sack
     - 'ft3/sk'
   * - Cubic Meter per Sack
     - 'm3/sk'
   * - Gallons per Sack
     - 'gal/sk'
   * - Cubic Meter per Kilogram
     - 'm3/kg'

Footage Cost units
------------
The footage_cost(value, units) function converts between different Footage Cost units for drilling, the currency is declared as a universal place holder using "cur". The input units are as per the list below:

.. list-table:: Footage Cost units
   :widths: 60 40
   :header-rows: 1

   * - Currency per Foot
     - 'cur/ft'
   * - Currency per Meter
     - 'cur/m'
   * - Currency per thousand Feet
     - 'cur/1000ft'
   * - Currency per thousand Meters
     - 'cur/1000m'

Mud Weight units
------------
The mud_weight(value, units) function converts between different Mud Weight units for drilling fluid. The input units are as per the list below:

.. list-table:: Mud Weight units
   :widths: 60 40
   :header-rows: 1

   * - Grams per Cubic Centimeter
     - 'g/cm3'
   * - Grams per Litre
     - 'g/L'
   * - Kilograms per Cubic Meter
     - 'kg/m3'
   * - Kilograms per Litre
     - 'kg/L'
   * - KiloPascals Per Meter
     - 'kPa/m'
   * - Pounds Per Cubic Feet
     - 'lb/ft3'
   * - Pounds Per Barrel
     - 'lb/bbl'
   * - Pounds Per Gallon
     - 'ppg'
   * - Pounds Per Square Inch Per Foot
     - 'psi/ft'
   * - Pounds Per Square Inch Per Hundred Feet
     - 'psi/100ft'
   * - Specific Gravity
     - 'SG'

Flow Rate units
------------
The flow_rate(value, units) function converts between different Flow Rate units for the circulation of drilling fluid. The input units are as per the list below:

.. list-table:: Flow Rate units
   :widths: 60 40
   :header-rows: 1

   * - Barrels per Hour
     - 'bbl/hr'
   * - Barrels per Minute
     - 'bbl/min'
   * - Cubic Feet per Minute
     - 'ft3/min'
   * - Cubic Meters per Hour
     - 'm3/hr'
   * - Cubic Meters per Minute
     - 'm3/min'
   * - Gallons per Hour
     - 'gal/hr'
   * - Gallons per Minute
     - 'gpm'
   * - Litres per Hour
     - 'L/hr'
   * - Litres per Minute
     - 'L/min'

Drilling Rate units
------------
The drilling_rate(value, units) function converts between different Drilling Rate units for the Rate of Penetration(ROP). The input units are as per the list below:

.. list-table:: Drilling Rate units
   :widths: 60 40
   :header-rows: 1

   * - Feet Per Day
     - 'ft/d'
   * - Feet Per Hour
     - 'ft/hr'
   * - Feet Per Minute
     - 'ft/min'
   * - Feet Per Second
     - 'ft/s'
   * - Meters Per Day
     - 'm/d'
   * - Meters Per Hour
     - 'm/hr'
   * - Meters Per Minute
     - 'm/min'
   * - Meters Per Second
     - 'm/s'

Weight Length units
------------
The weight_length(value, units) function converts between different Weight by Length units. The input units are as per the list below:

.. list-table:: Weight Length units
   :widths: 60 40
   :header-rows: 1

   * - Pounds per Foot
     - 'lb/ft'
   * - Kilograms per Meter
     - 'kg/m'

Geothermal Gradient units
------------
The geothermal_gradient(value, units) function converts between different Geothermal Gradient units. The input units are as per the list below:

.. list-table:: Geothermal Gradient units
   :widths: 60 40
   :header-rows: 1

   * - Degrees Centigrade per 100 Meters
     - 'c/100m'
   * - Degrees Fahrenheit per 100 Feet 
     - 'f/100ft'
