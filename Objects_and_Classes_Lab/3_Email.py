# Create class Email. The __init__ method should receive sender, receiver and a content. 
# It should also have a default set to False attribute called is_sent. 
# The class should have two additional methods:
# •	send() - sets the is_sent attribute to True
# •	get_info() - returns the following string: "{sender} says to {receiver}: {content}. Sent: {is_sent}"
# You will receive some information (separated by a single space) until you receive the command "Stop". 
# The first element will be the sender, the second one – the receiver, and the third one – the content. 
# On the final line, you will be given the indices of the sent emails separated by comma and space ", ". 
# Call the send() method for the given indices of emails. For each email, call the get_info() method.

class Email:
    def __init__(self, sender, receiver, content) -> None:
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False
        
    def send(self):
        self.is_sent = True

    def get_info(self):
        print(f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}')

commands = []
emails_list = []

while True:
    input_data = input()
    if input_data == 'Stop':
        break
    else:
        email_data = input_data.split(' ')
        emails_list.append(Email(email_data[0],email_data[1],email_data[2]))

sent_indices = list(map(int, input().split(', ')))

for i, email in enumerate(emails_list):
    if i in sent_indices:
        email.send() 
    email.get_info()
