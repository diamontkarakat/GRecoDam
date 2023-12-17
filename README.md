This class calculates the maximum output per day that the turbine can use to generate power

The useful volume of the reservoir in relation to the height of the water in the dam and its surface is given by the equation 2.
Equation 2 : 	
![εικόνα](https://github.com/diamontkarakat/GRecoDam/assets/72194340/c3108277-f656-49ad-ac18-454a7c7cc32f)


The current volume at any given time according to the continuity equation is the linear composition of the cumulative input curve, the cumulative output-loss curve and the cumulative consumption curve. Two restrictions are imposed on the above volume, the first concerns a minimum volume of Vmin corresponding to a level below which water is unusable for energy production. The second concerns a maximum volume of Vmax corresponding to a level beyond which the water through the dam overflow ends up at the receiver. The current volume for time T is given by equation 3.
Equation 3 : 	
![Screenshot_2-300x46](https://github.com/diamontkarakat/GRecoDam/assets/72194340/efc00edb-9409-48e1-bdf1-e556c95cd8a2)
 
Evaporation is ignored in the model due to the small size of the reservoirs. The geometric model is the one shown in figure 1. Given that this type of dams are constructed perpendicular to the flow of small torrents, the above geometric model is quite close to reality and offers an easy and simple way of describing the useful volume with relatively little geometric data.
![Screenshot_3-300x174](https://github.com/diamontkarakat/GRecoDam/assets/72194340/f2cf198e-e631-41f5-8ffe-f42629c64edf)

The function between current useful volume and change in height is calculated in Equation 4.

Equation 4 : 	
![Screenshot_4-300x32](https://github.com/diamontkarakat/GRecoDam/assets/72194340/83f04f8d-871b-4d1e-bb38-b9d0676c35e2)

Equation 4 is a linear relationship between useful volume of water in the reservoir and change in water level. The water surface (As) and water height (Dh) curve in the reservoir is also useful. The calculation of the equation of the two variables is presented in equation 5-6 and figure 3

![Screenshot_5-300x119](https://github.com/diamontkarakat/GRecoDam/assets/72194340/2f630c2d-1b15-4046-942c-ef285fdc094d)

Equation 5 :![Screenshot_6-300x60](https://github.com/diamontkarakat/GRecoDam/assets/72194340/0c0cba76-1f6e-4d1c-8f8c-207bdfa7ebb5)	

Equation 6 : ![Screenshot_7-300x61](https://github.com/diamontkarakat/GRecoDam/assets/72194340/720b9aaf-9fee-451f-b598-93577b28a65c)
	
In the literature, the current volume curve and the reservoir surface curve are usually shown in a common diagram. For this model the diagram is presented in Figure 4.

Figure 4 reservoir level-storage curve
![Screenshot_8-300x186](https://github.com/diamontkarakat/GRecoDam/assets/72194340/9c3f6896-2b30-4bcd-980f-e9f6ddaa5c8a)

The current maximum and minimum water volume are also shown in Figure 5
![Screenshot_9-300x139](https://github.com/diamontkarakat/GRecoDam/assets/72194340/0c9e72d4-31f6-4713-9fc3-8e2c5b47c562)

Figure 5 reservoir water’s volume
1.   Optimization Model

The goal of the optimization model is to find the vector of daily water supplies per year used to generate electricity. That is, the problem has 365 unknown variables. Restrictions include ensuring a minimum volume in the reservoir set at 10% of the maximum volume, ensuring a minimum irrigation supply. Also the volume of the reservoir is limited by a maximum value beyond which the excess water escapes from the overflow. The objective function is the annual energy production from the turbine. The energy production is given by equation 7.
Equation 7 : ![Screenshot_11-300x48](https://github.com/diamontkarakat/GRecoDam/assets/72194340/15c5f2fd-05ea-487e-badd-97d033318385)
	
	Εurbine : The energy produced

ρ        :  The density of water

g        :  The acceleration of gravity

Dh       : The net height of water drop

Qturbine     : The discharge of water

 

Based on the above the model is presented in the equations of Table 1
![Screenshot_10-768x194](https://github.com/diamontkarakat/GRecoDam/assets/72194340/1ad8589d-72ab-4a7f-be70-22a138cb6c96)

The model is solved by the harmony search algorithm and the whole process is organized in Python language.

