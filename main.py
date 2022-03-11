import requests

def get_ip_info(ip='127.0.0.1'):
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()

        data = {
            'IP': response.get('query'),
            'Int prov': response.get('isp'),
            'Org': response.get('org'),
            'Country': response.get('country'),
            'Region Name': response.get('regionName'),
            'City': response.get('city'),
            'ZIP': response.get('zip'),
            'Lat': response.get('lat'),
            'Lon': response.get('lon')
        }

        for i, j in data.items():
            print(f'{i}: {j}')

    except requests.exceptions.ConnectionError:
        print("[!] Please check your connection!")

def main():
    ip = input("Please enter a target IP: ")

    get_ip_info(ip=ip)

if __name__ == "__main__":
    main()