import json
from telethon import TelegramClient, events
from telethon.tl.types import PeerUser
from dotenv import load_dotenv
from logger import logger
import os

# Загружаем переменные из .env
load_dotenv()

# Получаем API ID и Hash из переменных окружения
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv('API_HASH')

# Проверяем, что переменные загружены
if not API_ID or not API_HASH:
    error_message = "Пожалуйста, укажите API_ID и API_HASH в файле .env"
    logger.error(error_message)
    raise ValueError(error_message)

# Файл для хранения ID пользователей
STORAGE_FILE = "responded_users.json"

# Текст ответа
RESPONSE_TEXT = (
    "Вітаю! На цю вакансію дуже багато бажаючих. Будь ласка, залишайте заявку і очікуйте. "
    "Тут також розміщуються інші вакансії, які можуть вас зацікавити:\n\n"
    "https://t.me/+XJV6Pu18xkBlYjVi"
)

# Загружаем ID пользователей из файла (если файл существует)
def load_responded_users():
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r") as file:
            return set(json.load(file))
    return set()

# Сохраняем ID пользователей в файл
def save_responded_users(users):
    with open(STORAGE_FILE, "w") as file:
        json.dump(list(users), file)

# Загружаем список отвеченных пользователей
responded_users = load_responded_users()

# Создаем клиент для вашего личного аккаунта
client = TelegramClient('my_account', API_ID, API_HASH)


@client.on(events.NewMessage())
async def handler(event):
    # Проверяем, что сообщение от пользователя, а не от канала или группы
    if isinstance(event.message.peer_id, PeerUser):
        user_id = event.message.from_id.user_id
        logger.info(f"Получено сообщение от пользователя с ID: {user_id}")

        # Если пользователь еще не получал сообщение, отправляем текст
        if user_id not in responded_users:
            logger.info(f"Отправляем сообщение пользователю с ID: {user_id}")
            await event.respond(RESPONSE_TEXT)
            responded_users.add(user_id)
            save_responded_users(responded_users)  # Сохраняем обновленный список
            logger.info(f"Пользователь с ID {user_id} добавлен в список отвеченных")
        else:
            logger.info(f"Пользователь с ID {user_id} уже получил сообщение ранее")


# Запускаем клиент
logger.info("Автоответчик запущен...")
with client:
    client.run_until_disconnected()