# Package: did_you_client
from enum import Enum
import msgpack
import zmq


class TaskCommand(Enum):
    do = 1
    done = 2

class TaskCommander(object):

    def __init__(self, configurator):
        context = zmq.Context()
        self._socket = context.socket(zmq.REQ)
        host = configurator.host
        port = configurator.request_port
        self._socket.connect("tcp://{}:{}".format(host, port))

    def run_command(self, command, task_name):
        task_message = {"name": task_name, "command": command.value}
        self._socket.send(msgpack.packb(task_message))
        return self._socket.recv()

class TaskSubscriber(object):

    def __init__(self, configurator):
        host = configurator.host
        port = configurator.subscription_port
        context = zmq.Context()
        self._socket = context.socket(zmq.SUB)
        self._socket.connect("tcp://{}:{}".format(host, port))
        self._socket.setsockopt(zmq.SUBSCRIBE, b'')

    def get_task_list(self):
        task_list = msgpack.unpackb(self._socket.recv())
        return task_list
