import unittest

from BMI import BMIcalculator,ProcessBMIdata


class TestBMI(unittest.TestCase):
    
    def setUp(self):
        
        self.bmi = BMIcalculator.BMI()
        
    def test_calculate(self):
        """
        Test that it can calculate a BMI
        """
        
        result = self.bmi.calculate((171/100),96)
        self.assertEqual(result, 56.14)
        
    def test_category(self):
        """
        Test that it can check the category of a BMI
        """
        result = self.bmi.category(16)
        self.assertEqual(result, 'Underweight')
        
        result = self.bmi.category(22)
        self.assertEqual(result, 'Normal weight')
        
        result = self.bmi.category(26)
        self.assertEqual(result, 'Overweight')
        
        result = self.bmi.category(31)
        self.assertEqual(result, 'Moderately obese')
        
        result = self.bmi.category(38)
        self.assertEqual(result, 'Severely obese')
        
        result = self.bmi.category(45)
        self.assertEqual(result, 'Very severely obese')
        
    def test_health_risk(self):
        """
        Test that it can check the health risk of a BMI
        """
        result = self.bmi.health_risk(16)
        self.assertEqual(result, 'Malnutrition risk')
        
        result = self.bmi.health_risk(22)
        self.assertEqual(result, 'Low risk')
        
        result = self.bmi.health_risk(26)
        self.assertEqual(result, 'Enhanced risk')
        
        result = self.bmi.health_risk(31)
        self.assertEqual(result, 'Medium risk')
        
        result = self.bmi.health_risk(38)
        self.assertEqual(result, 'High risk')
        
        result = self.bmi.health_risk(45)
        self.assertEqual(result, 'Very high risk')
        
class TestProcessBMIdata(unittest.TestCase):
    
    def setUp(self):
        self.people_data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
        { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
        { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
        { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
        {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
        {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
        
        self.instance = ProcessBMIdata.ProcessJsonBMI(self.people_data)

    def test_get_bmi_data(self):
        """
        Test that it can retrieve BMI data
        """
        
        result = self.instance.get_bmi_data()
        self.assertEqual(result, self.people_data)
        
    def test_process(self):
        """
        Test that it can calculate BMI for all json data
        """
        
        result = self.instance.process()
    
        self.assertEqual(result, self.people_data)
        
    def test_category_count(self):
        """
        Test that it can count BMI category type for all json data
        """
        self.instance.process()
        
        result = self.instance.category_count('Underweight')
        self.assertEqual(result,0)
        
        result = self.instance.category_count('Normal weight')
        self.assertEqual(result,0)
        
        result = self.instance.category_count('Overweight')
        self.assertEqual(result,0)
        
        result = self.instance.category_count('Moderately obese')
        self.assertEqual(result,0)

        result = self.instance.category_count('Severely obese')

        self.assertEqual(result,1)
        
        result = self.instance.category_count('Very severely obese')
        self.assertEqual(result,5)
        
if __name__ == '__main__':
    unittest.main()