from os import path
from time import strptime
from sys import argv

from git import Repo

script_root_directory = path.dirname(path.realpath(argv[0]))


def get_grader_name():
    return Repo(script_root_directory).config_reader().get_value("user", "name")


def get_grader_email():
    return Repo(script_root_directory).config_reader().get_value("user", "email")


def get_assignment_deadline():
    while True:
        deadline = input("What is the assignment deadline (yyyy-mm-dd hh:mm)? ")
        try:
            strptime(deadline, "%Y-%m-%d %H:%M")
            return deadline
        except:
            print("Incorrect datetime format.")


def get_assignment_subdirectories():
    subdirectories = input("What are the subdirectories to correct separated by space (ex: tp/tp6/pb1 tp/tp6/pb2)? ")
    return subdirectories.strip().split(" ")


def get_assignment_long_name():
    return input("What is the assignment long name (ex: Code final)? ")


def get_assignment_short_name():
    return input("What is the assignment short name (ex: tp6)? ")


def get_grading_directory(ensure_exists: bool = True):
    while True:
        directory = input("What is the grading directory? ")
        if ensure_exists:
            if path.isdir(directory):
                return directory
            else:
                print("The grading directory specified does not exist.")
        else:
            return directory


def get_group_number():
    return str(int(input("What is your group (ex: 1)? ")))
