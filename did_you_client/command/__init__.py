# Package: did_you_client.command
import os.path
import sys
from sh import notify_send
from time import sleep

from did_you_client import TaskCommand, TaskCommander, TaskSubscriber
from did_you_client.config import DidYouConfig

configuration_file = os.path.expanduser('~/.did_you_client.conf')


def run_client():
    if len(sys.argv) != 3:
        executable_name = sys.argv[0]
        print("Usage {} <command> <task-name>".format(executable_name))
        exit()
    command, task_name = sys.argv[1:]
    configurator = DidYouConfig(configuration_file)
    task_commander = TaskCommander(configurator)
    response = task_commander.run_command(
        TaskCommand[command], task_name)
    print("Got response: {}".format(str(response, 'UTF-8')))


def run_checker():
    configurator = DidYouConfig(configuration_file)
    sleep_period = int(configurator.sleep_period)

    task_subscriber = TaskSubscriber(configurator)

    run_once = len(sys.argv) == 2 and sys.argv[1] == 'list'
    while True:
        task_list = task_subscriber.get_task_list()
        if run_once:
            for task_index, task in enumerate(task_list, 1):
                print("{index}: {task}".format(
                    index=task_index, task=str(task, 'utf-8')))
            break
        if len(task_list) > 0:
            task_notification = ["{}: {}".format(index, str(task, 'UTF-8'))
                                 for index, task in enumerate(task_list, 1)]
            notify_send("TODO:", "\n".join(task_notification))
        sleep(sleep_period)
