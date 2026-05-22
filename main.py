from fastapi import FastAPI
from pydantic import BaseModel, validator, Field


app =FastAPI()

class Item(BaseModel):
    name: str = Field(..., min_length=3)
    price: float = Field(..., ge=0)
    description: str = None
    tax: float = Field(0.0, ge=0)

    @validator('tax')
    def validate_tax(cls, v):
        if v is not None and v<0:
            raise ValueError('Tax cannot be negative')
        return v

@app.post("/items/")
async def create_item(item: Item):
    return{
        "name": item.name,
        "price": item.price

    }