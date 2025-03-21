from celery import shared_task
import logging
import requests
import os

logger = logging.getLogger(__name__)

@shared_task
def send_telegram_message(message: str):
    """
    TODO:
    - Add to a generic class UtilityTasks inherited from Tasks
    """
    try:
        logger.info("--Sending Telegram Message--")
        bot_token = os.getenv("GRAM_BOT_TOKEN")
        chat_id = os.getenv("GRAM_CHAT_ID")

        # Telegram API URL
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {"chat_id": chat_id, "text": message}

        # Send the message
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            logger.info("-- Telegram Message Sent --")
    except Exception as e:
        logger.error("Error sending telegram message")
        