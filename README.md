# Maynard Facts 🌀

A dark, Tool-inspired web app that displays random facts about **Maynard James Keenan** — the enigmatic frontman of Tool, A Perfect Circle, and Puscifer.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

## Features

- **Dark Tool-Inspired UI** — Custom styling with Cinzel typography and gold accents
- **25+ Curated Facts** — About Maynard's music, winemaking, martial arts, and more
- **Fact Categories** — Auto-categorized as Tool, Winemaker, Military, etc.
- **Royalty-Free Images** — Sourced from [Unsplash](https://unsplash.com)
- **Mobile Responsive** — Works on all devices

## Live Demo

🚀 **[View on Streamlit Cloud](https://maynardfacts.streamlit.app)** *(deploy link)*

## Run Locally

```bash
# Clone the repository
git clone https://github.com/stonezone/maynard_facts.git
cd maynard_facts

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Then open http://localhost:8501 in your browser.

## Project Structure

```
maynard_facts/
├── app.py              # Main Streamlit application
├── facts.txt           # Facts database (one per line)
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── .streamlit/
    └── config.toml     # Streamlit dark theme config
```

## Adding Facts

Edit `facts.txt` and add new facts, one per line. Lines starting with `#` are treated as comments.

## Deploy to Streamlit Cloud

1. Push to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Select `app.py` as the main file
5. Deploy!

## Credits

- **Facts** — Compiled from various sources about Maynard James Keenan
- **Images** — [Unsplash](https://unsplash.com) (royalty-free)
- **Fonts** — [Cinzel](https://fonts.google.com/specimen/Cinzel) & [Raleway](https://fonts.google.com/specimen/Raleway) from Google Fonts

## License

MIT License — feel free to use and modify.

---

*"Think for yourself. Question authority."* — Timothy Leary / Tool
