import os
from dotenv import load_dotenv


load_dotenv()


# Telegram Configuration

TELEGRAM_BOT_TOKEN = os.getenv(
    "TELEGRAM_BOT_TOKEN"
)

TELEGRAM_CHAT_ID = os.getenv(
    "TELEGRAM_CHAT_ID"
)


# Market Configuration

MARKET_TYPE = "TSE"

DATA_SOURCE = "PUBLIC"


# Scanner Configuration

SCAN_INTERVAL = 300   # seconds (5 minutes)


# Analysis Configuration

MIN_SCORE = 80


# System Configuration

ENVIRONMENT = "production"
