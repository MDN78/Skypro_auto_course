from mailing import Mailing

to_send = Mailing("197373", "Moscow", "Lenina", "123", "23")
from_send = Mailing("188888", "Pskov", "Petrova", "23", "78")

print(f"Отправление {Mailing.track('1')} из {from_send.to_address()} в {to_send.from_address()}. Стоимость {Mailing.cost(23500)} рублей")


