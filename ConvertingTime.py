def convert_to_24_hour(hour, minute, period):
    # changes the hour based on the period (am/pm)
     if period == "am" and hour == 12:
        # 12 am is to be converted to 00
        hour = 0