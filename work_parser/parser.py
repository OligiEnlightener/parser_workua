from bs4 import BeautifulSoup, Tag


class Parser:
    def __init__(self, soup: BeautifulSoup):
        self.soup = soup

    def find_cards(self, id: str) -> list[Tag]:
        cards = self.soup.find('div', id=id)
        card_id = cards.find_all('a', attrs={'name': True})
        return card_id
