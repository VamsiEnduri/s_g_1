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



@fastapi_obj.post("/login")
def login_validation(login_cred_details:dict):
    print(login_cred_details)

    incoming_login_email=login_cred_details["email"]
    incoming_login_password=login_cred_details["password"]
    incoming_login_role=login_cred_details["role"]

    response = supabase_obj.table("users") \
    .select("name,email,role") \
    .eq("email", incoming_login_email) \
    .eq("password", incoming_login_password) \
    .eq("role", incoming_login_role) \
    .execute()

    print(response.data,"res from supabase after login")

    if len(response.data) == 0:
        return {
            "msg":"invalid credentials"
        }

    return {
        "msg":"login successful",
        "status":True,
        "loggedIn_user":response.data[0]
    }



@fastapi_obj.post("/register")
def user_registration(new_user:dict): # type annotation
    print("reg function")
    print(new_user)
    res=supabase_obj.table("users").insert(new_user).execute()

    return{
        "msg":"reg done successfully",
        "data":res.data
    }

# how to start be server ?

# uvicorn main:fastapi_obj --reload


# select *
# from users
# where email ="" and password="" and role=""