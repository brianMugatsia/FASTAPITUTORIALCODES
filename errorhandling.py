from fastapi import FastAPI,HTTPException
app= FastAPI()
items= {"1": {"name": "Item1", "price": 10}}
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="item not found"
        )
    
    return items[item_id]