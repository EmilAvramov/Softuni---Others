from abc import ABC


class Eatable(ABC):
    def eat(self):
        pass


class Workable(ABC):
    def work(self):
        pass


class Manager(ABC):
    def manage(self):
        pass

    def lunch_break(self):
        pass

    def set_worker(self, worker):
        pass


class Worker(Eatable, Workable):
    def eat(self):
        return "Lunch break....(5 secs)"

    def work(self):
        return "I'm normal worker. I'm working."


class SuperWorker(Eatable, Workable):
    def eat(self):
        return "Lunch break....(3 secs)"

    def work(self):
        return "I'm super worker. I work very hard!"


class Robot(Workable):
    def work(self):
        return "I'm a robot. I'm working...."


class WorkManager(Manager):
    def __init__(self) -> None:
        self.worker = ""

    def manage(self):
        return print(self.worker.work())

    def set_worker(self, worker):
        self.worker = worker


class BreakManager(Manager):
    def __init__(self) -> None:
        self.worker = ""

    def lunch_break(self):
        if isinstance(self.worker, Eatable):
            return print(self.worker.eat())

    def set_worker(self, worker):
        self.worker = worker


work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()
work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()
work_manager.set_worker(Robot())
work_manager.manage()

try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass
