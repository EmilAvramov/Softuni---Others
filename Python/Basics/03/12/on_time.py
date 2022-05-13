exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_converted = exam_hour * 60 + exam_minutes
arrival_converted = arrival_hour * 60 + arrival_minutes
difference = abs(exam_converted - arrival_converted)
difference_hours = difference // 60
difference_minutes = difference % 60
status = ""

if exam_converted < arrival_converted:
    status = "Late"
elif exam_converted == arrival_converted or arrival_converted < exam_converted <= arrival_converted + 30:
    status = "On time"
elif exam_converted > arrival_converted - 30:
    status = "Early"

if exam_converted == arrival_converted:
    print(f'{status}')
elif arrival_converted < exam_converted <= arrival_converted + 59:
    print(f'{status}', end='\n')
    print(f'{difference_minutes} minutes before the start.')
elif exam_converted >= arrival_converted + 60:
    print(f'{status}', end='\n')
    if difference_minutes < 10:
        print(f'{difference_hours}:0{difference_minutes} hours before the start.')
    else:
        print(f'{difference_hours}:{difference_minutes} hours before the start.')
elif arrival_converted > exam_converted >= arrival_converted - 59:
    print(f'{status}', end='\n')
    print(f'{difference_minutes} minutes after the start.')
elif exam_converted <= arrival_converted + 60:
    print(f'{status}', end='\n')
    if difference_minutes < 10:
        print(f'{difference_hours}:0{difference_minutes} hours after the start.')
    else:
        print(f'{difference_hours}:{difference_minutes} hours after the start.')