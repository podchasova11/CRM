import os

class Credentials:

    if os.environ["STAGE"] == "release":
        LOGIN = ""
        PASSWORD = ""

    elif os.environ["STAGE"] == "dev":
        LOGIN = ""
        PASSWORD = ""