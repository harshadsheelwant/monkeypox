import plotly.express as px
import pandas as pd

# Load dataset
df = pd.read_csv('/mnt/data/monkeypox_dataset.csv')

# Example: If you don't have latitude and longitude in your dataset, you can use iso_code to map locations.
# Let's filter the data for total cases (this is a simplified case; you can extend it)
filtered_df = df.groupby('location').sum().reset_index()

# Plot using Plotly
fig = px.scatter_geo(
    filtered_df,
    locations="location",   # This should match your location names
    locationmode="country names",  # Use country names
    color="total_cases",    # Color by total cases
    size="total_cases",     # Size of the dots by total cases
    projection="orthographic",  # Makes it look like a globe
    title="Monkeypox Global Cases",
)

fig.update_geos(
    showcountries=True, countrycolor="lightgray",
    showcoastlines=True, coastlinecolor="gray",
    showland=True, landcolor="lightgreen",
    showocean=True, oceancolor="lightblue"
)

fig.update_layout(height=700, margin={"r":0,"t":50,"l":0,"b":0})
fig.show()