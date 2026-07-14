def main():
    time = input("What time is it? ")
    ctime = convert(time)
    if 7 <= ctime <= 8:
        print("breakfirst time")
    elif 12 <= ctime <=13:
        print("lunch time")
    elif 18 <= ctime <= 19:
        print("dinner time")
    else:
        pass

def convert(time):
    hours, minutes = time.split(':')
    hours = int(hours)
    minutes = int(minutes)/60
    return hours+minutes
    


if __name__ == "__main__":
    main()
