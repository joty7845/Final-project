import random

# Initializing the seating plan
seats = [['F' for _ in range(6)] for _ in range(80)]

# Marking aisles (X) and storage areas (S)
for row in seats:
    row[3] = 'X'
    row[4] = 'S'
    row[5] = 'S'


def check_availability(seat_row, seat_col):
    return seats[seat_row][seat_col] == 'F'
# check the seat is available

def book_seat(seat_row, seat_col):
    if check_availability(seat_row, seat_col):
        seats[seat_row][seat_col] = 'R'
        print(f"Seat {seat_row + 1}{chr(seat_col + 65)} successfully booked.")
    else:
        print(f"Seat {seat_row + 1}{chr(seat_col + 65)} is not available.")
# booking seat

def free_seat(seat_row, seat_col):
    if seats[seat_row][seat_col] == 'R':
        seats[seat_row][seat_col] = 'F'
        print(f"Seat {seat_row + 1}{chr(seat_col + 65)} successfully freed.")
    else:
        print(f"Seat {seat_row + 1}{chr(seat_col + 65)} is not reserved.")


def show_booking_state():
    for row_num, row in enumerate(seats, start=1):
        print(f"Row {row_num}: {row}")

# make function about menu
def main():
    while True:
        print("\nMenu:")
        print("1. Check availability of seat")
        print("2. Book a seat")
        print("3. Free a seat")
        print("4. Show booking state")
        print("5. Exit program")

        choice = input("Enter your choice: ")

        if choice == '1':
            seat = input("Enter seat (e.g., 1A): ").strip().upper()
            row, col = int(seat[:-1]) - 1, ord(seat[-1]) - 65
            if check_availability(row, col):
                print(f"Seat {seat} is available.")
            else:
                print(f"Seat {seat} is not available.")

        elif choice == '2':
            seat = input("Enter seat to book (e.g., 1A): ").strip().upper()
            row, col = int(seat[:-1]) - 1, ord(seat[-1]) - 65
            book_seat(row, col)

        elif choice == '3':
            seat = input("Enter seat to free (e.g., 1A): ").strip().upper()
            row, col = int(seat[:-1]) - 1, ord(seat[-1]) - 65
            free_seat(row, col)

        elif choice == '4':
            show_booking_state()

        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
