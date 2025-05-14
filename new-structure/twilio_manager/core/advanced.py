from twilio_manager.services.advanced_service import configure_app_api, search_api

def configure_app(config_params: dict):
    """
    Configure application-level settings.
    """
    return configure_app_api(config_params)

def search_resources(query: str):
    """
    Perform an advanced search of resources.
    """
    return search_api(query)
