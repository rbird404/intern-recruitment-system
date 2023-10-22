import httpx
from httpx import Response

from src.config import BOT_TOKEN
from src.telegram_notification.schemas import NotificationSchema


async def send_notification(user_chat_id: int, message: NotificationSchema) -> Response:
    response = httpx.get(
        f'https://api.telegram.org/bot{BOT_TOKEN}'
        f'/sendMessage?&chat_id={str(user_chat_id)}'
        f'&text={message.generate_message()}'
    )

    return response
