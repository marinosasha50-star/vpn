import base64
import urllib.parse
import requests

# 1. Ваша ссылка на подписку
SUB_URL = " вставте сюда ссылку"

# 2. Точный User-Agent
USER_AGENT = "Happ/4.4.1/Android/17891107313301967618"

# 3. Ваш HWID
HWID = "79d812809150d073"

headers = {
    "User-Agent": USER_AGENT,
    "Hwid": HWID,
    "X-Hwid": HWID,
    "Accept": "*/*",
    "Connection": "keep-alive",
}


def fetch_servers():
    print("[+] Отправка запроса с точным User-Agent и HWID...")
    try:
        response = requests.get(SUB_URL, headers=headers, timeout=15)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[-] Ошибка запроса: {e}")
        return

    content = response.text.strip()

    # Декодирование из Base64
    try:
        padded = content + "=" * (-len(content) % 4)
        decoded = base64.b64decode(padded).decode("utf-8", errors="ignore")
    except Exception:
        decoded = content

    servers = [
        line.strip() for line in decoded.splitlines() if line.strip()
    ]

    print(f"\n[+] Найдено серверов: {len(servers)}\n")
    for idx, server in enumerate(servers, 1):
        decoded_name = urllib.parse.unquote(server)
        print(f"{idx}. {decoded_name}")

    # Сохранение в файл
    with open("servers.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(servers))
    print("\n[+] Серверы успешно сохранены в файл servers.txt")


if __name__ == "__main__":
    fetch_servers()