from fastapi import FastAPI
import asyncio
app= FastAPI()
async def fetch_user_data(user_id: int):
    await asyncio.sleep(1) #Simulating anexternalAPIcallordatabasequery
    return {"user_id":user_id, "name": "JohnDoe"}
async def fetch_transaction_history(user_id: int):
    await asyncio.sleep(2) #Simulating anotherexternalAPIcall
    return {"user_id":user_id, "transactions":["purchase1", "purchase2"]}
@app.get("/user/{user_id}")
async def get_user_info(user_id: int):
    user_data = await fetch_user_data(user_id)
    transaction_data = await fetch_transaction_history(user_id)
    return {**user_data,**transaction_data}