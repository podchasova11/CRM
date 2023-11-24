import os


class Links:

    STAGE = "https://release-crm.qa-playground.com" if os.environ["STAGE"] == "release" else "https://dev-crm.qa-playground.com"
