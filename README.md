# Sie-eng270-Project
Camille Perrin and Olivia Robles

## Project Description

The program similuates the impact of coral bleaching due to a certain raise of temperature. When under stress, corals can survive to a ceratin level but after reaching a treshold they die. We modelize the initial and final of health state of coral. The plot showing on top is the initial state. The plot showing on the bottom is the coral heatlh state after a certain time being under stress.

The program will:

1. getcoralcoord.py : Read file containing position of Great Barrier Reef Marine Park ("*data/Marine_Park.json*") and exctract the coordinates located only in the Great Barrier reef ("*coral_coordinates.csv*")

2. We manually add dates from 01.01.2018 to 01.01.2023 on each column of "*coral_coordinates.csv*" => Give us "*coral_coordinates_dates.csv*"

3. Add_temperature.py: Add temperature from 16.000 to 30.000 to each date and position on "*coral_coordinates_dates.csv*" => Gives us ("*Position_date_temp.csv*")

4. adjustement_temperature.c : Add certain temperature depending on the scenario chosen on "*coral_coordinates_dates.csv*" => Gives us  ("*Scenario_1.csv*"),("*Scenario_2.csv*"),("*Scenario_3.csv*")

5. 


6. scenario1.py, scenario2.py, scenario3.py:
   a. calculate initial point of life varying from 50 to 100 and plot it in function "*coral_coordinates.csv*"
   b. plot at the bottom with the actual point of life "*      *"
   
7. interface.py: GUI Interface, by clicking on the buttons, will execute scenario1.py, scenario2.py or scenario3.py
   



## Project structure
 
 "*data/*" contains input data
- "*results/*" contains program outputs
- "*code/*" contains program code
- ("*bin/*") generated after compiling C code


### Inputs and outputs
Inputs:
- "*data/Marine_Park.json*" is a tab-delimited file.
- "*data/seedvalues.json*" is a tab-delimited file.

Outputs:
- "*results/plausibilite.csv*" is a comma-delimted file.
- "*results/plot.png*" is an image file

### Implementation details





## Instructions

To reproduce results in the report, those steps should be followed:

1. Run getcoralcoord.py with input1 ("*data/Marine_Park.json*")
   -> Make sure that json and csv is imported : (import csv, import json)

2.  Run Add_temperature.py with input 2 ("*coral_coordinates_dates.csv*")
   -> Make sure that the library pandas is installed and random is imported : (import pandas as pd, import random)

3. Complie adjustement_temperature.c with this following line ran in the terminal
   
```{sh}
gcc -Wall adjustement_temperature.c -o file -lm && ./file
```

4. 

5. Run interface.py
   -> Make sure that the library tkinter is installed and that subbprocess is imported: (import subprocess, from tkinter import PhotoImage, import tkinter as tk)

6. Choose the scenario wanted by clicking on one of the 3 buttons => scenario1.py, scenario2.py or scenario3.py will run. 


## Requirements
Versions of Python and C used are as follows. The library used are also listed here.
```
$ python --version
Python 3.9.18

$ gcc --version
gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0

```

```{bash}
pip install geopandas numpy pandas matplotlib.pyplot
```

## Credits
