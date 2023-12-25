import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

def validate_args(FILE, MASK):
    """Validates if both `FILE` and `MASK` arguments exist.

    Args:
    FILE: The path to the text file.
    MASK: The path to the mask image.

    Returns:
    True if both arguments exist, False otherwise.
    """

    if not os.path.exists(FILE):
        FILE = "files/self_appreciation_2023.txt"
        return False

    if not os.path.exists(MASK):
        MASK = "images/masks/cloud.png"
        return False

    return True


def wordcloud_generator(FILE, MASK):
    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # Read the whole text.
    text = open(path.join(d, FILE)).read()

    # read the mask image
    image_mask = np.array(Image.open(path.join(d, MASK)))

    stopwords = set(STOPWORDS)

    # Customize my Wordcloud
    stopwords.add('smile')
    stopwords.add('legs')

    wc = WordCloud(background_color="white", max_words=6000, mask=image_mask,
                stopwords=stopwords, contour_width=3, contour_color='steelblue',
                collocations=False, max_font_size=100)

    # generate word cloud
    text_generated = wc.generate(text)

    # store to file
    wc.to_file(path.join(d, "images/gil_self.png"))

    # show
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.figure()
    plt.imshow(image_mask, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis("off")
    plt.show()


'''
Generates a word cloud from a text file.

Args:
  FILE: The path to the text file.
  MASK: The path to the mask image.
'''

# Read args
FILE = sys.argv[1]
MASK = sys.argv[2]

if validate_args(FILE, MASK):
  # Both arguments exist.
  wordcloud_generator(FILE, MASK)
else:
  # One or both arguments do not exist.
  print("One or both arguments do not exist -> using default values.")