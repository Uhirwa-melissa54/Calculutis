# melissa-calcutils

A simple student math utility package with no runtime dependencies.
This student-created educational package was prepared for Melissa's Python
Software Engineering lab. The implementation was created from scratch.

The distribution name is **melissa-calcutils**; the Python import name is
**calcutils**. Python 3.8 or later is required.

## Installation

Install the locally built wheel from the project root:

~~~powershell
py -m pip install .\dist\melissa_calcutils-0.1.0-py3-none-any.whl
~~~

After you publish to TestPyPI, you can also install with:

~~~powershell
py -m pip install --index-url https://test.pypi.org/simple/ melissa-calcutils
~~~

The package has not been published automatically.

## Usage

~~~python
from calcutils import add, multiply, average

print(add(10, 25))                 # 35
print(multiply(5, 4))              # 20
print(average([10, 20, 30, 40]))    # 25.0
print(average([]))                # 0.0
~~~

## Available functions

- add(a: float, b: float) -> float: return the sum.
- multiply(a: float, b: float) -> float: return the product.
- average(numbers: list) -> float: return the arithmetic mean, or 0.0
  when the list is empty.

Supply numeric values. Inputs are not coerced or validated. Python integers
are also accepted; add and multiply preserve Python's normal numeric behavior.

## Development and build

Run these PowerShell commands from the project root:

~~~powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m build
.\.venv\Scripts\python.exe -m twine check dist/*
~~~

Using the environment's Python directly avoids needing to change PowerShell's
activation execution policy. Requirements are development, build, and publishing
tools, with no runtime dependencies. Setuptools 77 or later is required for
modern MIT SPDX license metadata. Pip selects tools compatible with your
development interpreter.

The build creates a source archive and a wheel in dist/. Check the wheel in
a fresh environment:

~~~powershell
py -m venv .wheel-test-venv
.\.wheel-test-venv\Scripts\python.exe -m pip install --no-deps .\dist\melissa_calcutils-0.1.0-py3-none-any.whl
.\.wheel-test-venv\Scripts\python.exe -c "from calcutils import add, multiply, average; assert add(10, 25) == 35; assert multiply(5, 4) == 20; assert average([10, 20, 30, 40]) == 25.0; assert average([]) == 0.0; print('Wheel checks passed')"
~~~

## Publishing later

Only publish when you choose to do so:

~~~powershell
.\.venv\Scripts\python.exe -m twine upload --repository testpypi dist/*
~~~

Enter your TestPyPI token at Twine's password prompt, using __token__ as the
username if requested. Never put tokens in source files or commands.

The name melissa-calcutils follows PyPI naming rules and returned HTTP 404 on
both PyPI and TestPyPI when checked on 2026-10-08. This does not reserve the
name; confirm availability again before uploading.

## License

MIT License. Copyright (c) 2026 Melissa. See LICENSE.
