usernameInput = input("USERNAME : ")
passwordInput = input("PASSWORD : ")
if usernameInput == "admin" and passwordInput == "1129":
    print("-----     WELCOME      -----")
    print("----- NGILITY PEA SHOP -----")
    print("1. DATA S1 x1 : 10,000 ฿ ")
    print("2. DATA S2 x1 : 20,000 ฿ ")
    print("3. DATA S3 x1 : 30,000 ฿ ")
    userSelacted = int(input("Choose : "))
    if userSelacted == 1:
        productName = "DATA S1"
        productPrice = 10000
    elif userSelacted == 2:
        productName = "DATA S2"
        productPrice = 20000
    elif userSelacted == 3:
        productName = "DATA S3"
        productPrice = 30000

    print("Product you selected: ", productName, ":", productPrice, "฿")
    Selected = int(input("please select : "))
    print("Summary: ", productName, ":", Selected, "x", productPrice, "=", productPrice * Selected, "฿")