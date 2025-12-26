import streamlit as st
from engine import ask_ai
import pandas as pd
import sqlite3
import plotly.express as px

# 1. Dashboard Configuration
st.set_page_config(page_title="InsightSQL Analyst", page_icon="📈", layout="wide")
db_path = r"E:\Llama3_Business_Analyst\data\business.db"

# 2. Sidebar with Performance Chart
with st.sidebar:
    st.title("Project Details")
    st.info("Model: Llama 3 (Local)")
    st.info("Database: SQLite")
    st.markdown("---")
    st.header("📊 Sales Performance")
    
    try:
        conn = sqlite3.connect(db_path)
        query = """
        SELECT p.product_name, SUM(s.revenue) as total_revenue
        FROM sales s
        JOIN products p ON s.product_id = p.id
        GROUP BY p.product_name
        """
        df_chart = pd.read_sql_query(query, conn)
        conn.close()

        if not df_chart.empty:
            fig = px.bar(df_chart, 
                         x="product_name", 
                         y="total_revenue", 
                         labels={"product_name": "Product", "total_revenue": "Revenue ($)"},
                         color="total_revenue", 
                         color_continuous_scale="Viridis")
            fig.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Sidebar Chart Error: {e}")

# 3. Main Dashboard Interface
st.title("🤖 Llama 3 Business Intelligence Agent")
st.write("Analyze your sales data using natural language.")

user_query = st.text_input("What would you like to know?", 
                           placeholder="e.g., Which product had the highest revenue?")

if st.button("Run Analysis"):
    if user_query:
        with st.spinner("Llama 3 is analyzing..."):
            answer = ask_ai(user_query)
            
            st.subheader("Executive Summary")
            st.success(answer)
            
            # Data Preview Section
            st.markdown("---")
            st.subheader("Recent Sales Log")
            try:
                conn = sqlite3.connect(db_path)
                df_preview = pd.read_sql_query("SELECT * FROM sales ORDER BY sale_date DESC LIMIT 5", conn)
                st.dataframe(df_preview, use_container_width=True)
                conn.close()
            except Exception as e:
                st.error(f"Preview Error: {e}")
    else:
        st.warning("Please enter a question first.")