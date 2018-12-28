import pandas as pd

def sexTransformer(sex):
    switcher = {
        "Male": "M",
        "Female": "F",
        1: "M",
        2: "F"
    }
    return switcher.get(sex, "U")

# Transform the data to meet a standard schema
def transformMedicalData(df):
    #TODO, how can all of these happen in a single operation?
    df = df["gender"].apply(sexTransformer)
    df["full_name"] = df["first_name"].map(str).str.title() + df1["last_name"].str.title()
    df['date_of_birth'] = df['date_of_birth'].dt.strftime('%Y-%m-%d')
    df['incurred_date'] = df['incurred_date'].dt.strftime('%Y-%m-%d')
    df['allowed_amount'] = pd.to_numeric(df["allowed_amount"])
    df['net_paid'] = pd.to_numeric(df["net_paid"])
	return df

def mergeMetadata(df, metadata):
    # merge the two tables
	return mergedData