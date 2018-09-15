Genetic algorithms process information to find a natural solution to a problem following a search heuristic. 
They are inspired by Charles Darwin’s theory of natural evolution that selects fittest individuals naturally for reproduction to produce next generation. 

The process of natural selection starts with the selection of fittest individuals from a population.

There are five phases in a genetic algorithm.

Initial population
Fitness function
Selection
Crossover
Mutation



AlgoHack Genetic Algorithm for University semaster plan creation
This algorithm uses a base data set of 1 batch, 1 semaster, 11 subjects, 11 educators, 1 Lecture Hall and 1 labs
They each have fitness index for selection.
0 : unfit, 1 : OK 2: Good 3: Exellent, 4: Must

The algorithm development process uses python and sqlite db.
1. Auto creates a Relational data base model 
2. Auto generate data in an iterative process using set of natural rules.
3. Create semaster plan through search and natural selection using natural rules.

Data Structure
Please look at genetic_db.jpg

Modules + educatiors > Educator_modules
Educator_modules > Improved_Educator_modules
Improved_Educator_modules + (spaces > sessions) > Semaster Plan 

index.py - runner program
uni.py - main program
modules.py - modules data
educator.py - educators data
space.py - lecture halls and labs data
sessions.py - sessions in a day data
educator_modules.py - educator taught modules
semaster_calender.py - semaster plan

Assumptions 
A semaster is 15 weeks. 15 * 5 days.
11 modules taught by 11 lecturers
Modules have lectures and lab sessions
There are 300 total sessions per semaster
Some modules have one or more lectures per week.
One lecturer may teach multiple modules
Lectures are prefered in morning and lab sessions in afternoon
Holidays have not been considered.


Mini Project Team
Thilni Weerasinghe  
Niranjan Meegammanana

Website
https://girls-intech.blogspot.com
http://shilpasayura.org
