# accessing some project in one program, by typing number.

import time

while True:

    try:
        print("""
========= MENU =========
1 - Coffee Outlet
2 - Membership System
3 - Access System
0 - Exit
========================
""")
        selection = int(input("Choose Task by Typing Number 0-10: "))

        if selection == 0:
            print("\\"),time.sleep(1.5), print("| Exiting program... Thank you! |"),time.sleep(2), print("/")
            break
        
        if selection == 1:
            print("""
===========================================================  
=================== Your on Selection 1 ===================
===========================================================\n""")
            import coffee_outlet

            print("""\n
==========================================
===============Thank You!=================
==========================================\n""")
        elif selection == 2:
            print("""
===========================================================  
=================== Your on Selection 2 ===================
===========================================================\n""")
            import membership_status_system
            print("""\n
==========================================
===============Thank You!=================
==========================================\n""")
        elif selection == 3:
            print("""
===========================================================  
=================== Your on Selection 3 ===================
===========================================================\n""")
            import access_system
            print("""\n
==========================================
===============Thank You!=================
==========================================\n""")
        else:
            print("Wrong Selection.")
    except ValueError:
        print("Please enter a valid number.")
