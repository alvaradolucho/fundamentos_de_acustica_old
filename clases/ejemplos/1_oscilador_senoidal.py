import plotly.graph_objs as go
from plotly.subplots import make_subplots
from ipywidgets import interact

import numpy as np

# Define the initial x-axis values
t = np.linspace(0, 2, 400)

# Define the figure layout
fig = make_subplots(rows=1, cols=1)
fig.update_layout(
    title='Oscilador Senoidal',
    xaxis_title='Tiempo (s)',
    yaxis_title='Amplitud',
    yaxis_range=[-1, 1]
)

# Define the trace for the sine wave
trace = go.Scatter(x=t, y=np.sin(t), mode='lines', name='Onda Senoidal')

# Add the trace to the figure
fig.add_trace(trace)

# Define the interactive function to update the frequency and amplitude of the sine wave
@interact(frecuencia=(1, 10, 0.01), amplitud=(-1, 1, 0.01), phase=(0, 2*np.pi, 0.01))
def update_sine_wave(frecuencia, amplitud, phase):
    # Update the y-values of the trace based on the new frequency and amplitude
    fig.data[0].y = amplitud * np.sin(2 * np.pi * frecuencia * t + phase)
    fig.update_layout(title='Onda Senoidal: $A(t) = ' + str(round(amplitud, 1)) + '\cdot\sin(2\pi\cdot ' + str(round(frecuencia, 1)) +' t  + ' + str(round(phase, 1)) + ')$')
    # Update the y-axis range to match the new amplitude
    # Show the updated figure
    fig.show()