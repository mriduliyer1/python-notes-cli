# Python Notes CLI

A simple command-line application for managing notes and tasks in Python. Perfect for beginners learning Python and GitHub workflows!

## Features

- ✅ Add notes with title and description
- ✅ List all notes
- ✅ View a specific note by ID
- ✅ Edit notes
- ✅ Delete notes
- ✅ Persistent storage using SQLite

## Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mriduliyer1/python-notes-cli.git
cd python-notes-cli
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - **Linux/Mac:**
     ```bash
     source venv/bin/activate
     ```
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the CLI with:

```bash
python main.py [COMMAND] [OPTIONS]
```

### Commands

#### Add a note
```bash
python main.py add --title "My Title" --description "My description"
```

#### List all notes
```bash
python main.py list
```

#### View a specific note
```bash
python main.py view --id 1
```

#### Edit a note
```bash
python main.py edit --id 1 --title "Updated Title" --description "Updated description"
```

#### Delete a note
```bash
python main.py delete --id 1
```

## Example Workflow

```bash
# Add a few notes
python main.py add --title "Learn Python" --description "Complete the Python basics course"
python main.py add --title "Buy groceries" --description "Milk, eggs, bread"

# List all notes
python main.py list

# View a specific note
python main.py view --id 1

# Edit a note
python main.py edit --id 1 --title "Learn Python and Flask"

# Delete a note
python main.py delete --id 2
```

## Project Structure

```
python-notes-cli/
├── main.py              # CLI entry point with argparse
├── notes.py             # Note class and database logic
├── requirements.txt     # Python dependencies
├── tests/
│   └── test_notes.py    # Unit tests
├── .gitignore           # Git ignore rules
├── LICENSE              # MIT License
└── README.md            # This file
```

## Development

### Running Tests

```bash
python -m pytest tests/ -v
```

### Running with Coverage

```bash
python -m pytest tests/ --cov=. -v
```

## Next Steps (Issues to Work On)

Check the **Issues** tab in this repository for tasks to complete:

1. **Issue #1**: Core CRUD Functionality — implement the main add/list/view/edit/delete features
2. **Issue #2**: Unit Tests — write and run tests to ensure everything works
3. **Issue #3**: Polish & Deploy — improve the CLI, add better error handling, and create a release

## Contributing

1. Create a new branch for your feature: 
   ```bash
   git checkout -b feature/my-feature
   ```
2. Make your changes and test them
3. Commit with clear messages: 
   ```bash
   git commit -m "feat: add my feature"
   ```
4. Push to your branch: 
   ```bash
   git push origin feature/my-feature
   ```
5. Open a Pull Request

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Learning Resources

- [Python Official Docs](https://docs.python.org/3/)
- [SQLite3 Tutorial](https://docs.python.org/3/library/sqlite3.html)
- [argparse Documentation](https://docs.python.org/3/library/argparse.html)
- [pytest Documentation](https://docs.pytest.org/)
- [GitHub Docs](https://docs.github.com/)

---

Happy coding! 🚀 If you have questions, open an Issue or check the documentation above.
