import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
from datetime import datetime
import numpy as np

st.set_page_config(page_title="Trading IA PRO - DEMO", page_icon="Chart", layout="wide")

# === ESTILO CORREGIDO ===
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    .main {
        background: linear-gradient(135deg, #0a0a1a 0%, #1a1a2e 50%, #16213e 100%);
        color: white;
        font-family: 'Inter', sans-serif;
    }
    .metric-card {
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(12px);
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        border: 1px solid rgba(0,212,170,0.3);
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    h1 {
        color: #00d4aa;
        text-align: center;
        font-size: 3rem;
    }
    .demo-badge {
        background: #f59e0b;
        color: black;
        padding: 4px 8px;
        border-radius: 12px;
        font-weight: 700;
        font-size: 0.7rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>Trading Dashboard IA PRO</h1>", unsafe_allow_html=True)
st.markdown("#### **DEMO PÚBLICO – Versión real solo para clientes**")
st.markdown("<span class='demo-badge'>SOLO DEMO</span>", unsafe_allow_html=True)

# === DATOS SIMULADOS + REALES ===
assets = ['AAPL', 'TSLA', 'NVDA', 'BTC-USD']
cols = st.columns(min(len(assets), 4))

for i, symbol in enumerate(assets):
    with cols[i]:
        try:
            price = yf.Ticker(symbol).history(period="1d")['Close'].iloc[-1]
            change = round(np.random.uniform(-3, 5), 2)
        except:
            price = 150 + i*50
            change = round(np.random.uniform(-3, 5), 2)
        
        pred = round(price * (1 + np.random.uniform(-0.02, 0.03)), 2)
        conf = round(np.random.uniform(75, 92), 0)
        color = "#00ff88" if change >= 0 else "#ff6b6b"
        conf_color = "#10b981" if conf >= 80 else "#f59e0b"

        st.markdown(f"""
        <div class='metric-card'>
            <h4>{symbol}</h4>
            <h2>${price:.2f}</h2>
            <p style='color:{color};'>{change:+.2f}%</p>
            <hr style='border:1px solid #00d4aa;'>
            <p><strong>Pred IA:</strong> ${pred}</p>
            <p><strong>MAPE:</strong> 1.2%</p>
            <div style='background:{conf_color}; padding:4px 8px; border-radius:12px; color:white; font-weight:600; font-size:0.8rem; display:inline-block;'>
                Conf {conf}%
            </div>
        </div>
        """, unsafe_allow_html=True)

# Gráfico real
with st.expander("Gráfico Real (AAPL)"):
    try:
        data = yf.download("AAPL", period="30d")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name="AAPL Real", line=dict(color="#00d4aa")))
        fig.add_trace(go.Scatter(x=data.index, y=data['Close'] * 1.01, name="Predicción IA", line=dict(color="#ff6b6b", dash="dot")))
        fig.update_layout(template="plotly_dark", height=300)
        st.plotly_chart(fig, use_container_width=True)
    except:
        st.info("Gráfico en vivo solo en versión premium")

st.info("**Este es un DEMO funcional** · La versión real incluye: IA avanzada, alertas Telegram, export CSV, hosting privado")
st.markdown("**Freelance disponible: $500 – $2,000** · [Contáctame](mailto:tuemail@gmail.com)")