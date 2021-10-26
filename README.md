# ogPypeline

A python package for the oil and gas industry. Initial release is focused on 64 useful unit conversions across multiple disciplines.
Developed by Tim Clarke (c) 2021

## Table of Contents
**[Installation](#installation)**
**[Conversion Modules](#conversion-modules)**
*[Drilling Conversions](#drilling-conversions)*
*[Production Conversions](#production-conversions)*
*[Force and Power Conversions](#force-and-power-conversions)*
*[Fluid Conversions](#fluid-conversions)*
*[Gas Conversions](#gas-conversions)*
*[General Conversions](#general-conversions)*
**[License](#license)**

## Installation

You can install ogPypeline from [PyPI](https://pypi.org/project/ogPypeline/):

    python -m pip install ogPypeline

## Conversion Modules

The functions in the conversion modules all work in the same manner. A value (integer or float) and units (string) are passed into the function and a dictionary is returned using the different units as the key. See example of temperature conversion in the code below:
```python
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
```


### Conversion Function Lookup Table
|Module   |Function| Units|
|--------------|--------------|--------------|
|Drilling 1.01|*[dogleg(value, units)](#dogleg-units)*|deg/100ft, deg/30m|
|Drilling 1.02|*[axial_spring_con(value, units)](#axial-spring-constant-units)*|N/m, lb/in|
|Drilling 1.03|*[axial_dampening_coef(value, units)](#axial-dampening-coefficient-units)*|N-sec/m, lb-s/in|
|Drilling 1.04|*[torsional_spring_con(value, units)](#torsional-spring-constant-units)*|N-m/rad, lb-in/rad|
|Drilling 1.05|*[torsional_dampening_coef((value, units)](#torsional-dampening-coefficient-units)*|N-m-s/rad, lb-in-s/rad|
|Drilling 1.06|*[pressure_grad(value, units)](#pressure-gradient-units)*|psi/ft, kPa/m, Mpa/m, Pa/m|
|Drilling 1.07|*[yield_slurry(value, units)](#yield-slurry-units)*|ft3/sk, m3/sk, gal/sk, m3/kg|
|Drilling 1.08|*[footage_cost(value, units)](#footage-cost-units)*|cur/ft, cur/m, cur/1000ft, cur/1000m|
|Drilling 1.09|*[mud_weight(value, units)](#mud-weight-units)*|g/cm3, g/L, kg/m3, kg/L, kPa/m, lb/ft3, lb/bbl, ppg, psi/ft, psi/100ft, SG|
|Drilling 1.10|*[flow_rate(value, units)](#flow-rate-units)*|bbl/hr, bbl/min, ft3/min, m3/hr, m3/min, gal/hr, gpm, L/hr, L/min|
|Drilling 1.11|*[drilling_rate(value, units)](#drilling-rate)*|ft/d, ft/hr, ft/min, ft/s, m/d, m/hr, m/min, m/s|
|Drilling 1.12|*[weight_length(value, units)](#weight-length-units)*|m/m3, ft/bbl, ft/ft3, ft/gal(us)|
|Drilling 1.13|*[geothermal_gradient(value, units)](#geothermal-gradient-units)*|c/100m, f/100ft|
|Production 2.01|*[nozzle_size(value, units)](#nozzle-size-units)*|mm, 1/8in, 16/in, 32/in, 64/in|
|Production 2.02|*[nozzle_speed(value, units)](#nozzle-speed-units)*|ft/s, m/s|
|Production 2.03|*[oil_production_index(value, units)](#oil-production-index-units)*|bbl/d-psi, bbl/hr-psi, bbl/min-psi, ft3/d-psi, m3/d-kPa, m3/d-MPa, m3/hr-kPa, gal/d-psi, l/hr-kPa|
|Production 2.04|*[permeability(value, units)](#permeability-units)*|darcy, md, ud, m2, ft2|
|Production 2.05|*[pipe_capacity(value, units)](#pipe-capacity-volume-per-length-units)*|bbl/ft, m3/m, bbl/in, ft3/ft, gal(us)/ft, l/m, dm3/m, in3/ft|
|Production 2.06|*[production_rate(value, units)](#production-rate-units)*|m3/d, stb/d|
|Production 2.07|*[rotation(value, units)](#rotation-units)*|rad/sec,rpm|
|Production 2.08|*[section_modulus(value, units)](#section-modulus-units)*|cm3,in3|
|Production 2.09|*[moment_of_section(value, units)](#section-modulus-moment-of-section-units)*|cm4,ft4,in4,m4|
|Production 2.10|*[stress_elastic_modulus(value, units)](#stress-elastic-modulus-units)*|kg/cm2,kPa,Mpa,Pa,psi|
|Production 2.11|*[stroke_rate(value, units)](#stroke-rate-units)*|stk/hr,stk/min|
|Production 2.12|*[stroke_volume(value, units)](#stroke-volume-units)*|bbl/stk,m3/stk,gal/stk,L/stk|
|Force and Power 3.01|*[electric_current(value, units)](#electric-current-units)*|amp, biot, camp, gilbert, kamp, mamp, v/ohm, w/v|
|Force and Power 3.02|*[fracture_conductivity(value, units)](#fracture-conductivity-units)*|darcy-in, mu.m2-m|
|Force and Power 3.03|*[heat_capacity(value, units)](#heat-capacity-units)*|Btu/lb-F, J/kg-C|
|Force and Power 3.04|*[power_area(value, units)](#power-area-units)*|HP/in2, kW/mm2|
|Force and Power 3.05|*[angular_velocity(value, units)](#angular-velocity-units)*|deg/hr, deg/min, deg/sec, rad/hr, rad/min, rad/sec, rph, rpm, rps|
|Force and Power 3.06|*[force(value, units)](#force-units)*|daN, dyn, gf, kgf, kN, kip, MN, N, ozf, lbf, pdl, sn, tf-metric, tf-long, tf-short, hN, J/m, mN|
|Force and Power 3.07|*[power(value, units)](#power-units)*|BTU/sec, BTU/min, cal/min, cal/sec, ft-lb/min, ft-lb/sec, hp, hp-elec, hp-met, J/s, kcal/min, kcal/s, kg-m/min, kg-m/sec, kW, MW, N-m/s, ton-ref, var, W|
|Force and Power 3.08|*[velocity(value, units)](#velocity-units)*|ft/d, ft/hr, ft/min, ft/s, kph, k/min, k/sec, knot, mach, m/d, m/hr, m/min, m/sec, mph, mi/min, mi/sec|
|Fluid 4.01|*[fluid_consistency(value, units)](#fluid-consistency-units)*|dyne-s^n/cm2, eq.cp, lbf-s^n/100ft2, lbf-s^n/ft2, Pa-s^n|
|Fluid 4.02|*[fluid_yield_point(value, units)](#fluid-yield-point-units)*|dyne/cm2, kPa, Mpa, lbf/100ft2|
|Fluid 4.03|*[liquid_production_rates(value, units)](#liquid-production-rates-units)*|BPD, BPH, BPM, BPS, ft3/day, ft3/hr, ft3/min, ft3/sec, m3/day, m3/hr, m3/min, gal/day, gph, gpm, gal/sec, UK gal/day, UK gph, UK gpm, UK gal/sec|
|Fluid 4.04|*[viscosity(value, units)](#viscosity-units)*|cp, g/(cm.s), kg/(m.hr), kg/(m.s), kg-f.s/m2, kPa-s, N.s/m2, Pa-s, dyne-s/cm2, lbf-s/ft2, lbf-s/in2, lb/(ft.hr), lb/(ft.s), poundal.s/ft2, reyn|
|Fluid 4.05|*[oil_volume(value, units)](#oil-volume-units)*|bbl, BOE, gal, kL, MMBOE, KBOE, toe|
|Gas 5.01|*[gas_injection_rate(value, units)](#gas-injection-rate-units)*|m3/min, scfm|
|Gas 5.02|*[gas_production_index(value, units)](#gas-production-index-units)*|m3/d-MPa, m3/d-kPa, m3/hr-kPa, MMSCFD/psi, MSCF/hr-psi, MSCFD/psi, SCF/hr-psi, SCFD/psi|
|Gas 5.03|*[gas_production_rate(value, units)](#gas-production-rate-units)*|m3/min, MM, MMM3/d, scfm|
|Gas 5.04|*[gas_volume(value, units)](#gas-volume-units)*|BOE, m3, MMscf, MMsm3, KBOE, dam3, Mscf, ton_LNG|
|Gas 5.05|*[lng_volume(value, units)](#lng-volume-units)*|BOE, MMBOE, MMCF, KBOE, ton_LNG|
|Gas 5.06|*[specific_volume(value, units)](#specific-volume-units)*|bbl/UK ton, bbl/US ton, ft3/lb, in3/lb, m3/kg, UK gal/lb, US gal/lb, l/g, l/kg|
|Gas 5.07|*[specific_volume(value, units)](#specific-volume-units)*|bbl, cm3, dm3, ft3, in3, m3, yd3, fl oz,  gal, L, qt|
|General 6.01|*[acceleration(value, units)](#acceleration-units)*|g, cm/min2, cm/s2, ft/min2, ft/s2, Gal, in/h2, in/min2, in/s2, km/hr2, km/min2, km/s2, m/d2, m/h2, m/min2, m/s2, mi/hr2, mi/min2, mi/s2, mm/s2, knot/s|
|General 6.02|*[angle(value, units)](#angle-units)*|deg, gon, mil, mrad, min, quad, rad, r, sec|
|General 6.03|*[area(value, units)](#area-units)*|acre, ha, cm2, dm2, ft2, in2, km2, m2, mi2, mm2, yd2|
|General 6.04|*[density(value, units)](#density-units)*|g/cm3,g/L,kg/cm3,kg/m3,kg/L,oz/ft3,oz/in3,lb/ft3,lb/in3,ppg,slug/ft3,slug/in3,SG|
|General 6.05|*[distributed_force(value, units)](#distributed-force-units)*|daN/m, kg/m, kN/cm, klb/in, N/m	lbf/ft|
|General 6.06|*[frequency(value, units)](#frequency-units)*|gHz,Hz,kHz,mHz,rad/hr,rad/min,rad/sec,rph,rpm, rps|
|General 6.07|*[length(value, units)](#gas-injection-rate-units)*|cm, dm, dam, fath, ft, hm, in, km, league, m, mi, mm, nleague, nm, yd|
|General 6.08|*[pressure(value, units)](#pressure-units)*|bar, cm_Hg, cm_h2o, dyne/cm2, ft_air, ft_hg, ft_h2o, in_air, in_hg, in_h2o, kg/cm2, kg/m2, kPa, Mpa, m_Hg, m_h2o, mbar, N/cm2, N/m2, N/mm2, Pa, psf, psi, torr|
|General 6.09|*[time(value, units)](#time-units)*|day, decade, hr, minute, sec, yr|
|General 6.10|*[torque(value, units)](#torque-units)*|ft-oz	ft-lb, in-oz, in-lb, kg-cm, kg-m, kN-m, N-cm, N-m|
|General 6.11|*[volume(value, units)](#volume-units)*|bbl, bucket, bu_us, cm3, ft3, in3, m3, mm3, yd3, C, dr, drum, fl oz, gal_us, gill, gal_uk, kL, L, ml, Pt, qt_dr, qt_lq, tbsp, tsp, toe|
|General 6.12|*[weight(value, units)](#weight-units)*|ct, cg, dg, dram, gr, g, kg, kip, t_long, t_metric, mg, oz, lb, slug, t_short, toz, KdaN, daN|
|General 6.13|*[flowrate_mass(value, units)](#flowrate-mass-units)*|g/day, kg/day, lb/day, ton/day(l), ton/day(m), ton/day(s), g/hr, kg/hr, lb/hr, ton/hr(l), ton/hr(m), ton/hr(s), g/min, kg/min, lb/min, ton/min(l), ton/min(m), ton/min(s), g/sec, kg/sec, lb/sec, ton/sec(l), ton/sec(m), ton/sec(s)|
|General 6.14|*[flowrate_vol(value, units)](#flowrate-volume-units)*|BPD, ft3/day, m3/day, gal/day, BPH, ft3/hr, m3/hr, gph, BPM, ft3/min, m3/min, gpm, BPS, ft3/sec, m3/sec, gal/sec|
|General 6.15|*[volumetric_flow_rate(value, units)](#volumetric-flow-rate-units)*|L/hour, L/min, L/sec, mL/hour, mL/min, mL/sec, m3/hour, m3/min, m3/sec, mm3/hour, mm3/min, mm3/sec, ft3/hour, ft3/min, ft3/sec, gal(us)/hour, gal(us)/min, gal(us)/sec, gal(I)/hour, gal(I)/min, gal(I)/sec, cm3/hour, cm3/min, cm3/sec|
|General 6.16|*[energy(value, units)](#energy-units)*|boe, BTU, cal, nat gas ft3, ft-lb, ft-pdl, gJ, HP-hr, J, kcal, kg-m, kJ, kW-hr, L-atm, mJ, Nm, therm, thermie, ton-exp, tce, toe, W-hr|
|General 6.17|*[temperature(value, units)](#temperature-units)*|c, f, k|
***

### Drilling Conversions

#### Dogleg units
The _dogleg(value, units)_ function converts degrees per 100ft into degrees per 30m and vice versa. The input units are as per the table below
|Unit Full Length Description        |Function String Inputs       |
|-------------------------------|-----------------------------|
|degrees per 100ft              |'deg/100ft'                  |
|degrees per 30m                |'deg/30m'                    |

***
#### Axial Spring Constant units
The _axial_spring_con(value, units)_ function converts Newtons per Meter into Pounds per Inch and vice versa. The input units are as per the table below
|Unit Full Length Description        |Function String Inputs       |
|-------------------------------|-----------------------------|
|Newtons per Meter              |'N/m'                        |
|Pounds per Inch                |'lb/in'                      |

***
#### Axial Dampening Coefficient units
The _axial_dampening_coef(value, units)_ function converts Newton Seconds per Meter into Pound Seconds per Inch and vice versa. The input units are as per the table below
|Unit Full Length Description        |Function String Inputs       |
|-------------------------------|-----------------------------|
|Newton Seconds per Meter       |'N-s/m'                      |
|Pound Seconds per Inch         |'lb-s/in'                    |
***
#### Torsional Spring Constant units
The _torsional_spring_con(value, units)_ function converts Newton Meter per Radian into Pound Inch per Radian and vice versa. The input units are as per the table below
|Unit Full Length Description        |Function String Inputs       |
|-------------------------------|-----------------------------|
|Newton Meter per Radian        |'N-m/rad'                    |
|Pound Inch per Radian          |'lb-in/rad'                  |
***
#### Torsional Dampening Coefficient units
The _torsional_dampening_coef(value, units)_ function converts Newton Meter Second per Radian into Pound Inch Second per Radian and vice versa. The input units are as per the table below
|Unit Full Length Description        |Function String Inputs       |
|-------------------------------|-----------------------------|
|Newton Meter Second per Radian |'N-m-s/rad'                  |
|Pound Inch Second per Radian   |'lb-in-s/rad'                |
***
#### Pressure Gradient units
The _pressure_grad(value, units)_ function converts between different pressure gradient units. The input units are as per the table below
|Unit Full Length Description        |Function String Inputs       |
|-------------------------------|-----------------------------|
|pound per square inch per foot|'psi/ft'                	  |
|KiloPascal per Meter 		   |'kPa/m'                  	  |
|MegaPascal per Meter 		   |'MPa/m'                	 	  |
|Pascal per Meter 			   |'Pa/m'                		  |
***
#### Yield Slurry units
The _yield_slurry(value, units)_ function converts between different Yield Slurry units for cementing. The input units are as per the table below
|Unit Full Length Description        |Function String Inputs       |
|-------------------------------|-----------------------------|
|Cubic Feet per Sack 			|'ft3/sk'                	  |
|Cubic Meter per Sack 			|'m3/sk'                  	  |
|Gallons per Sack 				|'gal/sk'                     |
|Cubic Meter per Kilogram 		|'m3/kg'  					  |
***
#### Footage Cost units
The _footage_cost(value, units)_ function converts between different Footage Cost units for drilling, currency is declared as a universal place holder _"cur"_. The input units are as per the table below
|Unit Full Length Description        |Function String Inputs       |
|-------------------------------|-----------------------------|
|Currency per Foot 				|'cur/ft'                	  |
|Currency per Meter				|'cur/m'                  	  |
|Currency per thousand Feet 	|'cur/1000ft'                 |
|Currency per thousand Meters 	|'cur/1000m'				  |
***
#### Mud Weight units
The _mud_weight(value, units)_ function converts between different Mud Weight units for drilling fluid. The input units are as per the table below
|Unit Full Length Description        |Function String Inputs       |
|-------------------------------|-----------------------------|
|Grams per Cubic Centimeter		|'g/cm3'                	  |
|Grams per Litre				|'g/L'                  	  |
|Kilograms per Cubic Meter 		|'kg/m3'                 	  |
|Kilograms per Litre 			|'kg/L'				  		  |
|KiloPascals Per Meter			|'kPa/m'                	  |
|Pounds Per Cubic Feet			|'lb/ft3'                  	  |
|Pounds Per Barrel			 	|'lb/bbl'                 	  |
|Pounds Per Gallon			 	|'ppg'				 		  |
|Pounds Per Square Inch Per Foot|'psi/ft'                	  |
|Pounds Per Square Inch Per Hundred Feet|'psi/100ft'       	  |
|Specific Gravity		    	|'SG'				  		  |
***
#### Flow Rate units
The _flow_rate(value, units)_ function converts between different Flow Rate units for the circulation of drilling fluid. The input units are as per the table below
|Unit Full Length Description        |Function String Inputs       |
|-------------------------------|-----------------------------|
|Barrels per Hour				|'bbl/hr'                	  |
|Barrels per Minute				|'bbl/min'                    |
|Cubic Feet per Minute 			|'ft3/min'                 	  |
|Cubic Meters per Hour 			|'m3/hr'				  	  |
|Cubic Meters per Minute		|'m3/min'                	  |
|Gallons per Hour 				|'gal/hr'                  	  |
|Gallons per Minute			 	|'gpm'                 	  	  |
|Litres per Hour			 	|'L/hr'				 		  |
|Litres per Minute				|'L/min'                	  |
***
#### Drilling Rate units
The _drilling_rate(value, units)_ function converts between different Drilling Rate units for the Rate of Penetration(ROP). The input units are as per the table below
|Unit Full Length Description        |Function String Inputs       |
|-------------------------------|-----------------------------|
|Feet Per Day					|'ft/d'                	  	  |
|Feet Per Hour					|'ft/hr'                      |
|Feet Per Minute	 			|'ft/min'                 	  |
|Feet Per Second	 			|'ft/s'				  	  	  |
|Meters Per Day					|'m/d'                	  	  |
|Meters Per Hour 				|'m/hr'                  	  |
|Meters Per Minute			 	|'m/min'                 	  |
|Meters Per Second			 	|'m/s'				 		  |
***
#### Weight Length units
The _weight_length(value, units)_ function converts between different Weight by Length units. The input units are as per the table below
|Unit Full Length Description        |Function String Inputs       |
|-------------------------------|-----------------------------|
|Pounds per Foot				|'lb/ft'                  	  |
|Kilograms per Meter			|'kg/m'                       |
***
#### Geothermal Gradient units
The _geothermal_gradient(value, units)_ function converts between different Geothermal Gradient units. The input units are as per the table below
|Unit Full Length Description          |Function String Inputs       |
|---------------------------------|-----------------------------|
|Degrees Centigrade per 100 Meters|'c/100m'                  	|
|Degrees Fahrenheit per 100 Feet  |'f/100ft'                    |
***
*[Table of Contents](#table-of-contents)*
### Production Conversions

#### Nozzle Size units
The _nozzle_size(value, units)_ function converts between different Nozzle Size units. The input units are as per the table below
|Unit Full Length Description        |Function String Inputs       |
|-------------------------------|-----------------------------|
|Millimeters              		|'mm'                  		  |
|Eighth of an Inch              |'1/8in'                      |
|Sixteenth of an Inch           |'1/16in'                     |
|Thirty Seconds of an Inch      |'1/32in'                     |
|Sixty Fourths of an Inch       |'1/64in'                     |
***
#### Nozzle Speed units
The _nozzle_speed(value, units)_ function converts between different Nozzle Speed units. The input units are as per the table below
|Unit Full Length Description        |Function String Inputs       |
|-------------------------------|-----------------------------|
|Feet per Second				|'ft/s'                  	  |
|Meters per Second              |'m/s'                        |
***
#### Oil Production Index units
The _oil_production_index(value, units)_ function converts between different Oil Production Index units. The input units are as per the table below
|Unit Full Length Description                |Function String Inputs      |
|----------------------------------------|----------------------------|
|Barrels per Day - Pounds Per Square Inch|'bbl/d-psi'                 |
|Barrels per Hour - Pounds Per Square Inch|'bbl/hr-psi'               |
|Barrels per Minute - Pounds Per Square Inch|'bbl/min-psi'        	  |
|Cubic Feet per Day - Pounds Per Square Inch|'ft3/d-psi'              |
|Cubic Meter per Day - KiloPascal			|'m3/d-kPa'            	  |
|Cubic Meter per Day - MegaPascal           |'m3/d-MPa'               |
|Cubic Meter per Hour - KiloPascal			|'m3/hr-kPa'           	  |
|Gallons per Day - Pounds Per Square Inch   |'gal/d-psi'              |
|Litres per Hour - KiloPascal               |'l/hr-kPa'               |
***
#### Permeability units
The _permeability(value, units)_ function converts between different Permeability units. The input units are as per the table below
|Unit Full Length Description        |Function String Inputs       |
|-------------------------------|-----------------------------|
|Darcy							|'darcy'                  	  |
|MilliDarcy              		|'md'                         |
|MicroDarcy              		|'ud'                         |
|Square Metres             		|'m2'                         |
|Square Feet              		|'ft2'                        |
***
#### Pipe Capacity (Volume per Length) units
The _pipe_capacity(value, units)_ function converts between different Pipe Capacity units in volume per length. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Barrels per Foot               |'bbl/ft'                  	  |
|Cubic Meters per Meter         |'m3/m'                       |
|Barrels per Inch               |'bbl/in'                     |
|Cubic Feet per Foot      		|'ft3/ft'                     |
|US Gallons per Foot       		|'gal(us)/ft'                 |
|Litres per Meter				|'l/m'                        |
|Cubic Decimeter per Meter      |'dm3/m'                      |
|Square Feet              		|'in3/ft'                     |
***
#### Pipe Capacity (Length per Volume) units
The _pipe_cap_length_vol(value, units)_ function converts between different Pipe Capacity units in length per volume. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Meters per Cubic Meter         |'m/m3'                       |
|Feet per Barrel                |'ft/bbl'                     |
|Feet per Cubic Foot      		|'ft/ft3'                     |
|Feet per US Gallon      		|'ft/gal(us)'                 |
***
#### Production Rate units
The _production_rate(value, units)_ function converts between different Production Rate units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Cubic Meter per Day            |'m3/d'                       |
|Stock Tank Barrel per Day      |'stb/d'                      |
***
#### Rotation units
The _rotation(value, units)_ function converts between different Rotation units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Radian per Second              |'rad/sec'                    |
|Rotations per Minute           |'rpm'                        |
***
#### Section Modulus units
The _section_modulus(value, units)_ function converts between different Section Modulus units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Cubic Centimeter              	|'cm3'                    |
|Cubic Inch           			|'in3'                        |
***
#### Section Modulus - Moment of Section units
The _moment_of_section(value, units)_ function converts between different Section Modulus - Moment of Section units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Centimeter to the Power of 4 	|'cm4'                        |
|Foot to the Power of 4  		|'ft4'                        |
|Inch to the Power of 4        	|'in4'                        |
|Meter to the Power of 4		|'m4'                         |
***
#### Stress Elastic Modulus units
The _stress_elastic_modulus(value, units)_ function converts between different Stress Elastic Modulus units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Kilogram per Square Centimeter |'kg/cm2'                     |
|KiloPascal				  		|'kPa'                        |
|MegaPascal			        	|'Mpa'                        |
|Pascal							|'Pa'                         |
|Pounds per Square Inch			|'psi'                        |
***
#### Stroke Rate units
The _stroke_rate(value, units)_ function converts between different Stroke Rate units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Strokes per Hour				|'stk/hr'                     |
|Strokes per Minute		  		|'stk/min'                    |
***
#### Stroke Volume units
The _stroke_volume(value, units)_ function converts between different Stroke Volume units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Barrels per Stroke				|'bbl/stk'                    |
|Cubic Meters per Stroke		|'m3/stk'                     |
|US Gallons per Stroke			|'gal/stk'                    |
|Litres per Stroke				|'L/stk'                      |
***
*[Table of Contents](#table-of-contents)*
### Force and Power Conversions

#### Electric Current units
The _electric_current(value, units)_ function converts between different Electric Current units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Ampere              		    |'amp'                 		  |
|Abampere / BIOT                |'biot'                       |
|Centiampere           			|'camp'                       |
|Kiloampere           			|'kamp'                       |
|Milliampere           			|'mamp'                       |
|Gilbert                        |'gilbert'                    |
|Volt/Ohm					    |'v/ohm'                      |
|Watt/volt			            |'w/v'                        |
***
#### Fracture Conductivity units
The _fracture_conductivity(value, units)_ function converts between different Fracture Conductivity units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Darcy Inch            		    |'darcy-in'                   |
|mu.m2-m 		                |'mu.m2-m'                    |
***
#### Heat Capacity units
The _heat_capacity(value, units)_ function converts between different Heat Capacity units. The input units are as per the table below
|Unit Full Length Description        |Function String Inputs       |
|-------------------------------|-----------------------------|
|British Thermal Units per Pound - Degree Farenheit|'Btu/lb-F'|
|Joule per Kilogram Celsius 	|'J/kg-C'                     |
***
#### Power/Area units
The _power_area(value, units)_ function converts between different Power/Area units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Horsepower per Square Inch     |'HP/in2'					  |
|Kilowatt per Square Millimeter |'kW/mm2'                     |
***
#### Angular Velocity units
The _angular_velocity(value, units)_ function converts between different Angular Velocity units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Degrees per hour              	|'deg/hr'                 	  |
|Degrees per Minute             |'deg/min'                    |
|Degrees per Second				|'deg/sec'                    |
|Radians per hour				|'rad/hr'                     |
|Radians per Minute           	|'rad/min'                    |
|Radians per Second				|'rad/sec'                    |
|Revolutions per hour			|'rph'                        |
|Revolutions per Minute			|'rpm'                        |
|Revolutions per Second			|'rps'                        |
***
#### Force units
The _force(value, units)_ function converts between different Force units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|DekaNewtons              		|'daN'                 	  	  |
|Dynes             				|'dyn'                    	  |
|Gram-force						|'gf'                   	  |
|Kilogram-force					|'kgf'                  	  |
|KiloNewtons           			|'kN'                    	  |
|KIPS							|'kip'                    	  |
|KiloPounds-force				|'klbs'                       |
|MegaNewton						|'MN'                         |
|Newton							|'N'                          |
|Ounce-force	              	|'ozf'                 	      |
|Pound-force             		|'lbf'                        |
|Poundal         				|'pdl'                        |
|Sthene							|'sn'                     	  |
|Ton-force(metric)           	|'tf-metric'                  |
|Ton-force(long)				|'tf-long'                    |
|Ton-force(short)			    |'tf-short'                   |
|Hectonewton			        |'hN'                         |
|Joules per Meter			    |'J/m'                        |
|MillieNewton        			|'mN'                         |
***
#### Power units
The _power(value, units)_ function converts between different Power units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|British Thermal Units per Second |'BTU/sec'                  |
|British Thermal Units per Minute |'BTU/min'                  |
|Calories per Minute			|'cal/min'                    |
|Calories per Second			|'cal/sec'                    |
|Foot Pound-force per Minute  	|'ft-lb/min'                  |
|Foot Pound-force per Second	|'ft-lb/sec'                  |
|Horsepower     				|'hp'                         |
|Electric Horsepower    		|'hp-elec'                    |
|Metric Horsepower  			|'hp-met'                     |
|Joules per Second             	|'J/s'                 	      |
|Kilocalories per Minute   		|'kcal/min'                   |
|Kilocalories per Second		|'kcal/s'                     |
|Kilogram Force Meter per Minute |'kg-m/min'                  |
|Kilogram Force Meter per Second |'kg-m/sec'                  |
|Kilowatt        				|'kW'                         |
|Megawatt       			    |'MW'                         |
|Newton Meter per Second        |'N-m/s'                      |
|Ton of Refrigeration		    |'ton-ref'                    |
|Volt Ampere					|'var'                        |
|Watt                           |'W'                          |
***
#### Velocity units
The _velocity(value, units)_ function converts between different Velocity units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Feet per Day                   |'ft/d'                  	  |
|Feet per Hour 					|'ft/hr'                  	  |
|Feet per Minute				|'ft/min'                     |
|Feet per Second				|'ft/s'                       |
|Kilometers per Hour  			|'kph'                  	  |
|Kilometers per Minute 			|'k/min'                  	  |
|Kilometers per Second 			|'k/sec'                      |
|Nautical Miles per Hour    	|'knot'                    	  |
|Mach  							|'mach'                       |
|Meters per Day            		|'m/d'                 	      |
|Meters per Hour   				|'m/hour'                     |
|Meters per Minute				|'m/min'                      |
|Meters per Second 				|'m/sec'                      |
|Miles per Hour 				|'mph'                  	  |
|Miles per Minute        		|'mi/min'                     |
|Miles per Second       		|'mi/sec'                     |
***
*[Table of Contents](#table-of-contents)*
### Fluid Conversions

#### Fluid Consistency units
The _fluid_consistency(value, units)_ function converts between different Fluid Consistency units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|dyne-s^n/cm2 					|'dyne-s^n/cm2'               |
|eq.cp                			|'eq.cp'                      |
|lbf-s^n/100ft2       			|'lbf-s^n/100ft2'             |
|lbf-s^n/ft2                    |'lbf-s^n/ft2'                |
|Pa-s^n              			|'Pa-s^n'                     |
***
#### Fluid Yield Point units
The _fluid_yield_point(value, units)_ function converts between different Fluid Yield Point units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Dyne per Square Centimeter     |'dyne/cm2'                   |
|KiloPascal		                |'kPa'                        |
|MegaPascal                     |'Mpa'                        |
|Pound Force per Hundred Square Feet|'lbf/100ft2'             |
***
#### Liquid Production Rate units
The _liquid_production_rates(value, units)_ function converts between different Liquid Production Rate units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Barrels per Day     			|'BPD'                   	  |
|Barrels per Hour		        |'BPH'                        |
|Barrels per Minute             |'BPM'                        |
|Barrels per Second 			|'BPS'             			  |
|Cubic Feet per Day     		|'ft3/day'                    |
|Cubic Feet per Hour		    |'ft3/hr'                     |
|Cubic Feet per Minute          |'ft3/min'                    |
|Cubic Feet per Second			|'ft3/sec'             		  |
|Cubic Feet per Day     		|'m3/day'                     |
|Cubic Meter per Hour		    |'m3/hr'                      |
|Cubic Meter per Minute         |'m3/min'                     |
|Cubic Meter per Second			|'m3/sec'        			  |
|US Gallons per Day     		|'gal/day'                    |
|US Gallons per Hour		    |'gph'                        |
|US Gallons per Minute          |'gpm'                        |
|US Gallons per Second Feet		|'gal/sec'             		  |
|UK Gallons per Day     		|'UK gal/day'                 |
|UK Gallons per Hour		    |'UK gph'                     |
|UK Gallons per Minute          |'UK gpm'                     |
|UK Gallons per Second			|'UK gal/sec'             	  |
***
#### Viscosity units
The _viscosity(value, units)_ function converts between different Viscosity units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Centipoise		     			|'cp'                   	  |
|Gram per Centimeter Second     |'g/(cm.s)'                   |
|Kilogram per Meter Hour        |'kg/(m.hr)'                  |
|Kilogram per Meter Second		|'kg/(m.s)'        			  |
|Kilogram-force Second per Square Meter|'kg-f.s/m2'           |
|KiloPascal Second 			    |'kPa-s'                      |
|Newton Second per Square Meter |'N.s/m2'                     |
|Pascal Second					|'Pa-s'             		  |
|Poise				     		|'p'                          |
|Dyne Second per Square Centimeter|'dyne-s/cm2'               |
|Pound Force-Second per Square Foot|'lbf-s/ft2'               |
|Pound Force-Second per Square Inch|'lbf-s/in2'    			  |
|Pound per Foot Hour			|'lb/(ft.hr)'                 |
|Pound per Foot Second		    |'lb/(ft.s)'                  |
|Poundal Second per Square Foot |'poundal.s/ft2'              |
|Reyn							|'reyn'             		  |
***
#### Oil Volume units
The _oil_volume(value, units)_ function converts between different Oil Volume units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Barrel     					|'bbl'                        |
|Barrel of Oil Equivalent       |'BOE'                        |
|US Gallons                     |'gal'                        |
|Kiloliters						|'kL'             			  |
|Millions of Barrels of Oil Equivalent|'MMBOE'                |
|Thousands  of Barrels of Oil Equivalent|'KBOE'               |
|Tonnes of Oil Equivalent       |'toe'                        |
***
*[Table of Contents](#table-of-contents)*
### Gas Conversions

#### Gas Injection Rate units
The _gas_injection_rate(value, units)_ function converts between different Gas Injection Rate units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Cubic Meter per Minute			|'m3/min'               	  |
|Standard Cubic Feet per Minute |'scfm'                       |
***
#### Gas Production Index units
The _gas_production_index(value, units)_ function converts between different Gas Production Index units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Cubic Meter per Day - MegaPascal|'m3/d-MPa'                   |
|Cubic Meter per Day - KiloPascal|'m3/d-kPa'                        |
|Cubic Meter per Hour - KiloPascal|'m3/hr-kPa'                   |
|Million Standard Cubic Feet per Day per Pounds per Square Inch|'MMSCFD/psi'|
|Thousand Standard Cubic Feet per Hour per Pounds per Square Inch|'MSCF/hr-psi'|
|Thousand Standard Cubic Feet per Day per Pounds per Square Inch|'MSCFD/psi'|
|Standard Cubic Feet per Hour per Pounds per Square Inch|'SCF/hr-psi'|
|Standard Cubic Feet per Day per Pounds per Square Inch|'SCFD/psi'|
***
#### Gas Production Rate units
The _gas_production_rate(value, units)_ function converts between different Gas Production Rate units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Cubic Meters per Minute		|'m3/min'                     |
|Million Barrels     			|'MM'                         |
|Mega Standard Cubic Metres per Day |'MMM3/d'                 |
|Standard Cubic Feet per Minute	|'scfm'                       |
***
#### Gas Volume units
The _gas_volume(value, units)_ function converts between different Gas Volume units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Barrels of Oil Equivalent		|'BOE'                        |
|Cubic Meters	     			|'m3'                         |
|Million Standard Cubic Feet    |'MMscf'                      |
|Standard Cubic Feet per Minute	|'MMsm3'                      |
|Thousand Barrels of Oil Equivalent	|'KBOE'                   |
|Thousand Cubic Meter  			|'dam3'                       |
|Thousand Standard Cubic Feet   |'Mscf'                       |
|Ton Liquefied Natural Gas  	|'ton_LNG'                    |
***
#### LNG Volume units
The _lng_volume(value, units)_ function converts between different LNG Volume units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Barrels of Oil Equivalent		|'BOE'                        |
|Million Barrels of Oil Equivalent|'MMBOE'                    |
|Million Cubic Feet  			|'MMCF'                       |
|Thousand Barrels of Oil Equivalent	|'KBOE'                   |
|Ton Liquefied Natural Gas  	|'ton_LNG'                    |
***
#### Specific Volume units
The _specific_volume(value, units)_ function converts between different Specific Volume units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Barrels per Ton (U.K.)  		|'bbl/UK ton'                 |
|Barrels per Ton (U.S.)         |'bbl/US ton'                 |
|Cubic Foot per Pound  			|'ft3/lb'                     |
|Cubic Inch per Pound       	|'in3/lb'                     |
|Cubic Meter per Kilogram    	|'m3/kg'                      |
|Gallons (U.K.) per Pound   	|'UK gal/lb'                  |
|Gallons (U.S.) per Pound   	|'US gal/lb'                  |
|Liters per Gram             	|'l/g'                        |
|Liters per Kilogram  	        |'l/kg'                       |
***
#### Volume units
The _specific_volume(value, units)_ function converts between different Volume units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Barrels                 		|'bbl'                        |
|Cubic Centimeter               |'cm3'                        |
|Cubic Decimeter     			|'dm3'                        |
|Cubic Foot                 	|'ft3'                        |
|Cubic Inch                 	|'in3'                        |
|Cubic Meter                	|'m3'                         |
|Cubic Yard                 	|'yd3'                        |
|Fluid Ounce                	|'fl_oz'                      |
|Gallon             	        |'gal'                        |
|Liter                      	|'L'                          |
|Quart - Liquid     	        |'qt'                         |
***
*[Table of Contents](#table-of-contents)*
### General Conversions

#### Acceleration units
The _acceleration(value, units)_ function converts between different Acceleration units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|G-unit							|'g'               	          |
|Centimeter per Square Minute   |'cm/min2'                    |
|Centimeter per Square Second   |'cm/s2'               	      |
|Feet per Square Minute         |'ft/min2'                    |
|Galileo  						|'Gal'               	      |
|Inch per Square Hour 			|'in/h2'                      |
|Inch per Square Minute			|'in/min2'               	  |
|Inch per Square Second 		|'in/s2'                      |
|Kilometer per Square Hour		|'km/hr2'               	  |
|Kilometer per Square Minute    |'km/min2'                    |
|Kilometer per Square Second    |'km/s2'               	      |
|Meter per Square Day 			|'m/d2'                       |
|Meter per Square Hour			|'m/hr2'               	      |
|Meter per Square Minute 		|'m/min2'                     |
|Meter per Square Second		|'m/s2'               	      |
|Miles per Square Hour			|'mi/hr2'                     |
|Miles per Square Minute		|'mi/min2'               	  |
|Miles per Square Second        |'mi/s2'                      |
|Knot per Second    			|'knot/s'               	  |
|Millimeter per Square Second   |'mm/s2'                      |
***
#### Area units
The _area(value, units)_ function converts between different Area units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Acre							|'acre'            	          |
|Hectare  						|'ha'               	      |
|Square	Centimeters				|'cm2'                 		  |
|Square	Decimeter   			|'dm2'                 		  |
|Square	Feet					|'ft2'                 		  |
|Square	Inch					|'in2'                 		  |
|Square	Kilometer				|'km2'                 		  |
|Square	Meter					|'m2'                 		  |
|Square Mile					|'mi2'                 		  |
|Square	Millimeter				|'mm2'                 		  |
|Square	Yard					|'yd2'                 		  |
***
#### Density units
The _density(value, units)_ function converts between different Density units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Gram per Cubic Centimeter		|'g/cm3'           	          |
|Gram per Liter					|'g/L'               	      |
|Kilogram per Cubic Centimeter	|'kg/cm3'             		  |
|Kilogram per Cubic Meter       |'kg/m3'               		  |
|Kilogram per Liter				|'kg/L'               		  |
|Ounce per Cubic Foot			|'oz/ft3'              		  |
|Ounce per Cubic Inch			|'oz/in3'              		  |
|Pound per Cubic Foot			|'lb/ft3'              		  |
|Pound per Cubic Inch			|'lb/in3'              		  |
|Pound per US Gallon			|'ppg'                 		  |
|Slug per Cubic Foot			|'slug/ft3'              		  |
|Slug per Cubic Inch			|'slug/in3'              		  |
|Specific Gravity				|'SG'                 		  |
***
#### Distributed Force units
The _distributed_force(value, units)_ function converts between different Distributed Force units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Deka Newton per Meter			|'daN/m'           	          |
|Kilogram per Meter				|'kg/m'               	      |
|Kilonewton per Centimeter		|'kg/cm'               		  |
|Kilopound per Inch   			|'klb/in'              		  |
|Newton per Meter				|'N/m'                 		  |
|Poundforce per Feet			|'lbf/ft'              		  |
***
#### Frequency units
The _frequency(value, units)_ function converts between different Frequency units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Gigahertz          			|'gHz'           	          |
|Hertz							|'Hz'               	      |
|Kilohertz						|'kHz'               		  |
|Megahertz						|'mHz'                 		  |
|Radian per Hour				|'rad/hr'              	      |
|Radian per Minute				|'rad/min'             		  |
|Radian per Second   			|'rad/sec'             		  |
|Revolutions per Hour			|'rph'                 		  |
|Revolutions per Minute     	|'rpm'              		  |
|Revolutions per Second			|'rps'                 		  |
***
#### Length units
The _length(value, units)_ function converts between different Length units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Centimeter          			|'cm'           	          |
|Decimeter						|'dm'               	      |
|Dekameter						|'dam'               		  |
|Fathom 						|'fath'                 		  |
|Feet           				|'ft'              	      |
|Hectometer     				|'hm'             		  |
|Inch                			|'in'             		  |
|Kilometer						|'km'                 		  |
|League					     	|'league'              		  |
|Meter							|'m'                 		  |
|Miles		     				|'mi'             		  |
|Millimeter						|'mm'                 		  |
|Nautical League		     	|'nleague'              		  |
|Nautical Mile					|'nm'                 		  |
|Yard       					|'yd'                 		  |
***
#### Pressure units
The _pressure(value, units)_ function converts between different Pressure units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Atmosphere          			|'atm'           	          |
|Bar							|'bar'               	      |
|Centimeter of Mercury			|'cm_Hg'               		  |
|Centimeter of Water			|'cm_h2o'              		  |
|Dyne per Square Centimeter		|'dyne/cm2'            	      |
|Foot of Air				    |'ft_air'             		  |
|Foot of Mercury    			|'ft_hg'             		  |
|Foot of Water      			|'ft_h2o'              		  |
|Inch of Air			     	|'in_air'              		  |
|Inch of Mercury				|'in_hg'               		  |
|Inch of Water			     	|'in_h2o'              		  |
|Kilogram-force per Square Centimeter|'kg/cm2'             	  |
|Kilogram-force per Square Meter|'kg/m2'              		  |
|KiloPascal						|'kPa'                 		  |
|MegaPascal			     		|'Mpa'              		  |
|Millibar						|'mbar'                 	  |
|Meter of Water			     	|'m_h2o'              		  |
|Meter of Mercury 			    |'m_Hg'                		  |
|Newton per Square Centimeter  	|'N/cm2'              		  |
|Newton per Square Meter		|'N/m2'                 	  |
|Newton per Square Millimeter 	|'N/mm2'              		  |
|Pascal							|'Pa'                 		  |
|Pound-force per Square Foot   	|'psf'              		  |
|Pound-force per Square Inch	|'psi'                 		  |
|Torr			     			|'torr'              		  |
***
#### Time units
The _time(value, units)_ function converts between different Time units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Days		          			|'day'           	          |
|Decades						|'decade'              	      |
|Hours							|'hr'               		  |
|Minutes						|'minute'              		  |
|Seconds						|'sec'              	      |
|Years							|'year'             		  |
***
#### Torque units
The _torque(value, units)_ function converts between different Torque units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Foot Ounce-force      			|'ft-oz'           	          |
|Foot Pound-force				|'ft-lb'              	      |
|Inch Ounce-force				|'in-oz'               		  |
|Inch Pound-force				|'in-lb'              		  |
|Kilogram-force Centimeter		|'kg-cm'              	      |
|Kilogram-force Meter			|'kg-m'             		  |
|KiloNewton Meter      			|'kN-m'           	          |
|Newton Centimeter				|'N-cm'              	      |
|Newton Meter					|'N-m'               		  |
***
#### Torque units
The _torque(value, units)_ function converts between different Torque units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Barrel 		      			|'bbl'           	          |
|Bucket							|'bucket'              	      |
|Bushel							|'bu_us'               		  |
|Cubic Centimeter				|'cm3'              		  |
|Cubic Foot						|'ft3'              	      |
|Cubic Inch						|'in3'             		  	  |
|Cubic Meter	      			|'m3'           	          |
|Cubic Millimeter				|'mm3'              	      |
|Cubic Yard						|'yd3'               		  |
|Cup							|'C'               		  	  |
|Dram			      			|'dr'           	          |
|Drum							|'drum'              	      |
|Fluid Ounce					|'fl_oz'               		  |
|US Gallon						|'gal_us'              		  |
|Gill 							|'gill'              	      |
|UK Gallon			      		|'gal_uk'          	          |
|Kiloliter						|'kL'        	      	      |
|Liter							|'L'       	        		  |
|Milliliter						|'ml'	              		  |
|Pint							|'pt'	              	      |
|Quart - Dry	      			|'qt_dr'           	          |
|Quart - Liquid					|'qt_lq'              	      |
|Tablespoon						|'tbsp'               		  |
|Teaspoon						|'tsp'              		  |
|Tonne of Oil Equivalent		|'toe'              	      |
***
#### Weight units
The _weight(value, units)_ function converts between different Weight units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Carat   		      			|'ct'           	          |
|Centigram						|'cg'              		      |
|Decigram						|'dg'               		  |
|Dram							|'dram'            	 		  |
|Grain							|'gr'              		      |
|Gram			      			|'g'           		          |
|Kilogram						|'kg'              		      |
|KIP							|'kip'               		  |
|Ton - Long						|'t_long'          	 		  |
|Ton - Metric					|'t_metric'        		      |
|Ton - Short	      			|'t_short'         	          |
|Milligram						|'mg'              		      |
|Ounce							|'oz'               		  |
|Pound							|'lb'             	 		  |
|Slug							|'slug'            		      |
|Troy Ounce		      			|'toz'           	          |
|Kilodekanewton					|'KdaN'            		      |
|Dekanewton						|'daN'               		  |
***
#### Flowrate Volume units
The _flowrate_vol(value, units)_ function converts between different Flowrate Volume units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Barrels per Day	      		|'BPD'           	          |
|Cubic Feet per Day				|'ft3/day'          		  |
|Cubic Meters per Day			|'m3/day'              		  |
|US Gallons per Day				|'gal/day'       		      |
|Barrels per Hour				|'BPH'            		      |
|Cubic Feet per Hour			|'ft3/hr'               	  |
|Cubic Meters per Hour			|'m3/hr'               		  |
|US Gallons per Hour			|'gph'         		  		  |
|Barrels per Minute	      		|'BPM'           	          |
|Cubic Feet per Minute			|'ft3/min'          		  |
|Cubic Meters per Minute		|'m3/min'              		  |
|US Gallons per Minute			|'gpm'       		  		  |
|Barrels per Second      		|'BPS'           	          |
|Cubic Feet per Second			|'ft3/sec'          		  |
|Cubic Meters per Second		|'m3/sec'              		  |
|US Gallons per Second 			|'gal/sec'              	  |
***
#### Flowrate Volume units
The _volumetric_flow_rate(value, units)_ function converts between different Flowrate Volume units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Liters per Hour	      		|'L/hr'           	          |
|Liters per Minute				|'L/min'          		  	  |
|Liters per Second			    |'L/sec'              		  |
|Milliliters per Hour		    |'mL/hr'       		      	  |
|Milliliters per Minute			|'mL/min'            		  |
|Milliliters Feet per Second	|'mL/sec'               	  |
|Cubic Meters per Hour			|'m3/hr'               		  |
|Cubic Meters per Minute		|'m3/min'         		  	  |
|Cubic Meters per Second	    |'m3/sec'           	      |
|Cubic Feet per Hour			|'ft3/hr'          		      |
|Cubic Feet per Minute			|'ft3/min'              	  |
|Cubic Feet per Second			|'ft3/sec'       		  	  |
|US Gallons per Hour      		|'us_gal/hr'           	      |
|US Gallons per Minute			|'us_gal/min'          		  |
|US Gallons per Second			|'us_gal/sec'              	  |
|UK Gallons per Hour 			|'uk_gal/hr'              	  |
|UK Gallons per Minute			|'uk_gal/min'          		  |
|UK Gallons per Second			|'uk_gal/sec'              	  |
|Cubic Centimeters per Hour		|'cm3/hr'               	  |
|Cubic Centimeters per Minute	|'cm3/min'         		  	  |
|Cubic Centimeters per Second	|'cm3/sec'           	      |
***
#### Energy units
The _energy(value, units)_ function converts between different Energy Volume units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Barrels of Oil Equivalent  	|'boe'           	          |
|British Thermal Units			|'BTU'          		  	  |
|Calories					    |'cal'              		  |
|Cubic Feet of Natural Gas	    |'nat_gas_ft3'       		  |
|Foot Pounds					|'ft-lb'            		  |
|Foot Poundals					|'ft-pdl'               	  |
|GigaJoules						|'gJ'               		  |
|Horsepower Hours				|'HP-hr'         		  	  |
|Joules						    |'J'           	    		  |
|Kilocalories					|'kcal'          		      |
|Kilogram-force Meters			|'kg-m'              	 	  |
|KiloJoules						|'kJ'       		  	 	  |
|Kilowatt Hours		      		|'kW-hr'           	     	  |
|Liter Atmospheres				|'L-atm'          			  |
|MegaJoules						|'mJ'              	 		  |
|Newton Meters		 			|'Nm'              	 		  |
|Therms							|'therm'          		 	  |
|Thermies						|'thermie'              	  |
|Ton of Explosive				|'ton-exp'               	  |
|Tonne of Coal Equivalent		|'toc'         		  		  |
|Tonne of Oil Equivalent		|'toe'           	     	  |
|Watthour						|'W-hr'           	     	  |
***
#### Temperature units
The _temperature(value, units)_ function converts between different Temperature units. The input units are as per the table below
|Unit Full Length Description   |Function String Inputs       |
|-------------------------------|-----------------------------|
|Centigrade		          		|'c'            	          |
|Fahrenheit						|'f'                 	      |
|Kelvin							|'k'                		  |
***
*[Table of Contents](#table-of-contents)*
## License
Copyright 2021 Timothy Clarke

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.





# ogPypeline
