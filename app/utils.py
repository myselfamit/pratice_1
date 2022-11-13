import matplotlib.pyplot as plt
import base64
from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph =  base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(aa,aaa):
    plt.switch_backend('AGG')
    plt.figure(figsize=(15,25))
    plt.title('face8ook data')
    plt.plot(aa,aaa)
    plt.xlabel('numver')
    plt.ylabel('value')
    plt.tight_layout()
    graph = get_graph()
    return graph