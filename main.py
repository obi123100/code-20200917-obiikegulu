
from BMI.ProcessBMIdata import ProcessJsonBMI

def main():
    people_data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
        { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
        { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
        { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
        {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
        {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

    process = ProcessJsonBMI(people_data)
    
    people_bmi = process.process()
    number_of_overweight = process.category_count('Overweight')
    print('Persons Data with BMI, category and health risk \n\n',people_bmi,'\n\n')
    print('Number of Overweight in data:',number_of_overweight)

if __name__ == '__main__':
    main()