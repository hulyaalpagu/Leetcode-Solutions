import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    filtered = animals[animals['weight'] > 100]
    return filtered.sort_values(by='weight', ascending=False)[['name']]




