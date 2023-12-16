from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

FILE = 'datasets/daily_self_gil.txt'
MASK = 'images/masks/g.png'

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, FILE)).read()

# read the mask image
image_mask = np.array(Image.open(path.join(d, MASK)))

stopwords = set(STOPWORDS)
# print(stopwords)

wc = WordCloud(background_color="white", max_words=2000, mask=image_mask,
               stopwords=stopwords, contour_width=3, contour_color='steelblue')

# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "images/gil.png"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(image_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()