""" lab 3 """
from queue import Queue
import random
class MyDay:
    """
    class that simulates a day from life
    """

    def __init__(self) -> None:
        self.states = ['sleep', 'eat', 'relax', 'study', 'cry']
        self.transitions = {
            'sleep': ['eat', 'study'],
            'eat':['sleep', 'study'],
            'study':['eat', 'sleep', 'relax', 'cry'],
            'cry':['study'],
            'relax':['sleep', 'study']
            }
        self.current_state = 'sleep'
        self.event_queue = Queue()
        self.alert = False
        self.eat_times = 0
        self.flag = True
    def random_event(self, hour):
        """
        some random events, that can affect my day
        """
        if 1 <= hour <= 9:
            if self.current_state != 'study':
                if random.random() < 0.3:
                    print('oops, too many deadlines... I have to study')
                    #self.current_state = 'study'
                    self.event_queue.put('study')
            else:
                if random.random() < 0.4:
                    print('whatever, i want to sleep  zzzzzzzzz')
                    self.event_queue.put('sleep')
                    #self.current_state = 'sleep'
        elif 10 <= hour <= 17:
            if self.current_state == 'eat':
                if random.random() < 0.2:
                    print("it's time to learn something new")
                   # self.current_state = 'study'
                    self.event_queue.put('study')
        else:
            if self.current_state == 'study':
                if random.random() < 0.2:
                    print("o no, I'm going to fail everything! Now I just want to cry")
                   # self.current_state = 'cry'
                    self.event_queue.put('cry')
            elif self.current_state == 'cry':
                if random.random() < 0.7:
                    print('okay, somebody gotta do all those tasks')
                    #self.current_state = 'study'
                    self.event_queue.put('study')
                else:
                    print('I have no motivation to continue')
                    self.event_queue.put('cry')
                    self.flag = False
    def air_alert(self):
        """
        the air alert is on
        """
        print('ATTENTION THE AIR ALERT IS ON')
        self.alert = True

    def air_alert_is_over(self):
        """
        the air alert is over
        """
        print('THE AIR ALERT IS OVER')
        self.alert = False

    def simulate_day(self):
        """
        simulate one day
        """

        for hour in range(24):
            self.flag = True
            print(f'hour {hour}', end=': ')
            if random.random() < 0.15:
                self.random_event(hour)

            if self.event_queue.empty() or self.event_queue.get() == self.current_state:
                if not self.alert and random.random() < 0.02:
                    self.air_alert()
                else:
                    if self.alert:
                        print("sitting in the shelter")
                        if random.random() < 0.8:
                            self.air_alert_is_over()
                    else:
                        if self.flag:
                            if hour == 0:
                                if random.random() < 0.5:
                                    self.current_state = 'sleep'
                                    print('finishing my studying and going to sleep')

                                else:
                                    print('zzzzzz')
                                    self.current_state = 'sleep'
                            else:
                                if self.current_state == 'sleep':
                                    if 1 <= hour <= 8:
                                        print('zzzzzz')
                                    elif random.random() < 0.5 and hour == 9:
                                        print("good morning, it's time for breakfast")
                                        self.eat_times += 1
                                        self.current_state = 'eat'
                                    elif hour == 9:
                                        print('zzzzzz')
                                    elif hour == 10:
                                        print("it's too late, i have to study")
                                        self.current_state = 'study'
                                elif self.current_state == 'eat':
                                    if hour == 10:
                                        print("What a nice day, now it's time to attend classes")
                                        self.current_state = 'study'
                                    elif 23 <= hour <= 24:
                                        print("goodnight")
                                        self.current_state = 'sleep'
                                    else:
                                        print("back to studying!")
                                        self.current_state = 'study'
                                elif self.current_state == 'cry':
                                    print('still no motivation, but I have to work')
                                    self.current_state = 'study'

                                elif self.current_state == 'relax':
                                    if hour in(0, 23):
                                        print("it was a good day, now it's time to go to bed")
                                        self.current_state = 'sleep'
                                    elif 12 <= hour <= 19:
                                        print("that was a good break, let's return to studying")
                                        self.current_state = 'study'
                                    elif 1 <= hour <= 8:
                                        print('I just want to sleep')
                                        self.current_state = 'sleep'
                                    else:
                                        print('Relax time!')
                                else:
                                    if hour == 23:
                                        print('time to rest  zzzzzzzzzz')
                                        self.current_state = 'sleep'
                                    elif 17 <= hour <= 20 and self.eat_times == 0:
                                        print("i forgot to eat something, now it's dinner time")
                                        self.eat_times += 1
                                        self.current_state = 'eat'                                        
                                    elif hour in (12, 13, 16, 20) and self.eat_times < 3:
                                        print("let's eat something")
                                        self.eat_times += 1
                                        self.current_state = 'eat'
                                    elif 14 <= hour <= 19 and random.random()<0.25:
                                        print('so tired, I need a break')
                                        self.current_state = 'relax'
                                    elif 14 <= hour <= 16:
                                        print('programming is so fun')
                                    elif random.random() < 0.1:
                                        print("so much work, I can't do it anymore!    *cries*")
                                        self.current_state = 'cry'
                                    else:
                                        if random.random() < 0.5:
                                            print('studying math is so interesting')
                                        else:
                                            print('studying')
            print('__________________________________________________________')
a = MyDay()
a.simulate_day()
