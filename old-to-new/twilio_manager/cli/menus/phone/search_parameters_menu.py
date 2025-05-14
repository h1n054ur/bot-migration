from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.shared.ui.styling import print_warning

class SearchParametersMenu(BaseMenu):
    """Gather search parameters for available phone numbers."""
    def show(self):
        self.clear_screen()
        self.show_header("🔢 Search Parameters")

        # Country selection
        countries = ["+1", "+44", "+61"]
        print("Select country:")
        for idx, code in enumerate(countries, start=1):
            print(f"{idx}. {code}")
        country_choice = self.prompt_choice(
            [str(i) for i in range(1, len(countries) + 1)],
            default="1"
        )
        country = countries[int(country_choice) - 1]

        # Number type selection
        types = ["local", "mobile", "tollfree"]
        print("\nSelect number type:")
        for idx, nt in enumerate(types, start=1):
            print(f"{idx}. {nt}")
        type_choice = self.prompt_choice(
            [str(i) for i in range(1, len(types) + 1)],
            default="1"
        )
        number_type = types[int(type_choice) - 1]

        # Capabilities selection
        cap_options = ["voice", "sms", "mms"]
        print("\nSelect capabilities:")
        for idx, cap in enumerate(cap_options, start=1):
            print(f"{idx}. {cap.capitalize()}")
        capabilities = []
        while True:
            cap_input = input(
                "Enter numbers separated by commas (e.g. 1,2), or leave empty for none: "
            ).strip()
            if not cap_input:
                break
            choices = [c.strip() for c in cap_input.split(",")]
            valid = True
            selected = []
            for c in choices:
                if not c.isdigit() or not (1 <= int(c) <= len(cap_options)):
                    print_warning(f"Invalid selection: {c}")
                    valid = False
                    break
                selected.append(cap_options[int(c) - 1])
            if valid:
                capabilities = selected
                break

        # Optional pattern
        pattern = input("\nNumber pattern (optional): ").strip()

        return {
            "country_code": country,
            "number_type": number_type,
            "capabilities": capabilities,
            "pattern": pattern,
        }
