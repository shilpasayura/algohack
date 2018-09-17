# genetic 
AlgoHack Genetic Algorithm for University semaster plan creation
This algorithm uses a base data set of 1 batch, 1 semaster, 11 subjects, 11 educators, 1 Lecture Hall and 1 labs
They each have fitness index for selection.
0 : unfit, 1 : OK 2: Good 3: Exllent, 4: Must

The algorithm development process uses python and sqlite db.
1. Auto creates a Relational data base model 
2. Auto generate data in an iterative process using set of natural rules.
3. Create semaster plan through search and natural selection using natural rules.
5. Fixing and Reordering session allocations
6. Analysis of Session allocations to improve the algorithm

Data Structure
Modules + educatiors > Educator modules
Educator modules + spaces + sessions > Semaster Plan 

uni.py - main program
modules.py - Modules
educator.py - Educator Modules
space.py - Lecture halls and Labs
sessions.py - Sessions in a day
space_calender.py - Semaster Plan
stats.py - Statistical Analysis

 
Niranjan Meegammanana


http://shilpasayura.org
