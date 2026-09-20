import urllib.request
import os

images = {
    "W.png": "https://blogthumb.pstatic.net/MjAyMTA3MDZfMTQ4/MDAxNjI1NTc1MDU2ODM2.Ci1E5lfChHM610pp-IyplMMdsZOYmr4lwJZTb5mFscwg.pXxU_Yf1nlLtA2KtH0oOFl9elb0pyNs-Y2MVfwQlqZog.PNG.gigi905/W.png?type=w2",
    "WW.png": "https://postfiles.pstatic.net/MjAyMTA3MDZfMTE1/MDAxNjI1NTc0OTQ5NjY4.N-wQ-FAp1So7ekdAdhDeiF-Mo3HGvLzN3pZbO9IVYDsg.ngzcXLLnzw5itNERao40juxwtM_cw6MCuwAu3ZnNnOYg.PNG.gigi905/WW.png",
    "WWW.png": "https://postfiles.pstatic.net/MjAyMTA3MDZfMjA2/MDAxNjI1NTc0OTUwODU3.xeq0zUB9qkmeC35Lv7dNokNulFHnPCQhQe__Lb4WXwgg.NM6K61jdMPv3BYgKMYClBCHh5G2nGpRq44TnFa3WG-wg.PNG.gigi905/WWW.png",
    "A.png": "https://postfiles.pstatic.net/MjAyMTA3MDZfMjMw/MDAxNjI1NTc0OTQyODU4.Thqs3GVOiehBwsvFD0dlk3CdfgZeLjZeYvt661TPCoUg.CbEW85eBPXduHEIaFA3pT8hpipaxF7xb3E2l-TktHW0g.PNG.gigi905/A.png",
    "AA.png": "https://postfiles.pstatic.net/MjAyMTA3MDZfNTEg/MDAxNjI1NTc0OTQzMTE2.dgG8wUer32CIcvQf4MnVhX7MBLoXk711DiGfSVYDhfcg.G41who8EMwrkeiNt_M6mkJb3HkPNky8-vzS0BVFQV-Ig.PNG.gigi905/AA.png",
    "AAA.png": "https://postfiles.pstatic.net/MjAyMTA3MDZfMTM5/MDAxNjI1NTc0OTQ2MjM1.hXJpVPAPJ_GygAmLuT47TXbvpj-I1Epi92KDq4x5bk4g.tPugjhFp0yoAiMxdm4Ob8Fs3Ee3dZbLQxGPnSgKHgvwg.PNG.gigi905/AAA.png",
    "M.png": "https://postfiles.pstatic.net/MjAyMTA3MDZfMTYw/MDAxNjI1NTc0OTQ2NTA3.UAS1JkFXhrztgfuwMAqyDFgfcPRswDvuNcAgiCryY9cg._UzH-zmBLW19Zll_xNR6R6Y25V32zZvm3Pf8hXYxcTEg.PNG.gigi905/M.png",
    "MM.png": "https://postfiles.pstatic.net/MjAyMTA3MDZfMTIx/MDAxNjI1NTc0OTQ3MzYw.7X5-v0CXT_VnSefeFOKwWjwGmNN34-6mx9uRqhWRk_8g.LCH327FDywHHyQVEdx5H0M3rOiNmwoEJMaFbjVejU4og.PNG.gigi905/MM.png",
    "MMM.png": "https://postfiles.pstatic.net/MjAyMTA3MDZfNDkg/MDAxNjI1NTc0OTQ4MDQx.LAgh_ddFiX3y4pFGiTwBDyi6AczVr5kfwLoSSNc-mEEg.wtWNmurOrPOy0bNLXrqzET210tWrmEiyGDD1rwMOTX0g.PNG.gigi905/MMM.png",
    "MA.png": "https://postfiles.pstatic.net/MjAyMTA3MDZfMjI2/MDAxNjI1NTc0OTQ2ODAz.6lEU8fvhnEXt-5PqShvltHAiWeJ0K0eEM2Jejjg9ld8g.K5vj2Z7F7tNwPYFJsCXcfJKqzMi5PJORLulITDtUmkIg.PNG.gigi905/MA.png",
    "MMA.png": "https://postfiles.pstatic.net/MjAyMTA3MDZfMjg0/MDAxNjI1NTc0OTQ3NTgw.dtJ4GBmm_mpBoLVj67snncjTkOdXfHr-AR3TIq_IZAIg.jRToguuXiw3BttFGchHzLpUim8d5jo7NYLIrtOOY7UMg.PNG.gigi905/MMA.png",
    "MAA.png": "https://postfiles.pstatic.net/MjAyMTA3MDZfMTg4/MDAxNjI1NTc0OTQ3MTE4.EK2Ryglns50EWZwuvDBxZ53B5gtHU6ID5FPVSbqAXLwg.2usUklFbxcgkpi5N28-3RcD8WxlR4wAkw_0P_PUx25og.PNG.gigi905/MAA.png",
    "WM.png": "https://postfiles.pstatic.net/MjAyMTA3MDZfMTE1/MDAxNjI1NTc0OTQ4OTU5.CfNgKx6ywfnctu1OXO45_8_gDTTzuMgJEohglH-x95og.AQM4Zp_Q9EQkPSjvrq4dMB6qlK0vh4r9zNKMzutjdzUg.PNG.gigi905/WM.png",
    "WWM.png": "https://postfiles.pstatic.net/MjAyMTA3MDZfMiAg/MDAxNjI1NTc0OTUwMzYw.cTLre0mksfWtaaRg0Q6fczGL4dfznUaTUIzYVLOSnZUg.gI6h1lpTFX1NnPNRan9Ewr5BC8dDbF_DJ50ccI5_YuUg.PNG.gigi905/WWM.png",
    "WMM.png": "https://postfiles.pstatic.net/MjAyMTA3MDZfMTM3/MDAxNjI1NTc0OTQ5NDI4.FO_4d6J6Tw-v1y7hMnYer_RXZNW9LBJoitMOHf4fSTIg.eooJqLNInX0IRRomlyw76--EXHTnp2rwyDmtofh6gsEg.PNG.gigi905/WMM.png",
    "WA.png": "https://postfiles.pstatic.net/MjAyMTA3MDZfMTc5/MDAxNjI1NTc0OTQ4NTI3._4uZQYNeXJjhAmoEWhgeWSn7_Fx6-M2P_bzhtsipwyQg.pkRaW_YkPoDWV6fN6nVVoVrZt5UmlM-a77RVdxG3GOwg.PNG.gigi905/WA.png",
    "WWA.png": "https://postfiles.pstatic.net/MjAyMTA3MDZfMTAz/MDAxNjI1NTc0OTQ5OTA0.xDselkcynHNidvJ4HCFHPc2Dc0ctQNL1SFZWRFdt7lsg.DrOug-VQNXWaYGT5UZ3UVjXw1OYTNVjHyAG_gTRNCxEg.PNG.gigi905/WWA.png",
    "WAA.png": "https://postfiles.pstatic.net/MjAyMTA3MDZfMTkz/MDAxNjI1NTc0OTQ4NzM3.Jmlxu0QQOpiFGpIWKY6Oix8jGVbVO_BP8f_D21sAqvQg.qAxXYC5pVljXOVlNkoqQ6zlwveH6gvPOGcoVRWyWlEUg.PNG.gigi905/WAA.png",
    "WMA.png": "https://postfiles.pstatic.net/MjAyMTA3MDZfNTAg/MDAxNjI1NTc0OTQ5MTk1.SLIbdH4j-o8i0kFmKNQ0AUqf6BrElBbzHgWVlj5k_7cg.bJXrFVidBMXvTg8Cf3IePJIcmZwKVd4MDyBNO2zGH4kg.PNG.gigi905/WMA.png",
    "MMAA.png": "https://postfiles.pstatic.net/MjAyMTA3MDZfODcg/MDAxNjI1NTc0OTQ3ODEw.m-3-ieTVj8vTO60xIR7pQW2lPvB80LXzr3H4qh_irkgg.YS4rIMrYHOJaQMRIXkWe7i4MUoX9trdZi7lSXmgfKZog.PNG.gigi905/MMAA.png",
    "WWMM.png": "https://postfiles.pstatic.net/MjAyMTA3MDZfNDAg/MDAxNjI1NTc0OTUwNTg3.umWoc9ZfHAf451icrlN7M5pcZLbRzIQ6foHDUVvIDC4g.8br_IVoCwSSarUwFFmw3GjBwwut5BvUtrlOgpdg1324g.PNG.gigi905/WWMM.png",
    "WWAA.png": "https://postfiles.pstatic.net/MjAyMTA3MDZfNjkg/MDAxNjI1NTc0OTUwMTE3.icxNV5Jzm-myIhGaAtLibkzTQ35ppP6MjLkgCqG-hzYg.g62Wt_bHRSF31SgMPSxDXWPsduakWe-11cvKnCqow54g.PNG.gigi905/WWAA.png",
}

headers = {'User-Agent': 'Mozilla/5.0'}
for fname, url in images.items():
    path = os.path.join('images', 'jobs', fname)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp, open(path, 'wb') as out:
            out.write(resp.read())
        print(f"Downloaded: {fname} ({os.path.getsize(path)} bytes)")
    except Exception as e:
        print(f"Failed {fname}: {e}")
