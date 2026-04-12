import os
import pytest
from src.app import add_task, load_tasks, complete_task, remove_task


def setup_function():
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")


def test_add_task():
    add_task("Study Python")
    tasks = load_tasks()
    assert tasks[0]["task"] == "Study Python"


def test_empty_task():
    with pytest.raises(ValueError):
        add_task("")


def test_complete_task():
    add_task("Task 1")
    complete_task(0)
    tasks = load_tasks()
    assert tasks[0]["done"] is True


def test_remove_task():
    add_task("Task 2")
    remove_task(0)
    tasks = load_tasks()
    assert len(tasks) == 0
