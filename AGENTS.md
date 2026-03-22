# Project Overview & Tooling

## Project Layout

The `splitlog` project is organized as follows:

- **`splitlog/`**: Contains the source code.
  - `__init__.py`: Core logic for the `_Splitter` class and `split` function.
  - `__main__.py`: CLI entry point, handles argument parsing and file system initialization.
- **`tests/`**: Contains the test suite.
  - `__init__.py`: Test helpers, including `filesystem_to_dict` for verifying `fsspec` memory file systems.
  - `test_argument_parser.py`: Unit tests for CLI argument parsing.
  - `test_main.py`: Integration tests for the CLI entry point.
  - `test_splitter.py`: Unit tests for the core splitting logic.
  - `testcases/`: Fixtures for integration tests.
- **Configuration Files**:
  - `pyproject.toml`: Poetry configuration, dependency definitions, and tool settings.
  - `poetry.lock`: Locked dependency versions.
  - `.github/workflows/`: CI/CD configurations (linting, testing).

## Tools & Libraries

### Core Dependencies
- **`fsspec`**: Used to abstract file system interactions.
  - **`DirFileSystem`**: Used in the CLI (`splitlog/__main__.py`) to handle local output directories.
  - **`MemoryFileSystem`**: Used in tests (`tests/test_splitter.py`) to perform in-memory file operations, ensuring fast and isolated tests.
  - **`AbstractFileSystem`**: Used for type hinting to allow interchangeable backends.

### Development & Testing
- **`poetry`**: Manages dependencies, virtual environments, and packaging.
- **`pytest`**: The testing framework used for executing unit and integration tests.
  - **`pytest-cov`**: Generates coverage reports.
- **`mypy`**: Performs static type checking to ensure code quality and catch type-related errors.
- **`black`**: Enforces a consistent code style through automatic formatting.

### CLI
- **`argparse`**: Standard library module used for parsing command-line arguments.
