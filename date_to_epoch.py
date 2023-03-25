from datetime import datetime

def date_to_epoch(date: str, ) -> int:
    """Convert python str (yyyy-mm-dd) to epoch"""
    print(dir(date))
    date = datetime.strptime(date, "%Y-%m-%d")
    return date.strftime("%s")
