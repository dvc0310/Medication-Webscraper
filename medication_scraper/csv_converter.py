import pandas as pd

read_file = pd.read_csv (r'medication_scraper\drug_ratings.txt', delimiter='|')
read_file.to_csv(r"medication_scraper\meds.csv")

