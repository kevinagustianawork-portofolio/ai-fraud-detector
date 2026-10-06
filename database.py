# database.py
from typing import List, Dict

def get_simulated_transactions() -> List[Dict]:
    return [
        # Skenario 1: Transaksi Normal
        {"tx_id": "TX1001", "merchant": "Google Cloud", "amount": 15000000,
         "date": "2026-10-01", "user_id": "USR_01",
         "description": "Monthly server subscription"},

        # Skenario 2: Indikasi Split Invoicing
        {"tx_id": "TX1002", "merchant": "Vendor_X", "amount": 19500000,
         "date": "2026-10-02 09:00", "user_id": "USR_02",
         "description": "Office renovation phase 1"},
        {"tx_id": "TX1003", "merchant": "Vendor_X", "amount": 19500000,
         "date": "2026-10-02 09:05", "user_id": "USR_02",
         "description": "Office renovation phase 2"},
        {"tx_id": "TX1004", "merchant": "Vendor_X", "amount": 19000000,
         "date": "2026-10-02 09:10", "user_id": "USR_02",
         "description": "Office renovation phase 3"},

        # Skenario 3: Indikasi Cash Swiping
        {"tx_id": "TX1005", "merchant": "ATM_JKT_01", "amount": 2000000,
         "date": "2026-10-03 14:00", "user_id": "USR_03",
         "description": "Cash withdrawal"},
        {"tx_id": "TX1006", "merchant": "ATM_JKT_01", "amount": 2000000,
         "date": "2026-10-03 14:02", "user_id": "USR_03",
         "description": "Cash withdrawal"},
        {"tx_id": "TX1007", "merchant": "ATM_JKT_01", "amount": 2000000,
         "date": "2026-10-03 14:05", "user_id": "USR_03",
         "description": "Cash withdrawal"},
    ]
