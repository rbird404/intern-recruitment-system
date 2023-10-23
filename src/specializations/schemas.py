from pydantic import BaseModel, ConfigDict


class SpecializationBase(BaseModel):
    name: str
    description: str | None = None


class SpecializationCreate(SpecializationBase):
    ...


class SpecializationRead(SpecializationBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
