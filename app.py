#!/usr/bin/env python3
"""
Maynard James Keenan Fact Generator - Streamlit App

A dark, Tool-inspired web app that displays random facts about
Maynard James Keenan (Tool, A Perfect Circle, Puscifer).

Run with: streamlit run app.py
"""

import os
import random
import streamlit as st

# Page configuration - must be first Streamlit command
st.set_page_config(
    page_title="Maynard Facts",
    page_icon="🌀",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for Tool-inspired dark theme
CUSTOM_CSS = """
<style>
    /* Import Cinzel font for Tool aesthetic */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500&display=swap');

    /* Main app styling */
    .stApp {
        background: linear-gradient(180deg, #0a0a0a 0%, #1a1a1a 50%, #0d0d0d 100%);
        background-attachment: fixed;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Main container */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 900px;
    }

    /* Title styling */
    .main-title {
        font-family: 'Cinzel', serif;
        color: #c2b280;
        text-align: center;
        font-size: 3rem;
        font-weight: 600;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 30px rgba(194, 178, 128, 0.3);
    }

    .subtitle {
        font-family: 'Raleway', sans-serif;
        color: #888;
        text-align: center;
        font-size: 1rem;
        font-weight: 300;
        letter-spacing: 0.3em;
        text-transform: uppercase;
        margin-bottom: 2rem;
    }

    /* Spiral divider */
    .spiral-divider {
        text-align: center;
        font-size: 2rem;
        color: #c2b280;
        margin: 1.5rem 0;
        opacity: 0.7;
    }

    /* Fact card styling */
    .fact-card {
        background: linear-gradient(145deg, #1a1a1a 0%, #0f0f0f 100%);
        border: 1px solid #333;
        border-left: 4px solid #c2b280;
        border-radius: 8px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
    }

    .fact-text {
        font-family: 'Raleway', sans-serif;
        color: #e0e0e0;
        font-size: 1.3rem;
        line-height: 1.8;
        font-weight: 400;
    }

    .fact-label {
        font-family: 'Cinzel', serif;
        color: #c2b280;
        font-size: 0.85rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        margin-bottom: 1rem;
        opacity: 0.8;
    }

    /* Button styling */
    .stButton > button {
        font-family: 'Cinzel', serif;
        background: linear-gradient(145deg, #2a2a2a 0%, #1a1a1a 100%);
        color: #c2b280;
        border: 2px solid #c2b280;
        border-radius: 4px;
        padding: 0.8rem 2.5rem;
        font-size: 1rem;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 1rem;
    }

    .stButton > button:hover {
        background: #c2b280;
        color: #0a0a0a;
        box-shadow: 0 0 20px rgba(194, 178, 128, 0.4);
        transform: translateY(-2px);
    }

    .stButton > button:active {
        transform: translateY(0);
    }

    /* Image container */
    .image-container {
        text-align: center;
        margin: 2rem 0;
        opacity: 0.9;
    }

    .image-container img {
        border-radius: 8px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6);
    }

    /* Footer styling */
    .custom-footer {
        font-family: 'Raleway', sans-serif;
        color: #555;
        text-align: center;
        font-size: 0.8rem;
        margin-top: 3rem;
        padding-top: 2rem;
        border-top: 1px solid #222;
    }

    .custom-footer a {
        color: #c2b280;
        text-decoration: none;
    }

    /* Category tag */
    .category-tag {
        font-family: 'Raleway', sans-serif;
        display: inline-block;
        background: rgba(194, 178, 128, 0.15);
        color: #c2b280;
        padding: 0.3rem 0.8rem;
        border-radius: 3px;
        font-size: 0.75rem;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-top: 1rem;
    }

    /* Fibonacci sequence animation hint */
    @keyframes pulse {
        0%, 100% { opacity: 0.7; }
        50% { opacity: 1; }
    }

    .spiral-divider {
        animation: pulse 3s ease-in-out infinite;
    }
</style>
"""

# Curated Unsplash images (royalty-free, no attribution required)
HEADER_IMAGES = [
    # Sacred geometry / abstract spiral
    "https://images.unsplash.com/photo-1545987796-200677ee1011?w=800&q=80",
    # Dark geometric pattern
    "https://images.unsplash.com/photo-1557682250-33bd709cbe85?w=800&q=80",
    # Abstract dark texture
    "https://images.unsplash.com/photo-1518837695005-2083093ee35b?w=800&q=80",
]


def load_facts(filename: str) -> list[str]:
    """Load fun facts from the given filename.

    Each non-empty line in the file is considered a separate fact.
    Lines beginning with # are treated as comments and ignored.

    Args:
        filename: Path to the facts file.

    Returns:
        A list of fact strings.
    """
    facts: list[str] = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if not stripped or stripped.startswith("#"):
                    continue
                facts.append(stripped)
    except FileNotFoundError:
        st.error(f"Facts file '{filename}' not found.")
        return []
    except Exception as e:
        st.error(f"Error reading facts file: {e}")
        return []
    return facts


def categorize_fact(fact: str) -> str:
    """Determine the category of a fact based on keywords."""
    fact_lower = fact.lower()

    if any(word in fact_lower for word in ["hawaii", "honolulu", "blaisdell", "aloha"]):
        return "Hawaii"
    elif any(word in fact_lower for word in ["grammy", "award"]):
        return "Grammy Awards"
    elif any(word in fact_lower for word in ["danny carey", "drummer", "drums", "tabla", "polyrhythm"]):
        return "Danny Carey"
    elif any(word in fact_lower for word in ["adam jones", "guitarist", "special effects", "jurassic", "terminator"]):
        return "Adam Jones"
    elif any(word in fact_lower for word in ["justin chancellor", "bassist", "peach", "wal bass"]):
        return "Justin Chancellor"
    elif any(word in fact_lower for word in ["wine", "vineyard", "cellar", "grape", "merkin", "caduceus", "harvest"]):
        return "Winemaker"
    elif any(word in fact_lower for word in ["army", "military", "west point", "enlisted"]):
        return "Military"
    elif any(word in fact_lower for word in ["jiu-jitsu", "jiu‑jitsu", "black belt", "martial"]):
        return "Martial Arts"
    elif any(word in fact_lower for word in ["fear inoculum", "13-year", "13 year"]):
        return "Fear Inoculum"
    elif any(word in fact_lower for word in ["puscifer"]):
        return "Puscifer"
    elif any(word in fact_lower for word in ["perfect circle", "mer de noms", "thirteenth step", "howerdel"]):
        return "A Perfect Circle"
    elif any(word in fact_lower for word in ["tool", "aenima", "ænima", "lateralus", "fibonacci", "undertow", "opiate", "10,000 days"]):
        return "Tool"
    elif any(word in fact_lower for word in ["charity", "benefit", "rainn", "justice", "philanthrop"]):
        return "Philanthropy"
    else:
        return "Life & Career"


def main() -> None:
    """Main Streamlit app entry point."""
    # Inject custom CSS
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

    # Header
    st.markdown('<h1 class="main-title">Maynard Facts</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Tool • A Perfect Circle • Puscifer</p>', unsafe_allow_html=True)

    # Spiral divider (Fibonacci reference)
    st.markdown('<div class="spiral-divider">◉</div>', unsafe_allow_html=True)

    # Load facts
    script_dir = os.path.dirname(os.path.abspath(__file__))
    facts_file = os.path.join(script_dir, "facts.txt")
    facts = load_facts(facts_file)

    if not facts:
        st.warning("No facts available. Please ensure facts.txt contains facts.")
        return

    # Initialize session state for the current fact
    if "current_fact" not in st.session_state:
        st.session_state.current_fact = random.choice(facts)
    if "fact_count" not in st.session_state:
        st.session_state.fact_count = 0

    # Display current fact
    current_fact = st.session_state.current_fact
    category = categorize_fact(current_fact)

    st.markdown(f'''
    <div class="fact-card">
        <div class="fact-label">Did You Know?</div>
        <div class="fact-text">{current_fact}</div>
        <div class="category-tag">{category}</div>
    </div>
    ''', unsafe_allow_html=True)

    # Generate new fact button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🌀 Spiral Out", key="generate"):
            st.session_state.current_fact = random.choice(facts)
            st.session_state.fact_count += 1
            st.rerun()

    # Show header image (cycles through images based on fact count)
    image_index = st.session_state.fact_count % len(HEADER_IMAGES)
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.image(HEADER_IMAGES[image_index], use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown(f'''
    <div class="custom-footer">
        <p>{len(facts)} facts about Maynard James Keenan</p>
        <p>Images from <a href="https://unsplash.com" target="_blank">Unsplash</a> (royalty-free)</p>
        <p style="margin-top: 1rem; font-size: 0.7rem; color: #444;">
            "Think for yourself. Question authority." — Timothy Leary / Tool
        </p>
    </div>
    ''', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
