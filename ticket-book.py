print('''<--------- Book Your Ticket Here ---------->''')

total_count = 100
initial_total = total_count

def book_ticket():
    global total_count
    
    while True: 
        print(f"\nTotal tickets available: {total_count}")
        user = int(input("Enter No. of tickets to book --> "))
        
        if (user <= 0) or (user > total_count):  
            print("❌ Invalid ticket count. Try again!")
            continue   # ask again
        else:
            total_count -= user
            print(f"✅ Success! {user} tickets booked.")
            print(f"Remaining tickets: {total_count}")
            break 


def cancel_ticket(): 
    global total_count

    while True:
        print(f'Total Tickets Available {total_count}')
        user = int(input('Enter No. Tickets to cancel -->'))
    
        if user == 0 or user < 1 or user > 100:
            print('please Enter a valid Count')
            continue    
        else:
            total_count += user
            print(f"✅ Success! {user} tickets canclled.")
            print(f'Total Tickets Available {total_count}')
            break
    

def total_tickets_booked():
    global total_count

    booked = initial_total - total_count
    print(f'Total Tickets Book Till Now {booked}')



print('''
      1. Book Ticket
      2. Cancel Ticket
      3. Total Tickets Booked
      4. Exit
      ''')

while True:
    user  = int(input('Enter Your Choise here -->'))
    if user == 1:
      book_ticket()
    elif user == 2:
      cancel_ticket()
    elif user == 3:
        total_tickets_booked()
        break
    elif user == 4:
        print('Thanks For Using BookMySHow...!!😊')
        break
    else:
      print('Please Choose Valid Option')
      