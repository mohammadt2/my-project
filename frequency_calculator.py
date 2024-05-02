#frequency_calculator.py
def calculate_frequency_multiplier(lifts_per_minute, work_duration, V):

    if work_duration <= 1:
        if V < 75:
            if lifts_per_minute <= 0.2:
                return 1.00
            elif 0.2 < lifts_per_minute == 0.5:
                return 0.97
            elif lifts_per_minute == 1:
                return 0.94
            elif lifts_per_minute == 2:
                return 0.91
            elif lifts_per_minute == 3:
                return 0.88
            elif lifts_per_minute == 4:
                return 0.84
            elif lifts_per_minute == 5:
                return 0.80
            elif lifts_per_minute == 6:
                return 0.75
            elif lifts_per_minute == 7:
                return 0.70
            elif lifts_per_minute == 8:
                return 0.60
            elif lifts_per_minute == 9:
                return 0.52
            elif lifts_per_minute == 10:
                return 0.45
            elif lifts_per_minute == 11:
                return 0.41
            elif lifts_per_minute == 12:
                return 0.37
            elif lifts_per_minute >= 13:
                return 0.00
        elif V >= 75:
            if lifts_per_minute <= 0.2:
                return 1.00
            elif 0.2 < lifts_per_minute == 0.5:
                return 0.97
            elif lifts_per_minute == 1:
                return 0.94
            elif lifts_per_minute == 2:
                return 0.91
            elif lifts_per_minute == 3:
                return 0.88
            elif lifts_per_minute == 4:
                return 0.84
            elif lifts_per_minute == 5:
                return 0.80
            elif lifts_per_minute == 6:
                return 0.75
            elif lifts_per_minute == 7:
                return 0.70
            elif lifts_per_minute == 8:
                return 0.60
            elif lifts_per_minute == 9:
                return 0.52
            elif lifts_per_minute == 10:
                return 0.45
            elif lifts_per_minute == 11:
                return 0.41
            elif lifts_per_minute == 12:
                return 0.37
            elif  lifts_per_minute ==13:
                return 0.34
            elif lifts_per_minute == 14:
                return 0.31
            elif lifts_per_minute == 15:
                return 0.28
            elif lifts_per_minute > 15:
                return 0.00

    elif 1 < work_duration <= 2:
        if V < 75:
            if lifts_per_minute <= 0.2:
                return 0.95
            elif 0.2 < lifts_per_minute == 0.5:
                return 0.92
            elif lifts_per_minute == 1:
                return 0.88
            elif lifts_per_minute == 2:
                return 0.84
            elif lifts_per_minute == 3:
                return 0.79
            elif lifts_per_minute == 4:
                return 0.72
            elif lifts_per_minute == 5:
                return 0.60
            elif lifts_per_minute == 6:
                return 0.50
            elif lifts_per_minute == 7:
                return 0.42
            elif lifts_per_minute == 8:
                return 0.35
            elif lifts_per_minute == 9:
                return 0.30
            elif lifts_per_minute == 10:
                return 0.26
            elif lifts_per_minute >= 11:
                return 0.00
        elif V >= 75:
            if lifts_per_minute <= 0.2:
                return 0.95
            elif 0.2 < lifts_per_minute == 0.5:
                return 0.92
            elif lifts_per_minute == 1:
                return 0.88
            elif lifts_per_minute == 2:
                return 0.84
            elif lifts_per_minute == 3:
                return 0.79
            elif lifts_per_minute == 4:
                return 0.72
            elif lifts_per_minute == 5:
                return 0.60
            elif lifts_per_minute == 6:
                return 0.50
            elif lifts_per_minute == 7:
                return 0.42
            elif lifts_per_minute == 8:
                return 0.35
            elif lifts_per_minute == 9:
                return 0.30
            elif lifts_per_minute == 10:
                return 0.26
            elif lifts_per_minute == 11:
                return 0.23
            elif  lifts_per_minute ==12:
                return 0.21
            elif lifts_per_minute >= 13:
                return 0.00

    elif 2 < work_duration <= 8:
        if V < 75:
            if lifts_per_minute <= 0.2:
                return 0.85
            elif 0.2 < lifts_per_minute == 0.5:
                return 0.81
            elif lifts_per_minute == 1:
                return 0.75
            elif lifts_per_minute == 2:
                return 0.65
            elif lifts_per_minute == 3:
                return 0.55
            elif lifts_per_minute == 4:
                return 0.45
            elif lifts_per_minute == 5:
                return 0.35
            elif lifts_per_minute == 6:
                return 0.27
            elif lifts_per_minute == 7:
                return 0.22
            elif lifts_per_minute == 8:
                return 0.18
            elif lifts_per_minute >= 9:
                return 0.00
        elif V >= 75:
            if lifts_per_minute <= 0.2:
                return 0.85
            elif 0.2 < lifts_per_minute == 0.5:
                return 0.81
            elif lifts_per_minute == 1:
                return 0.75
            elif lifts_per_minute == 2:
                return 0.65
            elif lifts_per_minute == 3:
                return 0.55
            elif lifts_per_minute == 4:
                return 0.45
            elif lifts_per_minute == 5:
                return 0.35
            elif lifts_per_minute == 6:
                return 0.27
            elif lifts_per_minute == 7:
                return 0.22
            elif lifts_per_minute == 8:
                return 0.18
            elif  lifts_per_minute ==9:
                return 0.15
            elif  lifts_per_minute ==10:
                return 0.13
            elif lifts_per_minute >= 11:
                return 0.00
