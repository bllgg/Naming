import os
import random
import csv


def generate_random_name(length=8):
    """
    Generate a unique random string of a given length.

    Args:
        length (int): The length of the random string.

    Returns:
        str: The generated unique random string.
    """
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    while True:
        random_name = ''.join(random.choice(letters) for _ in range(length))
        if not os.path.exists(os.path.join(folder_path, random_name)):
            return random_name


def rename_files_with_random_names():
    """
    Rename files in a folder with unique random names and create a mapping CSV.
    """
    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Create a mapping dictionary for original and random names
    mapping = {}

    for original_name in files:
        random_name = generate_random_name()
        mapping[original_name] = random_name

        # Rename the file with the unique random name
        original_path = os.path.join(folder_path, original_name)
        random_path = os.path.join(folder_path, random_name)
        os.rename(original_path, random_path)

    # Save the mapping to a CSV file
    csv_file_path = os.path.join(folder_path, 'mapping.csv')
    with open(csv_file_path, 'w', newline='') as csvFile:
        csv_writer = csv.writer(csvFile)
        csv_writer.writerow(['Original Name', 'Random Name'])
        for original_name, random_name in mapping.items():
            csv_writer.writerow([original_name, random_name])


def restore_files_with_mapping():
    """
    Restore original file names using the mapping CSV.
    """
    # Check if the mapping CSV file exists
    csv_file_path = os.path.join(folder_path, 'mapping.csv')
    if not os.path.exists(csv_file_path):
        print("Mapping CSV not found. Aborting restoration.")
        return

    # Read the mapping from the CSV file
    mapping = {}
    with open(csv_file_path, 'r') as csvFile:
        csv_reader = csv.reader(csvFile)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            mapping[row[1]] = row[0]

    # Rename files back to their original names
    for random_name, original_name in mapping.items():
        random_path = os.path.join(folder_path, random_name)
        original_path = os.path.join(folder_path, original_name)
        os.rename(random_path, original_path)


def exit_program():
    """
    Function to exit the program.
    """
    print("Exiting.")
    raise SystemExit  # or use sys.exit()


def main():
    """
    Main function to interactively choose the operation.
    """
    operations = {
        '1': rename_files_with_random_names,
        '2': restore_files_with_mapping,
        '3': exit_program
    }

    while True:
        print("Choose operation:")
        print("1. Rename files with random names")
        print("2. Restore original file names")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        selected_operation = operations.get(choice)
        if selected_operation:
            selected_operation()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    # Specify the folder path
    folder_path = r'C:\path\to\your\folder'
    main()
