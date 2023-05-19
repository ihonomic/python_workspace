import json


def isValid(stale: str, latest: str, otjson: object) -> bool:
    """The isValid function takes in three parameters: stale (the previous version of the text), latest (the current version of the text), and otjson (the operations in the form of a JSON string).

    First, we parse the JSON string into a list of dictionaries using json.loads.

    We initialize a cursor index variable cursor_idx to 0, and a result string variable to an empty string. We'll use cursor_idx to keep track of our position in the text as we apply the operations.

    Next, we iterate over the operations. For each operation, we check the op field to determine which operation to apply.

    For a "skip" operation, we simply increment cursor_idx by the count value.

    For a "delete" operation, we check if we are trying to delete characters beyond the end of the string. If so, we return False immediately. Otherwise, we split the stale string into two parts: the characters before the cursor (char_before_cursor) and the characters after the cursor plus the characters we want to delete (char_after_cursor). We then concatenate char_before_cursor and char_after_cursor to get the updated string, and set cursor_idx to the index of the first character after the deleted characters.

    For an "insert" operation, we again split the stale string into two parts: the characters before the cursor (char_before_cursor) and the characters after the cursor (char_after_cursor). We then concatenate char_before_cursor, the characters to be inserted, and char_after_cursor to get the updated string. We set cursor_idx to the index of the last inserted character.

    Finally, after applying all the operations, we compare the resulting string to latest. If they are equal, we return True. Otherwise, we return False.

        Args:
            stale (str): _description_
            latest (str): _description_
            otjson (object): _description_

        Returns:
            bool: _description_
    """
    operations = json.loads(otjson)
    cursor_idx = 0  # start cursor index from 0

    string = stale
    # The idea is to perform the operations on the stale string & compare if it matches with the latest string.
    for operation in operations:
        if operation["op"] == "skip":
            count = operation["count"]
            cursor_idx += count

            # check if past-end
            if cursor_idx > len(string):
                return False

        elif operation["op"] == "delete":
            count = operation["count"]

            # check if past-end
            if cursor_idx + count > len(string):
                return False

            char_before_cursor = string[:cursor_idx]
            char_after_cursor = string[cursor_idx + count :]
            string = char_before_cursor + char_after_cursor

        elif operation["op"] == "insert":
            chars = operation["chars"]
            char_before_cursor = string[:cursor_idx]
            char_after_cursor = string[cursor_idx:]
            string = char_before_cursor + chars + char_after_cursor

            cursor_idx += len(chars)

    return string == latest


if __name__ == "__main__":
    test_cases = [
        {
            "stale": "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
            "latest": "Repl.it uses operational transformations.",
            "operations": '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}]',
        },
        {
            "stale": "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
            "latest": "Repl.it uses operational transformations.",
            "operations": '[{"op": "skip", "count": 45}, {"op": "delete", "count": 47}]',
        },
        {
            "stale": "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
            "latest": "Repl.it uses operational transformations.",
            "operations": '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}, {"op": "skip", "count": 2}]',
        },
        {
            "stale": "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
            "latest": "We use operational transformations to keep everyone in a multiplayer repl in sync.",
            "operations": '[{"op": "delete", "count": 7}, {"op": "insert", "chars": "We"}, {"op": "skip", "count": 4}, {"op": "delete", "count": 1}]',
        },
        {
            "stale": "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
            "latest": "We can use operational transformations to keep everyone in a multiplayer repl in sync.",
            "operations": '[{"op": "delete", "count": 7}, {"op": "insert", "chars": "We"}, {"op": "skip", "count": 4}, {"op": "delete", "count": 1}]',
        },
        {
            "stale": "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
            "latest": "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
            "operations": "[]",
        },
    ]

    for case in test_cases:
        print(isValid(case["stale"], case["latest"], case["operations"]))


# Expected outcomes:
# // true
# // false, delete past end
# // false, skip past end
# // true
# // false
# // true
