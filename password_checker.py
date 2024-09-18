import re

def check_password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[@#$%^&+=]', password) is not None
    
    # Counting how many criteria are met
    criteria_met = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])
    
    # Feedback based on the number of criteria met
    if criteria_met == 5:
        strength = "Strong"
    elif criteria_met >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    # Detailed feedback on missing criteria
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not upper_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lower_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Password should contain at least one number.")
    if not special_criteria:
        feedback.append("Password should contain at least one special character (@, #, $, etc.).")
    
    # Return strength and feedback
    return strength, feedback

# Example usage
password = input("Enter your password: ")
strength, feedback = check_password_strength(password)

print(f"Password Strength: {strength}")
if feedback:
    print("Feedback:")
    for item in feedback:
        print(f"- {item}")
