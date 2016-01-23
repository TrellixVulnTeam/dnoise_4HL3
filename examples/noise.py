import code.utils
import code.noise
import os
import urllib


root_path = '../data'
img_url = 'http://sipi.usc.edu/database/download.php?vol=misc&img=4.2.04'
img_name = 'Lenna.tiff'
img_path = os.path.join(root_path, img_name)

if not os.path.exists(root_path):
    os.makedirs(root_path)

if not os.path.exists(img_path):
    urllib.urlretrieve(img_url, img_path)

image = code.utils.Image(path=img_path)
noisy = image.noisy(code.utils.GaussianNoise(std=0.5))

x = image.get()
y = noisy.get()

print code.noise.mse(x, y)
print code.noise.psnr(x, y)
print code.noise.ssim(x, y)
