tickets = []

completed_history = []

counters = [None, None]

next_ticket_number = 1

priority_streak = 0

def issue_ticket(purpose, service_type="regular"):

    global next_ticket_number

    valid_purposes = ["Enrollment", "Records", "Payment"]

    valid_types = ["regular", "priority"]

    if purpose not in valid_purposes:

        raise ValueError("Invalid purpose. Choose Enrollment, Records, or Payment.")

    if service_type not in valid_types:

        raise ValueError("Invalid service type. Choose regular or priority.")

    ticket = {

        "number": next_ticket_number,

        "purpose": purpose,

        "service_type": service_type,

        "status": "waiting"

    }

    tickets.append(ticket)

    number = next_ticket_number

    next_ticket_number += 1

    return number

def issue_many(*requests):

    valid_purposes = ["Enrollment", "Records", "Payment"]

    valid_types = ["regular", "priority"]

    validated = []

    for request in requests:

        if not isinstance(request, (tuple, list)) or len(request) != 2:

            raise ValueError("Each request must be (purpose, service_type).")

        purpose, service_type = request

        if purpose not in valid_purposes:

            raise ValueError("Invalid purpose: " + str(purpose))

        if service_type not in valid_types:

            raise ValueError("Invalid service type: " + str(service_type))

        validated.append((purpose, service_type))

    issued_numbers = []

    for purpose, service_type in validated:

        issued_numbers.append(issue_ticket(purpose, service_type))

    return issued_numbers

def active_ticket_numbers():

    return {number for number in counters if number is not None}

class WaitingTicketIterator:

    def __init__(self, ticket_list, active_numbers=None):

        self.ticket_list = ticket_list

        self.active_numbers = set(active_numbers or [])

        self.position = 0

    def __iter__(self):

        return self

    def __next__(self):

        while self.position < len(self.ticket_list):

            ticket = self.ticket_list[self.position]

            self.position += 1

            if (

                ticket["status"] == "waiting"

                and ticket["number"] not in self.active_numbers

            ):

                return ticket

        raise StopIteration

def waiting_snapshot(waiting, active_numbers=None):

    active_numbers = set(active_numbers or [])

    return list(

        WaitingTicketIterator(waiting, active_numbers)

    )

def next_ticket(waiting, priority_streak):

    active_numbers = active_ticket_numbers()

    iterator = WaitingTicketIterator(

        waiting,

        active_numbers

    )

    waiting_tickets = list(iterator)

    if priority_streak >= 2:

        for ticket in waiting_tickets:

            if ticket["service_type"] == "regular":

                return ticket

    for ticket in waiting_tickets:

        if ticket["service_type"] == "priority":

            return ticket

    if waiting_tickets:

        return waiting_tickets[0]

    return None

def call_next_ticket():

    global priority_streak

    free_counter = None

    for index in range(len(counters)):

        if counters[index] is None:

            free_counter = index

            break

    if free_counter is None:

        return None, "Both counters are busy."

    selected = next_ticket(

        tickets,

        priority_streak

    )

    if selected is None:

        return None, "No waiting tickets."

    counters[free_counter] = selected["number"]

    if selected["service_type"] == "priority":

        priority_streak += 1

    else:

        priority_streak = 0

    return (

        selected,

        "Ticket called to Counter " +

        str(free_counter + 1) + "."

    )

def complete_counter(counter_number):

    if counter_number not in (1, 2):

        return False, "Counter number must be 1 or 2."

    index = counter_number - 1

    ticket_number = counters[index]

    if ticket_number is None:

        return False, "That counter is already free."

    for ticket in tickets:

        if ticket["number"] == ticket_number:

            ticket["status"] = "served"

            completed_history.append(

                ticket.copy()

            )

            counters[index] = None

            return (

                True,

                "Ticket " +

                str(ticket_number) +

                " completed."

            )

    return False, "Ticket could not be found."

def complete_ticket(ticket_number):

    for index in range(len(counters)):

        if counters[index] == ticket_number:

            return complete_counter(index + 1)

    for ticket in tickets:

        if ticket["number"] == ticket_number:

            if ticket["status"] == "served":

                return False, "Ticket was already completed."

            if ticket["status"] == "cancelled":

                return False, "Ticket was cancelled."

            return (

                False,

                "Ticket is not currently assigned to a counter."

            )

    return False, "Ticket does not exist."

def cancel_ticket(ticket_number):

    if ticket_number in active_ticket_numbers():

        return (

            False,

            "Ticket is currently being served and cannot be cancelled."

        )

    for ticket in tickets:

        if ticket["number"] == ticket_number:

            if ticket["status"] != "waiting":

                return (

                    False,

                    "Ticket is not waiting and cannot be cancelled."

                )

            ticket["status"] = "cancelled"

            return (

                True,

                "Ticket " +

                str(ticket_number) +

                " cancelled."

            )

    return False, "Ticket does not exist."

def waiting_tickets():

    return waiting_snapshot(

        tickets,

        active_ticket_numbers()

    )

def estimated_position(ticket_number):

    original = None

    for ticket in tickets:

        if ticket["number"] == ticket_number:

            original = ticket

            break

    if original is None:

        return None

    if (

        original["status"] != "waiting"

        or ticket_number in active_ticket_numbers()

    ):

        return 0

    simulation = []

    for ticket in tickets:

        simulation.append(ticket.copy())

    simulated_active = active_ticket_numbers()

    simulated_streak = priority_streak

    calls_until_ticket = 0

    while True:

        candidates = []

        for ticket in simulation:

            if (

                ticket["status"] == "waiting"

                and ticket["number"] not in simulated_active

            ):

                candidates.append(ticket)

        if not candidates:

            return None

        selected = None

        if simulated_streak >= 2:

            for ticket in candidates:

                if ticket["service_type"] == "regular":

                    selected = ticket

                    break

        if selected is None:

            for ticket in candidates:

                if ticket["service_type"] == "priority":

                    selected = ticket

                    break

        if selected is None:

            selected = candidates[0]

        calls_until_ticket += 1

        if selected["number"] == ticket_number:

            return calls_until_ticket

        simulated_active.add(

            selected["number"]

        )

        if selected["service_type"] == "priority":

            simulated_streak += 1

        else:

            simulated_streak = 0

def report(**kwargs):

    counts = {

        "waiting": len(waiting_tickets()),

        "served": sum(

            1

            for ticket in tickets

            if ticket["status"] == "served"

        ),

        "cancelled": sum(

            1

            for ticket in tickets

            if ticket["status"] == "cancelled"

        ),

        "free_counters": sum(

            1

            for counter in counters

            if counter is None

        )

    }

    for key, value in counts.items():

        if kwargs.get(key, True):

            print(

                key.replace("_", " ").title()

                + ":"

                ,

                value

            )

def show_waiting():

    current = waiting_tickets()

    print("\nWaiting Tickets")

    if not current:

        print("No waiting tickets.")

        return

    for index in range(len(current)):

        ticket = current[index]

        position = estimated_position(

            ticket["number"]

        )

        print(

            str(index + 1)

            + ". Ticket "

            + str(ticket["number"])

            + " | "

            + ticket["purpose"]

            + " | "

            + ticket["service_type"]

            + " | estimated call position: "

            + str(position)

        )

def show_status():

    print("\nCounter Status")

    for index in range(len(counters)):

        if counters[index] is None:

            print(

                "Counter "

                + str(index + 1)

                + ": FREE"

            )

        else:

            print(

                "Counter "

                + str(index + 1)

                + ": Ticket "

                + str(counters[index])

            )

    print("\nCompleted History")

    if not completed_history:

        print("No completed services.")

    else:

        for ticket in completed_history:

            print(

                "Ticket "

                + str(ticket["number"])

                + " | "

                + ticket["purpose"]

                + " | "

                + ticket["service_type"]

            )

def menu_issue_ticket():

    print("\n1. Enrollment")

    print("2. Records")

    print("3. Payment")

    purpose_choice = input(

        "Choose purpose: "

    )

    purpose_map = {

        "1": "Enrollment",

        "2": "Records",

        "3": "Payment"

    }

    if purpose_choice not in purpose_map:

        print("Invalid purpose.")

        return

    service_type = input(

        "Enter service type (regular/priority): "

    ).strip().lower()

    try:

        number = issue_ticket(

            purpose_map[purpose_choice],

            service_type

        )

        print(

            "Ticket issued:",

            number

        )

    except ValueError as error:

        print(error)

def menu_call_next():

    ticket, message = call_next_ticket()

    print(message)

    if ticket is not None:

        print(

            "Ticket "

            + str(ticket["number"])

            + " | "

            + ticket["purpose"]

            + " | "

            + ticket["service_type"]

        )

def menu_complete():

    value = input(

        "Enter ticket number to complete: "

    )

    try:

        number = int(value)

    except ValueError:

        print(

            "Ticket number must be numeric."

        )

        return

    success, message = complete_ticket(number)

    print(message)

def menu_cancel():

    value = input(

        "Enter ticket number to cancel: "

    )

    try:

        number = int(value)

    except ValueError:

        print(

            "Ticket number must be numeric."

        )

        return

    success, message = cancel_ticket(number)

    print(message)

def run_menu():

    while True:

        print("\nCampus Service Queue Manager")

        print("1. Issue a ticket")

        print("2. Call the next ticket")

        print("3. Complete a service")

        print("4. Cancel a waiting ticket")

        print("5. Show waiting tickets")

        print("6. Show counter status and completed history")

        print("7. Show a summary report")

        print("8. Exit")

        choice = input(

            "Enter your choice: "

        ).strip()

        if choice == "1":

            menu_issue_ticket()

        elif choice == "2":

            menu_call_next()

        elif choice == "3":

            menu_complete()

        elif choice == "4":

            menu_cancel()

        elif choice == "5":

            show_waiting()

        elif choice == "6":

            show_status()

        elif choice == "7":

            report(

                waiting=True,

                served=True,

                cancelled=True,

                free_counters=True,

                source="menu"

            )

        elif choice == "8":

            print("Program ended.")

            break

        else:

            print(

                "Invalid menu choice. Please choose 1 to 8."

            )

if __name__ == "__main__":

    run_menu()