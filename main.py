import os, logging, sys
from src.modules.utils.logger import Logger
from src.modules.helper.config import Config
from src.modules.viewbot.viewbot import ViewBot

# Set title
if os.name == 'nt':
    os.system(f"title Tracker.gg View Bot • Starting...")

# Set logging system
logging.basicConfig(handlers=[logging.FileHandler('tracker_viewbot.log', 'w+', 'utf-8')], level=logging.ERROR, format='%(asctime)s: %(message)s')

# Main class
class Main():
    def __init__(self) -> None:
        self.config = Config()
        self.logger = Logger()
        self.viewbot = ViewBot()

    def start(self):
        # Prepare the console
        self.logger.print_logo()

        # Start the view bot
        self.viewbot.start()

if __name__ == "__main__":
    try:
        Tool = Main()
        Tool.start()
    except KeyboardInterrupt:
        exit(0)
    except Exception as e:
        logging.error(f"ERROR: {e}")