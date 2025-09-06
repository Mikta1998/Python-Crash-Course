
sent_messages = ["Hello.", "How are you?", "What's your name?"]
arrived_messages = []


def send_messages(sent, arrived):
    while sent:
        sending_message = sent.pop()
        print("\nSending the following message:")
        print(sending_message)
        arrived.append(sending_message)



def show_messages(arrived):
    print(f"\nArrived messages:")
    for message in arrived:
        print(f"{message}")


send_messages(sent_messages[:], arrived_messages)
show_messages(arrived_messages)
print(sent_messages)