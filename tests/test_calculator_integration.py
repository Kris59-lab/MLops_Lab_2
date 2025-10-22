from src.calculator import calculator


def test_addition_and_subtraction(monkeypatch, capsys):
    inputs = iter(['1', '20', '5', 'yes', '2', '15', '3', 'no'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    calculator()

    captured = capsys.readouterr()
    # Verify addition result (20 + 5 = 25)
    assert "The result of addition is: 25.0" in captured.out
    # Verify subtraction result (15 - 3 = 12)
    assert "The result of subtraction is: 12.0" in captured.out
    assert "Thank you for using the calculator. Goodbye!" in captured.out


def test_division_by_zero(monkeypatch, capsys):
    inputs = iter(['4', '10', '0', 'no'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    calculator()

    captured = capsys.readouterr()
    assert "Cannot divide by zero." in captured.out
    assert "Thank you for using the calculator. Goodbye!" in captured.out


def test_division(monkeypatch, capsys):
    inputs = iter(['4', '20', '4', 'no'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    calculator()

    captured = capsys.readouterr()
    assert "The result of division is: 5.0" in captured.out
    assert "Thank you for using the calculator. Goodbye!" in captured.out


def test_multiplication(monkeypatch, capsys):
    inputs = iter(['3', '3', '7', 'no'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    calculator()

    captured = capsys.readouterr()
    assert "The result of multiplication is: 21.0" in captured.out
    assert "Thank you for using the calculator. Goodbye!" in captured.out


def test_invalid_operation(monkeypatch, capsys):
    inputs = iter(['5', '1', '10', '5', 'no'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    calculator()

    captured = capsys.readouterr()
    assert (
        "Invalid input. Please enter a number between 1 and 4."
        in captured.out
    )
    assert "The result of addition is: 15.0" in captured.out


def test_non_numeric_input(monkeypatch, capsys):
    """Test non-numeric input for numbers."""
    # Inputs: operation '1', invalid input 'abc', then valid numbers
    inputs = iter(['1', 'abc', '10', '5', 'no'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    calculator()

    captured = capsys.readouterr()
    assert "Invalid input. Please enter numeric values." in captured.out
    assert "The result of addition is: 15.0" in captured.out


def test_invalid_yes_no_response(monkeypatch, capsys):
    """Test invalid response to yes/no prompt."""
    # Inputs: operation, numbers, invalid response 'maybe', then 'no'
    inputs = iter(['1', '5', '3', 'maybe', 'no'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    calculator()

    captured = capsys.readouterr()
    assert "Invalid input. Please enter 'yes' or 'no'." in captured.out
    assert "The result of addition is: 8.0" in captured.out
    assert "Thank you for using the calculator. Goodbye!" in captured.out
