def percent(numerator, denominator):
    percent = numerator / float(denominator) * 100
    DECIMAL_PLACES = 2
    return str(round(percent, DECIMAL_PLACES)) + '%'
