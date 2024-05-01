# coupling_calculator.py

def calculate_coupling_multiplier(coupling, V):
    if V < 75:
        if coupling == "Good":
            return 1.00
        elif coupling == "Fair":
            return 0.95
        elif coupling == "Poor":
            return 0.90
    elif V >= 75:
        if coupling == "Good":
            return 1.00
        elif coupling == "Fair":
            return 1.00
        elif coupling == "Poor":
            return 0.90
