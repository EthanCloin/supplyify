# Request Flow

Request -> Nginx -> gunicorn -> flask_app

the flask_app part is all ive done in local development.
i need gunicorn to communicate web requests to my flask app
and nginx to receive web requests from the web.

i configure gunicorn via gunicorn_config.py and run via CLI

```bash
.venv/bin/gunicorn --config=gunicorn_config.py "app:create_app()"
```

i configure nginx via /etc/nginx/nginx.conf

i also had to manually run the fresh-tables.sql script from the python interpreter.

there's a bug w manage orders

# Environment

Digital Ocean Droplet running Ubuntu 24.04.

using root user (i know i'll change that)

# Installations

python3.12 and gunicorn already installed in this user

just needed to apt install:
nginx
python3.12-venv

# Configuration

/etc/nginx/nginx.conf holds the file that tells the web server what to do w requests.
main outcome is that i point incoming requests to the server ip to a unix socket. same socket is provided to gunicorn and thats where the two apps chat.

supplyify/gunicorn_config.py is the file that configures gunicorn and is passed as an arg to the CLI:

```bash
.venv/bin/gunicorn --config=gunicorn_config.py "app:create_app()"
```

# Operation

had to prep the database file by running a python interpreter and executing the 'fresh-tables.sql' script.

need to set up some way to spin up gunicorn besides using the manual CLI command in foreground. maybe systemd?

also need to get my domain setup. and get a cert generated
