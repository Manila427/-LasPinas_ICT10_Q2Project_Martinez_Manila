
from pyscript import document, when

club_members = [
    "gabby chua",
    "manila martinez",
    "yza santiago",
    "kate velo",
    "yna sabulao",
    "sophie gamban",
    "becca vinco",
    "athena silva"
]

@when("click", "#checkMember")
def check_member(event):

    first_name = document.querySelector("#first_name").value.strip().lower()
    last_name = document.querySelector("#last_name").value.strip().lower()

    result = document.querySelector("#result")

    if first_name == "" or last_name == "":
        result.innerHTML = "Please enter your first and last name!"

    else:
        full_name = first_name + " " + last_name

        if full_name in club_members:
            result.innerHTML = full_name.title() + " is a Glee Club member!"
        else:
            result.innerHTML = full_name.title() + " is not in the list."
