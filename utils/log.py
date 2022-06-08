# Flexible event logging system
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Logging setting and creation of log file
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=BASE_DIR / 'backend.log',
                    )

logging.info("Log are activated.")