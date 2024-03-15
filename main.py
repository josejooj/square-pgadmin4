import os, subprocess, dotenv

# Load .env file
dotenv.load_dotenv()

# Define some paths to use later
APPLICATION_PATH = os.getcwd()
PGADMIN_PATH = f"{APPLICATION_PATH}/.local/lib/python3.11/site-packages/pgadmin4"

# Create private pgadmin folder
# This folder will store database, log, and another things about pgAdmin
if not os.path.isdir("/application/.pgadmin4"):
    os.mkdir("/application/.pgadmin4")

# Copy the configuration file inside pgAdmin path
os.system(f"cp config_local.py {PGADMIN_PATH}/config_local.py")

# Define command to finally run pgadmin
command = [
    # this invocates gunicorn as a python module
    "python", "-m", "gunicorn", 
    # pgadmin by default is open on port 5050, this bind requests on :80 to :5050
    "--bind", "0.0.0.0:80",
    # Setup workers (Dont't change workers this! This should be 1)
    # Changing this may cause problems with CSRF!
    "--workers=1", 
    # Setup threads count
    '--threads=36',
    # tells gunicorn the application it will run
    "pgAdmin4:app"
]

subprocess.run(command, cwd=PGADMIN_PATH, env=os.environ)