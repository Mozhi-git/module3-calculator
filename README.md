# Module 3 Calculator

A command-line calculator application built with Python and tested with pytest.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Input validation
- Division-by-zero error handling
- Interactive command-line interface

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```
## Usage

Run the calculator:

```bash
python3 -m app.main
```

## Testing

Run the tests:

```bash
python3 -m pytest
```

Run tests with coverage:
```bash
python3 -m pytest --cov=app --cov-report=term-missing --cov-fail-under=100
```