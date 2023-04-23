import Gov
import LinkedList
import matplotlib.pyplot as plt
import threading


def start_threads(a, b, c, e, people):
    linkedlist = LinkedList.LinkedList(people)
    Urzad = Gov.Gov()
    t = threading.Thread(Urzad.sort_queue(a=a, b=b, c=c, e=e, linkedlist=linkedlist))
    t.start()
    return Urzad.get_time()


def draw(czas_obslugi):
    etykiety = ['3A,3B,3C,1E', '3A,3B,3C', '1A,2B,3C,1E', '2A,2B,2C,3E']
    plt.bar(etykiety, czas_obslugi)
    plt.title('Czas obsługi dla poszczególnych zestawów okienek')
    plt.xlabel('Wersje urzędów')
    plt.ylabel('Średni czas obsługi')
    plt.show()


def main():
    time40_1 = 0
    time40_2 = 0
    time40_3 = 0
    time40_4 = 0
    time30_1 = 0
    time30_2 = 0
    time30_3 = 0
    time30_4 = 0
    for _ in range(100):
        time40_1 += start_threads(3,3,3,1,40)
        time40_2 += start_threads(3,3,3,0,40)
        time40_3 += start_threads(1,2,3,1,40)
        time40_4 += start_threads(2,2,2,3,40)
        time30_1 += start_threads(3,3,3,1,30)
        time30_2 += start_threads(3,3,3,0,30)
        time30_3 += start_threads(1,2,3,1,30)
        time30_4 += start_threads(2,2,2,3,30)

    draw([time40_1/100, time40_2/100, time40_3/100, time40_4/100])
    draw([time30_1/100, time30_2/100, time30_3/100, time30_4/100])


if __name__ == '__main__':
    main()























'''
def activate(people):
    linkedlist1 = LinkedList.LinkedList(people)
    linkedlist2 = LinkedList.LinkedList(people)
    linkedlist3 = LinkedList.LinkedList(people)
    linkedlist4 = LinkedList.LinkedList(people)
    Urzad1 = Gov.Gov()
    Urzad2 = Gov.Gov()
    Urzad3 = Gov.Gov()
    Urzad4 = Gov.Gov()
    Urzad1.sort_queue(linkedlist=linkedlist1)        
    time40_1 = Urzad1.get_time()
    Urzad2.sort_queue(a=3, b=3, c=3, e=0, linkedlist=linkedlist2)        
    time40_2 = Urzad2.get_time()
    Urzad3.sort_queue(a=2, b=2, c=2, e=3, linkedlist=linkedlist3)        
    time40_3 = Urzad3.get_time()
    Urzad4.sort_queue(a=1, b=2, c=3, e=1, linkedlist=linkedlist4)       
    time40_4 = Urzad4.get_time()
    return time40_1, time40_2, time40_3, time40_4

def draw(time40_1, time40_2, time40_3, time40_4):
    czas_obslugi = [time40_1/100, time40_2/100, time40_3/100, time40_4/100]

    etykiety = ['3A,3B,3C,1E', '3A,3B,3C', '1A,2B,3C,1E', '2A,2B,2C,3E']

    plt.bar(etykiety, czas_obslugi)

    plt.title('Czas obsługi dla poszczególnych okienek')
    plt.xlabel('Wersje urzędów')
    plt.ylabel('Średni czas obsługi')

    plt.show()

def main():
    time40_1 = 0
    time40_2 = 0
    time40_3 = 0
    time40_4 = 0
    time30_1 = 0
    time30_2 = 0
    time30_3 = 0
    time30_4 = 0
    for _ in range(100):
        people = 40
        time1, time2, time3, time4 = activate(people)
        time40_1 += time1
        time40_2 += time2
        time40_3 += time3
        time40_4 += time4
        people = 30
        time1, time2, time3, time4 = activate(people)
        time30_1 += time1
        time30_2 += time2
        time30_3 += time3
        time30_4 += time4


    print('Średni czas dla 30 klientów:',time30_1/100,time30_2/100,time30_3/100,time30_4/100,'\nŚredni czas dla 40 klientów:',time40_1/100,time40_2/100,time40_3/100,time40_4/100)
    draw(time40_1, time40_2, time40_3, time40_4)
    draw(time30_1, time30_2, time30_3, time30_4)
if __name__ == '__main__':
    main()
'''