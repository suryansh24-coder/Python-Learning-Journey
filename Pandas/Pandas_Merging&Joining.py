import pandas as pd

employee = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["A","B","C"]
})

salary = pd.DataFrame({
    "ID":[1,2,3],
    "Salary":[50000,60000,70000]
})
print(employee.merge(salary,on="ID")) 
employee.merge(salary,on="ID",how="inner")    
employee.merge(salary,on="ID",how="left")    
employee.merge(salary,on="ID",how="right")    
employee.merge(salary,on="ID",how="outer")    
    
    
    
    
    