import pandas as pd
import extract

def process_fda_data(raw_records):

    if not raw_records:
        reports_df = pd.DataFrame()
        drugs_df = pd.DataFrame()
        reactions_df = pd.DataFrame()
        return reports_df, drugs_df, reactions_df
    
    df = pd.json_normalize(raw_records)

    #reports
    reports_df = df[['safetyreportid', 'receiptdate', 'patient.patientonsetage', 'patient.patientsex']].drop_duplicates(subset=['safetyreportid'])
    print(f"Shape of reports_df: {reports_df.shape}")

    #drugs
    print(f"Rows before explosion: {len(df)}")

    drug_exploded_df = df.explode('patient.drug')
    print(f"Rows post explosion: {len(df)}")

    drugs_df = drug_exploded_df[['safetyreportid', 'patient.drug']]
    print(f"Shape of drugs_df: {drugs_df.shape}")

    drug_list = drugs_df['patient.drug'].tolist()
    flat_drugs = pd.json_normalize(drug_list)
    flat_drugs['safetyreportid'] = drugs_df['safetyreportid'].values
    print(f"Drugs columns are: {flat_drugs.columns.tolist()}")

    #reactions

    reaction_exploded_df = df.explode('patient.reaction')
    reactions_df = reaction_exploded_df[['safetyreportid', 'patient.reaction']]
    print(f"Shape of reactions_df: {reactions_df.shape}")

    reaction_list = reactions_df['patient.reaction'].tolist()
    flat_reactions = pd.json_normalize(reaction_list)
    flat_reactions['safetyreportid'] = reactions_df['safetyreportid'].values
    print(f"Reactions columns are: {flat_reactions.columns.tolist()}")

    return reports_df, flat_drugs, flat_reactions

if __name__ == "__main__":
    process_data = extract.fetch_fda_data(5)

    reports, drugs, reactions = process_fda_data(test_data)

    if reports is not None:
        print(f"Success! Reports: {reports.shape}, Drugs: {drugs.shape}, Reactions: {reactions.shape}")