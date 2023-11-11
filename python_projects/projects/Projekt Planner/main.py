import csv


# Pierwsza linia pliku wydarzenia.csv wyznacza klucze słownika i nie może być modyfikowana

def load_events():
    events = []
    with open('wydarzenia.csv', 'r', newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            events.append(row)
    f.close()
    return events


def save_events(events):
    with open('wydarzenia.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=["date", "time", "name", "description"])
        writer.writeheader()
        for event in events:
            writer.writerow(event)
        f.close()


def add_event(events):
    while True:
        date = input('Enter the date of the event (DD/MM/YYYY): ')
        time = input('Enter the time of the event (HH:MM): ')
        if len(date) != 10 or len(time) != 5 or time[2] != ':' or date[2] != '/' or date[5] != '/':
            print('Bad time format.')
        else:
            break
    while True:
        name = input('Enter the name of the event: ')
        if name != '':
            break
    description = input('Enter a description of the event (not needed): ')
    events.append({
        'date': date,
        'time': time,
        'name': name,
        'description': description
    })


def delete_event(events):
    date = input('Enter the date of the event (DD/MM/YYYY): ')
    time = input('Enter the time of the event (HH:MM): ')
    name = input('Enter the name of the event: ')
    for i, event in enumerate(events):
        if event['date'] == date and event['time'] == time and event['name'] == name:
            del events[i]
            return
    print('Event not found.')


def sort_events(events, key, reverse):
    return sorted(events, key=lambda x: x[key], reverse=reverse)


def search_events(events, query):
    search_results = []
    for event in events:
        if query in event['name'] or query in event['description']:
            search_results.append(event)
    return search_results


def print_events(events):
    for event in events:
        print(f"{event['date']} {event['time']} - {event['name']}")
        print(f"{event['description']}\n")
#test
def test_add_event():
    date = '10/01/2000'
    time = '11:00'
    name = 'nazwa'
    description = ''
    result = add_event([date,time,name,description])
    assert result

def main():
    events = load_events()
    while True:
        print('1. Display events')
        print('2. Add an event')
        print('3. Delete an event')
        print('4. Search an event')
        print('5. Sort events')
        print('6. Quit')
        choice = input('Enter your choice: ')
        if choice == '1':
            print_events(events)
        elif choice == '2':
            add_event(events)
            save_events(events)
        elif choice == '3':
            delete_event(events)
            save_events(events)
        elif choice == '4':
            query = input('Enter the search query: ')
            search_results = search_events(events, query)
            print_events(search_results)
        elif choice == '5':
            key = input('Sort by (date, time, name): ')
            if key == '1':
                key = 'date'
            elif key == '2':
                key = 'time'
            elif key == '3':
                key = 'name'
            if key != 'date' and key != 'name' and key != 'time':
                print('Bad key. Sorting failed.')
                continue
            reverse = input('Sort in reverse order? (y/N): ')
            reverse = True if reverse == 'y' else False
            events = sort_events(events, key, reverse)
            print_events(events)
        elif choice == '6':
            break
        else:
            print('Bad choice.\n')


if __name__ == '__main__':
    main()
