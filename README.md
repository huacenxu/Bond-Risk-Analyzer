## Bond Risk Analyzer
#### Overview
The Bond Risk Analyzer automates the review of bond-related exceptions, focusing on resolving BondCalc (Risk Calculation System) failures and validating risk analytics. It uses decision tree logic to streamline exception handling and improve efficiency.

#### Key Features
Automated Exception Handling: Identifies and resolves bond-related issues, including BondCalc failures.
Proxy CUSIP (Security Identifier) Generation: Dynamically identifies proxy CUSIPs based on bond attributes (e.g., security type, coupon type).
Risk Validation: Checks attributes like Static Yield, Model OAD, and YTM for consistency.
Data Processing: Outputs structured summaries of exceptions, including root cause analysis.

#### Technical Details
Language: Python
Libraries: pandas, datetime
Input: Excel file (test.xlsx) with bond exception details.
Output: Summary of exceptions with statuses, root causes, and proxy CUSIPs.

#### Usage

Clone Repository:
git clone https://github.com/huacenxu/bond-risk-analyzer.git
cd bond-risk-analyzer

Run Script:
Place test.xlsx in the data/ folder and execute:

Sample Input Data
| **CUSIP**    | **AladdinClient** | **NewRiskClient** | **StaticYield** | **ModelOAD** | **YTM** | **ExceptionDescription**       |
|--------------|-------------------|-------------------|-----------------|--------------|---------|---------------------------------|
| ABCD1234     | ClientA           | Risk001           | 1.5             | 0.3          | 0.5     | BondCalc Failure               |
| EFGH5678     | ClientB           | Risk002           | 55.0            | 0.8          | 1.0     | Yield Out of Range             |
| IJKL9012     | ClientC           | Risk003           |                 | 0.6          | 0.9     | Missing Yield                  |

Output:
Displays a DataFrame of processed exceptions. Results can be exported as a CSV.

#### Next Steps: 
Add advanced logic for handling additional bond attributes.
Integrate predictive analytics for exception handling.
Connect with upstream systems for root cause analysis.
