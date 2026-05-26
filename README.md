# GLAM MAKEUP STORE

A desktop application for managing a beauty store, built with Python and PyQt5.

## Requirements
- Python 3.x
- Dependencies (install via `pip install -r requirements.txt`):
  - PyQt5>=5.15
  - pandas>=2.2
  - openpyxl>=3.1
  - DateTime>=5.5

## Running the Application
To launch the application, run:
```bash
python main.py
```

## Project Structure
- `main.py`: Main entry point for the application.
- `API/`: Contains logic for data interaction (pandas/openpyxl) with the data source.
- `GUI/`: Contains all UI-related code (PyQt5 windows, sub-windows, and assets).
  - `GUI/sub_ventanas/`: Feature-specific modules (inventory, clients, sales, etc.).
  - `GUI/ui/` & `GUI/sub_ventanas/ui/`: Qt Designer (`.ui`) files.
- `registros.xlsx`: Main data source/database for the store.
- `config.json`: Application configuration.

## Key Notes
- **Data Source:** The application heavily relies on `registros.xlsx` located in the root directory.
- **Configuration:** `config.json` uses an absolute path for `logo_path` and may need to be updated if the project is moved.
- **UI:** The project uses Qt Designer files. Changes to `.ui` files must be managed appropriately.
