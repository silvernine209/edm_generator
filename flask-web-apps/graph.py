import matplotlib.pyplot as plt
import io
import base64
import numpy as np

def build_graph(emotion_label, percentage):
    y_pos = np.arange(len(emotion_label))
    img = io.BytesIO()
    plt.bar(y_pos, percentage, color=('b', 'g', 'g', 'g', 'g', 'g', 'g'))
    plt.xticks(y_pos, emotion_label)
    plt.ylabel('Emotion')
    plt.title('Emotion Classification')
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)