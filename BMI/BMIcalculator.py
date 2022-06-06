

    
class BMI:
    
    def calculate(self,height,weight):
        
        bmi = weight/height
        
        return round(bmi, 2)
        
    def category(self,bmi_value):
        
        if bmi_value < 18.5:
            category = 'Underweight'
        elif bmi_value < 25:
            category = 'Normal weight'
        elif bmi_value < 30:
            category = 'Overweight'
        elif bmi_value < 35:
            category = 'Moderately obese'
        elif bmi_value < 40:
            category = 'Severely obese'
        else :
            category = 'Very severely obese'
            
        return category
        
    def health_risk(self,bmi_value):
        if bmi_value < 18.5:
            health_risk = 'Malnutrition risk'
        elif bmi_value < 25:
            health_risk = 'Low risk'
        elif bmi_value < 30:
            health_risk = 'Enhanced risk'
        elif bmi_value < 35:
            health_risk = 'Medium risk'
        elif bmi_value < 40:
            health_risk = 'High risk'
        else :
            health_risk = 'Very high risk'
            
        return health_risk
        