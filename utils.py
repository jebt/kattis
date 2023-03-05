import difflib
import colorama


def diff_strings(str1, str2):
    colorama.init()  # initialize colorama
    seq_matcher = difflib.SequenceMatcher(None, str1, str2)
    diffs = ""
    for op, i1, i2, j1, j2 in seq_matcher.get_opcodes():
        if op == 'replace':
            # mark replacements with a special marker
            diffs += colorama.Fore.RED + str1[i1:i2] + colorama.Style.RESET_ALL
            diffs += colorama.Fore.GREEN + str2[j1:j2] + colorama.Style.RESET_ALL
        elif op == 'delete':
            # mark deletions with a special marker
            diffs += colorama.Fore.RED + str1[i1:i2] + colorama.Style.RESET_ALL
        elif op == 'insert':
            # mark insertions with a special marker
            diffs += colorama.Fore.GREEN + str2[j1:j2] + colorama.Style.RESET_ALL
        else:
            # no change
            diffs += str1[i1:i2]
    return diffs
