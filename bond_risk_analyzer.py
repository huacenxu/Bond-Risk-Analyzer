import pandas as pd
import numpy as np
from datetime import date, timedelta

class DecisionTreeProcessor:
    def __init__(self, data):
        self.df = data
        self.final_Status_Df = pd.DataFrame(columns=[
            'Client', 'RiskClient', 'CUSIP', 'Status', 'Comment', 'RootCause',
            'StaticYield', 'ModelOAD', 'YTM', 'ProxyCUSIP'
        ])
    
    def decision_tree(self, row):
        cusip = row['CUSIP']
        exception_desc = row.get('ExceptionDescription', '')

        if "BondCalc Failure" in exception_desc:
            proxy_cusip = self.find_nearest_neighbor({
                'cusip': cusip,
                'issue_date': row.get('IssueDate'),
                'maturity': row.get('MaturityDate'),
                'sec_type': row.get('SecType'),
                'coupon_type': row.get('CouponType'),
                'put_call': row.get('Put/CallInfo')
            }) or 'DEFAULT_PROXY'

            self.final_Status_Df.loc[len(self.final_Status_Df)] = {
                'Client': row['Client'],
                'RiskClient': row['RiskClient'],
                'CUSIP': cusip,
                'Status': 'Follow Up',
                'Comment': 'BondCalc Failure detected',
                'RootCause': 'BondCalc',
                'StaticYield': row.get('StaticYield'),
                'ModelOAD': row.get('ModelOAD'),
                'YTM': row.get('YTM'),
                'ProxyCUSIP': proxy_cusip
            }
        else:
            # Add other decision logic here
            pass
    
    def find_nearest_neighbor(self, target_details):
        """
        Mock function to simulate finding a nearest neighbor.
        """
        return "MOCK_CUSIP"

    def process_all(self):
        for _, row in self.df.iterrows():
            self.decision_tree(row)
        return self.final_Status_Df

# Load the data from the mock file
file_path = 'data/test_sample.xlsx'  
data = pd.read_excel(file_path, header=0)

# Run the processor
processor = DecisionTreeProcessor(data)
final_Status_Df = processor.process_all()

# Print filtered output
filtered_output = final_Status_Df[['Client', 'RiskClient', 'CUSIP', 'Status', 'Comment', 'RootCause', 'ProxyCUSIP']]
print(filtered_output.head())
