from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.cli.menus.account.account_info_menu import AccountInfoMenu
from twilio_manager.cli.menus.account.api_keys_menu import ApiKeysMenu
from twilio_manager.cli.menus.account.subaccounts_menu import SubaccountsMenu
from twilio_manager.cli.menus.account.sip_trunks_menu import SipTrunksMenu
from twilio_manager.cli.menus.account.twiml_apps_menu import TwimlAppsMenu
from twilio_manager.shared.ui.styling import print_warning

class AccountMenu(BaseMenu):
    """Account menu: routes to account sub-flows."""
    def show(self):
        self.clear_screen()
        self.show_header("⚙️ Account")
        print("1. View Account Info")
        print("2. Manage API Keys")
        print("3. Manage Subaccounts")
        print("4. Manage SIP Trunks")
        print("5. Manage TwiML Apps")
        print("0. 🔙 Back")
        options = ["1", "2", "3", "4", "5", "0"]
        choice = self.prompt_choice(options, default="0")
        if choice == "1":
            AccountInfoMenu(self).show()
        elif choice == "2":
            ApiKeysMenu(self).show()
        elif choice == "3":
            SubaccountsMenu(self).show()
        elif choice == "4":
            SipTrunksMenu(self).show()
        elif choice == "5":
            TwimlAppsMenu(self).show()
        elif choice == "0":
            self.exit_to_parent()
        else:
            print_warning("Option not implemented yet.")
            self.show()
