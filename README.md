# Summary

An example project as part of a resource i am developing for new web developers

The resource is under development and currently visible [here via Notion](https://ethancloin.notion.site/My-Example-Supplify-b599e8a14c39452f81bb0c28395ac309?pvs=4)

# Running Locally

Structured as a Flask API serving HTML, just run app.py and visit your localhost.
You will just need to create a virtual environment with project dependencies first!

(using zsh on macOS)

```bash
# from the app/ directory
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

from here run the app using your IDE or from your terminal

```bash
python3 app.py
```

# Database

Utilizing SQLite!

[Download from their site](https://sqlite.org/download.html) and use the CLI to interact with the db file like

```bash
sqlite3 supplify.db
.schema
```
