"""
aai4323_hw5.py
AAI4323_5323
September 28, 2026
University of Oklahoma

In this script, you will rewrite the function that is used to recognize revenue from contracts.
The function calculate_quarterly_revenue adds contract revenues to your accounting system.
Currently it just adds them.  You need to change it so that it only does so if the customer
does not have a fix requested and 20 days has elapsed since the contract was signed.

The data from the CRM system is stored in a separate file called givens_hw5.csv.  The
blocks of code to fix have TODO: in front of them.  You will insert your own code in
each segment to complete the script.  You must also fill in information into the standardized
header to match the CR you created in section (1) of the assignment.

There are assertion statements in the code that mimic the tests for the homework.
"""

# Import contracts data
from givens_hw5 import contracts

#####################################################################
# Standardized Header
# Author:  Derek Bransford (OU ID:113762944)
# Date:    September 28, 2026
# CR ID:   CR-2026-0928-REV-001
# Purpose: Remediate a SOX control deficiency by making revenue
#          recognition compliant with ASC 606. Revenue is recognized
#          only after the customer has accepted the system, meaning no
#          fix has been requested and the 20-day acceptance window has
#          elapsed since contract signature.
# Approved by: Margaret Ellison, Corporate Controller (Business Owner)

# #####################################################################

def calculate_quarterly_revenue(contracts_list: list) -> float:
    """
    Calculates total quarterly revenue based on a list of contract dictionaries.
    Applies the new Tier 2 revenue recognition rule (ASC 606).
    """
    total_revenue = 0.0
    
    # TODO:  Enter the minimum number of days required to recognize revenue and create a comment
    # to explain what RECOGNITION_DAYS means
    RECOGNITION_DAYS = 20
    
    # TODO:  This is the current incorrect function to calculate quarterly revenue.  Fix it so that
    # it is compliant.  Include a comment that references your CR ID and explains the new logic.
    for contract in contracts_list:
        requested_fix = contract.get('requested_fix', False)
        days_active = contract.get('days_active', 0)

        if not requested_fix and days_active >= RECOGNITION_DAYS:
            total_revenue += contract.get('value', 0.0)

    return total_revenue

# This is the main section of the assignment that calls your functions.
def main():
    # Call the calculate_quarterly_revenue function to get the revenue to add to your
    # accounting system

    quarterly_revenue = 0
    quarterly_revenue += calculate_quarterly_revenue(contracts)
    print("Quarterly revenue is", quarterly_revenue)

    assert quarterly_revenue == 25000, "Your quarterly revenue is inaccurate"


if __name__ == "__main__":
    main()