class TrainTask:
    @classmethod
    def print(cls):
        print(1)
        print(f"{cls.__name__}")

    def run(self, a, b):
        print(2)
        result = a + b.split()
        self._run(a, b)
        return a + b.split()

    def __call__(self, *args, **kwargs):
        print(3)
        return self.run(*args, **kwargs)


class TrainTaskCelery(TrainTask):
    class Meta:
        abstract = True

    def perform(self, *args, **kwargs):
        print(4)
        return self.run(*args, **kwargs)


class RefreshAndFlushGrouping(TrainTaskCelery):
    @classmethod
    def _run(cls, trains, session):
        print(trains)
        print("Session : ", session)


if __name__ == "__main__":
    t = RefreshAndFlushGrouping()
    t.print()

    t.perform([1, 5, 6], "labla")
