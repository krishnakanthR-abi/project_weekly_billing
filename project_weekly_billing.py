"""This program provides summary of employees and projects having two different classes Project and Employee"""
import pandas as pd

timesheet = pd.read_csv(
    "C://Users//krishnakanth.ravi//Downloads//timesheet_327362000020551004.csv"
)
timesheet = timesheet.iloc[:223, :]


class Employee:
    """
    A class to represent Project summary
    ...
    Attributes
    ----------
    employees : str
    tags : str
    billing_amount_in_inr : float
    billing_amount_in_usd : int
    total_hours_spent : int

    Methods
    -------
    calculate_activity_summary():
        returns activity summary of employees against working hours
    calculate_employee_summary():
        returns employee summary of employees against working hours
    display_bar_chart():
        returns bar plot of employees against working hours

    """

    def __init__(
        self,
        employees=None,
        tags=None,
        billing_amount_in_inr=None,
        billing_amount_in_usd=None,
        total_hours_spent=None,
    ):
        """
        Constructs all the necessary attributes for the Employee object.

        Parameters
        ----------
            employees : str
            tags : str
            billing_amount_in_inr : float
            billing_amount_in_usd : int
            total_hours_spent : int
        """

        self.employees = list(pd.unique(timesheet["User"]))
        self.tags = list(pd.unique(timesheet["Tag"]))

        timesheet["Hours(For Calculation)"] = timesheet[
            "Hours(For Calculation)"
        ].astype(float)
        billing_amount_in_inr = timesheet["Hours(For Calculation)"] * 40 * 75
        self.billing_amount_in_inr = billing_amount_in_inr.sum()

        billing_amount_in_usd = timesheet["Hours(For Calculation)"] * 40
        self.billing_amount_in_usd = billing_amount_in_usd.sum()
        self.total_hours_spent = timesheet["Hours(For Calculation)"].sum()
        print(
            self.employees,
            self.tags,
            self.billing_amount_in_usd,
            self.billing_amount_in_inr,
            self.total_hours_spent,
        )

    def calculate_activity_summary(self):
        """returns activity summary of employees against working hours"""
        return timesheet.pivot_table(
            index="Tag", columns="User", values="Hours(For Calculation)", aggfunc="sum"
        )

    def calculate_employee_summary(self):
        """returns employee summary of employees against working hours"""
        return timesheet.groupby("User")["Hours(For Calculation)"].sum()

    def display_bar_chart(self):
        """returns bar plot of employees against working hours"""
        return timesheet.plot.bar(x="User", y="Hours(For Calculation)", rot=0)


Employee_instance = Employee()
print(Employee_instance.calculate_activity_summary())
print(Employee_instance.calculate_employee_summary())
print(Employee_instance.display_bar_chart())

class Project:
    """
    A class to represent Project summary
    ...
    Attributes
    ----------
    projects : str
    tags : str
    billing_amount_in_inr : float
    billing_amount_in_usd : int
    total_hours_spent : int

    Methods
    -------
    calculate_activity_summary():
        returns activity summary of employees against working hours
    calculate_project_summary():
        returns project summary of employees against working hours
    display_bar_chart():
        returns bar plot of employees against working hours

    """

    def __init__(
        self,
        projects=None,
        tags=None,
        total_billing_amount=None,
        billing_amount_in_usd=None,
        total_hours_spent=None,
    ):
        """
        Constructs all the necessary attributes for the project object.

        Parameters
        ----------
            projects : str
            tags : str
            billing_amount_in_inr : float
            billing_amount_in_usd : int
            total_hours_spent : int
        """
        self.projects = list(pd.unique(timesheet["Project Name"]))
        self.tags = list(pd.unique(timesheet["Tag"]))

        timesheet["Hours(For Calculation)"] = timesheet[
            "Hours(For Calculation)"
        ].astype(float)
        billing_amount_in_inr = timesheet["Hours(For Calculation)"] * 40 * 75
        self.total_billing_amount = billing_amount_in_inr.sum()

        billing_amount_in_usd = timesheet["Hours(For Calculation)"] * 40
        self.billing_amount_in_usd = billing_amount_in_usd.sum()
        self.total_hours_spent = timesheet["Hours(For Calculation)"].sum()
        print(
            self.tags,
            self.projects,
            self.billing_amount_in_usd,
            self.total_billing_amount,
            self.total_hours_spent,
        )

    def calculate_activity_summary(self):
        """returns dictionary key : Tag, values : Hours(For calculation)"""
        return pd.Series(
            timesheet["Hours(For Calculation)"].values, index=timesheet.Tag
        ).to_dict()

    def calculate_project_summary(self):
        """returns dictionary key : Project Name, values : Hours(For calculation)"""
        return pd.Series(
            timesheet["Hours(For Calculation)"].values, index=timesheet["Project Name"]
        ).to_dict()

    def display_bar_chart(self):
        """returns bar plot of Project Name against working hours"""
        return timesheet.plot.bar(x="Project Name", y="Hours(For Calculation)", rot=0)


Project_instance = Project()
print(Project_instance.calculate_activity_summary())
print(Project_instance.calculate_project_summary())
print(Project_instance.display_bar_chart())
