# File Renaming Tool

A Python script to rename files in a folder with random names, create a mapping CSV file, and restore original file names.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Step 1: Configure Folder Path](#step-1-configure-folder-path)
  - [Step 2: Run the Script](#step-2-run-the-script)
  - [Step 3: Restore Original File Names](#step-3-restore-original-file-names)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Random File Name Generation:** Generates unique random names for files in a specified folder.
- **Mapping CSV Creation:** Creates a CSV file mapping original file names to random names.
- **File Name Restoration:** Restores original file names using the mapping CSV.

## Getting Started

### Prerequisites

- Python 3.9.7 or higher

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/file-renaming-tool.git
   cd file-renaming-tool
   pip install -r requirements.txt
   
##Usage

###Configure Folder Path
```bash
folder_path = r'C:\path\to\your\folder'
```
###Run the Script
```bash
python rename_files.py
```
###Restore Original File Names
```bash
python rename_files.py
```

## Customization
Adjust the length of generated random names in ```generate_random_name``` function

## Contributing
Contributions are welcome! Open an issue or submit a pull request.

## License
Feel free to replace placeholders like `your-username` and customize paths based on your specific project details.
