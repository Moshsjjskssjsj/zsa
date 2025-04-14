import requests
import requests
import time
import re
import requests
import random
import names
from faker import Faker
import time

BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
BLACK = "\033[30m"
RESET = "\033[0m"





#mail=str(input("Enter Your Mail: "))

BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
red ="\033[31m"
logo="""


░▒▓█▓▒░░▒▓██████▓▒░  
░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░▒▓█▓▒▒▓███▓▒░ 
░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓██████▓▒░  
                     
 Tools: Auto IG Create
 version:1.1.0
 Author: Devil OP
 Channel: Team Devil                    

"""

print(logo)
print(f"******************\n\n")
amo=int(input(red+f"Enter Your Amount: {RESET}"))
print(f"******************\n")

for i in range(amo):
    fake = Faker()
    user= fake.user_name()
    rand = str(random.randint(111, 999))
    first_name = names.get_first_name()
    username=user+rand+first_name
    Password=("Account Password:145680")
    print(f"{BLUE}Account Username: {GREEN} {username} {RESET}")
    print(f"{BLUE}Account Password: {GREEN} 145680 {RESET}")



    cookies = {
        'visited': '1742624202.763664',
        'cf_clearance': 'JBJAj.tehsGo8f5vR3bxTaEXSfQVk40_YuCu_p81B4Q-1742624206-1.2.1.1-6fnSbw1cf7Kw3zIA76AjRTL17xUeXeuL2RdRfYoTb.77lDkYxEdSlNCWEgZ5egQhw8cZCCqcD0QdGfzikxd9ivGMcPlRDfT1fEA_A9w_FJyVKaAaGeW9vevb.k13DpHJj4.0rU2eE8izvZtIQaC38YRNGi4Ag8h5p7yJ04YX41PE8idEBGoOBcgLxEfs76_UZnxW39sTZ0FmES9qjTl0ZL9d9Opo0BGSuHtCf6ahT_EMkbE2pLTbJ7D8lRTbfDSoS5hnHfzK83Cdf_du0TEqI4tP1S8mdYE1oSiCj664ga_kgjFoDO5dPuK9_CaAq0ZJwZDi1XDaatUsxDELVbetvEdhlkovUoJ_WZQmuWjiIME',
    }

    headers = {
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/x-www-form-urlencoded',
      'origin': 'https://mails.org',
      'priority': 'u=1, i',
      'referer': 'https://mails.org/',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
      # 'cookie': 'visited=1742624202.763664; cf_clearance=JBJAj.tehsGo8f5vR3bxTaEXSfQVk40_YuCu_p81B4Q-1742624206-1.2.1.1-6fnSbw1cf7Kw3zIA76AjRTL17xUeXeuL2RdRfYoTb.77lDkYxEdSlNCWEgZ5egQhw8cZCCqcD0QdGfzikxd9ivGMcPlRDfT1fEA_A9w_FJyVKaAaGeW9vevb.k13DpHJj4.0rU2eE8izvZtIQaC38YRNGi4Ag8h5p7yJ04YX41PE8idEBGoOBcgLxEfs76_UZnxW39sTZ0FmES9qjTl0ZL9d9Opo0BGSuHtCf6ahT_EMkbE2pLTbJ7D8lRTbfDSoS5hnHfzK83Cdf_du0TEqI4tP1S8mdYE1oSiCj664ga_kgjFoDO5dPuK9_CaAq0ZJwZDi1XDaatUsxDELVbetvEdhlkovUoJ_WZQmuWjiIME',
    }

    data = {
      'token': '0f7e934473a4dadc4955203f8900b879',
      'timestamp': '1742629842',
      'hash': '46304af6e0462b516c0807144f34f4fa8f2589a1efee10eaafd15ce8a48322d9',
    }

    response = requests.post('https://mails.org/api/email/delete', cookies=cookies, headers=headers, data=data)
    mail=(response.json() ['message'])
    token=(response.json() ['token'])

    #print("{BLUE}Account Username: {GREEN} {username} {RESET}")





    url = "https://www.instagram.com/api/v1/accounts/send_verify_email/"

    payload = {
      'device_id': "Z9ui8wABAAGF8JvKCz2ja6d-8sRF",
      'email': f"{mail}",
      'jazoest': "22811"
    }

    headers = {
      'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36",
      'sec-ch-ua-full-version-list': "\"Chromium\";v=\"134.0.0.0\", \"Not:A-Brand\";v=\"24.0.0.0\", \"Brave\";v=\"134.0.0.0\"",
      'sec-ch-ua-platform': "\"Android\"",
      'sec-ch-ua': "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Brave\";v=\"134\"",
      'sec-ch-ua-model': "\"\"",
      'sec-ch-ua-mobile': "?1",
      'x-ig-app-id': "1217981644879628",
      'x-requested-with': "XMLHttpRequest",
      'x-instagram-ajax': "1021172622",
      'x-csrftoken': "IABNpcFm9iP0BqX98QfsaJeSFhusvokJ",
      'x-web-session-id': "3tpmom:l2jkic:4dy536",
      'x-asbd-id': "359341",
      'x-ig-www-claim': "hmac.AR3l2VExfkPaEmnGfSGDaCoBJzLWurqpKZ_TX1oGKKeoOuR9",
      'sec-ch-ua-platform-version': "\"13.0.0\"",
      'sec-gpc': "1",
      'accept-language': "en-US,en;q=0.9",
      'origin': "https://www.instagram.com",
      'sec-fetch-site': "same-origin",
      'sec-fetch-mode': "cors",
      'sec-fetch-dest': "empty",
      'referer': "https://www.instagram.com/accounts/signup/email/",
      'priority': "u=1, i",
      'Cookie': "ig_did=6D271D6C-4818-46FE-AD79-824A93C6E486; datr=86LbZ2_VVlDLdkKC-OXIHNMI; dpr=3; mid=Z9ui8wABAAGF8JvKCz2ja6d-8sRF; ps_l=1; ps_n=1; ig_nrcb=1; rur=\"VLL\\05473487778148\\0541774273472:01f7da7d6125bbf6d739d61fb42ab66056c62254c7f9ceaa312cde5d1db5e7d7e6706422\"; csrftoken=IABNpcFm9iP0BqX98QfsaJeSFhusvokJ; wd=360x640"
    }

    response = requests.post(url, data=payload, headers=headers)

    #print(response.text)




    #code=input("Enter Your Code: ")

    cookies = {
        'visited': '1742624202.763664',
        'cf_clearance': 'JBJAj.tehsGo8f5vR3bxTaEXSfQVk40_YuCu_p81B4Q-1742624206-1.2.1.1-6fnSbw1cf7Kw3zIA76AjRTL17xUeXeuL2RdRfYoTb.77lDkYxEdSlNCWEgZ5egQhw8cZCCqcD0QdGfzikxd9ivGMcPlRDfT1fEA_A9w_FJyVKaAaGeW9vevb.k13DpHJj4.0rU2eE8izvZtIQaC38YRNGi4Ag8h5p7yJ04YX41PE8idEBGoOBcgLxEfs76_UZnxW39sTZ0FmES9qjTl0ZL9d9Opo0BGSuHtCf6ahT_EMkbE2pLTbJ7D8lRTbfDSoS5hnHfzK83Cdf_du0TEqI4tP1S8mdYE1oSiCj664ga_kgjFoDO5dPuK9_CaAq0ZJwZDi1XDaatUsxDELVbetvEdhlkovUoJ_WZQmuWjiIME',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://mails.org',
        'priority': 'u=1, i',
        'referer': 'https://mails.org/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
        # 'cookie': 'visited=1742624202.763664; cf_clearance=JBJAj.tehsGo8f5vR3bxTaEXSfQVk40_YuCu_p81B4Q-1742624206-1.2.1.1-6fnSbw1cf7Kw3zIA76AjRTL17xUeXeuL2RdRfYoTb.77lDkYxEdSlNCWEgZ5egQhw8cZCCqcD0QdGfzikxd9ivGMcPlRDfT1fEA_A9w_FJyVKaAaGeW9vevb.k13DpHJj4.0rU2eE8izvZtIQaC38YRNGi4Ag8h5p7yJ04YX41PE8idEBGoOBcgLxEfs76_UZnxW39sTZ0FmES9qjTl0ZL9d9Opo0BGSuHtCf6ahT_EMkbE2pLTbJ7D8lRTbfDSoS5hnHfzK83Cdf_du0TEqI4tP1S8mdYE1oSiCj664ga_kgjFoDO5dPuK9_CaAq0ZJwZDi1XDaatUsxDELVbetvEdhlkovUoJ_WZQmuWjiIME',
    }

    data = {
        'last_cache_id': '0',
        'token': f'{token}',
        'timestamp': '1742629843',
        'hash': '69a738018384d4beb83ab7ff0a31bb792feb87b700018b1d5babcd6943f7841a',
    }

    time.sleep(10)
    response = requests.post('https://mails.org/api/email/inbox', cookies=cookies, headers=headers, data=data)
    datas=(response.json() ['emails'])

    import json
    for key in datas:
        subject = datas[key]['subject']
        code = subject.split(' ')[0] 
        print(f"{BLUE}Email Verify Code: {GREEN} {code} {RESET}")


    url = "https://www.instagram.com/api/v1/accounts/check_confirmation_code/"

    payload = {
      'code': code,
      'device_id': "Z9ui8wABAAGF8JvKCz2ja6d-8sRF",
      'email': f"{mail}",
      'jazoest': "22912"
    }

    headers = {
      'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36",
      'Accept-Encoding': "gzip, deflate, br, zstd",
      'sec-ch-ua-full-version-list': "\"Chromium\";v=\"134.0.0.0\", \"Not:A-Brand\";v=\"24.0.0.0\", \"Brave\";v=\"134.0.0.0\"",
      'sec-ch-ua-platform': "\"Android\"",
      'sec-ch-ua': "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Brave\";v=\"134\"",
      'sec-ch-ua-model': "\"\"",
      'sec-ch-ua-mobile': "?1",
      'x-ig-app-id': "1217981644879628",
      'x-requested-with': "XMLHttpRequest",
      'x-instagram-ajax': "1021172622",
      'x-csrftoken': "mUPMUA9doDWz0ybqsUmK9zs2tdvuOY8S",
      'x-web-session-id': "zpjrlm:l2jkic:mzg1c2",
      'x-asbd-id': "359341",
      'x-ig-www-claim': "0",
      'sec-ch-ua-platform-version': "\"13.0.0\"",
      'sec-gpc': "1",
      'accept-language': "en-US,en;q=0.9",
      'origin': "https://www.instagram.com",
      'sec-fetch-site': "same-origin",
      'sec-fetch-mode': "cors",
      'sec-fetch-dest': "empty",
      'referer': "https://www.instagram.com/accounts/signup/emailConfirmation/?next=%2Faccounts%2Flogout%2F",
      'priority': "u=1, i",
      'Cookie': "ig_did=6D271D6C-4818-46FE-AD79-824A93C6E486; datr=86LbZ2_VVlDLdkKC-OXIHNMI; dpr=3; mid=Z9ui8wABAAGF8JvKCz2ja6d-8sRF; ps_l=1; ps_n=1; ig_nrcb=1; csrftoken=mUPMUA9doDWz0ybqsUmK9zs2tdvuOY8S; ds_user_id=73149577685; wd=360x640"
    }

    response = requests.post(url, data=payload, headers=headers)
    #print(response.text)
    signup=response.json() ['signup_code']



    import requests

    url = "https://www.instagram.com/api/v1/web/accounts/web_create_ajax/"

    payload = {
      'enc_password': "#PWD_INSTAGRAM_BROWSER:10:1742737462:AZ5QAP3s1A8k46qERB+msSWgnthKKx2T5UPgUVSocrVulwd9VNP+MRdmXGSC/icvLbVOOJuf14VCfmbbSpOBysavuc2KJhzGnIJwOwVRvjhO//fVxWAl9RMAt2vFXZNUWwlhzlym8lVxcQ==",
      'day': "29",
      'email': f"{mail}",
      'failed_birthday_year_count': "{}",
      'first_name': f"{first_name}",
      'month': "11",
      'username': f"{username}",
      'year': "1997",
      'client_id': "Z9ui8wABAAGF8JvKCz2ja6d-8sRF",
      'seamless_login_enabled': "1",
      'tos_version': "row",
      'force_sign_up_code': f"{signup}",
      'extra_session_id': "mf656s:l2jkic:mzg1c2",
      'jazoest': "22912"
    }

    headers = {
      'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36",
      'sec-ch-ua-full-version-list': "\"Chromium\";v=\"134.0.0.0\", \"Not:A-Brand\";v=\"24.0.0.0\", \"Brave\";v=\"134.0.0.0\"",
      'sec-ch-ua-platform': "\"Android\"",
      'sec-ch-ua': "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Brave\";v=\"134\"",
      'sec-ch-ua-model': "\"\"",
      'sec-ch-ua-mobile': "?1",
      'x-ig-app-id': "1217981644879628",
      'x-requested-with': "XMLHttpRequest",
      'x-instagram-ajax': "1021172622",
      'x-csrftoken': "mUPMUA9doDWz0ybqsUmK9zs2tdvuOY8S",
      'x-web-session-id': "mf656s:l2jkic:mzg1c2",
      'x-asbd-id': "359341",
      'x-ig-www-claim': "0",
      'sec-ch-ua-platform-version': "\"13.0.0\"",
      'sec-gpc': "1",
      'accept-language': "en-US,en;q=0.9",
      'origin': "https://www.instagram.com",
      'sec-fetch-site': "same-origin",
      'sec-fetch-mode': "cors",
      'sec-fetch-dest': "empty",
      'referer': "https://www.instagram.com/accounts/signup/username/?next=%2Faccounts%2Flogout%2F",
      'priority': "u=1, i",
      'Cookie': "ig_did=6D271D6C-4818-46FE-AD79-824A93C6E486; datr=86LbZ2_VVlDLdkKC-OXIHNMI; dpr=3; mid=Z9ui8wABAAGF8JvKCz2ja6d-8sRF; ps_l=1; ps_n=1; ig_nrcb=1; csrftoken=mUPMUA9doDWz0ybqsUmK9zs2tdvuOY8S; ds_user_id=73149577685; wd=360x640"
    }

    response = requests.post(url, data=payload, headers=headers)

    print(response.json())
