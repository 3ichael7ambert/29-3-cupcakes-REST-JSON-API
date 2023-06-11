# Cupcakes

## Install the following

```bash
pip install -r requirements.txt
```

## Then create and seed the database

```bash
psql < seed_cupcakes.sql
python seed.py
```

## refrence to install Flask

```bash
python -m venv venv
source venv/bin/activate
pip install flask
flask run
```

## Test   the data

```bash
source venv/bin/activate
# (venv)
python -m unittest -v tests
```

### error handling

```bash
pip install flask jinja2
deactivate # deactivate venv
#REINSTALL
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate.bat  # For Windows (Command Prompt)
pip install flask==2.0.2 jinja2==3.0.2
pip install -r requirements.txt

```
