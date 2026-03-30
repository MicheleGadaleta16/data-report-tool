from jinja2 import Environment, FileSystemLoader
import logging
import pandas as pd

def generate_report(df: pd.DataFrame, output_path: str) -> None:
    logger = logging.getLogger(__name__)
    
    # carica i template dalla cartella templates/
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report.html')
    
    # prepara i dati da passare al template
    html = template.render(
        total_rows=len(df),
        total_cols=len(df.columns),
        table=df.to_html(classes='table', border=0)
    )
    
    # salva il file HTML
    with open(output_path, 'w') as f:
        f.write(html)
    
    logger.info(f"Report generato: {output_path}")