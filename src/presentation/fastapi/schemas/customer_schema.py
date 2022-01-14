from pydantic import BaseModel


class CreateCustomerSchema(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    genre: str
    cpf_cnpj: str
