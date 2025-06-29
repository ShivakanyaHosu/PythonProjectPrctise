browser_Name = input("Enter the browser name\n")
match browser_Name:
    case "Firefox":
        print("Starting Firefox")
    case "Chrome":
        print("Execute the chrome code")
    case "Edge":
        print("Execute the Edge code")
    case "Safari":
        print("Execute the Safari code")
    case _:  # default when nothing match
        print("Browser Not found")
