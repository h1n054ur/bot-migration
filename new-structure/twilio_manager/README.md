# Twilio Manager CLI

A command-line tool to manage Twilio resources including phone numbers, messaging, voice calls, account settings, and advanced utilities.

## Features

- **Phone Number Management**: Search, purchase, configure, and release phone numbers.
- **Messaging**: Send SMS/MMS, view message logs, and delete messages.
- **Voice**: Place calls, list conferences, recordings, and call logs.
- **Account**: View account info, list API keys, subaccounts, SIP trunks, and TwiML apps.
- **Advanced**: Custom configuration and resource search utilities.

## Installation

1. **Clone the repository**  
   ```bash
   git clone <repo_url>
   cd twilio_manager
   ```

2. **Create and activate a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the CLI using Python’s module flag:

```bash
python -m twilio_manager
```

Navigate the menus using the numeric options presented.

## Project Structure

```
twilio_manager/
├── cli/menus/
│   ├── base_menu.py
│   ├── main_menu.py
│   ├── phone_menu.py
│   ├── phone/
│   │   ├── search_menu.py
│   │   └── ...
│   ├── messaging/
│   ├── voice/
│   ├── account/
│   └── advanced/
├── core/
│   ├── phone_numbers.py
│   ├── messaging.py
│   ├── voice.py
│   ├── account.py
│   └── advanced.py
├── services/
│   ├── phone_service.py
│   ├── message_service.py
│   ├── voice_service.py
│   ├── account_service.py
│   └── advanced_service.py
├── shared/
│   └── ui/styling.py
├── requirements.txt
└── __main__.py
```

## Contributing

Contributions and feedback are welcome! Please open an issue or submit a pull request.

