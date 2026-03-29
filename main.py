import time
import random
import math
import streamlit as st
import pandas as pd

from simulation import run_simulation

def main():

    st.markdown(
    '<p style="font-family: Rubik; font-size: 60px;">Super Puff Inventory Simulator</p>',
    unsafe_allow_html=True
)
    
    st.markdown(
    '<p style="font-family: Rubik; font-size: 15px;">Welcome to Super Puff Inventory Simulator, here you can simulate up to 200 weeks of inventory orders, demand, and backlogging to see the results. Some background info about Super Puff before you get into it! Super Puff sells these puffy blankets, that can either get really warm or really cold. Thats why the company seems to sell the most (get the most demand) in Summer and Winter seasons. Also there is a set holding cost for thier inventory of $50 per unit, per year. Keep this in mind while making your decision for ordering. Goodluck, and remember customers are relying on you! </p>',
    unsafe_allow_html=True
)
    order_amount = st.slider("Order Amount Per Week", 5, 400, 150, 2 )
    fixed_order_cost = st.slider("Select a fixed order cost", 100, 2000, 500, 10 )
    backlog_cost_per = st.slider("Select a backlog cost per item (for a whole year)", 5, 100, 50, 1 )
    SimTime = st.number_input("Simulation Weeks", 1, 200, 52,1)
    Weeks = st.number_input("Satring Week?", 1, 52, 1,1)

    if st.button("Run simulation"):
        sim_results = run_simulation(order_amount, SimTime, Weeks, fixed_order_cost, backlog_cost_per)
        st.title("Results")

        st.header("Raw Data Chart")
        df = pd.DataFrame(sim_results)
        st.dataframe(sim_results)

        st.header("Order Amount Vs Demand")
        st.line_chart(df[["order_amount", "demand"]])

        st.header("Demand and Inventory Averages")
        st.dataframe(df["demand"].describe())
        st.dataframe(df["inventory"].describe())

        st.markdown(
        f'<h3 style="color: #e74c3c; text-align: center;">Final Cost: ${df["total_cost"].iloc[-1]:,.2f}</h3>',
        unsafe_allow_html=True
        )




if __name__ == "__main__":
    main()