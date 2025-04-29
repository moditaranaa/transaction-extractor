import os
from utils.pdf_reader import extract_text_from_pdf
from utils.transaction_parser import extract_transactions
from utils.categorizer import categorize_transactions
from utils.summary_generator import generate_summary

def main():
    print("Started transaction extraction automation...")

    pdf_path = input("Enter path to transaction PDF file: ").strip()

    if not os.path.exists(pdf_path):
        raise FileNotFoundError("The specified PDF file does not exist.")

    print("Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)

    print("Parsing transactions...")
    transactions = extract_transactions(text)

    if not transactions:
        print("Warning: No valid transactions detected in the input.")
        return

    print("Categorizing transactions...")
    categorized_transactions = categorize_transactions(transactions)

    print("Generating final report...")
    generate_summary(categorized_transactions)

    print("All tasks completed successfully.")

if __name__ == "__main__":
    main()