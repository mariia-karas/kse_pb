from data.data import get_data, load_data
from create_hall import create_hall
from config import FILE_PATH

while True:
    try: 
        user_choice = int(input("Enter your choice: "))
    except Exception as e:
        print(e)
        user_choice = None
        

    if user_choice == 0:
        break

    if user_choice == 1:
        print("create hall")
        create_hall(FILE_PATH)

    if user_choice == 2:
        print("show available")

        def show_empty_seats(FILE_PATH):
            halls = get_data(FILE_PATH)
            hall_name = input("Hall name? ")
            if hall_name not in halls:
                print("Hall does not exist")
            else:
                selected_hall = halls[hall_name]
                empty_seats = []
                for seat in selected_hall:
                    for key, value in seat.items():
                        if value is False:
                            empty_seats.append(key)
                return empty_seats
        print(show_empty_seats(FILE_PATH))

    if user_choice == 3:
        print("book seat")

    if user_choice == 4:
        print("cancel booking")