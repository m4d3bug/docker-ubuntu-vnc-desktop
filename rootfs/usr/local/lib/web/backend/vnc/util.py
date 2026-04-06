from contextlib import contextmanager
from gevent import GreenletExit


@contextmanager
def ignored(*exceptions):
    try:
        yield
    except GreenletExit as e:
        raise e
    except exceptions:
        pass
