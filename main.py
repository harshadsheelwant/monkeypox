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

data = {
    "Model": ["Linear Regression", "Decision Tree", "Random Forest", "ElasticNet"],
    "MAE": [1.150246, 0.944960, 1.051216, 1.106351],
    "MSE": [174.22348, 163.138241, 110.402201, 173.725202],
    "MAPE": ["2.261138e+15", "1.597036e+15", "1.987033e+15", "2.089191e+15"],
    "R²": [0.773268, 0.787694, 0.856324, 0.773916]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display the table
st.markdown("### Model Performance Metrics")
st.table(df)
