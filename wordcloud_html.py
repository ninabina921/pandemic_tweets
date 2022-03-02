from wordcloud import WordCloud
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import io
import urllib
import base64

def word_cloud(csv):
    df = pd.read_csv(csv)
    txt = ' '.join(df['tweet'])
    wc = WordCloud(width = 300, height = 200, random_state=1, background_color='black', colormap='Pastel1', collocations=False).generate(txt)
    buffer = io.BytesIO()
    wc.to_image().save(buffer, 'png')
    b64 = base64.b64encode(buffer.getvalue())
    image_64 = 'data:image/png;base64,' + urllib.parse.quote(b64)
    return image_64