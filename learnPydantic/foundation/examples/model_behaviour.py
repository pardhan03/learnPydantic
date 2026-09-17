from pydantic import BaseModel, field_validator, model_validator, computed_field

class User(BaseModel):
    username: str

    @field_validator('username')
    def username_legth(cls, value):
        if value < 4:
            raise ValueError("User name lenght must be more that 4 character")
        return value