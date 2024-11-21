from appDhully.service.PBBService import PBBService
from appDhully.KiT.KiT import main as kit_main

class SincronizationProcessService:
    def display_sync_menu(self):
        print("Select Synchronization Protocol")
        print("1. PBB Synchronization")
        print("2. KIT Synchronization")
        option = int(input("Enter an option: "))
        if option == 1:
            self.pbb_synchronization()
        elif option == 2:
            self.start_kit_synchronization()
        else:
            print("Invalid option. Please try again.")
            self.display_sync_menu()

    def pbb_synchronization(self):
        self.start_pbb_synchronization([{"cliente_name": "Bob", "pass": "123", "value": ["Sync_b", "Cancel_b"]},
                                        {"cliente_name": "Alice", "pass": "123", "value": ["Sync_a"]}])

    def menu_cases(self):
        while True:
            print("Submenu:")
            print("1. S_a/S_b")
            print("2. C_a/S_b")
            print("3. C_a/C_b")
            print("4. S_b/C_b/S_a")
            print("0. Return to main menu")
            option = int(input("Enter an option: "))
            if option == 1:
                self.start_pbb_synchronization([{"cliente_name": "Alice", "pass":"123", "value": ["Sync_a"]},
                                                {"cliente_name": "Bob", "pass":"123", "value": ["Sync_b"]}])
                # Add your logic for Option 1 here
            elif option == 2:
                self.start_pbb_synchronization([{"cliente_name": "Alice", "pass":"123", "value": ["Cancel_a"]},
                                                {"cliente_name": "Bob", "pass":"123", "value": ["Sync_b"]}])
                # Add your logic for Option 2 here
            elif option == 3:
                self.start_pbb_synchronization([{"cliente_name": "Alice", "pass":"123", "value": ["Cancel_a"]},
                                                {"cliente_name": "Bob", "pass":"123", "value": ["Sync_b"]}])
                # Add your logic for Option 3 here
            elif option == 4:
                self.start_pbb_synchronization([{"cliente_name": "Bob", "pass":"123", "value": ["Sync_b", "Cancel_b"]},
                                                {"cliente_name": "Alice", "pass":"123", "value": ["Sync_b"]}])
            elif option == 0:
                break
            else:
                print("Invalid option. Please try again.")
    def start_pbb_synchronization(self, l):
        print("Starting PBB synchronization...")
        pbbService = PBBService()
        pbbService.startProcess(l)

    def start_kit_synchronization(self):
        print("Starting KIT synchronization...")
        kit_main()