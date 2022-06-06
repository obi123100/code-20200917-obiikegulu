from BMI.BMIcalculator import BMI

class ProcessJsonBMI:
    
    def __init__(self,bmi_data):
        self.bmi_data = bmi_data
        
    def get_bmi_data(self):
        
        return self.bmi_data
    
    def process(self):
        
        
        for i in self.bmi_data:
            height = i['HeightCm']
            
            height_in_meters = height/100
            weight = i['WeightKg']
            bmi = BMI()
            bmi_value = bmi.calculate(height=height_in_meters,weight= weight)
            
            i['bmi'] = bmi_value
            i['category'] = bmi.category(bmi_value)
            i['health_risk'] = bmi.health_risk(bmi_value)
            
        return self.bmi_data
    
            
    def category_count(self,category):
        
        count = sum(x['category'] == category for x in self.bmi_data)     
        
        return count
            


