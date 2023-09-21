from mailing import Mailing
from address import Address

to_send = Address("197373", "Moscow", "Lenina", "123", "23")
from_send = Address("188888", "Pskov", "Petrova", "23", "78")

delivery = Mailing("123", "22222", to_send.address, from_send.address)

print(f"Отправление {delivery.cost} из {delivery.from_address()} в {delivery.to_address()}. Стоимость {delivery.cost} рублей.")


