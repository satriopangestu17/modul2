# pip3 install plotly -U
# untuk install package
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = 'browser'
import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([2,1,4,1,3])
myFig = go.Figure(
    data = go.Bar(x=x, y=y)
)

myFig.show()  ##klik knan view source
myFig.write_html('plotlyTes.html', auto_open=True)

# flask, server back end
# bikin server jangan kerjakan di server seperti jupyter lab

