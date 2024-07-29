import argparse

from bs4 import BeautifulSoup

import settings
from work_parser.parser import Parser
from work_parser.request import RequestEngine


def main(db: bool):
    page = settings.START_PAGE

    while True:
        page_number = f"PAGE: {page}"
        print(page_number)

        request_engine = RequestEngine()
        response = request_engine.get_response(settings.HOST + settings.ROOT_PATH, params={
            'page': page,
        })

        parser_engine = Parser(BeautifulSoup(response.text, 'html.parser'))
        cards = parser_engine.find_cards("pjax-jobs-list")
        print(cards)
        if not cards:
            break
        else:
            page += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Work UA parser")
    parser.add_argument('-db', default=False)

    args = parser.parse_args()
    main(args.db)
