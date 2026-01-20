import pandas as pd
import glob
import os

INPUT_ROOT = ""
OUTPUT_ROOT = "data_csv_converted"

os.makedirs(OUTPUT_ROOT, exist_ok=True)

folders = [
    "api_data_aadhar_enrolment",
    "api_data_aadhar_demographic",
    "api_data_aadhar_biometric"
]

for folder in folders:
    input_path = os.path.join(INPUT_ROOT, folder)
    output_path = os.path.join(OUTPUT_ROOT, folder)
    os.makedirs(output_path, exist_ok=True)

    excel_files = glob.glob(os.path.join(input_path, "*.xlsx"))

    for file in excel_files:
        df = pd.read_excel(file)
        name = os.path.splitext(os.path.basename(file))[0]
        csv_file = os.path.join(output_path, f"{name}.csv")
        df.to_csv(csv_file, index=False)
        print(f"Converted: {file}")

print("✅ All Excel files converted to CSV")
