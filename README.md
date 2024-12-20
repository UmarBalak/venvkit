# venvkit

A command-line tool to manage Python virtual environments across your entire PC. This tool allows you to create, list, and delete virtual environments conveniently.

## Features

- **List virtual environments** in specified directories or throughout the entire PC.
- **Create new virtual environments** in a specified directory or the current directory.
- **Delete existing virtual environments** safely.
- **Display information about virtual environments** in simple way.

## Installation

```bash
pip install venvkit
```

## Usage

The tool can be used with the following commands:

* List virtual environments:
    ```bash
    vk list [directory1] [directory2] ...
    ```
    If no directories are specified, it searches the current working directory.

* Create a new virtual environment:
    ```bash
    vk create <env_name> [base_dir]
    ```
    If no base directory is provided, it creates the environment in the current directory.

* Delete a virtual environment:
    ```bash
    vk delete <venv_path>
    ```

* Display information about a virtual environment:
    ```bash
    vk info <venv_path>
    ```
    Displays the Python version and installed packages for the specified virtual environment.

### Help Command

For detailed usage information, run:
```bash
vk help
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.