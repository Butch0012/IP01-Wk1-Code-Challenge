def convert_to_24_hour(hour, minute, period):
    # changes the hour based on the period (am/pm)
    if period == "am" and hour == 12:
        # 12 am is to be converted to 00
        hour = 0
    elif period == "pm" and hour != 12:
        # For pm (except 12 pm), add 12 to the hour
        hour += 12
    # Formating the time to a four-digit string with leading zeros
    return f"{hour:02d}{minute:02d}"
