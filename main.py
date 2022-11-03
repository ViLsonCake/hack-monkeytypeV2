import time
import pyautogui
import lxml
import keyboard
from bs4 import BeautifulSoup
from selenium import webdriver


class MonkeyType:
    """Hack MonkeyType"""
    def __init__(self):
        self.link = 'https://monkeytype.com'

        self.optinons = webdriver.ChromeOptions()
        self.optinons.add_argument('user-agent=Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 107.0.0.0Safari / 537.36')

        self.driver = webdriver.Chrome(
            executable_path=r'C:\Users\user\PycharmProjects\Monkeytype\test_selenium\chromedriver_win32\chromedriver.exe',
            options=self.optinons
        )

        pyautogui.PAUSE = 0.5
        pyautogui.FAILSAFE = True

        self.list_letter = []


    def main(self):
        self.start_driver()
        keyboard.wait('Ctrl')
        self.write_text(self.scraping())


    def start_driver(self):
        self.driver.get(url=self.link)  #start driber
        time.sleep(3)

        return self.driver.page_source


    def scraping(self) -> str:
        self.soup = BeautifulSoup(self.driver.page_source, 'lxml')
        self.list_words = self.soup.find('div', id="words").find_all('div', class_="word")

        for i in self.list_words:                                               #>
            self.list_letter.append(i.find_all('letter'))                       #>
                                                                                #>
        for i in range(len(self.list_letter)):                                  #>
            for j in range(len(self.list_letter[i])):                           #>
                self.list_letter[i][j] = str(self.list_letter[i][j])[8]         #>--converting html code to text
                                                                                #>
        self.list_letter = list(map(lambda x: ''.join(x), self.list_letter))    #>
                                                                                #>
        self.total_text = ' '.join(self.list_letter)                            #>
                                                                                #>
        return self.total_text


    def write_text(self, text: str):
        pyautogui.typewrite(text, 0.04)    #writing text an interval of 0.04


if __name__ == '__main__':
    solution = MonkeyType()
    solution.main()
