import os
import pandas as pd


def validate_skill_number(skill_number):
    return 1 <= skill_number <= 10


def get_skill_column(skill_number):
    return f"Skill_{skill_number}"


def filter_jobs_by_skill(data, skill_number, min_level):
    column = get_skill_column(skill_number)
    return data[data[column] >= min_level]


def get_jobs_by_skill(data, skill_number, min_level):
    filtered = filter_jobs_by_skill(data, skill_number, min_level)