import pandas as pd
import logging


def process_data(df: pd.DataFrame) -> pd.DataFrame:
    logger=logging.getLogger(__name__)
    if df is None:
        logger.error("DataFrame vuoto — impossibile processare")
        return None

    df=df.drop_duplicates()
    df=df.dropna(how='all', axis=1)
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    logger.info(f'dimensione del Dataframe: {df.shape}')
    return df