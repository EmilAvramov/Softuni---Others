class Worker:
    def __repr__(self) -> str:
        return "I'm working!!"


class SuperWorker:
    def __repr__(self) -> str:
        return "I work very hard!!! "


class Manager:
    def __init__(self) -> None:
        self.worker = ""

    def manage(self):
        return print(self.worker)

    def set_worker(self, worker):
        self.worker = worker


worker = Worker()
super_worker = SuperWorker()
manager = Manager()

manager.set_worker(worker)
manager.manage()

try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
