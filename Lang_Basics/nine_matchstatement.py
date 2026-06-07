# whenever there is multiple conditions we can use match statement similar to switch case

day=10
match day:
    case 1:print('Sunday')
    case 2:print('Monday')
    case 3:print('Tuesday')
    case 4:print('Wednesday')
    case 5:print('Thursday')
    case 6:print('Friday')
    case 7:print('Saturday')
    case _:print('Invalid weekday')

# another e.g.: combine values
dayz = 4
match dayz:
    case 2| 3| 4| 5| 6:print('Weekday')
    case 1| 7: print('Weekend')
    case _:
        print('Invalid weekday')