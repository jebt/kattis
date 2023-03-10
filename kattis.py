import importlib
import re
import sys
import webbrowser
from os import listdir
from os.path import splitext, isfile

import requests

import problems.whichisgreater as current_problem
from utils import diff_strings

# problem_id = "next"
problem_id = "current_problem"

problem_locations = ["problems/archive", "problems"]


def main():
    if problem_id == "next":
        set_up_next()
        sys.exit(1)

    problems = [current_problem]
    # problems = get_problems()
    for problem in problems:
        print(f"\n{problem.__name__}")
        for i, (sample_input, sample_output) in enumerate(problem.samples):
            calculated_output = str(problem.solve(sample_input))
            if calculated_output == sample_output.strip():
                print(f"[sample {i}] correct")
            else:
                print(f"[sample {i}] see diff below\n" + diff_strings(calculated_output, sample_output))


def set_up_next():
    next_problem_id = find_next_problem_id()

    # open the webpage with the problem description
    url = f"https://open.kattis.com/problems/{next_problem_id}"
    webbrowser.open(url)

    # check if it exists locally
    next_exists = False
    next_problem_path = None
    for location in problem_locations:
        file_name_to_check = f"{location}/{next_problem_id}.py"
        if isfile(file_name_to_check):
            next_exists = True
            next_problem_path = file_name_to_check
            print(f"{next_problem_path} exists locally but is not accepted on kattis.com yet, exiting")
            # instead of exiting implement that it runs it (change print above)
            # set_problem(next_problem_path)
    if next_exists:
        sys.exit(1)
    else:
        # make pid.py with scraped samples
        next_problem_path = f"problems/{next_problem_id}.py"
        scrape_and_create_problem_module(next_problem_id, next_problem_path)
        # change problem_id = "..." (if possible during runtime)
        change_code(next_problem_path)
        # import problems.{problem_id} as problem and run it
        set_and_run_problem_module(next_problem_path)


def set_and_run_problem_module(problem_path):
    raise NotImplementedError
    # probably first set the module level problem_id variable and then call a seperate function to run it (which should
    # also be used in the main function normally)


def change_code(next_problem_id: str):
    raise NotImplementedError
    # change import statement?
    # change "problem_id = ..."?


def scrape_and_create_problem_module(next_problem_id: str, next_problem_path: str):
    url = f"https://open.kattis.com/problems/{next_problem_id}"
    response = requests.get(url)
    text = None
    if response.status_code == 200:
        text = str(response.content)
    else:
        print('Request failed with status code:', response.status_code)
        raise NotImplementedError
    with open("template.py") as f:
        new_module = f.read()
    if "<th>Sample Output 1</th>" in text:
        pattern = re.compile(r'<pre>(.*?)</pre>', re.DOTALL)
        matches = pattern.findall(text)
        match_count = len(matches)
        i1, i2, i3, i4, o1, o2, o3, o4 = [None] * 8
        if match_count == 0:
            raise ValueError("No samples?")
        if match_count % 2 != 0:
            raise ValueError("Uneven number of sample inputs + sample outputs?")
        if match_count > 8:
            raise ValueError("More than 4 sample input+output pairs?")
        if match_count >= 2:
            i1 = matches[0]
            o1 = matches[1]
        if match_count >= 4:
            i2 = matches[2]
            o2 = matches[3]
        if match_count >= 6:
            i3 = matches[4]
            o3 = matches[5]
        if match_count >= 8:
            i4 = matches[6]
            o4 = matches[7]

        if match_count < 8:
            new_module = new_module.replace('''
    (
        # Input 4
        """input_4""",
        # Output 4
        """output_4"""
    ),''', "")
        if match_count < 6:
            new_module = new_module.replace('''
    (
        # Input 3
        """input_3""",
        # Output 3
        """output_3"""
    ),''', "")
        if match_count < 4:
            new_module = new_module.replace('''
    (
        # Input 2
        """input_2""",
        # Output 2
        """output_2"""
    ),''', "")
            if match_count < 2:
                new_module = new_module.replace('''
    (
        # Input 1
        """input_1""",
        # Output 1
        """output_1"""
    ),''', "")

        if match_count > 0:
            new_module = new_module.replace("input_1", i1)
            new_module = new_module.replace("output_1", o1)
        if match_count > 2:
            new_module = new_module.replace("input_2", i2)
            new_module = new_module.replace("output_2", o2)
        if match_count > 4:
            new_module = new_module.replace("input_3", i3)
            new_module = new_module.replace("output_3", o3)
        if match_count > 6:
            new_module = new_module.replace("input_4", i4)
            new_module = new_module.replace("output_4", o4)
    else:
        print("No samples found!")
        raise NotImplementedError

    with open(next_problem_path, "w") as file:
        file.write(new_module)

    raise NotImplementedError


def find_next_problem_id():
    url = "https://open.kattis.com/problems?order=%2Bdifficulty_category"
    with open("config.txt") as f:
        cookie = f.read()
    headers = {
        "cookie": cookie
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return extract_next_problem_id(response.content)
    else:
        print('Request failed with status code:', response.status_code)
        raise NotImplementedError


def extract_next_problem_id(response_content):
    text = str(response_content)

    # pattern = re.compile(
    #     r'<td><a href="/problems/(.*?)">(.*?)</a></td>\n\s+<td>\n\s+<div class="status is-status-untried">' +
    #     r'<i class="fas fa-times status-icon is-not-attempted"></i>Not Attempted</div>')
    pattern = re.compile(r'<td><a href="/problems/(.{1,64})">.{1,64}</a></td>\\n\s+\\n\s+\\n\s+<td>\\n\s+'
                         r'<div class="status is-status-untried">')

    match = pattern.search(text)

    if match:
        return match.group(1)
    else:
        print('No matches found. Perhapss all problems on the first page are "Accepted" and should look next page!')
        raise NotImplementedError


def get_problems():
    problems = []
    for location in problem_locations:
        for file_name in listdir(location):
            name_parts = splitext(file_name)
            if name_parts[1] == ".py":
                module = f"{location.replace('/', '.')}.{name_parts[0]}"
                problems.append(importlib.import_module(module))
                print(f"imported {module}")
    print(f"{len(problems)=}")
    return problems


if __name__ == "__main__":
    main()
