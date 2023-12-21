# SIE- ENG270-Project Repository
Camille Perrin and Olivia Robles

## Project Description

The program similuates the impact of coral bleaching due to a certain raise of temperature. When under stress, corals can survive to a ceratin level but after reaching a treshold, they die. We modelize the initial and final health state of coral. The results will be showing as two plot, on top is the initial state in 2023 and on the bottom is the coral heatlh state in 2100 after being under stress for a prolonged period of time. To differenciate the different health states of corals we used colors varying from green to red/brown.

The program will:

1. **getcoralcoord.py** : Read file containing position of Great Barrier Reef Marine Park ("*Marine_Park.json*") and exctract the coordinates located only in the Great Barrier Reef
   
   => Gives us "*coral_coordinates.csv*"

2. **Create_temp_file.py** :

      a. Add dates on a new csv file going from 01/01/2018 to 31/12/2022 (it did not take under consideration 29/02/2020 since it was a leap year <br>
      b. Add temperature from 16.000 to 30.000 to each date and going through 3625 lines (for each coral coordinates).The temperature followed a normal distribution (or Gaussian distribution) around 25.000 <br>
   
   => Gives us "*temperature_data.csv*"
   
3. **adjustement_temperature.c** : Add certain temperature on "*temperature_data.csv*" depending on the scenario chosen
   
    => Gives us  "*scenario1.csv*", "*scenario2.csv*", "*scenario3.csv*","*scenario_past.csv*"

4. **GetPDVfinal.c**:
   
      a. calculate the initial points of life varying randomly from 50 to 100 <br>
      b. calculate the final points of life by a series of calculation and function (hotspots, dhw, growth rate...) <br>
      c. associtaion in a new file (one for each scenario) the initial points of life (PDV_ini) on a column and the final points of life (PDV) on another column <br>
   
   => Gives us  "*PDV_scenario1.csv*", "*PDV_scenario2.csv*", "*PDV_scenario3.csv*"


5. **scenario1.py**, **scenario2.py** or **scenario3.py**:
   
      a. It will associate to each points of life located in ("*PDV_scenario1.csv*"),("*PDV_scenario2.csv*"),("*PDV_scenario3.csv*") to a coral position (located in "*coral_coordinates.csv*") <br>
      b. It will plot dots representing the coral in the Great Barrier Reef in function of their health. The points are distinct by their colors. <br>
      c. (On top is the initial state and at the bottom is the final state) <br>
   
6. **interface.py**: GUI Interface allows the user to choose their scenario by clicking on three different buttons. When clicking, it will execute scenario1.py, scenario2.py or scenario3.py
   



## Project structure

All the files necessary to run our project are located in the same folder.

### Inputs and outputs

Each inputs and outputs are listed here in function of the different steps explained in Project Description.

1. Input: "*Marine_Park.json*"
   Output: "*coral_coordinates.csv*"

2. Input: None
   Output: "*temperature_data.csv*"
   
3. Input: "*temperature_data.csv*"
   Output: "*scenario1.csv*", "*scenario2.csv*", "*scenario3.csv*", "*scenario_past.csv*"

4. Input:"*scenario1.csv*", "*scenario2.csv*", "*scenario3.csv*", "*scenario_past.csv*"
   Output: "*PDV_scenario1.csv*", "*PDV_scenario2.csv*", "*PDV_scenario3.csv*"

5. Input: "*PDV_scenario1.csv*", "*PDV_scenario2.csv*", "*PDV_scenario3.csv*" , "*coral_coordinates.csv*"
   Output: "*plot1.png*", "*plot2.png*", "*plot3.png*"


### Implementation details

**For python**: you need to insall these libraries 

```{bash}
pip install geopandas numpy pandas matplotlib.pyplot
```

**For C**: you need to compile using these commands 

   Step 1: 
   
```{sh}
gcc -Wall adjustement_temperature.c -o file -lm && ./file
```

   step 2: 
   
```{sh}
gcc -Wall GetPDVfinal.c -o tt -lm && ./tt
```

## Instructions

To reproduce results in the report, those steps should be followed:

1. Run **getcoralcoord.py** with input1 ("*Marine_Park.json*")
   -> Make sure that json and csv is imported : (import csv, import json)

2.  Run **Create_temp_file.py**
   -> Make sure that dateime, timedelta, csv ,random are imported : (import csv, from datetime import datetime, timedelta,  import random)

3. Compile **adjustement_temperature.c** (by wrinting the line given above) in the terminal

4. Compile **GetPDVfinal.c** (by wrinting the line given above) in the terminal

5. Run interface.py
   -> Make sure that the library tkinter is installed and that subbprocess is imported: (import subprocess, from tkinter import PhotoImage, import tkinter as tk)
   -> Make sure that the library matplotlib is installed and import matplotlib.pyplot as plt , import csv to run the different scenarios

7. Choose the scenario wanted by clicking on one of the 3 buttons => scenario1.py, scenario2.py or scenario3.py will run. 


## Requirements
Versions of Python and C used are as follows. The library used are also listed here.
```
$ python --version
Python 3.9.18

$ gcc --version
gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0

```


