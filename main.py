from fastapi import FastAPI
import pandas as pd
import numpy as np

app = FastAPI()

# setup database
companies = pd.read_json("company.json")
phoneNumbers = pd.read_json("phone.json")
addresses = pd.read_json("address.json")
phoneNumbers = phoneNumbers.drop('id', axis=1)
addresses = addresses.drop('id', axis=1)
companies = pd.merge(companies, phoneNumbers, left_on='id', right_on='company_id')
companies = companies.drop('company_id', axis=1)
companies = pd.merge(companies, addresses, left_on='id', right_on='company_id')
companies = companies.drop('company_id', axis=1)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/checkCompany/")
async def get_company(company_name: str, line1: str, phone_number: str, postal_code: str):
    df = companies
    fullMatch = df.loc[df['company_name'] == company_name].loc[df['line1'] == line1].loc[df['phone_number'] == phone_number].loc[df['postal_code'] == postal_code]
    if not fullMatch.empty:
        return {"fullMatch": fullMatch.to_dict(orient='records'), "partialMatches": None}
    partialMatches = []
    for var, val in vars().items():
        try:
            partialMatches.append(df.loc[df[var] == val].to_dict(orient='records'))
        except:
            continue
    return {"fullMatch": None, "partialMatches": partialMatches}