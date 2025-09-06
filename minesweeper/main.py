from minesweeper.webdriver_utils import create_driver
from minesweeper.game_bot import MinesweeperBot

if __name__ == "__main__":
    driver = create_driver(headless=False)
    driver.get("https://www.google.com/fbx?fbx=minesweeper")
    bot = MinesweeperBot(driver, rows=9, cols=9)
    bot.play()
