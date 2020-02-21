ntime = '1w2d3h4m5s'
wtime = '1day2weeks3s5hours10m'
wwtime = '11m2w3d4s12h'

import json

def Reverse(lst: list): 
    lst.reverse() 
    return lst 


def numjoin(lst):
    for value in range(len(lst)):
        if lst[value].isdigit():
            if lst[value+1].isdigit():
                lst[value] = lst[value] + lst[value+1]
                del lst[value+1]
                lst.append('')
    return lst


def get_time(time:str):
    ftimel = []
    timeb = []
    ftimel.extend(time)
    numjoin(ftimel)
    Reverse(ftimel)
    for  unit in range(len(ftimel)):
        try:
            if ftimel[unit].isalpha():
                ftimel[unit] = '"' + ftimel[unit] + '"' + ':'
            elif ftimel[unit].isdigit() and ftimel[unit + 1].isalpha():
                ftimel[unit] = ftimel[unit] + ','
        except IndexError:
            pass
        except Exception as e:
            print(e)

    ftimel[0] = '{' + ftimel[0]
    ftimel[-1] = ftimel[-1] + '}'

    ftimel = ''.join(ftimel)


    res = json.loads(ftimel)

    if 'w' not in res.keys():
        res['w'] = 0
    if 'd' not in res.keys():
        res['d'] = 0
    if 'h' not in res.keys():
        res['h'] = 0
    if 'm' not in res.keys():
        res['m'] = 0
    if 's' not in res.keys():
        res['s'] = 0
    
    return res


def Format(unFormattedTimeString:str):
    ufts = unFormattedTimeString.lower()
    if 'weeks' in ufts:
        uftsl = ufts.split('weeks')
        ufts = 'w'.join(uftsl)
    if 'week' in ufts:
        uftsl = ufts.split('week')
        ufts = 'w'.join(uftsl)
    if 'days' in ufts:
        uftsl = ufts.split('days')
        ufts = 'd'.join(uftsl)
    if 'day' in ufts:
        uftsl = ufts.split('day')
        ufts = 'd'.join(uftsl)
    if 'minutes' in ufts:
        uftsl = ufts.split('minutes')
        ufts = 'm'.join(uftsl)
    if 'minute' in ufts:
        uftsl = ufts.split('minute')
        ufts = 'm'.join(uftsl)
    if 'seconds' in ufts:
        uftsl = ufts.split('seconds')
        ufts = 's'.join(uftsl)
    if 'second' in ufts:
        uftsl = ufts.split('second')
        ufts = 's'.join(uftsl)
    if 'hours' in ufts:
        uftsl = ufts.split('hours')
        ufts = 'h'.join(uftsl)
    if 'hour' in ufts:
        uftsl = ufts.split('hour')
        ufts = 'h'.join(uftsl)
    return ufts




def get_time_to_seconds(time_str: str):
    time = get_time(Format(time_str))
    seconds = time['s']
    minutes = time['m'] * 60
    hours = time['h'] * 60 * 60
    days = time['d'] * 60 * 60 * 24
    weeks = time['w'] * 60 * 60 * 24 * 7
    timeInSeconds = seconds + minutes + hours + days + weeks
    print(timeInSeconds, type(timeInSeconds))
    return timeInSeconds

    

def main():
    print('\n\n')
    get_time_to_seconds(ntime)
    print()
    print('-' * 10)
    print()
    get_time_to_seconds(wtime)
    print()
    print('-' * 10)
    print()
    get_time_to_seconds(wwtime)
    print('\n\n')

if __name__ == '__main__':
    main()

