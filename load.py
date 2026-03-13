import os
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def load_to_postgres(reports_df, drugs_df, reactions_df):

    db_url = os.getenv("DATABASE_url")
    engine = create_engine(db_url)
    try:
        reports_df.to_sql(name= "adverse_reports", con= engine, if_exists= 'replace', index= False)
        drugs_df.to_sql(name= "report_drugs", con= engine, if_exists= 'replace', index= False)
        reactions_df.to_sql(name= "report_reactions", con= engine, if_exists= 'replace', index= False)
    except SQLAlchemyError as e:
        print(f"connection error with db {e}")


