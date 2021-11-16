from dotenv import load_dotenv
from os import getenv


load_dotenv()

class var:
    DB_HOST      = getenv("DB_HOST")
    DB_USER      = getenv("DB_USER")
    DB_PASSWOORD = getenv("DB_PASSWOORD")
    DB_NAME      = getenv("DB_NAME")

    API_ID       = int(getenv("API_ID"))
    API_HASH     = getenv("API_HASH")
    BOT_TOKEN    = getenv("BOT_TOKEN")



