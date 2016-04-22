# Package: did_you_client.command
import os.path
import sys
from sh import notify_send
from time import sleep

from did_you_client import TaskCommand, TaskCommander, TaskSubscriber
from did_you_client.config import DidYouConfig

configuration_file = os.path.expanduser('~/.did_you_client.conf')

def run_client():
    if len(sys.argv) < 2:
        executable_name = sys.argv[0]
        print("Usage {} <command> [<parameter>]".format(executable_name))
        exit()
    configurator = DidYouConfig(configuration_file)
    if sys.argv[1] == "list":
        task_subscriber = TaskSubscriber(configurator)
        task_list = task_subscriber.get_task_list()
        for task in task_list:
            print(str(task, 'utf-8'))
    else:
        command, task_name = sys.argv[1:]
        task_commander = TaskCommander(configurator)
        response = task_commander.run_command(
            TaskCommand[command], task_name)
        print("Got response: {}".format(str(response, 'UTF-8')))
