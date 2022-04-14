from scrapper import parse_post
import tqdm
import pandas as pd
urls = [
'https://forums.developer.nvidia.com/t/using-bin-file-after-tensorrt-optimization/129330',
'https://forums.developer.nvidia.com/t/onnx-runtime-for-drive-agx-xavier/145676',
'https://forums.developer.nvidia.com/t/onnx-runtime-for-drive-px2/145684',
'https://forums.developer.nvidia.com/t/cross-compilation-using-boost-library/110663',
'https://forums.developer.nvidia.com/t/nvros/83775',
'https://forums.developer.nvidia.com/t/no-hdmi-signal-from-xavier-a/70602',
'https://forums.developer.nvidia.com/t/sdkmanager-0-9-9-flash-agx-failed/',
'https://forums.developer.nvidia.com/t/i-convert-opencvs-mat-to-dwimagecuda-but-the-dwlandmarkdetector-detectlandmarks-return-error/80746','https://forums.developer.nvidia.com/t/convert-cv-mat-to-dwimagecpu/70750'
'https://forums.developer.nvidia.com/t/installing-pip-on-drive-px2/73941',
'https://forums.developer.nvidia.com/t/tensorflow-installation-on-drive-px2/72076#5324624'
'https://forums.developer.nvidia.com/t/how-to-test-aurixcan/70979',
'https://forums.developer.nvidia.com/t/can-communication-terminates-using-can-utils-on-px2/52924'
]
data = []
for url in tqdm.tqdm(urls):
    # print(url)
    # if url[:38] != 'https://forums.developer.nvidia.com/t/': continue
    data.append(parse_post(url))
# print(data[0])
pd.DataFrame(
    {
        'url': [e[0] for e in data],
        'posts': [e[1] for e in data]
    }
).to_csv(f'missing.csv',index=False)
print(f'missing.csv saved') 
for url in urls:
    print(parse_post(url))