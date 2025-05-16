from handlers import add_new_channels, analyze_text, parse_yandex_response


# from middlewares.DataBaseConnection import save_interest


async def process_message(message: str):
    if message.text:
        yandex_response = analyze_text(message.text)
        interest, channels = parse_yandex_response(yandex_response)
        # username = message.sender.username if message.sender else "unknown"
        # await save_interest(interest, username)
        add_new_channels(channels)
