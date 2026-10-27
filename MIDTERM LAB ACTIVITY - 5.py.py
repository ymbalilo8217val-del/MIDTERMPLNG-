class CustomerNode:
    def __init__(self, name):
        self.name = name
        self.next = None


class WaitingList:
    def __init__(self):
        self.head = None

    def add_customer(self, name):
        new_node = CustomerNode(name)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def serve_customer(self):
        if self.head is None:
            print("Waiting list is empty.")
        else:
            print("Served:", self.head.name)
            self.head = self.head.next

    def cancel_customer(self, name):
        if self.head is None:
            print("Waiting list is empty.")
            return
        if self.head.name == name:
            self.head = self.head.next
            print("Cancelled:", name)
            return
        current = self.head
        while current.next is not None:
            if current.next.name == name:
                current.next = current.next.next
                print("Cancelled:", name)
                return
            current = current.next
        print("Customer not found.")

    def display_waiting(self):
        names = []
        current = self.head
        while current is not None:
            names.append(current.name)
            current = current.next
        if len(names) == 0:
            print("Waiting: None")
        else:
            print("Waiting: " + " -> ".join(names) + " -> None")

    def count_customers(self):
        count = 0
        current = self.head
        while current is not None:
            count = count + 1
            current = current.next
        print("Customers waiting:", count)


class SongNode:
    def __init__(self, title):
        self.title = title
        self.prev = None
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_song(self, title):
        new_node = SongNode(title)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.current = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def next_song(self):
        if self.current is None:
            print("Playlist is empty.")
        elif self.current.next is None:
            print("Already at the last song.")
        else:
            self.current = self.current.next
            print("Current:", self.current.title)

    def previous_song(self):
        if self.current is None:
            print("Playlist is empty.")
        elif self.current.prev is None:
            print("Already at the first song.")
        else:
            self.current = self.current.prev
            print("Current:", self.current.title)

    def show_current(self):
        if self.current is None:
            print("Playlist is empty.")
        else:
            print("Current:", self.current.title)

    def display_forward(self):
        titles = []
        song = self.head
        while song is not None:
            titles.append(song.title)
            song = song.next
        if len(titles) == 0:
            print("Forward: None")
        else:
            print("Forward: " + " <-> ".join(titles))

    def display_backward(self):
        titles = []
        song = self.tail
        while song is not None:
            titles.append(song.title)
            song = song.prev
        if len(titles) == 0:
            print("Backward: None")
        else:
            print("Backward: " + " <-> ".join(titles))

    def remove_song(self, title):
        if self.head is None:
            print("Playlist is empty.")
            return
        song = self.head
        while song is not None and song.title != title:
            song = song.next
        if song is None:
            print("Song not found.")
            return
        if song == self.current:
            if song.next is not None:
                self.current = song.next
            else:
                self.current = song.prev
        if song.prev is not None:
            song.prev.next = song.next
        else:
            self.head = song.next
        if song.next is not None:
            song.next.prev = song.prev
        else:
            self.tail = song.prev
        print("Removed:", title)


def run_waiting_list():
    waiting = WaitingList()
    while True:
        print()
        print("1 Add customer")
        print("2 Serve customer")
        print("3 Cancel customer")
        print("4 Display waiting list")
        print("5 Count customers")
        print("0 Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            name = input("Enter customer name: ").strip()
            if name != "":
                waiting.add_customer(name)
            else:
                print("Invalid")
        elif choice == "2":
            waiting.serve_customer()
        elif choice == "3":
            name = input("Enter customer name to cancel: ").strip()
            if name != "":
                waiting.cancel_customer(name)
            else:
                print("Invalid")
        elif choice == "4":
            waiting.display_waiting()
        elif choice == "5":
            waiting.count_customers()
        elif choice == "0":
            break
        else:
            print("Invalid")


def run_playlist():
    playlist = Playlist()
    while True:
        print()
        print("1 Add song")
        print("2 Next song")
        print("3 Previous song")
        print("4 Show current")
        print("5 Display forward")
        print("6 Display backward")
        print("7 Remove song")
        print("0 Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            title = input("Enter song title: ").strip()
            if title != "":
                playlist.add_song(title)
            else:
                print("Invalid")
        elif choice == "2":
            playlist.next_song()
        elif choice == "3":
            playlist.previous_song()
        elif choice == "4":
            playlist.show_current()
        elif choice == "5":
            playlist.display_forward()
        elif choice == "6":
            playlist.display_backward()
        elif choice == "7":
            title = input("Enter song title to remove: ").strip()
            if title != "":
                playlist.remove_song(title)
            else:
                print("Invalid")
        elif choice == "0":
            break
        else:
            print("Invalid")


while True:
    choice = input("Select application (1 Waiting List, 2 Playlist, q to quit): ").strip()
    if choice == "q":
        break
    elif choice == "1":
        run_waiting_list()
    elif choice == "2":
        run_playlist()
    else:
        print("Invalid")