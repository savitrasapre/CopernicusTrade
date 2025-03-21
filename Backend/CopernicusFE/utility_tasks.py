from celery import shared_task
import logging
import requests

logger = logging.getLogger(__name__)

@shared_task
def send_telegram_message(message: str):
    try:
        logger.info("--Sending Telegram Message--")
        bot_token = "7530716852:AAGmsm7o2QLLLdZ_ZbpTihnFj8l6nDT3HvE"
        chat_id = "7958367256"
        message = "Hello, World!"

        # Telegram API URL
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {"chat_id": chat_id, "text": message}

        # Send the message
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            logger.info("-- Telegram Message Sent --")
    except Exception as e:
        logger.error("Error sending telegram message")
        