from starlette.config import Config

config = Config(".env")

# JWT_EXP: int = 60 * 24 * 93  # 93 days while debug
# JWT_ALG: str = config("ALGORITHM")
# JWT_SECRET: str = config("SECRET_KEY")

DATABASE_URL = config("DATABASE_URL")

API_KEY = config("API_KEY")
TARGET_URL = config("TARGET_URL")
CSV_ROUTE = config("CSV_ROUTE")
CERTIFICATION_FILE = config("CERTIFICATION_FILE")
SLACK_OWL_BOT_TOKEN = config("SLACK_OWL_BOT_TOKEN")
