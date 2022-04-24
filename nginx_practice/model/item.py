from pydantic import BaseModel, validator

from common_lib.errors import CustomValidationError


class Item(BaseModel):
    name: str
    price: float
    description: str | None = None
    tax: float | None = None
    tags: list = []

    @classmethod
    @validator("name")
    def validate_name(cls, v: str):
        if not v.isalpha():
            raise CustomValidationError("name must be character")
        return v
