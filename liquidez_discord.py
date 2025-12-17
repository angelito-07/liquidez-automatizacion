import requests
from datetime import date

WEBHOOK_URL = "https://discord.com/api/webhooks/1450954441485189196/cg7YzvUOW0Mr3qrV-bVsq2doRaK9v4Qw-NHA8lkrN6lTa1JgWZYDVY4pAdr5RQuaiAPu"

hoy = date.today()

mensaje = {
    "content": f"""📊 **Liquidez Global**
📅 {hoy}

🟢 **LIQUIDEZ EXPANSIVA**

• PBoC: Inyección neta
• FED: Liquidez entrando
• BCE: Neutral
• Oro: Al alza
"""
}

requests.post(WEBHOOK_URL, json=mensaje)
