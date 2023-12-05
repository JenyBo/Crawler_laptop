import requests
from bs4 import BeautifulSoup

# URL của trang web bạn muốn fetch dữ liệu
url = "https://www.dienmayxanh.com/Product/GetGalleryItemInPopup?productId=309822&isAppliance=false&galleryType=5&colorId=0"

# Headers tương tự như trong mã JavaScript của bạn
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"118\", \"Microsoft Edge\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest",
    "cookie": "_gcl_au=1.1.738031116.1698070583; _pk_id.8.8977=dcf548d406f21758.1698070584.; _fbp=fb.1.1698070583670.1429305075; MWG_CART_ID=6a32a2e531eb4a5ebedd; DMX_Personal=%7B%22UID%22%3A%221fac04c179c418c0dffc5b5a92beea5c94fb8c7e%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; MWG_PRODUCT_BASIC_DB=9r8paGEY6dsXxZQiWvu3NnW7JWyQ_vhxn%2Fjcr4RHWf4CrDGAbzGUNQ--; lhc_per=vid|8eabefd1b53b5a98f97b; DMX_View=DESKTOP; ck_idcompare=; _hjid=6a271feb-5574-4136-837d-c6a15a68cfbb; _hjSessionUser_34921=eyJpZCI6ImYyYzA0ZTMyLTM3NzAtNTRkNy1hN2Y3LTIxMTU3ZjQwNWI3MyIsImNyZWF0ZWQiOjE2OTgwNzEyMjYzNTMsImV4aXN0aW5nIjp0cnVlfQ==; _gcl_aw=GCL.1698219711.CjwKCAjw-eKpBhAbEiwAqFL0mso0Sat2AxBned7-K8_r7SFD1fyd0cj33yDiNj2KWJww1cH_vrV9FRoCT94QAvD_BwE; _gac_UA-38936689-1=1.1698219712.CjwKCAjw-eKpBhAbEiwAqFL0mso0Sat2AxBned7-K8_r7SFD1fyd0cj33yDiNj2KWJww1cH_vrV9FRoCT94QAvD_BwE; _utm_thegioididong=6aeaad7c-5b7b-4e4e-9728-e2dd0c0d8998; TBMCookie_3209819802479625248=650811001699101879K62XsYnsy5M2oU/d2DuvU2fogto=; ___utmvm=###########; .AspNetCore.Antiforgery.vxaTqZ_mpZk=CfDJ8LGxpY5S4oNOtwPjcnJpYZ_RNI-gh6u5B8T-DqnuTUaDr2I_QwrM_gfArRLipYJlEqFBp9d8I_qodijVfo3fh-RG3jTqQURhBwJaOPFbrqLnnalk8fzTOAUiYRelqYtB17BeTydkIZK8pg3-LGGTBqM; _gid=GA1.2.642907606.1699101881; _pk_ref.8.8977=%5B%22%22%2C%22%22%2C1699101881%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.8.8977=1; _ce.irv=false; cebs=1; __zi=3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXar4Am7k4lUJMK0Z9S8RnvD9MGyXpW_Jjrb94o0.1; _ce.clock_event=1; _ce.clock_data=104%2C42.115.239.106%2C1%2C67bfd2dfdba18bd2d40c958d4aa22109; cebsp_=5; _gat_UA-38936689-1=1; _ga_5MXNSQHGT3=GS1.2.1699101881.6.1.1699102425.60.0.0; _ce.s=v~3c2727d2ad3e3313dbb9deab49124db72a517c48~lcw~1699102434087~vpv~4~v11.fhb~1698158841771~v11.lhb~1698158902253~lva~1699101881476~v11.cs~218102~v11.s~ecb058d0-7b0f-11ee-a3af-ade24fc24e2e~v11.sla~1699102434088~gtrk.la~lok1pwrq~v11.send~1699102433991~lcw~1699102434089; _ga=GA1.2.1576400894.1698070583; SvID=dmxcart2772|ZUY+5|ZUY8u; _ga_Y7SWKJEHCE=GS1.1.1699101880.7.1.1699102435.59.0.0",
    "Referer": "https://www.dienmayxanh.com/laptop/asus-vivobook-go-15-e1504fa-r5-nj630w",
    "Referrer-Policy": "no-referrer-when-downgrade",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0"
}

# Gửi yêu cầu GET với headers
response = requests.get(url, headers=headers)

# Sử dụng BeautifulSoup để parse nội dung trang web
soup = BeautifulSoup(response.text, 'html.parser')

# Bây giờ bạn có thể xử lý dữ liệu ở đây theo nhu cầu của bạn.
print(soup)
