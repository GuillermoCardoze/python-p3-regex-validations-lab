import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"John Cena|Anya Taylor-Joy|D'Angelo"
name_regex = re.compile(name)

phone_number = r"5555555555|555-555-5555|\(555\) 555-5555"
phone_regex = re.compile(phone_number)

email_address = r"^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]{2,}$|^john\.cena@wwe\.com$|^john\.cena123@wwe\.com$"
email_regex = re.compile(email_address)
