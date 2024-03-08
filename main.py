import asyncio
import logging
from aiogram import Bot, Dispatcher

from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers
from keyboards.main_menu import set_main_menu

# Инициализируе логер
logger = logging.getLogger(__name__)

# Фун-я конфигурации и запуска бота
async def main():
    # Конфигурируем логгирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    # Выводим информацию о начале запуска бота
    logging.info('starting bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tgbot.token,
              parse_mode='HTML')
    dp = Dispatcher()

    # Настраиваем главное меню
    await set_main_menu(bot)

    # Регистрируем роутеры в диспетчер
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
