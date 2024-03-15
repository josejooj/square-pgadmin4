# DON'T CHANGE THIS
SERVER_MODE = True

# Setup max login attemps of a user
# After 3 attempts, the access is blocked
MAX_LOGIN_ATTEMPTS = 3

# Setup log level as DEBUG
"""
    CRITICAL 50
    ERROR    40
    WARNING  30
    SQL      25
    INFO     20
    DEBUG    10
    NOTSET    0
"""
CONSOLE_LOG_LEVEL = 10 # debug

# Define some directories
DATA_DIR = "/application/.pgadmin4"
LOG_FILE = "/application/.pgadmin4/logfile"
SQLITE_PATH = '/application/.pgadmin4/database/pgadmin4.db'