exam_hour = int(input())
exam_min = int(input())
arrive_hour = int(input())
arrive_min = int(input())

exam_time = exam_hour * 60 + exam_min
arrive_time = arrive_hour * 60 + arrive_min
time_difference = exam_time - arrive_time

hh = abs(time_difference) // 60
mm = abs(time_difference) % 60

if time_difference <= -1:
    print('Late')
    if -59 <= time_difference <= -1:
        print(f'{mm} minutes after the start')
    elif time_difference <= -60:
        if (-69 <= time_difference <= -60) or (-129 <= time_difference <= -120) or (-189 <= time_difference <= -180):
            print(f'{hh}:0{mm} hours after the start')
        else:
            print(f'{hh}:{mm} hours after the start')
    else:
        print(f'{hh}:{mm} hours after the start')
elif 0 <= time_difference <= 30:
    print('On time')
    if 1 <= time_difference <= 30:
        print(f'{mm} minutes before the start')
elif time_difference >= 31:
    print('Early')
    if 31 <= time_difference <= 59:
        print(f'{mm} minutes before the start')
    elif time_difference >= 60:
        if (60 <= time_difference <= 69) or (120 <= time_difference <= 129) or (180 <= time_difference <= 189):
            print(f'{hh}:0{mm} hours before the start')
        else:
            print(f'{hh}:{mm} hours before the start')
    else:
        print(f'{hh}:{mm} hours before the start')


# exam_hour = int(input())
# exam_min = int(input())
# arrive_hour = int(input())
# arrive_min = int(input())
#
# exam_time = exam_hour * 60 + exam_min
# arrive_time = arrive_hour * 60 + arrive_min
# time_difference = exam_time - arrive_time
#
# hh = abs(time_difference) // 60
# mm = abs(time_difference) % 60
#
# if time_difference <= -1:
#     print('Late')
#     if -59 <= time_difference <= -1:
#         print(f'{mm} minutes after the start')
#     elif time_difference <= -60:
#         if -69 <= time_difference <= -60:
#             print(f'{hh}:0{mm} hours after the start')
#         else:
#             print(f'{hh}:{mm} hours after the start')
#     elif -179 <= time_difference <= -120:
#         if -129 <= time_difference <= 120:
#             print(f'{hh}:0{mm} hours before the start')
#         else:
#             print(f'{hh}:{mm} hours before the start')
#     elif -240 <= time_difference <= -180:
#         if -189 <= time_difference <= -180:
#             print(f'{hh}:0{mm} hours before the start')
#         else:
#             print(f'{hh}:{mm} hours before the start')
#     else:
#         print(f'{hh}:{mm} hours after the start')
# elif 0 <= time_difference <= 30:
#     print('On time')
#     if 1 <= time_difference <= 30:
#         print(f'{mm} minutes before the start')
# elif time_difference >= 31:
#     print('Early')
#     if 31 <= time_difference <= 59:
#         print(f'{mm} minutes before the start')
#     elif 60 <= time_difference <= 119:
#         if 60 <= time_difference <= 69:
#             print(f'{hh}:0{mm} hours before the start')
#         else:
#             print(f'{hh}:{mm} hours before the start')
#     elif 120 <= time_difference <= 179:
#         if 120 <= time_difference <= 129:
#             print(f'{hh}:0{mm} hours before the start')
#         else:
#             print(f'{hh}:{mm} hours before the start')
#     elif 180 <= time_difference <= 240:
#         if 180 <= time_difference <= 189:
#             print(f'{hh}:0{mm} hours before the start')
#         else:
#             print(f'{hh}:{mm} hours before the start')
#     else:
#         print(f'{hh}:{mm} hours before the start')
