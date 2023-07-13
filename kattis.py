import html
import importlib
import os
import re
import subprocess
import sys
import webbrowser
import colorama
from os import listdir
from os.path import splitext, isfile

import requests

import problems.janitortroubles as current_problem

from utils import diff_strings

problem_id = "janitortroubles"
# problem_id = "current_problem"

PROBLEM_LOCATIONS = ["problems/archive", "problems"]


def main():
    ask_to_submit = True
    if problem_id == "next":
        problems = set_up_next()
        assert len(problems) == 1, f"{len(problems)=}, should be 1 in this case"
    elif problem_id == "all":
        problems = get_problems()
        assert len(problems) > 1, f"{len(problems)=}, should be more than 1"
        ask_to_submit = False
    elif len(problem_id.split()) > 1 and problem_id.split()[0] == "get":
        specific_problem_id = "".join(problem_id.split()[1::])
        problems = set_up_specific(specific_problem_id)
        assert len(problems) == 1, f"{len(problems)=}, should be 1 in this case"
    else:
        problem_name = current_problem.__name__.split(".")[-1]
        assert problem_id == problem_name, f"problem_id {problem_id} doesn't match problem_name {problem_name}"
        problems = [current_problem]
    run_problems(problems, ask_to_submit)


def run_problems(problems, ask_to_submit):
    all_succes = True
    for problem in problems:
        print(f"\n{problem.__name__}")
        succes = True
        for i, (sample_input, sample_output) in enumerate(problem.samples):
            calculated_output = str(problem.solve(sample_input))
            if calculated_output == sample_output.strip():
                print(f"[sample {i}] {colorama.Fore.GREEN}correct{colorama.Style.RESET_ALL}")
            else:
                succes = False
                all_succes = False
                print(f"{colorama.Fore.RED}[sample {i}] see diff below{colorama.Style.RESET_ALL}\n" +
                      diff_strings(calculated_output, sample_output))
        if ask_to_submit and succes:
            # Get the path of the current Python executable and the current script
            python_exe = sys.executable
            script_path = os.path.join(os.getcwd(), 'submit.py')

            # Activate the virtual environment
            venv_activate = os.path.join(os.getcwd(), 'venv', 'Scripts', 'activate')
            subprocess.run([venv_activate], shell=True)

            # Call the script with an argument 'argument1'
            subprocess.run([python_exe, script_path, f'problems/{problem_id}.py'])
    if len(problems) > 1:
        if all_succes:
            print("\n" + colorama.Fore.GREEN + "all good" + colorama.Style.RESET_ALL + f" ({len(problems)})")
        else:
            print("\n" + colorama.Fore.RED + "mistakes were made" + colorama.Style.RESET_ALL)


def set_up_specific(specific_problem_id):
    problems = set_up(specific_problem_id)
    return problems


def set_up_next() -> list:
    next_problem_id = find_next_problem_id()
    problems = set_up(next_problem_id)
    return problems


def set_up(next_problem_id: str):
    # open the webpage with the problem description
    url = f"https://open.kattis.com/problems/{next_problem_id}"
    webbrowser.open(url)

    # check if it exists locally
    for location in PROBLEM_LOCATIONS:
        file_name_to_check = f"{location}/{next_problem_id}.py"
        if isfile(file_name_to_check):
            next_problem_path = file_name_to_check
            print(f"{next_problem_path} exists locally but is not accepted on kattis.com yet, exiting")
    else:
        # make pid.py with scraped samples
        next_problem_path = f"problems/{next_problem_id}.py"
        scrape_and_create_problem_module(next_problem_id, next_problem_path)
        # change problem_id = "..." (if possible during runtime)
        change_code(next_problem_id)
        # import problems.{problem_id} as problem and run it

    problems = import_and_set_problems([next_problem_path])
    return problems


def import_and_set_problems(problem_paths):
    problems = []
    for problem_path in problem_paths:
        location = "/".join(problem_path.split("/")[:-1])
        file_name = problem_path.split("/")[-1]
        name_parts = splitext(file_name)
        if name_parts[1] == ".py":
            module = f"{location.replace('/', '.')}.{name_parts[0]}"
            problems.append(importlib.import_module(module))
            print(f"imported {module}")
    return problems


def change_code(next_problem_id: str):
    # change "problem_id = ..."
    with open("kattis.py") as f:
        kattis_code = f.read()

    # string in next line is weirdly cut up so that it doesn't get replaced itself
    new_kattis_code = kattis_code.replace('pro' + 'blem_id = "ne' + 'xt"', f'problem_id = "{next_problem_id}"')
    new_kattis_code = new_kattis_code.replace('pro' + 'blem_id = "ge' + 't ', f'problem_id = "')

    # change import statement
    pattern = r'import\s+problems\.(\w+)\s+as\s+current_problem'
    match = re.search(pattern, new_kattis_code)
    if match:
        captured_string = match.group(1)
    else:
        print("No match")
        raise ValueError
    new_kattis_code = new_kattis_code.replace(
        f"import problems.{captured_string} as current_problem", f"import problems.{next_problem_id} as current_problem"
    )
    with open("kattis.py", "w") as f:
        f.write(new_kattis_code)


def scrape_and_create_problem_module(next_problem_id: str, next_problem_path: str):
    url = f"https://open.kattis.com/problems/{next_problem_id}"
    response = requests.get(url)
    if response.status_code == 200:
        problem_text = str(response.content)
    else:
        print('Request failed with status code:', response.status_code)
        raise NotImplementedError

    if "<th>Sample Output 1</th>" in problem_text:
        new_module = create_prepared_module(problem_text)
    else:
        print("No samples found!")
        raise NotImplementedError

    with open(next_problem_path, "w") as file:
        file.write(new_module)


def create_prepared_module(problem_text):
    samples_from_i = problem_text.index("<th>Sample Output 1</th>")
    problem_text = problem_text[samples_from_i::]
    pattern = re.compile(r'<pre>(.*?)</pre>', re.DOTALL)
    matches = pattern.findall(problem_text)
    match_count = len(matches)
    if match_count == 0:
        raise ValueError("No samples?")
    if match_count % 2 != 0:
        raise ValueError("Uneven number of sample inputs + sample outputs?")
    if match_count > 10:
        raise ValueError("More than 5 sample input+output pairs?")
    io_pairs = match_count // 2
    new_module = replace_template_io(io_pairs, matches)

    # delete unused input/output samples from the template
    for i in range(io_pairs + 1, 6):
        new_module = new_module.replace(f'''
    (
        # Input {i}
        """input_{i}""",
        # Output {i}
        """output_{i}"""
    ),''', "")
    return new_module


def replace_template_io(io_pairs, matches):
    with open("template.py") as f:
        new_module = f.read()
    for i in range(1, io_pairs + 1):
        new_module = new_module.replace(f"input_{i}", html.unescape(matches[i * 2 - 2]))
        new_module = new_module.replace(f"output_{i}", html.unescape(matches[i * 2 - 1]))
    return new_module


def find_next_problem_id():
    # url = "https://open.kattis.com/problems?order=%2Bdifficulty_category"
    url = "https://open.kattis.com/problems?order=difficulty_category"
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
    pattern = re.compile(r'<td><a href="/problems/(.{1,64})">.{1,64}</a></td>\\n\s+\\n\s+\\n\s+<td>\\n\s+'
                         r'<div class="status is-status-untried">')
    match = pattern.search(text)
    if match:
        return match.group(1)
    else:
        print('No matches found. Perhapss all problems on the first page are "Accepted" and should look next page!'
              'Or maybe EduSiteCookie needs to be refreshed.')
        raise NotImplementedError


def get_problems():
    problems = []
    for location in PROBLEM_LOCATIONS:
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
