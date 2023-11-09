from bs4 import BeautifulSoup
import requests
import smtplib

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                         " Chrome/114.0.0.0 Safari/537.36",
           "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7,uz;q=0.6,en-GB-oxendict;q=0.5"}

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
price = float(soup.find(name="span", class_="a-offscreen").getText().split("$")[1])

title = soup.find(id="productTitle").get_text().strip()
BUY_PRICE = 90

if price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("shaxzodbotirjonov5@gmail.com", "zulwidoddoegykjy")
        connection.sendmail(
            from_addr="shaxzodbotirjonov5@gmail.com",
            to_addrs="shaxzodbotirjonov5@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
