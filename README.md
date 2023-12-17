This class calculates the maximum output per day that the turbine can use to generate power

This class calculates the maximum output per day that the turbine can use to generate power

The useful volume of the reservoir in relation to the height of the water in the dam and its surface is given by the equation 2.
Equation 2 : 	

The current volume at any given time according to the continuity equation is the linear composition of the cumulative input curve, the cumulative output-loss curve and the cumulative consumption curve. Two restrictions are imposed on the above volume, the first concerns a minimum volume of Vmin corresponding to a level below which water is unusable for energy production. The second concerns a maximum volume of Vmax corresponding to a level beyond which the water through the dam overflow ends up at the receiver. The current volume for time T is given by equation 3.
Equation 3 : 	

 

Evaporation is ignored in the model due to the small size of the reservoirs. The geometric model is the one shown in figure 1. Given that this type of dams are constructed perpendicular to the flow of small torrents, the above geometric model is quite close to reality and offers an easy and simple way of describing the useful volume with relatively little geometric data.

The function between current useful volume and change in height is calculated in Equation 4.

Equation 4 : 	

Equation 4 is a linear relationship between useful volume of water in the reservoir and change in water level. The water surface (As) and water height (Dh) curve in the reservoir is also useful. The calculation of the equation of the two variables is presented in equation 5-6 and figure 3

Equation 5 : 	
Equation 6 : 	

In the literature, the current volume curve and the reservoir surface curve are usually shown in a common diagram. For this model the diagram is presented in Figure 4.

Figure 4 reservoir level-storage curve

The current maximum and minimum water volume are also shown in Figure 5

Figure 5 reservoir water’s volume
1.   Optimization Model

The goal of the optimization model is to find the vector of daily water supplies per year used to generate electricity. That is, the problem has 365 unknown variables. Restrictions include ensuring a minimum volume in the reservoir set at 10% of the maximum volume, ensuring a minimum irrigation supply. Also the volume of the reservoir is limited by a maximum value beyond which the excess water escapes from the overflow. The objective function is the annual energy production from the turbine. The energy production is given by equation 7.
Equation 7 : 	
	Εurbine : The energy produced

ρ        :  The density of water

g        :  The acceleration of gravity

Dh       : The net height of water drop

Qturbine     : The discharge of water

 

Based on the above the model is presented in the equations of Table 1

The model is solved by the harmony search algorithm and the whole process is organized in Python language.

