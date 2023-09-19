from smartphone import Smartphone

samsung = Smartphone("Samsung", "A30", "+79992345567")
apple = Smartphone("Apple", "iPhone 12", "+79214443535")
huawei = Smartphone("Huawei", "Select", "+79821234567")
xiaomi = Smartphone("Xiaomi", "E320", "+79372433524")
aurora = Smartphone("Aurora", "A1", "+79632234345")

catalog = [samsung, apple, huawei, xiaomi, aurora]

for i in catalog:
    print(i.show_device())