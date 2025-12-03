import re


def convert_list_item(markdown):
    if re.search(r"\s*\d+.\s+[a-zA-Z]+", markdown):
        markdown1 = markdown.split(".")
        output = f"<li>{markdown1[1].strip()}</li>"
    else:
        output = "Invalid format"

    return output


test = convert_list_item(" 1. My item")
print(test)
