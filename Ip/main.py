from urllib import response
import requests
from pyfiglet import Figlet
import folium


logo = r'''
(c)StalkerVrk
'''
print(logo)

def getInfoByIp(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}', verify=False).json()
        print(response)

        data = {
            '[Ip]' : response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]' : response.get('org'),
            '[Country]' : response.get('country'),
            '[Region Name]' : response.get('regionName'),
            '[City]' : response.get('city'),
            '[ZIP]' : response.get('zip'),
            '[Lat]' : response.get('lat'),
            '[Lon]' : response.get('lon'),
        } 

        for i,j in data.items():
            print(f'{i} : {j}')
        
        result = folium.Map(location=[response.get('lat'), response.get('lon')])
        result.save(f'{response.get("city")}_{response.get("org")}.html')

    except requests.exceptions.ConnectionError:
        print('[!] Error for connection')

def main():
    previewText = Figlet(font='slant') 
    print(previewText.renderText('by Horrible'))
    ip = input("Enter ip: ")
    
    getInfoByIp(ip)

if __name__ == '__main__':
    main()