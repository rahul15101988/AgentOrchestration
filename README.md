# Agent Orchestration

A small, installable Python package for coordinating agent workflows.

## Development setup

Create or activate a virtual environment, then install the package in editable
mode:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install --editable .
```

Run the test suite with:

```powershell
python -m unittest discover -s tests -v
```

The package source lives in `src/agent_orchestration`, and tests live in
`tests/`.
