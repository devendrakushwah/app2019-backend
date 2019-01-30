from datetime import datetime

def timestamp_to_date(timestamp):
    ts = int(timestamp)
    return str((datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')))