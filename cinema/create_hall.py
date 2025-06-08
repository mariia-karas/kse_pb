from data.data import get_data, load_data
from config import FILE_PATH

def create_hall(file_path):
    halls = get_data(file_path) 
    hall_name = input("Яку назву залу бажаєте?")
    if hall_name not in halls:
        rows_number = int(input("Яка к-сть рядів в залі?"))
        columns_number = int(input("Яка к-сть місць в ряді?"))

        hall_name_dict = {hall_name: [] }

        for i in range(1, rows_number+1):
            for j in range(1, columns_number+1):
                seat_dict = {f"{i}-{j}": False}
                hall_name_dict[hall_name].append(seat_dict)
        halls.update(hall_name_dict)
    else:
        print("Зала уже існує")

    load_data(halls, file_path)
