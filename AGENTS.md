# Agent Instructions

This repository is a Python-based desktop application using **PyQt5**.

## Entry Point
- The application starts at `main.py`.

## Structure
- `GUI/`: Contains all UI-related code (PyQt5 windows, sub-windows, and assets).
- `GUI/sub_ventanas/`: Contains specific feature-based windows (e.g., inventory, clients).
- `GUI/sub_ventanas/ui/`: Contains the original Qt Designer (`.ui`) files.
- `API/`: Likely handles data logic and interaction with the `registros.xlsx` file.

## Dependencies
- Dependencies are listed in `requirements.txt`.
- Key libraries: `PyQt5`, `pandas`, `openpyxl`.

## Development Notes
- **Config:** `config.json` uses an absolute path for `logo_path`. This may need to be updated depending on the environment.
- **UI:** The project relies on `.ui` files loaded at runtime or converted to Python. Ensure any changes to `.ui` files are handled correctly.
- **Data:** The application heavily depends on `registros.xlsx` in the root directory.
