# Script che scarica dati da un URL pubblico, li pulisce, 
# li salva in CSV e genera un report HTML.
# Uso: python main.py --url "https://..." --output "report.html"
# Per aiuto: python main.py --help

import argparse
import logging
from src.fetcher import fetch_data
from src.processor import process_data
from src.reporter import generate_report

parser = argparse.ArgumentParser(prog='datareporttool',
                                 description='Download data from an URL', epilog='Thank you for choose us!')
parser.add_argument('--url', required=True, help='URL da cui scaricare i dati')
parser.add_argument('--output', default='report.html', help='Nome file HTML di output')
args = parser.parse_args()


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)

# 1. già fatto — args.url e args.output

# 2. scarica
df = fetch_data(args.url)

# 3. pulisci
df = process_data(df)

# 4. genera report
generate_report(df, args.output)

logger = logging.getLogger(__name__)
logger.info("Download iniziato")
logger.error("URL non valido")
logger.warning("Dati mancanti in alcune colonne")

logger.info(f"Script avviato — URL: {args.url} — Output: {args.output}")
