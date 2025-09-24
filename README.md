# CORD-19 Data Explorer

An interactive **Streamlit** web app for exploring COVID-19 research papers using a cleaned sample of the [CORD-19 dataset](https://www.kaggle.com/datasets/allen-institute-for-ai/CORD-19-research-challenge).  
The app lets you filter papers by year, view publication trends, identify top journals, and visualize frequent words in paper titles with a word cloud.

---

## ✨ Features
- Interactive year slider to filter publications.
- Publications-over-time bar chart.
- Top publishing journals bar chart.
- Word cloud of paper titles.
- Scrollable table showing a sample of the filtered data.

---

## 🛠️ Requirements
- Python 3.8+
- Packages:
  - `pandas`
  - `matplotlib`
  - `wordcloud`
  - `streamlit`

Install all dependencies:

```bash
pip install -r requirements.txt
