from pprint import pprint
import re
import csv
# читаем адресную книгу в формате CSV в список contacts_list
telephon = r"(8|\+7)?\s*(\(*)(\d{3})(\)*)(\s*|\-)(\d{3})(\s*|-)(\d{2})(\s*|-)(\d{2})\s*(\(*)(\w\w\w\.)*\s*(\d{4})*(\))*"
sub_telephon = r"+7(\3)\6-\8-\10 \12\13"



def read_phonebook_raw():
    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def get_new_phonebook(contacts_list):
    new_phonebook = list()
    for contact in contacts_list:
        new_contact = list()
        patter = r"\w+"
        full_name_str = ",".join(contact[:3])
        result_contact = re.findall(patter, full_name_str)
        while len(result_contact) < 3:
            result_contact.append('')
        new_contact += result_contact
        new_contact.append(contact[3])
        new_contact.append(contact[4])
        patern_telephon = re.compile(telephon)
        new_telephon = patern_telephon.sub(sub_telephon, contact[5])
        new_contact.append(new_telephon)
        new_contact.append(contact[6])
        new_phonebook.append(new_contact)
    # pprint(new_phonebook)
    return new_phonebook


def defcontact_comparison(new_phonebook):
    phone_book = dict()
    for contact in new_phonebook:
        # pprint(contact)
        if contact[0] in phone_book:
            print(contact[0])
            contact_value = phone_book[contact[0]]
            for i in range(len(contact_value)):
                if contact[i]:
                    contact_value[i] = contact[i]
        else:
            phone_book[contact[0]] = contact
    # pprint(phone_book)
    return list(phone_book.values())


def write_new_phonebook(new_phonebook):
    with open("phonebook5.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(new_phonebook)


if __name__ == '__main__':
#     # read_phonebook_raw()
#     # get_new_phonebook(read_phonebook_raw())
#     # defcontact_comparison(get_new_phonebook(read_phonebook_raw()))
    write_new_phonebook(defcontact_comparison(get_new_phonebook(read_phonebook_raw())))
#     # get_new_phonebook(new_contact)
#     # delete_duplicates_contact(new_phonebook)