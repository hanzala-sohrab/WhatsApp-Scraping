import configparser
import time

from whatsapp_scraper import WhatsappScrapper


def load_settings():
    """
    Loading and assigning global variables from our settings.txt file
    """
    config_parser = configparser.RawConfigParser()
    config_file_path = '../settings.txt'
    config_parser.read(config_file_path)

    browser = config_parser.get('config', 'BROWSER')
    browser_path = config_parser.get('config', 'BROWSER_PATH')
    name = config_parser.get('config', 'NAME')
    page = config_parser.get('config', 'PAGE')

    settings = {
        'browser': browser,
        'browser_path': browser_path,
        'name': name,
        'page': page
    }
    return settings


def main():
    """
    Loading all the configuration and opening the website
    (Browser profile where whatsapp web is already scanned)
    """
    settings = load_settings()
    scrapper = WhatsappScrapper(
        settings['page'], settings['browser'], settings['browser_path'])

    if scrapper.open_conversation(settings['name']):
        # scrapper.send_message("hola")
        previous_in_message = None
        while True:
            # last_in_message, emojis = scrapper.read_last_in_message()
            last_in_message = scrapper.read_last_in_message()
            # print(last_in_message, emojis)
            if previous_in_message != last_in_message:
                print(last_in_message)
                previous_in_message = last_in_message


            time.sleep(1)


if __name__ == '__main__':
    main()
