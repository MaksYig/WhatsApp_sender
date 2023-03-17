import pywhatkit
import json
import os
import sys





def main_sender():
    file_path = "contacts.json"
    print('Hello welcome to Sender.')
    type_send = int(input("If you want to send message now, press (1)\nIf you want send message later, press (2)\nIf you want to add new contact, press (3)\nIf you want delete contact, press (4)\n"))
    # Check if contact file exist:
    if not os.path.isfile(file_path):
        with open(file_path, "w") as f:
            json.dump({"contacts":[]}, f)
    # Opening JSON file
    f = open('contacts.json')
    contacts = json.load(f)
    if type_send == 1:
        if os.path.isfile(file_path) and len(contacts['contacts']) > 0:
            print("Choose to whom you want send message...")
            for (i, item) in enumerate(contacts['contacts']):
                print(f" For {item['name']}, press ({i+1})")
            send_to = int(input('Choose:'))
            receiver = contacts['contacts'][send_to-1]['phone']
            message = input("Your message:")
            pywhatkit.sendwhatmsg_instantly(phone_no=receiver, message=message)
            print('Choose your next steps:')
            res = int(input("Send another message, press (1)\nExit script, press (2)\n"))
            if res == 1:
                main_sender()
            if res == 2:
                sys.exit()
            else:
                print("Wrong choise, try again.")
                print('Choose your next steps:')
                res = int(input("\nSend another message, press (1)\nExit script, press (2)"))
        else:
            print('You don have any contacts. You need to add some.')
            cont = int(input('If you want to add contact, press (1)\n'))
            if cont == 1:
                print("Add new contact...")
                name = input('Enter contact name:')
                phone = input('Enter contact phone number (with (+) country code):')
                # Load the JSON data from the file into a Python variable
                with open("contacts.json", "r") as f:
                    data_from_json = json.load(f)
                data = {
                    "name": name,
                    "phone": phone,
                }
                data_from_json['contacts'].append(data)
                # Convert the Python object back to JSON format
                json_data = json.dumps(data_from_json, indent=4)
                # Write the updated JSON data back to the file
                with open("contacts.json", "w") as f:
                    f.write(json_data)
                print(f"Thank you. Your contact {name} with number {phone}, was added to contacts")
                main_sender()
            else:
                print('Wrong chose. Thank you!')
                sys.exit()

    if type_send == 2:
        print("Choose to whom you want send message...")
        for (i, item) in enumerate(contacts['contacts']):
            print(f" For {item['name']}, press ({i+1})")
        send_to = int(input('Choose:'))
        receiver = contacts['contacts'][send_to-1]['phone']
        hour = int(input("Enter Hour when to send:"))
        minutes = int(input("Input minutes, when to send:"))
        message = input("Your message:")
        pywhatkit.sendwhatmsg(phone_no=receiver, message=message, time_hour=hour, time_min=minutes)
        print('Choose your next steps:')
        res = int(input("Send another message, press (1)\nExit script, press (2)\n"))
        if res == 1:
            main_sender()
        if res == 2:
            sys.exit()
        else:
            print("Wrong choise, try again.")
            print('Choose your next steps:')
            res = int(input("\nSend another message, press (1)\nExit script, press (2)"))
    if type_send == 3:
        print("Add new contact...")
        name = input('Enter contact name:')
        phone = input('Enter contact phone number (with (+) country code):')
        # Load the JSON data from the file into a Python variable
        with open("contacts.json", "r") as f:
            data_from_json = json.load(f)
        data = {
            "name": name,
            "phone": phone,
        }
        data_from_json['contacts'].append(data)
        # Convert the Python object back to JSON format
        json_data = json.dumps(data_from_json, indent=4)
        # Write the updated JSON data back to the file
        with open("contacts.json", "w") as f:
            f.write(json_data)
        print(f"Thank you. Your contact {name} with number {phone}, was added to contacts")
        main_sender()
    if type_send == 4:
        print("Choose a contact to delete...")
        for (i, item) in enumerate(contacts['contacts']):
            print(f" For {item['name']}, press ({i+1})")
        send_to = int(input('Choose:'))
        contact = contacts['contacts'][send_to-1]
        # Open the JSON file and load the array
        with open("contacts.json", "r") as f:
            data = json.load(f)
        # Find the index of the object you want to delete
        index_to_delete = -1
        for i, obj in enumerate(data["contacts"]):
            if obj["phone"] == contact['phone']:
                index_to_delete = i
                break
        # If the object was found, remove it from the array
        if index_to_delete != -1:
            data["contacts"].pop(index_to_delete)
        # Save the modified array back to the JSON file
        with open("contacts.json", "w") as f:
            json.dump(data, f, indent=4)

        print('Choose your next steps:')
        res = int(input("Send another message, press (1)\nExit script, press (2)\n"))
        if res == 1:
            main_sender()
        if res == 2:
            sys.exit()
        else:
            print("Wrong choise, try again.")
            print('Choose your next steps:')
            res = int(input("\nSend another message, press (1)\nExit script, press (2)"))

def main():
    main_sender()

if __name__ == '__main__':
    main()