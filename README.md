# Super Puff Inventory Simulator
 
Welcome to the **Super Puff Inventory Simulator**! Here you can simulate up to 200 weeks of inventory orders, demand, and backlogging to see the results.
 
## About Super Puff
 
Super Puff sells puffy blankets that can get really warm or really cold. Because of this, the company sees the most demand during **Summer** and **Winter** seasons. There is also a set holding cost for inventory of **$50 per unit, per year** — keep this in mind while making your ordering decisions.
 
Good luck, and remember — customers are relying on you!
 
## How to Run
 
Make sure you have Python and the required packages installed:
 
```bash
pip install streamlit pandas
```
 
Then launch the app:
 
```bash
streamlit run main.py
```
 
This will open the simulator in your browser where you can set your order amount, choose a simulation length, and view the results.
 
## Features
 
- Seasonal demand simulation (Spring, Summer, Fall, Winter)
- Adjustable order quantity and simulation length
- Backlog tracking and cost penalties
- Interactive charts and summary statistics
 