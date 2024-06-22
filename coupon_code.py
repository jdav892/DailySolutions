from datetime import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code != correct_code:
        return False
    if type(entered_code) != str:
        return False 
    current_date_comp = datetime.strptime(current_date, "%B %d, %y")
    expiration_date_comp = datetime.strptime(expiration_date, "%B %d, %y")
    
    return current_date_comp <= expiration_date_comp
     