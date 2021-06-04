import phonenumbers
from phonenumbers import timezone, geocoder, carrier

phoneNumber = phonenumbers.parse("+624115085555") #this is only a random number from Indonesia, you need to change the phonenumbers.parse to use it

timeZone = timezone.time_zones_for_number(phoneNumber)

Carrier = carrier.name_for_number(phoneNumber, 'en')

Region = geocoder.description_for_number(phoneNumber, 'en')

print(phoneNumber)
print(timeZone)
print(Carrier)
print(Region)