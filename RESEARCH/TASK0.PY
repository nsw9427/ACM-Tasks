def get_ordinal(day):

    day = int(day)

    if day >= 11 and day <= 13:
        return str(day) + "th"

    if day % 10 == 1:
        return str(day) + "st"
    elif day % 10 == 2:
        return str(day) + "nd"
    elif day % 10 == 3:
        return str(day) + "rd"
    else:
        return str(day) + "th"


def transform_logs(input_text):

    words = input_text.split()

    months = [
        "January", "February", "March",
        "April", "May", "June",
        "July", "August", "September",
        "October", "November", "December"
    ]

    i = 0

    while i < len(words):

        # 1. Hide email addresses
        if "@" in words[i] and "." in words[i]:
            words[i] = "[HIDDEN]"

        # 2. Convert date + time
        elif "/" in words[i] and i + 1 < len(words):

            date_parts = words[i].split("/")
            time_parts = words[i + 1].split(":")

            if len(date_parts) == 3 and len(time_parts) == 2:

                day = int(date_parts[0])
                month = int(date_parts[1])
                year = date_parts[2]

                hour = int(time_parts[0])
                minute = time_parts[1].rstrip(".,!?")

                if hour >= 12:
                    period = "PM"
                else:
                    period = "AM"

                if hour > 12:
                    hour = hour - 12

                new_date = (get_ordinal(day)+ " "+ months[month - 1]+ " "+ year+ ", "+ str(hour)+ ":"+ minute+ " "+ period)

                words[i] = new_date
                words[i + 1] = ""


        # 3. Add a flag to ERROR
        if "ERROR" in words[i]:
            words[i] = "🚨 " + words[i]

        i += 1

    return " ".join(words)

s = input("Enter the text: ")
print(transform_logs(s))