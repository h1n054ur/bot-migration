def handle_purchase_command(pre_selected_number=None):
    """Handle the purchase of a phone number.
    
    Args:
        pre_selected_number (str, optional): Phone number to purchase directly
    """
    from twilio_manager.cli.menus.phone.purchase_menu import PurchaseMenu
    PurchaseMenu(pre_selected_number).show()