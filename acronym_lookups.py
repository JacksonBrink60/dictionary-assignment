acro = {"LOL": "laugh out loud", "BRB": "be right back",
        "AFK": "away from keyboard", "ASAP": "as soon as possible", "BTW": "by the way"}
enteracro = ""
while not "Q" in enteracro:
    enteracro = ""
    meaning = ""
    enteracro = input("Enter an acronym (or Q to quit): ").upper().strip()
    if enteracro == "Q":
        break
    yn = ""
    if enteracro in acro:
        print(acro[f"{enteracro}"])
    elif enteracro == "LIST":
        print(acro)
    else:
        yn = input(
            f"{enteracro} in no in the dictionary. Would you like to add it? (yes/no): ")
    if yn == "yes":
        meaning = input(f"Eter the meaning for {enteracro}: ")
        acro[f"{enteracro}"] = f"{meaning}"
        print(f"{enteracro} has been added to the dictionary")
print("Goodbye")
