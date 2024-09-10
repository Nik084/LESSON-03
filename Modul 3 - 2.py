default = 'university.help@gmail.com'
sender_ = input('Нажмите "Enter" для выбора e-mail адреса отправителя по умолчанию или введите другой e-mail адрес: ')
recipient_ = input('Введите e-mail адрес получателя: ')
message_ = input('Наберите текст сообщения: ')
def send_email(message, recipient,*, sender=default):
    domen = ['.com', '.ru', '.net']
    if sender_ == '':
        sender = default
    if '@' in sender and '@' in recipient:
        if sender[sender.rfind('.'):] in domen and recipient[recipient.rfind('.'):] in domen:
            if recipient == sender:
                print ('Нельзя отправить письмо самому себе!')
            else:
                if sender == default:
                    print (f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
                else:
                    print (f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    else:
        print (f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
send_email(message_, recipient_, sender=sender_)
