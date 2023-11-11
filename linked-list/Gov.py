from random import randint
import LinkedList
import time


class Gov:
    __working_hours = 0
    __clients = 0
    __positions = {
        'A': [],
        'B': [],
        'C': [],
        'E': [],
    }

    def get_time(self):
        return self.__working_hours

    def assing(self, positions=__positions, linkedlist=LinkedList.LinkedList(), e=1):
        for i in range(linkedlist.list_size()):
            if linkedlist.get_node(i) is not None:
                if [] in positions[linkedlist.get_node(i)[0]]:
                    positions[linkedlist.get_node(i)[0]].append([linkedlist.get_node(i)[1], linkedlist.get_node(i)[2]])
                    positions[linkedlist.get_node(i)[0]].remove([])
                    linkedlist.delete_node(i)
                if [] in positions['E']:
                    positions['E'].append([linkedlist.get_node(i)[1], linkedlist.get_node(i)[2]]) 
                    positions['E'].remove([])
                    linkedlist.delete_node(i)
        self.__positions = positions
        return linkedlist, positions

    def results(self):
        print(f"Koniec zmiany, trwała {self.__working_hours} jednostek czasu. Obsłużono {self.__clients} klientów.")

    def check(self, values):
        for num in values:
            empty_count = 0
            for n in num:
                if not n:
                    empty_count += 1
            if empty_count != len(num):
                return False
        return True

    def sort_queue(self, a=3, b=3, c=3, e=1, positions=__positions, linkedlist=LinkedList.LinkedList()):

        positions = {'A': [[] for _ in range(a)],
                     'B': [[] for _ in range(b)],
                     'C': [[] for _ in range(c)],
                     'E': [[] for _ in range(e)],
                     }
        counter = 0
        czas = 0
        self.__clients = linkedlist.list_size()
        linkedlist, positions = self.assing(positions=positions, linkedlist=linkedlist)
        

        while self.check(positions.values()) is False:
            for times in positions.values():
                for i in range(len(times)):
                    if times[i] == []:
                        continue
                    else:
                        times[i][0] -= 1
                        if times[i][0] == 0:
                            # print(f"Klient nr. {times[i][1] + 1} obsłużony")
                            times[i] = []
                        # else:
                        #     print(f"Pozostały czas klienta nr. {times[i][1] + 1}: {times[i][0]}")

            if linkedlist.list_size() > 2:
                linkedlist, positions = self.assing(positions, linkedlist, e)                       
            # print(f"Kolejka A {positions['A']}\nKolejka B {positions['B']}\nKolejka C {positions['C']}\nKolejka E {positions['E']}\n")
            # time.sleep(0.5)
            czas += 1
            self.__working_hours = czas
        
        return self.results()

    def __init__(self) -> None:
        pass


'''
Aby przyspieszyć algorytm można użyć wielowątkowości.
'''
