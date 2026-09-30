# uvicorn
# fastapi

SUPABASE_URL="https://nbqplffymgdlfmzokmzi.supabase.co"
SUPABASE_KEY="sb_publishable_sHGG099DttuTDX7S9qWB7Q_cfsw85Yx"

# pip install supabase
# pip install uvicorn fastapi
# python -m pip install uvicorn fastapi
# py -m pip install uvicorn fastapi

from fastapi import FastAPI # importing FastAPI class
from supabase import create_client
fastapi_obj=FastAPI() # creating fastapi object
supabase_obj=create_client(SUPABASE_URL,SUPABASE_KEY)

@fastapi_obj.post("/register")
def user_registration(new_user:dict):
    print("reg function")
    print(new_user)
    res=supabase_obj.table("users").insert(new_user).execute()

    return{
        "msg":"reg done successfully",
        "data":res.data
    }

# how to start be server ?

# uvicorn main:fastapi_obj --reload