# Multi-Inheritance

class Contact:
    all_contacts = [ ]

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def displayContacts(self):
        for c in Contact.all_contacts:
            print('name: ', c.name, '\temail: ', c.email)

class MailSender:
    def send_mail(self, message):
        print('Sendng email to {0:18s}: {1:35s}'.format(self.email, message))
    
    def emailBlast(self, message):
        for c in Contact.all_contacts:
            c.send_mail(message)

class EmailableContact(Contact, MailSender):
    pass

print(EmailableContact('John Smith', 'jsmith@gmail.com'))
e4 = print(EmailableContact('Alex Ander', 'aander@gmail.com'))

print(e4.send_email('End of Fall Semester will be Dec 1.'))


# ------------------------------------------------------------------

# Polymorphism Code
# used when there are common method names. Needs to have 'common interface' (same name but different behaviors)
# 
