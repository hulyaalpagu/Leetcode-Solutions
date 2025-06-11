import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
   manager_counts=employee.groupby('managerId').size().reset_index(name='report_count')
   managers_with_5=manager_counts[manager_counts['report_count']>=5]
   return pd.merge(managers_with_5, employee, left_on='managerId', right_on='id')[['name']]





