# This program provides summary of employees and projects
# having two different classes Project and Employee
import pandas as pd
import numpy as np


class Project:
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

    def __init__(self, project_name, data):
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
        self.employees = list(
            pd.unique(data.loc[data["Project Name"] == project_name, "User"])
        )
        self.tags = list(
            pd.unique(data.loc[data["Project Name"] == project_name, "Tag"])
        )

        data["Hours(For Calculation)"] = data["Hours(For Calculation)"].astype(float)

        self.billing_amount_in_inr = data.loc[
            data["Project Name"] == project_name, "billing_amount_inr"
        ].sum()

        self.billing_amount_in_usd = data.loc[
            data["Project Name"] == project_name, "billing_amount_usd"
        ].sum()

        self.total_hours_spent = data.loc[
            data["Project Name"] == project_name, "Hours(For Calculation)"
        ].sum()
        print(
            self.employees,
            self.tags,
            self.billing_amount_in_usd,
            self.billing_amount_in_inr,
            self.total_hours_spent,
        )

        self.table = data.loc[
            data["Project Name"] == project_name,
            ("Tag", "User", "Hours(For Calculation)"),
        ]

    def calculate_activity_summary(self):
        """returns activity summary of employees against working hours"""
        return self.table.pivot_table(
            index="Tag", columns="User", values="Hours(For Calculation)", aggfunc="sum"
        )

    def calculate_employee_summary(self):
        """returns employee summary of employees against working hours"""
        return self.table.groupby("User")["Hours(For Calculation)"].sum()

    def display_bar_chart(self):
        """returns bar plot of employees against working hours"""
        return self.table.plot.bar(x="User", y="Hours(For Calculation)", rot=0)


class Employee:
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

    def __init__(self, employee_name, data):
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
        self.projects = list(
            pd.unique(data.loc[data["User"] == employee_name, "Project Name"])
        )
        self.tags = list(pd.unique(data.loc[data["User"] == employee_name, "Tag"]))
        data["Hours(For Calculation)"] = data["Hours(For Calculation)"].astype(float)

        self.total_billing_amount = data.loc[
            data["User"] == employee_name, "billing_amount_inr"
        ].sum()

        self.billing_amount_in_usd = data.loc[
            data["User"] == employee_name, "billing_amount_usd"
        ].sum()

        self.total_hours_spent = data.loc[
            data["User"] == employee_name, "Hours(For Calculation)"
        ].sum()
        print(
            self.tags,
            self.projects,
            self.billing_amount_in_usd,
            self.total_billing_amount,
            self.total_hours_spent,
        )
        self.table = data.loc[
            data["User"] == employee_name, ("Tag", "User", "Hours(For Calculation)")
        ]

    def calculate_activity_summary(self):
        """returns dictionary key : Tag, values : Hours(For calculation)"""
        return pd.Series(
            self.table["Hours(For Calculation)"].values, index=self.table.Tag
        ).to_dict()

    def calculate_project_summary(self):
        """returns dictionary key : Project Name,
        values : Hours(For calculation)"""
        return pd.Series(
            self.table["Hours(For Calculation)"].values, index=self.table["User"]
        ).to_dict()

    def display_bar_chart(self):
        """returns bar plot of Project Name against working hours"""
        return self.table.plot.bar(x="User", y="Hours(For Calculation)", rot=0)


if __name__ == "__main__":

    data = pd.read_csv("data/timesheet_327362000020551004.csv")
    data = data.iloc[:223, :]
    data["billing_amount_usd"] = np.where(data["Role"] == "Employee", 25, 40)
    data["billing_amount_inr"] = data["billing_amount_usd"] * 75

    projects_list = list(pd.unique(data["Project Name"]))
    project_instance = []
    for project_name in projects_list:
        project_instance.append(Project(project_name, data))

    employees_list = list(pd.unique(data["User"]))
    employee_instance = []
    for employee_name in employees_list:
        employee_instance.append(Employee(employee_name, data))
