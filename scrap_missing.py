from scrapper import parse_post

urls = [
'https://forums.developer.nvidia.com/t/using-bin-file-after-tensorrt-optimization/129330',

]
for url in urls:
    print(parse_post(url))