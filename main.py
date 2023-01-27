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
async def get_company(company_name: str, address_line1: str, phone_number: str, zip: str):
    df = companies
    df = df.loc[df['company_name'] == company_name].loc[df['line1'] == address_line1].loc[df['phone_number'] == phone_number].loc[df['postal_code'] == zip]
    return df.to_json(orient = 'records')