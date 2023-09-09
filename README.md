# MacOSPhotoDirImport

```
# Photo Importer

This Python script allows you to import new photos from a chosen directory into the Photos app on macOS.

## Prerequisites

- macOS operating system
- Python 3.x

## Installation

1. Clone or download this repository to your local machine.

2. Make sure you have Python installed on your macOS system. If not, you can download it from the official Python website: [Python Downloads](https://www.python.org/downloads/)

3. Install the required dependencies by running the following command in your terminal:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Open the terminal and navigate to the project directory.

2. Run the script by executing the following command:

   ```
   python photodir-import.py
   ```

3. You will be prompted to enter the path to the directory containing the new photos you want to import. Provide the full path and press Enter.

4. The script will iterate through all the supported image files in the chosen directory and import them into the Photos app.

5. Once the process is complete, you will see a success message in the terminal.

## Configuration

You can modify the script to support additional file types by adding the corresponding extensions to the `SUPPORTED_EXTENSIONS` list in the `photodir-import.py` file.

```python
SUPPORTED_EXTENSIONS = [".jpg", ".jpeg", ".png"]
```

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

```
