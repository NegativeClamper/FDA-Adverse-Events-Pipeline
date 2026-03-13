# 🧬 OpenFDA Pharmacovigilance ETL Pipeline



## 📌 Architecture Overview
An automated, Python-based Extract, Transform, Load (ETL) pipeline that ingests live pharmacovigilance data (adverse drug events) from the US government's OpenFDA REST API. The pipeline resolves the NoSQL-to-SQL impedance mismatch by dynamically flattening deeply nested JSON payloads and loading them into a relational cloud PostgreSQL data warehouse for downstream BI analytics.

## 🛠️ The Tech Stack
* **Language:** Python 3.x
* **Extraction:** `requests` (REST API integration, pagination handling)
* **Transformation:** `pandas` (JSON normalization, Cartesian explosion prevention)
* **Storage Engine:** PostgreSQL (Cloud-hosted via Neon)
* **ORM / Database Driver:** `SQLAlchemy`

## 🏗️ The Engineering Challenge: Resolving Nested JSON
The OpenFDA API delivers patient data as complex 3D JSON documents (e.g., a single patient record contains arrays of multiple drugs and multiple medical reactions). Pushing this directly to a SQL database is impossible. 

This pipeline's Transformation engine isolates the data into three distinct relational branches:
1. **Adverse Reports (Core):** Deduplicates and normalizes patient demographics.
2. **Report Drugs (Dimension):** Explodes array-type fields and normalizes nested drug dictionaries to map multiple medications back to a single patient ID.
3. **Report Reactions (Dimension):** Explodes MedDRA (Medical Dictionary for Regulatory Activities) reaction terms without triggering a Cartesian product database crash.

## 🗄️ Relational Database Schema
The cleaned data is loaded into PostgreSQL using the following schema:
* `adverse_reports`: `safetyreportid` (PK), `receiptdate`, `patientsex`, `patientonsetage`
* `report_drugs`: `safetyreportid` (FK), `medicinalproduct`, `drugdosagetext`, `drugadministrationroute`
* `report_reactions`: `safetyreportid` (FK), `reactionmeddrapt`

## 🚀 How to Run Locally
1. Clone the repository and install dependencies:
   ```bash
   pip install -r requirements.txt