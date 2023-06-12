"""
File: weather_master.py
Name: Sean Wang
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100


def main():
    """
    TODO: program can find highest、lowest and  average temperature and cold days(below 16 °C)
    """
    print("stanCode \"Weather Master 4.0\"!")
    temp = float(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
    h_t = -float('Inf')
    l_t = float('Inf')
    total = 0
    days = 0
    c_days = 0
    avg = 0
    if temp == EXIT:
        print('No temperatures were entered.')
    else:
        while True:
            if temp == EXIT:
                break
            if temp > h_t:
                h_t = temp
            if temp <= l_t:
                l_t = temp
            days += 1
            total = total + temp
            avg = total / days
            if temp < 16:
                c_days += 1
            temp = float(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
        print('Highest temperature= '+str(h_t))
        print('Lowest temperature= '+str(l_t))
        print('Average temperature= '+str(avg))
        print(str(c_days)+' cold day(s)')


if __name__ == '__main__':
    main()