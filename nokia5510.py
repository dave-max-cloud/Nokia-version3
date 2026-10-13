def main():
    while True:
        main_menu = """
    Welcome to Nokia
    Press
    1:Phonebook
    2:Messages
    3:Chat
    4:Call register
    5:Tones
    6:Settings
    7:Call divert
    8:Music
    9.Games
    10.Calculator
    11.Reminders
    12.Clock
    13.Profiles
    14.Service
    15.Sim services
    0.Back
    H.Home
    """
        print (main_menu)
        menu_choice = input("Select an option:")
        if menu_choice == "H":
            continue
        match menu_choice:
            case "1" :  
                result = phonebook()
                if result == "home":
                    continue
            case "2":
                result = messages()
                if result == "home":
                    continue
            case "3":
                print("Chat")
            case "4":
                result = call_register()
                if result == "home":
                    continue
            case "5":
                result = tones()
                if result == "home":
                    continue
            case "6":
                result = settings()
                if result == "home":
                    continue
            case "7": print("Call divert")
            case "8":
                result = music()
                if result == "home":
                    continue
            case "9": print("Games")
            case "10": print("Calculator")
            case "11": print("Reminders")
            case "12":
                result = clock()
                if result == "home":
                    continue
            case "13": print("Profiles")
            case "14": print("Services")
            case "15": print("SIM services")
            case "0":  
                break
            case _: print("Invalid")


def phonebook():
    decision_one = True
    while(decision_one):
        print("Phone book")
        phone_book = """
                Welcome to phonebook
                Press
                1.Search
                2.Service Nos
                3.Add name
                4.Erase
                5.Edit
                6.Copy
                7.Assign tone
                8.Send b'card
                9.Options
                10.Speed dails
                11.Voice tags
                0.Return
                H.Home
            """
        print(phone_book)
        phonebook_choice = input("Select an option:")
        match phonebook_choice:
            case "1": print("Search")
            case "2": print("Service Nos")
            case "3": print("Add name")
            case "4": print("Erase")
            case "5": print("Edit")
            case "6": print("Copy")
            case "7": print("Assign tone")
            case "8": print("Send b'card")
            case "9": 
                result = phonebook_options()
                if result == "home":
                    return "home"
            case "10": print("Speed dial")
            case "11": print("Voice tags")
            case "0": decision_one = False
            case "H": return "home"
            case _: print("invalid")


def phonebook_options():
    decision_two = True
    while(decision_two):
        print("Options") 
        option_menu = """
        1.Memory in use
        2.Type of view
        3.Memory status
        0.Return
        H.Home
        """
        print(option_menu)
        option_prompt = input("Select an option:")
        match(option_prompt):
            case "1": print("Memory in use")
            case "2": print("Type of use")
            case "3": print("Memory status")
            case "0": decision_two = False
            case "H": return "home"
            case _: print("Invalid")


def messages():
    print("Messages")
    decision_three = True
    while(decision_three):
        messages_menu = """
                                    
                Welcome to Message Menu
                1.Write messages
                2.Inbox
                3.Outbox
                4.Picture messages 
                5.Templates
                6.Smileys
                7.Messages settings
                8.Info service
                9.Voice mailbox number
                10.Service command editor
                0.Return
                H.Home
                """
        print(messages_menu)
        message_choice = input("Select an option:")
        match message_choice:
            case "1": print("1.Write messages")
            case "2": print("2.Inbox")
            case "3": print("3.Outbox")
            case "4": print("4.Picture messages")
            case "5": print("5.Templates")
            case "6": print("6.Smileys")
            case "7": 
                result = message_settings()
                if result == "home":
                    return "home"
            case "8": print("8.Info service")
            case "9": print("9.Voice mailbox number")
            case "10": print("10.Service command editor")
            case "0": decision_three = False
            case "H": return "home"
            case _: print("Invalid")


def message_settings():
    decision_four = True
    while(decision_four):
        print("7.Message settings")
        message_settings_menu = """
                            1.Set 1
                            2.Common
                            0.Return
                            H.Home
                            """
        print(message_settings_menu)
        message_settings_choice = input("Select an option:")
        match message_settings_choice:
            case "1":
                print("Set 1")
                result = set1()
                if result == "home":
                    return "home"
            case "2":
                print("Common")
                result = common()
                if result == "home":
                    return "home"
            case "0": decision_four = False
            case "H": return "home"
            case _: print("Invalid")


def set1():
    decision_five = True
    while(decision_five):
        set_1_menu = """
                                        1.Message centre number
                                        2.Message sent as
                                        3.Message validity
                                        0.Go back
                                        H.Home
                                    """
        print(set_1_menu)
        set_1_choice = input("Select an option")
        match set_1_choice:
            case "1": print("1.Message centre number")
            case "2": print("2.Message sent as")
            case "3": print("3.Message validity") 
            case "0": decision_five = False
            case "H": return "home"
            case _: print("Invalid")


def common():
    choice_zero = True
    while(choice_zero):
        common_menu = """
                                        1.Deliivery reports
                                        2.Reply via same centre
                                        3.Character support
                                        0.Return
                                        H.Home
                                        """
        print(common_menu)
        common_choice = input("Select an option:")
        match common_choice:
            case "1": print("1.Delivery reports")
            case "2": print("2.Reply via same centre")
            case "3": print("3.Character support")
            case "0": choice_zero = False
            case "H": return "home"
            case _: print("Invalid")


def call_register():
    menu_choice = True
    while(menu_choice):
        print("Call register")
        call_register_menu = """
                1.Missed calls
                2.Received calls
                3.Dailled numbers
                4.Erase recent call lists
                5.Show call duration
                6.Show all costs
                7.Call cost settings
                8.Prepaid credit
                0.Return
                H.Home
                    """
        print(call_register_menu)
        call_register_choice = input("Select an option:")
        match call_register_choice:
            case "1": print("1.Missed calls")
            case "2": print("2.Received calls")
            case "3": print("3.Dailed numbers")
            case "4": print("4.Erase recent call list")
            case "5": 
                print("Show call duration")
                result = show_call_duration()
                if result == "home":
                    return "home"
            case "6":
                print("Show call costs")
                result = show_call_costs()
                if result == "home":
                    return "home"
            case "7":
                print("Call cost settings")
                result = call_cost_settings()
                if result == "home":
                    return "home"
            case "8": print("Prepaid credit")
            case "0": menu_choice = False
            case "H": return "home"
            case _: print("Invalid")


def show_call_duration():
    option_one = True
    while(option_one):
        show_call_duration_menu = """
                            1.Last call duration
                            2.All call's duration
                            3.Received call's duration
                            4.Dailled call's duration
                            5.Clear timers
                            0.Return
                            H.Home
                        """
        print(show_call_duration_menu)
        show_call_duration_choice = input("Select an option:")
        match show_call_duration_choice:
            case "1": print("Last call duration")
            case "2": print("All call's duration")
            case "3": print("Received call's duration")
            case "4": print("Dailled call's duration")
            case "5": print("Clear timer")
            case "0": option_one = False
            case "H": return "home"
            case _: print("Invalid")


def show_call_costs():
    option_two = True
    while(option_two):
        show_call_costs_menu = """
                            1.Last call cost
                            2.All call's cost
                            3.Clear counters
                            0.Return
                            H.Home
                            """
        print(show_call_costs_menu)
        show_call_costs_choice = input("Select an option:")
        match show_call_costs_choice:
            case "1": print("1.Last call cost")
            case "2": print("2.All call's cost")
            case "3": print("3.Clear counters")
            case "0": option_two = False
            case "H": return "home"
            case _: print("Invalid")


def call_cost_settings():
    option_three = True
    while(option_three):
        call_cost_settings_menu = """
                            1.Call cost limit
                            2.Show costs in
                            0.Return
                            H.Home
                            """
        print(call_cost_settings_menu)
        call_cost_settings_choice = input("Select an option:")
        match call_cost_settings_choice:
            case "1": print("1.Call cost limit")
            case "2": print("2.Show costs in")
            case "0": option_three = False
            case "H": return "home"
            case _: print("Invalid")


def tones():
    option_four = True
    while(option_four):
        print("Tones")
        tones_menu = """
                    1.Ringing tone
                    2.Ringing volume
                    3.Incoming call alert
                    4.Message alert tone
                    5.Keypad tones
                    6.Warming tones
                    7.Vibrating alert
                    8.Screen saver
                    0.Return
                    H.Home
                    """
        print(tones_menu)
        tones_choice = input("Select an option:")
        match tones_choice:
            case "1": print("1.Ringing tone")
            case "2": print("2.Ringing volume")
            case "3": print("3.Incoming call alert")
            case "4": print("4.Message alert tone")
            case "5": print("5.Keypad tones")
            case "6": print("6'Warming")
            case "7": print("7.Vibrating alert")
            case "8": print("8.Screen saver")
            case "0": option_four = False
            case "H": return "home"
            case _: print("Invalid")


def settings():
    option_five = True
    while(option_five):
        print("Settings")
        settings_menu = """
                1.Call settings
                2.Phone settings
                3.Security settings
                4.Restore factory settings
                0.Return
                H.Home
                """
        print(settings_menu)
        settings_choice = input("Select an option:")
        match settings_choice:
            case "1":
                result = call_settings()
                if result == "home":
                    return "home"
            case "2":
                result = phone_settings()
                if result == "home":
                    return "home"
            case "3":
                result = security_settings()
                if result == "home":
                    return "home"
            case "4": print("Restore factory settings")
            case "0": option_five = False
            case "H": return "home"
            case _: print("Invalid")


def call_settings():
    option_six = True
    while(option_six):      
        print("Call settings")
        call_settings_menu = """
                            1.Automatic redical
                            2.Speed dailling
                            3.Call waiting options
                            4.Own number sending
                            5.Phone line in use 
                            6.Automatic answer
                            0.Return
                            H.Home
                            """
        print(call_settings_menu)
        call_settings_choice = input("Select an option:")
        match call_settings_choice:
            case "1": print("1.Automatic redical")
            case "2": print("2.Speed dailling")
            case "3": print("3.Call waiting options")
            case "4": print("4.Own number sending")
            case "5": print("Phone line in use")
            case "6": print("6.Automatic answer")
            case "0": option_six = False
            case "H": return "home"
            case _: print("Invalid")


def phone_settings():
    option_eight = True
    while(option_eight):
        print("Phone setting")
        phone_settings_menu = """
                            1.Language
                            2.Cell info display
                            3.Welcome note
                            4.Network selection
                            5.Confirm SIM service actions
                            0.Return
                            H.Home
                            """
        print(phone_settings_menu)
        phone_settings_choice = input("Select an option:")
        match phone_settings_choice:
            case "1": print("1.Language")
            case "2": print("2.Cell info display")
            case "3": print("3.Welcome selection")
            case "4": print("4.Network selection")
            case "5": print("5.Confirm SIM service actions")
            case "0": option_eight = False
            case "H": return "home"
            case _: print("Invalid")


def security_settings():
    option_nine = True
    while(option_nine):      
        print("Security settings")
        security_settings_menu = """
                            1.Pin code
                            2.Call barring service
                            3.Fixed dialling
                            4.Closed user group
                            5.Security level
                            6.Change access codes
                            0.Return
                            H.Home
                            """
        print(security_settings_menu)
        security_settings_choice = input("Select an option:")
        match security_settings_choice:
            case "1": print("1.Pin code")
            case "2": print("2.Call barring service")
            case "3": print("3.Fixed dailing")
            case "4": print("4.Closer user group")
            case "5": print("5.Change access codes")
            case "0": option_nine = False
            case "H": return "home"
            case _: print("Invalid")


def music():
    option_ten = True
    while(option_ten):
        print("Music")
        music_menu = """
                 1.Music player
                 2.Radio
                 3.Recorder
                 4.Track list
                 0.Return
                 H.Home
                 """
        print(music_menu)
        music_choice = input("Select an option:")
        match music_choice:
            case "1": print("1.Music player")
            case "2": print("2.Radio")
            case "3": print("Recorder")
            case "4": print("Track list")
            case "0": option_ten = False
            case "H": return "home"
            case _: print("Invalid")


def clock():
    decision_ten = True
    while(decision_ten):
        print("Clock")
        clock_menu = """
                 1.Alarm clock 
                 2.Clock settings 
                 3.Date setting 
                 4.Stopwatch 
                 5.Countdown timer 
                 6.Auto update of date and time
                 0.Return
                 H.Home
                 """
        print(clock_menu)
        clock_choice = input("Select an option:")
        match clock_choice:
            case "1": print("1.Alarm clock")
            case "2": print("2.Clock settings")
            case "3": print("3.Date settings")
            case "4": print("4.Stopwatch")
            case "5": print("5.Countdown timer")
            case "6": print("6.Auto update of date and time")
            case "0": decision_ten = False
            case "H": return "home"
            case _: print("Invalid")


main()
