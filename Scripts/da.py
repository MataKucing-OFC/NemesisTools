import requests
import concurrent.futures

def get_da_pa(domain):
    url = f"https://api.xploitsec.com/dapa?domain={domain}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if len(data) > 0 and "Status" in data[0] and data[0]["Status"] == "Success":
            return data[0]
        else:
            return None
    else:
        return None

def scan_domain(domain):
    da_pa_data = get_da_pa(domain)
    if da_pa_data:
        upa = da_pa_data["domAuthority"]
        pda = da_pa_data["pageAuthority"]
        print(f"-| {domain} DA: {upa} PA: {pda}")
        result = f"Domain: {domain} DA: {upa} PA: {pda}\n"
    else:
        result = f"Domain: {domain}\nData tidak tersedia\n----------------------\n"

    with open("/Results/da_pa_result.txt", "a") as file:
        file.write(result)

def main():
    banner = """
    
██████╗░░█████╗░  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██║░░██║███████║  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
██║░░██║██╔══██║  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██████╔╝██║░░██║  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═════╝░╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

    """
    print(banner)
    file_path = input("root@list:~# ")

    try:
        with open(file_path, "r") as file:
            domains = file.read().splitlines()
    except FileNotFoundError:
        print("File tidak ditemukan")
        return

    thread_count = int(input("root@thread:~# "))

    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_count) as executor:
        executor.map(scan_domain, domains)

if __name__ == "__main__":
    main()