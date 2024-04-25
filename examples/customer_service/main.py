import shlex
import argparse
from src.swarm.swarm import Swarm
from src.tasks.task import Task
from configs.general import test_root, test_file, engine_name, persist
from src.validator import validate_all_tools, validate_all_assistants
from src.arg_parser import parse_args, parse_task_input


def main():
    args = parse_args()
    swarm = Swarm(engine_name=engine_name, persist=persist)
    swarm.initialize()  # Initialize the engine

    if args.test is not None:
        test_files = args.test
        test_file_paths = [f"{test_root}/{file}" for file in test_files] if test_files else [f"{test_root}/{test_file}"]
        swarm.run_tests(test_file_paths=test_file_paths)
    else:
        while True:
            if not args.input:
                swarm.load_tasks()
                swarm.deploy()

            task_input = input("Enter a task (or 'exit' to quit): ")
            if task_input.lower() == 'exit':
                break

            parsed_args = parse_task_input(task_input)
            swarm.add_task(Task(**parsed_args))
            swarm.deploy()

if __name__ == "__main__":
    main()
    print("\n\n🍯🐝🍯 Swarm operations complete 🍯🐝🍯\n\n")
