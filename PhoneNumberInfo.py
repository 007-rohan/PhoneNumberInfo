import phonenumbers
from phonenumbers import timezone, geocoder, carrier
number = input("Enter your Phone Number starting from + : ")
phone_number = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone_number)
carr = carrier.name_for_number(phone_number, "en")
reg = geocoder.description_for_number(phone_number, "en")
print(phone_number)
print(time)
print(carr)
print(reg)