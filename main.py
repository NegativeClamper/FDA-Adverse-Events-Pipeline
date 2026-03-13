import extract
import transform
import load

def run_pipeline():
    print("Starting FDA Adversse Events Pipeline...")

    print("Extracting...")
    raw_data = extract.fetch_fda_data(999)

    print("Transforming... ")
    reports, drugs, reactions = transform.process_fda_data(raw_data)

    print("loading data into postgreSQL cloud...")
    load.load_to_postgres(reports, drugs, reactions)

    print("Pipeline executed successfully, data pushed to PostgreSQL cloud.")


if __name__ == "__main__":
    run_pipeline()