import copy
import sys
import unittest

PURPOSES = ["Enrollment", "Records", "Payment"]
SERVICE_TYPES = ["regular", "priority"]

ticket_counter = 0


def reset_ticket_counter():
    global ticket_counter
    ticket_counter = 0


def issue_ticket(purpose, service_type="regular"):
    global ticket_counter

    purpose = str(purpose).strip().capitalize()
    service_type = str(service_type).strip().lower()

    if purpose not in PURPOSES:
        raise ValueError("Invalid purpose. Choose Enrollment, Records or Payment.")

    if service_type not in SERVICE_TYPES:
        raise ValueError("Invalid service type. Choose regular or priority.")

    ticket_counter = ticket_counter + 1
    ticket = {
        "id": ticket_counter,
        "purpose": purpose,
        "service_type": service_type,
        "status": "waiting",
    }
    return ticket


def issue_many(*requests):
    checked = []
    for request in requests:
        if not isinstance(request, (tuple, list)) or len(request) < 1:
            raise ValueError("Each request must be (purpose, service_type).")

        purpose = str(request[0]).strip().capitalize()
        if len(request) > 1:
            service_type = str(request[1]).strip().lower()
        else:
            service_type = "regular"

        if purpose not in PURPOSES or service_type not in SERVICE_TYPES:
            raise ValueError("Invalid request: " + str(request))

        checked.append((purpose, service_type))

    new_tickets = []
    for purpose, service_type in checked:
        new_tickets.append(issue_ticket(purpose, service_type))
    return new_tickets


def next_ticket(tickets, priority_streak):
    priority_waiting = []
    regular_waiting = []

    for ticket in tickets:
        if ticket["status"] == "waiting":
            if ticket["service_type"] == "priority":
                priority_waiting.append(ticket)
            else:
                regular_waiting.append(ticket)

    if len(priority_waiting) == 0 and len(regular_waiting) == 0:
        return None, priority_streak

    if priority_streak >= 2 and len(regular_waiting) > 0:
        return regular_waiting[0], 0
    elif len(priority_waiting) > 0:
        return priority_waiting[0], priority_streak + 1
    else:
        return regular_waiting[0], 0


def report(**info):
    print("\n--- QUEUE REPORT ---")
    for key in info:
        name = key.replace("_", " ").title()
        print(name + ":", info[key])
    print("--------------------\n")


def estimate_waiting_position(tickets, ticket_id, streak=0):
    copy_of_tickets = copy.deepcopy(tickets)

    found = False
    for ticket in copy_of_tickets:
        if ticket["id"] == ticket_id and ticket["status"] == "waiting":
            found = True
    if found == False:
        return None

    position = 0
    while True:
        chosen, streak = next_ticket(copy_of_tickets, streak)
        if chosen is None:
            return None
        position = position + 1
        if chosen["id"] == ticket_id:
            return position
        chosen["status"] = "served"


class WaitingTicketIterator:
    def __init__(self, tickets):
        self.tickets = tickets
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.tickets):
            ticket = self.tickets[self.index]
            self.index = self.index + 1
            if ticket["status"] == "waiting":
                return ticket
        raise StopIteration


class CampusQueueApp:
    def __init__(self):
        self.tickets = []
        self.counters = {1: None, 2: None}
        self.priority_streak = 0

    def show_menu(self):
        print("==============================")
        print("  CAMPUS SERVICE QUEUE")
        print("==============================")
        print("1 Issue a ticket")
        print("2 Call the next ticket")
        print("3 Complete a service")
        print("4 Cancel a waiting ticket")
        print("5 Show waiting tickets")
        print("6 Show counters and history")
        print("7 Show summary report")
        print("8 Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter option (1-8): ").strip()

            if choice == "1":
                self.issue()
            elif choice == "2":
                self.call_next()
            elif choice == "3":
                self.complete_service()
            elif choice == "4":
                self.cancel()
            elif choice == "5":
                self.show_waiting()
            elif choice == "6":
                self.show_counters_and_history()
            elif choice == "7":
                self.show_report()
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Enter a number from 1 to 8.")

    def issue(self):
        print("Purposes: Enrollment, Records, Payment")
        purpose = input("Enter purpose: ").strip()
        service_type = input("Enter service type (regular/priority): ").strip()
        if service_type == "":
            service_type = "regular"

        try:
            ticket = issue_ticket(purpose, service_type)
        except ValueError as error:
            print("Error:", error)
            return

        self.tickets.append(ticket)
        position = estimate_waiting_position(self.tickets, ticket["id"], self.priority_streak)
        print("Ticket", ticket["id"], "issued for", ticket["purpose"], "(" + ticket["service_type"] + ")")
        print("Estimated queue position:", position)

    def call_next(self):
        free_counter = None
        for number in self.counters:
            if self.counters[number] is None and free_counter is None:
                free_counter = number

        if free_counter is None:
            print("All counters are busy. Complete a service first.")
            return

        ticket, self.priority_streak = next_ticket(self.tickets, self.priority_streak)
        if ticket is None:
            print("No waiting tickets.")
            return

        ticket["status"] = "calling"
        self.counters[free_counter] = ticket
        print("Counter", free_counter, "is serving ticket", ticket["id"], "-", ticket["service_type"], ticket["purpose"])

    def complete_service(self):
        text = input("Enter counter number (1 or 2): ").strip()
        if not text.isdigit():
            print("Counter number must be a number.")
            return

        number = int(text)
        if number not in self.counters:
            print("Invalid counter. Choose 1 or 2.")
            return

        ticket = self.counters[number]
        if ticket is None:
            print("Counter", number, "is already free.")
            return

        ticket["status"] = "served"
        self.counters[number] = None
        print("Ticket", ticket["id"], "completed at counter", number)

    def cancel(self):
        text = input("Enter ticket number to cancel: ").strip()
        if not text.isdigit():
            print("Ticket number must be a number.")
            return

        ticket_id = int(text)
        found = None
        for ticket in self.tickets:
            if ticket["id"] == ticket_id:
                found = ticket

        if found is None:
            print("Ticket", ticket_id, "does not exist.")
        elif found["status"] != "waiting":
            print("Cannot cancel. Ticket status is", found["status"])
        else:
            found["status"] = "cancelled"
            print("Ticket", ticket_id, "cancelled.")

    def show_waiting(self):
        print("--- WAITING TICKETS ---")
        count = 0
        for ticket in WaitingTicketIterator(self.tickets):
            count = count + 1
            position = estimate_waiting_position(self.tickets, ticket["id"], self.priority_streak)
            print("Ticket", ticket["id"], "|", ticket["service_type"], "|", ticket["purpose"], "| Call position:", position)
        if count == 0:
            print("No waiting tickets.")

    def show_counters_and_history(self):
        print("--- COUNTERS ---")
        for number in self.counters:
            ticket = self.counters[number]
            if ticket is None:
                print("Counter", number, ": FREE")
            else:
                print("Counter", number, ": BUSY with ticket", ticket["id"])

        print("--- COMPLETED SERVICES ---")
        found = False
        for ticket in self.tickets:
            if ticket["status"] == "served":
                found = True
                print("Ticket", ticket["id"], "|", ticket["service_type"], "|", ticket["purpose"])
        if found == False:
            print("No completed services yet.")

    def show_report(self):
        waiting = 0
        served = 0
        cancelled = 0
        for ticket in self.tickets:
            if ticket["status"] == "waiting":
                waiting = waiting + 1
            elif ticket["status"] == "served":
                served = served + 1
            elif ticket["status"] == "cancelled":
                cancelled = cancelled + 1

        free = 0
        for number in self.counters:
            if self.counters[number] is None:
                free = free + 1

        report(
            total_tickets=len(self.tickets),
            waiting_tickets=waiting,
            served_tickets=served,
            cancelled_tickets=cancelled,
            free_counters=free,
            priority_streak=self.priority_streak,
        )


class TestQueue(unittest.TestCase):
    def setUp(self):
        reset_ticket_counter()

    def test_ticket_numbers(self):
        t1 = issue_ticket("Enrollment", "regular")
        t2 = issue_ticket("Records", "priority")
        self.assertEqual(t1["id"], 1)
        self.assertEqual(t2["id"], 2)

    def test_fairness(self):
        tickets = [
            issue_ticket("Enrollment", "priority"),
            issue_ticket("Records", "priority"),
            issue_ticket("Payment", "priority"),
            issue_ticket("Enrollment", "regular"),
        ]
        streak = 0

        ticket, streak = next_ticket(tickets, streak)
        self.assertEqual(ticket["id"], 1)
        ticket["status"] = "calling"

        ticket, streak = next_ticket(tickets, streak)
        self.assertEqual(ticket["id"], 2)
        ticket["status"] = "calling"

        ticket, streak = next_ticket(tickets, streak)
        self.assertEqual(ticket["id"], 4)
        self.assertEqual(streak, 0)

    def test_both_counters_busy(self):
        app = CampusQueueApp()
        app.tickets.append(issue_ticket("Enrollment"))
        app.tickets.append(issue_ticket("Records"))

        app.call_next()
        app.call_next()

        self.assertIsNotNone(app.counters[1])
        self.assertIsNotNone(app.counters[2])

    def test_cancelled_is_skipped(self):
        tickets = [
            issue_ticket("Enrollment", "regular"),
            issue_ticket("Records", "regular"),
        ]
        tickets[0]["status"] = "cancelled"

        ticket, streak = next_ticket(tickets, 0)
        self.assertEqual(ticket["id"], 2)

    def test_iterator_ends(self):
        tickets = [issue_ticket("Enrollment", "regular")]
        iterator = WaitingTicketIterator(tickets)

        item = next(iterator)
        self.assertEqual(item["id"], 1)

        with self.assertRaises(StopIteration):
            next(iterator)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        unittest.main(argv=[sys.argv[0]])
    else:
        app = CampusQueueApp()
        app.run()