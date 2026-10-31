from Address import Address
from Mailing import Mailing

address_to = Address(180245, 'Moscow', 'Street', 14, 55)
address_from = Address(1802421, 'Saint-Petersberg', 'Street01', 41, 155)

mailing_1 = Mailing(Mailing_To_Address = address_to, Mailing_From_Address = address_from, 
                    Mailing_Cost = 1250.12, Mailing_Track = '28363486b386b38096b73456y')

print(f"Отправление {mailing_1.mailing_track} из {mailing_1.from_address} в {mailing_1.to_address}. Стоимость {mailing_1.mailing_cost} рублей")