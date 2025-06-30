import pandas as pd

def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    def invalid(ip):
        parts = ip.split('.')
        return (
            len(parts) != 4 or
            any(not p.isdigit() or int(p) > 255 or (len(p) > 1 and p[0] == '0') for p in parts)
        )

    logs = logs.copy()
    logs['invalid'] = logs['ip'].apply(invalid)

    result = (
        logs[logs['invalid']]
        .groupby('ip')
        .size()
        .reset_index(name='invalid_count')
        .sort_values(['invalid_count', 'ip'], ascending=[False, False])
    )

    return result
