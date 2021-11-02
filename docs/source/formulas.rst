Formula Modules
==================

These modules contain over 100 commonly used formulas for the oil and gas industry. 

Usage
------------
Each of the formula functions is tailored specifically to the formula it is calculating, however, there are underlying principles. The formula functions take in value inputs (integers or floats) and unit inputs (strings). These inputs are then converted to the appropriate input for the specific formula, i.e. converting to the appropriate pressure units. Upon completion of the calculation, a dictionary is returned using the different units as the key. See example code below:

.. code-block:: console

   from ogPypeline import basic_formulas as bas_for
   
   # This function takes in the pressure and depth to calculate the necessary mud weight. 
   # To see the range of pressure units that can be input into the function see the Pressure units section under General Conversions.
   # To see the range of depth units that can be input into the function the Length units section under General Conversions. 
   mud_weight  = bas_for.pressure_to_mud_weight(5000,'psi', 8000,'ft')
   print(mud_weight)
   # outputs the following dictionary:
   {
       'g/cm3': 1.440221153846154,
       'g/L': 1440.221153846154,
       'kg/m3': 1440.221153846154,
       'kg/L': 1.440221153846154,
       'kPa/m': 14.13062139423077,
       'lb/ft3': 89.91828365384616,
       'lb/bbl': 504.8076923076923,
       'ppg': 12.01923076923077,
       'psi/ft': 0.625033653846154,
       'psi/100ft': 62.46621995192309,
       'SG': 1.440221153846154
   }
   # Each key representing a different mud weight unit
   print(mud_weight['ppg'])
   # outputs the following float:
   12.01923076923077
