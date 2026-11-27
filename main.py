import sqlite3
import pandas as pd
import streamlit as st

st.title("money SMP Players")

with sqlite3.connect("money.db") as conn:
    # Show all players
    st.header("All players")
    table = pd.read_sql_query(
        "SELECT PLAYER NAME, SEASON INTRODUCED, NUMBER OF TIMES PLAYED, NUMBER OF WINS FROM player_details ORDER BY name",
        conn,
    )
    st.dataframe(table, hide_index=True)

