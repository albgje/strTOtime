ntime = "1w2d3h4m5s"
wtime = "1day2weeks3s5hours10m"
wwtime = "11m2w3d4s12h"

import json

def Reverse(lst: list): 
    lst.reverse() 
    return lst 

def parse_int(x):
    temp = []
    for c in str(x).strip():
        if c.isdigit():
            temp.append(c)
        else:
            break
    return int("".join(temp)) if "".join(temp) else None

def parse_str(x):
    temp = []
    for c in str(x).strip():
        if c.isalpha():
            temp.append(c)
        else:
            break
    return str("".join(temp)) if "".join(temp) else None

def num_join(string):
    if type(string) == list:
        string = "".join(string)
    elif type(string) == tuple:
        string = "".join(string)
    elif type(string) == int or type(string) == float:
        raise TypeError("You can only pass tuples lists or strings.")
    elif type(string) == str:
        string = string
    string = Format(string)
    string = string.replace("w", " w ")
    string = string.replace("d", " d ")
    string = string.replace("h", " h ")
    string = string.replace("m", " m ")
    string = string.replace("s", " s ")
    string = string.split()
    return string
    

def get_time(time:str):
    try:
        ftimel = []
        #ftimel.extend(time)
        ftimel = num_join(time)
        #print(ftimel)
        Reverse(ftimel)
        for  unit in range(len(ftimel)):
            try:
                if ftimel[unit].isalpha():
                    ftimel[unit] = """ + ftimel[unit] + """ + ":"
                elif ftimel[unit].isdigit() and ftimel[unit + 1].isalpha():
                    ftimel[unit] = ftimel[unit] + ","
            except IndexError:
                pass
            except Exception as e:
                print(e)

        ftimel[0] = "{" + ftimel[0]
        ftimel[-1] = ftimel[-1] + "}"

        ftimel = "".join(ftimel)

        res = json.loads(ftimel)

        if "w" not in res.keys():
            res["w"] = 0
        if "d" not in res.keys():
            res["d"] = 0
        if "h" not in res.keys():
            res["h"] = 0
        if "m" not in res.keys():
            res["m"] = 0
        if "s" not in res.keys():
            res["s"] = 0
        #print(res, type(res))
        return res

    except:
        print("Error")
        rtrn = {"s":0,"w":0,"d":0,"h":0,"m":0}
        return rtrn


def Format(unFormattedTimeString:str):
    ufts = unFormattedTimeString.lower()
    uftsr = ufts.replace("weeks", "w").replace("week", "w").replace("days", "d").replace("day", "d").replace("hours", "h").replace("hour", "h").replace("minutes", "m").replace("minute", "m").replace("seconds", "s").replace("second","s")

    return uftsr




def get_time_to_seconds(time_str: str):
    time = get_time(Format(time_str))
    seconds = time["s"]
    minutes = time["m"] * 60
    hours = time["h"] * 60 * 60
    days = time["d"] * 60 * 60 * 24
    weeks = time["w"] * 60 * 60 * 24 * 7
    timeInSeconds = seconds + minutes + hours + days + weeks
    #print(timeInSeconds, type(timeInSeconds))
    return timeInSeconds

def get_seconds_to_str(seconds: int):
    """ From a number of seconds determines the amount of years, months, weeks, days, hours, minutes, and seconds. 

    Assumes: 1 millenia = 10 centuries
             1 century = 10 decades
             1 decade = 10 years
             1 year = 12 months
             1 month = 4 weeks
             1 week = 7 days
             1 day = 24 hours
             1 hour = 60 minutes
             1 minute = 60 seconds
    """


    minutes, seconds = divmod(seconds, 60)
    hours, minutes   = divmod(minutes, 60)
    days, hours      = divmod(hours,   24)
    weeks, days      = divmod(days,     7)
    months, weeks    = divmod(weeks,    4)
    years, months    = divmod(months,  12)
    decades, years   = divmod(years,   10)
    centuries, decades=divmod(decades, 10)
    millenia,centuries=divmod(centuries, 10)

    if millenia == 0:
        millenium = ""
    elif millenia == 1:
        millenium = "1 millenium"
    elif millenia >= 2:
        millenium = "{} millenia".format(millenia)
    if centuries == 0:
        century = ""
    elif centuries == 1:
        century = "1 century"
    elif centuries >= 2:
        century = "{} centuries".format(centuries)
    if decades == 0:
        decade = ""
    elif decades == 1:
        decade = "1 decade"
    elif decades >= 2:
        decade = "{} decades".format(decades)
    if years == 0:
        year = ""
    elif years == 1:
        year = "1 year"
    elif years >= 2:
        year = "{} years".format(years)
    if months == 0:
        month = ""
    elif months == 1:
        month = "1 month"
    elif months >= 2:
        month = "{} months".format(months)
    if weeks == 0:
        week = ""
    elif weeks == 1:
        week = "1 week"
    elif weeks >= 2:
        week = "{} weeks".format(weeks)
    if days == 0:
        day = ""
    elif days == 1:
        day = "1 day"
    elif days >= 2:
        day = "{} days".format(days)
    if hours == 0:
        hour = ""
    elif hours == 1:
        hour = "1 hour"
    elif hours >= 2:
        hour = "{} hours".format(hours)
    if minutes == 0:
        minute = ""
    elif minutes == 1:
        minute = "1 minute"
    elif minutes >= 2:
        minute = "{} minutes".format(minutes)
    if seconds == 0:
        second = ""
    elif seconds == 1:
        second = "1 second"
    elif seconds >= 2:
        second = "{} seconds".format(seconds)

    if millenium != "":
        century = " " + century
    if century != "":
        decade = " " + decade
    if decade != "":
        year = " " + year
    if year != "":
        month = " " + month
    if month != "":
        week = " " + week
    if week != "":
        day = " " + day
    if day != "":
        hour = " " + hour
    if hour != "":
        minute = " " + minute
    if minute != "":
        second = " " + second

    formatted = millenium + century + decade + year + month + week + day + hour + minute + second
    formatted = formatted.strip() + "."
    formaty = []
    formatyo = []
    formatyo = formatted.split()
    for i in formatyo:
        if i != "":
            formaty.append(i)
    return " ".join(formaty)


    

def main():
    print("\n\n")
    h = get_time_to_seconds(ntime)
    print(h)
    print()
    h = get_seconds_to_str(get_time_to_seconds(ntime))
    print(h)
    print()
    print("-" * 10)
    print()
    h = get_time_to_seconds(wtime)
    print(h)
    print()
    h = get_seconds_to_str(get_time_to_seconds(wtime))
    print(h)
    print()
    print("-" * 10)
    print()
    h = get_time_to_seconds(wwtime)
    print(h)
    print()
    h = get_seconds_to_str(get_time_to_seconds(wwtime))
    print(h)
    print("\n\n")

if __name__ == "__main__":
    main()

