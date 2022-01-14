from dataclasses import dataclass


@dataclass
class CustomerDTO:
  first_name: str
  last_name: str
  phone_number: str
  genre: str
  cpf_cnpj: str