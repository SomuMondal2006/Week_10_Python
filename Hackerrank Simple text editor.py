# Hackerrank: Simple text editor
# https://www.hackerrank.com/challenges/simple-text-editor/problem



import io
import sys

sample_input = """
8
1 abc
3 3
2 3
1 xy
3 2
4
4
3 1
"""

sys.stdin = io.StringIO(sample_input.strip())


def simple_text_editor():
    """
    Implements a simple text editor with append, delete, print, and undo operations.
    """

    s = [] 

    history = [] 

    try:
        num_operations = int(sys.stdin.readline())
    except (IOError, ValueError):
        num_operations = 0

    for _ in range(num_operations):
        line = sys.stdin.readline().split()
        op_type = int(line[0])

        if op_type == 1:
            text_to_append = line[1]
            history.append((1, len(text_to_append)))
            s.extend(list(text_to_append))

        elif op_type == 2:
            k = int(line[1])
            deleted_part = "".join(s[-k:])
            history.append((2, deleted_part))
            del s[-k:]

        elif op_type == 3:
            k = int(line[1])
            print(s[k - 1])

        elif op_type == 4:
            if not history:
                continue
            last_op_type, data = history.pop()

            if last_op_type == 1:
                length_to_delete = data
                del s[-length_to_delete:]
            
            elif last_op_type == 2:
                text_to_re_append = data
                s.extend(list(text_to_re_append))

simple_text_editor()