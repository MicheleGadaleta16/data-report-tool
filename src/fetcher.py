import pandas as pd
import requests
import logging
from io import StringIO

def fetch_data(url: str) -> pd.DataFrame:
    """
    Scarica un CSV da un URL e lo ritorna come DataFrame.
    
    :param url: URL del file CSV
    :return: DataFrame con i dati scaricati
    """
    logger = logging.getLogger(__name__)
    
    
    try:
        r = requests.get(url)
        r.raise_for_status()  # lancia eccezione se status != 200
        df = pd.read_csv(StringIO(r.text))
        logger.info(f"Scaricate {len(df)} righe da {url}")
        return df
    except Exception as e:
        logger.error(f"Errore durante il download: {e}")
    
        return None
