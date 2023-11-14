import os

def get_absolute_path(relative_path: str) -> str:
    return os.path.abspath(os.path.join(os.getcwd(), relative_path))

def read(relative_path: str) -> str:
    absolute_path = get_absolute_path(relative_path)
    try: 
        with open(absolute_path, mode="r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"The file '{absolute_path}' does not exist."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# use example:
# this should be relative to root directory
# help_doc_location = r"assets/help.md"
# help_message = utils.open_file(help_doc_location)
# print(help_message)