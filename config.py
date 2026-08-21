import os

from dotenv import load_dotenv


load_dotenv()


# =========================
# Telegram Configuration
# =========================

TELEGRAM_BOT_TOKEN = os.getenv(
    "TELEGRAM_BOT_TOKEN"
)

TELEGRAM_CHAT_ID = os.getenv(
    "TELEGRAM_CHAT_ID"
)


# =========================
# Market Configuration
# =========================

MARKET_TYPE = "TSE"

DATA_SOURCE = "PUBLIC"


# =========================
# Data Mode
# =========================

# True:
# استفاده از داده آزمایشی برای تست سیستم
#
# False:
# استفاده از منبع واقعی بازار

USE_MOCK_DATA = True


# =========================
# Scanner Configuration
# =========================

# فاصله بررسی بازار (ثانیه)
# 300 = هر 5 دقیقه

SCAN_INTERVAL = 300


# =========================
# Analysis Configuration
# =========================

MIN_SCORE = 80


# =========================
# System Configuration
# =========================

ENVIRONMENT = "production"
