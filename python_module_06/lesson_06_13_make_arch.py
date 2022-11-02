import shutil
from pathlib import Path

def create_backup(path, file_name, employee_residence):
    full_path = Path(path, file_name)
    with open(full_path, "wb") as file:
        for key, value in employee_residence.items():
            employee = f"{key} {value}\n"
            file.write(employee.encode())
        return shutil.make_archive("backup_folder", "zip")


if __name__ == "__main__":
    path = r"C:\Users\Rezerv\Desktop\1"
    file_name = "1.bin"
    employee_residence = {'Michael': 'Canada', 'John': 'USA', 'Liza': 'Australia'}
    print(create_backup(path, file_name, employee_residence))
