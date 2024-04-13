def case():

    while True:
        vale = int(input("введите пункт меню: "))
        try:
            match vale:
                case "1":
                    print("hello1")
                case "2":
                    print("hello2")
                case "3":
                    print("hello3")
                case "4":
                    print("hello4")
                case "5":
                    print("hello5")
                case "6":
                    print("hello6")
                case "7":
                    print("hello7")
                case "0":
                    quit()
                case "_":
                    print("Unknown command.")
        except:
            print("ERROR")
            break