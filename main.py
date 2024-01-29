import os
import random
import csv

def generate_random_name(length=8):
    """
    Generate a random string of a given length.

    Args:
        length (int): The length of the random string.

    Returns:
        str: The generated random string.
    """
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(letters) for _ in range(length))

def rename_files(folder_path):
    """
    Rename files in a folder with random names and create a mapping CSV.

    Args:
        folder_path (str): The path to the folder containing the files.
    """
    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Create a mapping dictionary for original and random names
    mapping = {}

    for original_name in files:
        random_name = generate_random_name()
        mapping[original_name] = random_name

        # Rename the file with the random name
        original_path = os.path.join(folder_path, original_name)
        random_path = os.path.join(folder_path, random_name)
        os.rename(original_path, random_path)

    # Save the mapping to a CSV file
    csv_file_path = os.path.join(folder_path, 'mapping.csv')
    with open(csv_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Original Name', 'Random Name'])
        for original_name, random_name in mapping.items():
            csv_writer.writerow([original_name, random_name])

def restore_files(folder_path, csv_file_path):
    """
    Restore original file names using the mapping CSV.

    Args:
        folder_path (str): The path to the folder containing the files.
        csv_file_path (str): The path to the CSV file with the mapping.
    """
    # Read the mapping from the CSV file
    mapping = {}
    with open(csv_file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            mapping[row[1]] = row[0]

    # Rename files back to their original names
    for random_name, original_name in mapping.items():
        random_path = os.path.join(folder_path, random_name)
        original_path = os.path.join(folder_path, original_name)
        os.rename(random_path, original_path)

if __name__ == "__main__":
    # Specify the folder path
    folder_path = r'C:\path\to\your\folder'

    # Stage 1: Rename files and create mapping CSV
    rename_files(folder_path)

    # Stage 2: Restore original file names using the mapping CSV
    restore_files(folder_path, os.path.join(folder_path, 'mapping.csv'))
