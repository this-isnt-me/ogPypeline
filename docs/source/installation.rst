Conversion Modules
==================


Usage
------------
The functions in the conversion modules all work in the same manner. A value (integer or float) and units (string) are passed into the function and a dictionary is returned using the different units as the key. See example of temperature conversion in the code below:

.. code-block:: console

   (.venv) $ pip install ogPypeline
   import general as gen

   converted_temps  = gen.temperature(37, 'c')
   print(converted_temps)
   # outputs the following dictionary:
   {
	   'c' : 37,
	   'f' : 98.6,
	   'k' : 310.15
   }
   # Each key representing a different temperature unit: 
   # c - Celcius, 
   # f - Fahrenheit, 
   # and k - Kelvin 
   print(converted_temps['k'])
   # outputs the following float:
   310.15
   
Drilling Conversions
------------

Dogleg units
^^^^^^^^^^^^
The _dogleg(value, units)_ function converts degrees per 100ft into degrees per 30m and vice versa. The input units are as per the table below:
+-------------------------------+-------------------------------+
|Unit Full Length Description   |Function String Inputs         |
+===============================+===============================+
|degrees per 100ft              |'deg/100ft'                    |
+-------------------------------+-------------------------------+
|degrees per 30m                |'deg/30m'                      |
+-------------------------------+-------------------------------+

