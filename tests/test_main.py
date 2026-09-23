import runpy
from app.main import main

def test_main(monkeypatch, capsys):
    inputs = iter(["power", "add", "hello", "divide", "10", "0", "add", "5", "3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    main()
    output = capsys.readouterr().out
    assert "Welcome to the Calculator!" in output
    assert "Invalid operation. Please try again." in output
    assert "Invalid number. Please enter numeric values." in output
    assert "Error: Division by zero is not allowed." in output
    assert "Result: 8.0" in output
    assert "Goodbye!" in output


def test_main_entry_point(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "exit")
    runpy.run_path("app/main.py", run_name="__main__")
    assert "Goodbye!" in capsys.readouterr().out