BMI Calculator Offline Coding Challenge
==============================


Overview
------------

Given the following JSON data

    [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
    { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
    { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
    { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
    
as the input with weight and height parameters of a person, we have to perform the following:

1) Calculate the BMI (Body Mass Index) using Formula1, BMI Category and Health risk
from Table 1 of the person and add them as 3 new columns

2) Count the total number of overweight people using ranges in the column BMI Category
of Table 1, check this is consistent programmatically and add any other observations in
the documentation

3) Create build, tests to make sure the code is working as expected and this can later be
added to an automation build / testing / deployment pipeline

4) Write a solid production-grade Python3 Program to solve this problem, imagine this will
be used in-product for 1 million patients. We are only interested in a standalone
backend application, we are NOT expecting a UI, webpage, frontend, Mobile App,
microsite, docker, web app etc. Simple and clean solution. Feel free to explore and use
the standard Python libraries or any open source Python modules


How to run application
------------
CD to the project root and contain `main.py` and use `python3 main.py` to run script

For the test, CD to the project root and contain `test.py` and run test with `python3 -m unittest test`


Project Organization
------------
     
    ├── BMI
    │   ├── __init__.py        
    │   ├── BMIcalculator.py      <- Class that handle BMI data.
    │   └── ProcessBMIdata.py     <- Class for processing person json data.
    │
    ├── main.py          <- Entry to the application.
    ├── README.md          <- The  README for project overview and to run project.
    │
    ├── test.py             <- A script to run all unit test.
    
    
 


