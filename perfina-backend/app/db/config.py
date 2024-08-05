import os

# Get the directory of the current file (config.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the SQLite database file
DB_PATH = os.path.join(BASE_DIR, "db.sqlite3")

TORTOISE_ORM = {
    "connections": {"default": f"sqlite://{DB_PATH}"},
    "apps": {
        "models": {
            "models": ["models.transaction"],
            "default_connection": "default",
        },
    },
}
