def percent(numerator, denominator):
    percent = numerator / float(denominator) * 100
    DECIMAL_PLACES = 2
    return str(round(percent, DECIMAL_PLACES)) + '%'
    
def percentage(score):
    DECIMAL_PLACE = 2
    CONVERT_TO_PERCENT = 100
    percent = score.wins / float(score.total) * CONVERT_TO_PERCENT
    return round(percent, DECIMAL_PLACE)
