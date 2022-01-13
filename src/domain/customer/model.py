from typing import List

from src.domain.address.model import Address


class Customer:
    def __init__(self, first_name, last_name, phone_number, genre, cpf_cnpj):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.genre = genre
        self.cpf_cnpj = cpf_cnpj
        self.addresses: List[Address] = []

    def add_address(self, address: Address):
        if address.primary == True:
            others_primary = list(filter(lambda ad: ad.primary == True, self.addresses))
            if others_primary:
                others_primary[0].primary == False
        self.addresses.append(address)




