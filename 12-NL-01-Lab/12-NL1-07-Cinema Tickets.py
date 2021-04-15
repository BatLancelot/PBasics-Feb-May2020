movie_name = input()

standard_ticket_sold = 0
student_ticket_sold = 0
kid_ticket_sold = 0
total_tickets_sold = 0

while movie_name != 'Finish':
    total_seats = int(input())
    free_seats = total_seats
    ticket_type = input()

    while free_seats > 0 and ticket_type != 'End':
        total_tickets_sold += 1
        free_seats -= 1

        if ticket_type == 'student':
            student_ticket_sold += 1

        elif ticket_type == 'standard':
            standard_ticket_sold += 1

        else:
            kid_ticket_sold += 1

        if free_seats > 0:
            ticket_type = input()

    total_seats_percentage = 100 - (free_seats / total_seats * 100)
    print(f"{movie_name} - {total_seats_percentage:.2f}% full.")
    movie_name = input()

print(f"Total tickets: {total_tickets_sold}")

student_percentage = student_ticket_sold / total_tickets_sold * 100
print(f"{student_percentage:.2f}% student tickets.")

standard_ticket_percentage = standard_ticket_sold / total_tickets_sold * 100
print(f"{standard_ticket_percentage:.2f}% standard tickets.")

kid_ticket_percentage = kid_ticket_sold / total_tickets_sold * 100
print(f"{kid_ticket_percentage:.2f}% kids tickets.")
