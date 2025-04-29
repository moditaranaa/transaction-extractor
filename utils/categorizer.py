import json

def load_category_config(path='category_config.json'):
    with open(path, 'r') as f:
        return json.load(f)

def categorize_transactions(transactions):
    """
    Categorize based on config-driven vendor keywords.
    """
    config = load_category_config()
    categorized = []

    for txn in transactions:
        narration = txn['Narration'].lower()
        vendor = txn['Vendor'].lower()
        assigned = False

        for category, keywords in config.items():
            for keyword in keywords:
                if keyword.lower() in narration or keyword.lower() in vendor:
                    txn['Category'] = category
                    assigned = True
                    break
            if assigned:
                break

        if not assigned:
            txn['Category'] = "Miscellaneous"

        categorized.append(txn)

    return categorized