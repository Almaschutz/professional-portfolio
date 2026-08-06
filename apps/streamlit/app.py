import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Product Growth Explorer",
    page_icon="📊",
    layout="wide"
)

st.title("Product Growth Explorer")
st.caption("Interactive portfolio demo: funnel, cohorts and segmentation")

df = pd.DataFrame({
    "segment": ["Organic", "Paid", "Partner", "Referral"],
    "signups": [12000, 18000, 6500, 4200],
    "activation_rate": [0.48, 0.31, 0.42, 0.55],
    "retention_30d": [0.34, 0.20, 0.29, 0.40]
})

metric = st.selectbox(
    "Metric",
    ["activation_rate", "retention_30d", "signups"]
)

fig = px.bar(
    df.sort_values(metric),
    x=metric,
    y="segment",
    orientation="h",
    text_auto=".1%" if "rate" in metric or "retention" in metric else True,
    title=f"{metric.replace('_', ' ').title()} by segment"
)
st.plotly_chart(fig, use_container_width=True)

st.dataframe(df, use_container_width=True)
