dynamic_channel_list = set()


def add_new_channels(channels: list[str]):
    for ch in channels:
        if ch.startswith("@"):  # только Telegram-юзернеймы
            dynamic_channel_list.add(ch)
