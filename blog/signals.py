from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message
import requests

TELEGRAM_BOT_TOKEN = '7733383691:AAEtqFuM5Z5OwOPLWpL97GyiiZzDrGYaxlU'
CHAT_ID = '1486580350'

@receiver(post_save, sender=Message)
def send_message_to_telegram(sender, instance, created, **kwargs):
    if created:
        text = instance.text
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {
            'chat_id': CHAT_ID,
            'text': text
        }
        requests.post(url, data=data)
