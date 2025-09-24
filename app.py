import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


@st.cache_data
def load_data():
    
    df = pd.read_csv("metadata.csv")  
    # Basic cleaning 
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['publish_year'] = df['publish_time'].dt.year
    return df

df = load_data()

# ---------- Layout ----------
st.title("CORD-19 Data Explorer")
st.write(
    "Interactive exploration of COVID-19 research papers. "
    "Filter by year range and browse key visualizations."
)

# ---------- Widgets ----------
years = df['publish_year'].dropna().astype(int)
min_year, max_year = int(years.min()), int(years.max())
year_range = st.slider(
    "Select publication year range:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

# Filter data
mask = df['publish_year'].between(year_range[0], year_range[1])
filtered = df[mask]

st.write(f"Showing **{len(filtered):,}** papers from {year_range[0]} to {year_range[1]}.")

# ---------- Visualization 1: Publications over time ----------
st.subheader("Publications by Year")
year_counts = filtered['publish_year'].value_counts().sort_index()
fig1, ax1 = plt.subplots()
ax1.bar(year_counts.index, year_counts.values)
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Papers")
st.pyplot(fig1)

# ---------- Visualization 2: Top Journals ----------
st.subheader("Top Journals")
top_journals = filtered['journal'].value_counts().head(10)
fig2, ax2 = plt.subplots()
top_journals.plot(kind='bar', ax=ax2)
ax2.set_xlabel("Journal")
ax2.set_ylabel("Number of Papers")
st.pyplot(fig2)

# ---------- Visualization 3: Word Cloud of Titles ----------
st.subheader("Word Cloud of Paper Titles")
titles = " ".join(filtered['title'].dropna())
wc = WordCloud(width=800, height=400, background_color="white",
               colormap="plasma", max_words=100).generate(titles)
fig3, ax3 = plt.subplots()
ax3.imshow(wc, interpolation='bilinear')
ax3.axis("off")
st.pyplot(fig3)

# ---------- Data Sample ----------
st.subheader("Sample Data")
st.dataframe(filtered.head(20))
