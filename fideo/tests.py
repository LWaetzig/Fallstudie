
import plotly.express as px
import pandas as pd

# Beispieldaten erstellen
df = pd.DataFrame({'x': [0, 1, 2, 3,4,5,6,7,8,9,10], 'y': [0, 1, 2, 3,4,5,6,7,8,9,10]})

# Plot erstellen
fig = px.line(df, x='x', y='y')


# Pfeil hinzufügen
fig.update_layout(
    annotations=[
        dict(
            x=1,
            y=3,
            xref='x',
            yref='y',
            text='Trend',
            showarrow=True,
            arrowhead=3,
            arrowsize=1,
            arrowwidth=4,
            arrowcolor='darkred',
            ax=70,
            ay=70
        )
    ]
)

# Plot anzeigen
fig.show()
