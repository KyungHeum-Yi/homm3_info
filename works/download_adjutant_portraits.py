import urllib.request
import os

images = {
    "팔라딘.png": "https://blogfiles.pstatic.net/MjAyMTAzMjhfMjI3/MDAxNjE2OTM2MTY5MzY3.MUDXKFjwV0EUd9sE3O3itYbYW1Ly1720Ihf_dsieQ38g.kLg_CZOZsDk1AG6FooNaWbKjIc9UE8heD7aRV3tNw3Ug.PNG.gigi905/1616936108.png",
    "교주.png": "https://blogfiles.pstatic.net/MjAyMTAzMjhfMTU2/MDAxNjE2OTM2MTY5NjAy.zDxrhlxsvpECst8OW7xk13Anw1K5vTST3Twu0QC1XMcg.3_9invI20krDQT4U674HKmkLLEo6z2hrdeMM8-vmy3Yg.PNG.gigi905/1616936112.png",
    "템플 가디언.png": "https://blogfiles.pstatic.net/MjAyMTAzMjhfMTMx/MDAxNjE2OTM2MTY5ODI3.7p4oGw_emtzCZ7boXl8ze4BaiVye97yFz9dGP_5lUSUg.6-cMZtXFovyqW5QMQQ_ukFEsQxAXsLtG_OYHMGWS7FAg.PNG.gigi905/1616936115.png",
    "서큐버스.png": "https://blogfiles.pstatic.net/MjAyMTAzMjhfMjg3/MDAxNjE2OTM2MTcwMDU2.-j2KijlncaKDZDcqHO5AJQk2zw-zNAO-S5-Ky9rTI24g.g-pPFsJ-prLWr1WnXCXsqMW7iK-_bh0EC5zGBDw1bh8g.PNG.gigi905/1616936118.png",
    "소울 이터.png": "https://blogfiles.pstatic.net/MjAyMTAzMjhfMjk0/MDAxNjE2OTM2MTcwMzAz.NYNWmjji0W4X3I4hiSUvVo6Jz6fqnw3d2BoNFYXS-bEg.e3kln8grcNoE4DOx8UYX9N_oedqY1PJhxIDWlp3DBFEg.PNG.gigi905/1616936120.png",
    "브루트.png": "https://blogfiles.pstatic.net/MjAyMTAzMjhfMjYy/MDAxNjE2OTM2MTcwNTU0.IcW0ME687blCHpJxYoNQobgrO_0Pj-RAdLpcXdhtkwIg.MjaeStbRz7LpN2fm5J68sk4O4js5mNVuLC_aDV9F-BQg.PNG.gigi905/1616936122.png",
    "오우거 리더.png": "https://blogfiles.pstatic.net/MjAyMTAzMjhfMzIg/MDAxNjE2OTM2MTcwNzg4.WmsvsnoJc2U5XIGnph0UohOxhVQNvdpFwqjuhomMDl4g.OKvljSqEFyEp44Vs5r8nmGsAbyyzLSipfI3a8ff30CIg.PNG.gigi905/1616936124.png",
    "도마뱀 리더.png": "https://blogfiles.pstatic.net/MjAyMTAzMjhfMTU2/MDAxNjE2OTM2MTcxMDM5._oEua2VFWQD2NyLqJWQpgPc62oaGHq-vGlErBjUKQ_0g.n3JW9uNcPA7mS3Txj0gjdtG-KE66KwTrwLOPh1tUeUcg.PNG.gigi905/1616936128.png",
    "성령.png": "https://blogfiles.pstatic.net/MjAyMTAzMjhfMjIw/MDAxNjE2OTM2MTcxMjgw.fx2H8DBp_F4lXlt1oDm8tH0KG29GDU7GFJIrnw7Tnt8g.bzyVJeH8V0qcmYlvi-Bow626Epep26VokXA3VudrQqIg.PNG.gigi905/1616936130.png"
}

out_dir = os.path.join(os.path.dirname(__file__), "images", "부관_portrait")
os.makedirs(out_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0'}

for name, url in images.items():
    dst = os.path.join(out_dir, name)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = resp.read()
        with open(dst, "wb") as f:
            f.write(data)
        print(f"Downloaded {name} ({len(data)} bytes)")
    except Exception as e:
        print(f"Failed {name}: {e}")
