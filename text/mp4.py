import urllib.request
import urllib.parse
# from . import setting
# def publicity_system(self):
#     # company_name = '浙江大成工程项目管理有限公司'
#     # header = self.random_header()
#     url = 'https://apd-eaa2e5230fde9c9f670e04710d69cb27.v.smtcdns.com/vhot2.qqvideo.tc.qq.com/AcpYqDNuLd_1q7XuCKP1bwUCVAFbih3qyDumG43hJyi4/uwMROfz0r5zA4aQXGdGnC2dfDmY9yfV170dnketddn1Q9gxX/u0323i1dwko.mp4?sdtfrom=v1104&guid=67862235c2ffcf1e20cb4a79e6e17d5f&vkey=730B3CB4C17F90C049909624A5C8FB3226E9AD0C5C04F8422DEC8587746E958FD3A13DEEE5D193A01A5D12271C006D7A87421E08A2A00DBB0F668DC3242EAAA87327841E9F2D4E9D7185730EC79C22B16BB028FD7FFA3F4596DF42E0F21346E8A9C14B101863B41F0FE2F70C3750F4127629892B253049CF'
#     self.headers = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
#     }
#     # zz = urllib.parse.urlencode(data).encode(encoding='UTF8')
#     request = urllib.request.Request(url, headers=self.headers)
#     response = urllib.request.urlopen(request)
#     json_data = response.text
#     print(json_data,)
#
#
#
url = 'https://apd-eaa2e5230fde9c9f670e04710d69cb27.v.smtcdns.com/vhot2.qqvideo.tc.qq.com/AcpYqDNuLd_1q7XuCKP1bwUCVAFbih3qyDumG43hJyi4/uwMROfz0r5zA4aQXGdGnC2dfDmY9yfV170dnketddn1Q9gxX/u0323i1dwko.mp4?sdtfrom=v1104&guid=67862235c2ffcf1e20cb4a79e6e17d5f&vkey=730B3CB4C17F90C049909624A5C8FB3226E9AD0C5C04F8422DEC8587746E958FD3A13DEEE5D193A01A5D12271C006D7A87421E08A2A00DBB0F668DC3242EAAA87327841E9F2D4E9D7185730EC79C22B16BB028FD7FFA3F4596DF42E0F21346E8A9C14B101863B41F0FE2F70C3750F4127629892B253049CF'
import requests
import os

def download_video(url):
    try:
        print('准备下载视频:'+url)
        headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
                }
        response = requests.get(url, headers=headers)
        data = response.content
        if data:
            file_path = 'Dai_hao.mp4'
            print('文件为:'+file_path)
            if not os.path.exists(file_path):
                with open(file_path, 'wb')as f:
                    f.write(data)
                    f.close()
                    print('视频下载成功:'+url)
    except Exception:
        print('视频下载失败')
download_video(url)