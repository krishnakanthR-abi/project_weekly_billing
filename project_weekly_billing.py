# Create Project classesProject(+arepropertiesand–aremethods)+employees -All the employees working in the project+tags-All the tags related to the project+billing_amount_in_inr -Total billing amount for the project+billing_amount_in_usd+total_hours_spent−calculate_acitivity_summary()→ Table with Rows as Tags and Columns asEmployees−calculate_employee_summary()→Table of Employee vs hours_spent−write_report_to_json()*−write_report_to_html()**−display_bar_chart()→ Sho
import pandas as pd
timesheet = pd.read_csv("C://Users//krishnakanth.ravi//Downloads//timesheet_327362000020551004.csv")
timesheet = timesheet.iloc[:223,:]

class Project:

    def __init__(self, employees=None, tags=None, 
                billing_amount_in_inr=None, billing_amount_in_usd=None, 
                total_hours_spent=None):
        
        self.employees = list(pd.unique(timesheet["User"]))
        self.tags = list(pd.unique(timesheet["Tag"]))

        timesheet["Hours(For Calculation)"] = timesheet["Hours(For Calculation)"].astype(float)
        billing_amount_in_inr = timesheet["Hours(For Calculation)"]*40*75
        self.billing_amount_in_inr = billing_amount_in_inr.sum()
        
        billing_amount_in_usd = timesheet["Hours(For Calculation)"]*40
        self.billing_amount_in_usd = billing_amount_in_usd.sum()
        self.total_hours_spent = timesheet["Hours(For Calculation)"].sum()
        print(self.employees, self.tags, self.billing_amount_in_usd, self.billing_amount_in_inr, self.total_hours_spent)
        
    def calculate_activity_summary(self):
        return timesheet.pivot_table (index='Tag', columns='User', 
                values='Hours(For Calculation)', aggfunc = "sum")
        
    def calculate_employee_summary(self):
        return timesheet.groupby("User")["Hours(For Calculation)"].sum()
    
    def display_bar_chart(self):
        return timesheet.plot.bar(x='User', y='Hours(For Calculation)', rot=0)

Project_instance = Project()
print(Project_instance.calculate_activity_summary())
print(Project_instance.calculate_employee_summary())
print(Project_instance.display_bar_chart())

class Employee:

    def __init__(self, projects=None, tags=None, 
                total_billing_amount=None, billing_amount_in_usd=None, 
                total_hours_spent=None):
        self.projects = list(pd.unique(timesheet["Project Name"]))
        self.tags = list(pd.unique(timesheet["Tag"]))
        
        timesheet["Hours(For Calculation)"] = timesheet["Hours(For Calculation)"].astype(float)
        billing_amount_in_inr = timesheet["Hours(For Calculation)"]*40*75
        self.total_billing_amount = billing_amount_in_inr.sum()
        
        billing_amount_in_usd = timesheet["Hours(For Calculation)"]*40
        self.billing_amount_in_usd = billing_amount_in_usd.sum()
        self.total_hours_spent = timesheet["Hours(For Calculation)"].sum()
        print(self.tags, self.projects, self.billing_amount_in_usd, 
                self.total_billing_amount, self.total_hours_spent)

    def calculate_acitivity_summary(self):
        return pd.Series(timesheet["Hours(For Calculation)"].values,
                index=timesheet.Tag).to_dict()

    def calculate_project_summary(self):
        return pd.Series(timesheet["Hours(For Calculation)"].values,
                index=timesheet["Project Name"]).to_dict()

    def display_bar_chart(self):
        return timesheet.plot.bar(x='Project Name', 
                y='Hours(For Calculation)', rot=0)

    
Employee_instance = Employee()
print(Employee_instance.calculate_acitivity_summary())
print(Employee_instance.calculate_project_summary())
print(Employee_instance.display_bar_chart())