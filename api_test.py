import requests
import json
import pandas as pd

url = "https://api.fda.gov/drug/event.json?limit=5"

response = requests.get(url)

print(response.status_code)

data = response.json()
all_keys = data.keys()

reports = data['results']
#print(reports[0].keys())

df = pd.json_normalize(reports)
#print(df.columns.tolist())
print(f"Rows before explosion: {len(df)}")

df = df.explode('patient.drug')
print(f"Rows post explosion: {len(df)}")

reports_df = df[['safetyreportid', 'receiptdate', 'patient.patientonsetage', 'patient.patientsex']].drop_duplicates(subset=['safetyreportid'])
drugs_df = df[['safetyreportid', 'patient.drug']]

print(f"Shape of reports_df: {reports_df.shape}")
print(f"Shape of drugs_df: {drugs_df.shape}")

drug_list = drugs_df['patient.drug'].tolist()
flat_drugs = pd.json_normalize(drug_list) 
flat_drugs['safetyreportid'] = drugs_df['safetyreportid'].values

print(flat_drugs.columns.tolist())