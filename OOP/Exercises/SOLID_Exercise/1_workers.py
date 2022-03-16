from abc import ABC, abstractmethod


class IWorker(ABC):
    @staticmethod
    @abstractmethod
    def work():
        pass


class Worker(IWorker):
    @staticmethod
    def work():
        print("I'm working!!")


class SuperWorker(IWorker):

    @staticmethod
    def work():
        print("I work very hard!!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker: IWorker):
        assert isinstance(worker, IWorker), '`worker` must be of type {}'.format(IWorker)
        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


if __name__ == '__main__':
    worker = Worker()
    manager = Manager()
    manager.set_worker(worker)
    manager.manage()

    super_worker = SuperWorker()
    try:
        manager.set_worker(super_worker)
    except AssertionError:
        print("manager fails to support super_worker....")

    worker = Worker()
    manager = Manager()
    manager.set_worker(worker)
    manager.manage()

    super_worker = SuperWorker()
    try:
        manager.set_worker(super_worker)
        manager.manage()
    except AssertionError:
        print("manager fails to support super_worker....")
