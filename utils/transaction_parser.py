import re

def extract_transactions(text):
    """
    Extracts transactions from text based on date, amount, and Dr/Cr pattern.
    """
    lines = text.split('\n')
    transactions = []

    pattern = re.compile(
        r'(?P<date>\d{2}-\d{2}-\d{2})\s+'
        r'(?P<vendor>.+?)\s+'
        r'(?P<amount>\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?)\s+'
        r'(?P<type>Dr\.|Cr\.)',
        re.IGNORECASE
    )

    for line in lines:
        match = pattern.search(line)
        if match:
            date = match.group("date").strip()
            vendor = match.group("vendor").strip()
            amount = float(match.group("amount").replace(",", ""))
            txn_type = "Credit" if match.group("type").lower() == "cr." else "Debit"

            transactions.append({
                'Date': date,
                'Vendor': vendor,
                'Amount': amount,
                'Type': txn_type,
                'Narration': line.strip()
            })

    return transactions