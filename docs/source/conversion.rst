Conversion Modules
==================

Usage
------------
The functions in the conversion modules all work in the same manner. A value (integer or float) and units (string) are passed into the function and a dictionary is returned using the different units as the key. See example of temperature conversion in the code below:

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
    # Each key representing a different temperature unit: 
    # c - Celcius, 
    # f - Fahrenheit, 
    # and k - Kelvin 
    print(converted_temps['k'])
    # outputs the following float:
    310.15