# letsencrypt_domeneshop_paloalto

This project automates the process of obtaining Let's Encrypt SSL certificates using Certbot for domains managed by Domeneshop and deploying them to Palo Alto Networks firewalls.

## Features

- Automates certificate issuance with Certbot.
- Integrates with Domeneshop DNS for domain validation.
- Deploys certificates to Palo Alto firewalls via API.
- Supports multiple domains and firewalls.
- Scheduled renewals and deployments.

## Requirements

- Python 3.6+
- Certbot installed
- Access to Domeneshop API credentials
- Access to Palo Alto Networks firewall API credentials

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/letsencrypt_domeneshop_paloalto.git
   cd letsencrypt_domeneshop_paloalto
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure your credentials and settings in `config.yaml`.

## Usage

Run the main script to obtain and deploy certificates:

```bash
python main.py
```

## License

MIT License

## Contributing

Feel free to submit issues and pull requests.
