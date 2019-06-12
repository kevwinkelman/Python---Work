import openpyxl
wb = openpyxl.load_workbook('C:\\Users\\kwinkelman-x\\OneDrive - KB Home\\Desktop\\sabaa\\saba_users.xlsx')
ws = wb["saba"]

def SearchUserName(username):
        for cell in ws['A']:
            if cell.value.startswith(username):
                print("Found username: " + cell.value)
            else:
                continue

while True:
    try:
        print("\nEnter username: ", end = '')
        usernameInput = input()
        print("Hit ENTER to end program.")
        if usernameInput == "":
            print("\nEnd of program.")
            break
        else:
            SearchUserName(usernameInput)
    except ValueError:
        print("so like we have an error here. pls try again ty")