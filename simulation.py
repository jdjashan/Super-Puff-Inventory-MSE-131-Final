import random

def run_simulation(order_amount, SimTime, Weeks, fixed_order_cost, backlog_cost_per):
    # Name variables for everything in process
    Demand = 0
    holding_cost = 50
    items_backloged = 0

    # Create Indexing for all Weekly Values
    results = []

    #Have variables for totals
    total_costs = 0
    total_holding = 0

    #Add variables for seasons
    if Weeks <= 12:
        Season = 1
        SeasonName = "Winter"
    elif Weeks <= 25:
        Season = 2
        SeasonName = "Spring"
    elif Weeks <= 38:
        Season = 3
        SeasonName = "Summer"
    elif Weeks <= 52:
        Season = 4
        SeasonName = "Fall"
    # Get Order amount by user or let them choose optimal


    for i in range (SimTime):
        results.append({
        "week": Weeks,
        "demand": int(Demand/52),
        "total_cost": total_costs,
        "inventory": total_holding,
        "season": SeasonName,
        "order_amount": order_amount
        })
        if Season == 1:
            Demand, Weeks, Season, SeasonName = Winter_Demand(Weeks)
        elif Season == 2:
            Demand, Weeks, Season, SeasonName = Spring_Demand(Weeks)
        elif Season == 3:
            Demand, Weeks, Season, SeasonName = Summer_Demand(Weeks)
        elif Season == 4:
            Demand, Weeks, Season, SeasonName = Fall_Demand(Weeks)

        total_costs = total_costs + fixed_order_cost
        total_holding = total_holding + (order_amount - int(Demand/52))
        if total_holding < 0:
            items_backloged = abs(total_holding)
            total_costs = total_costs + items_backloged*(backlog_cost_per/52)
        elif total_holding > 0:
            total_costs = total_costs + total_holding*(holding_cost/52)
    return results



def Spring_Demand(Week):
        Season = 2
        Demand = random.randint(1000,2500)
        SeasonName = "Spring"
        Week += 1
        if Week > 25:   
            Season = 3
            SeasonName = "Summer"
        return Demand, Week, Season, SeasonName
def Summer_Demand(Week):
    Season = 3
    Demand = random.randint(4500,9000)
    Week += 1
    SeasonName = "Summer"
    if Week > 38:   
        Season = 4
        SeasonName = "Fall"
    return Demand, Week, Season, SeasonName

def Fall_Demand(Week):
    Season = 4
    Demand = random.randint(3000,5000)
    SeasonName = "Fall"
    Week += 1
    if Week > 51:   
        Season = 1
        SeasonName = "Winter"
    return Demand, Week, Season, SeasonName

def Winter_Demand(Week):
    Season = 1
    Demand = random.randint(6000,10000)
    SeasonName = "Winter"
    if Week >= 52:
        Week = 0
    else:
        Week += 1
    if Week > 12:   
        Season = 2
        SeasonName = "Winter"
    return Demand, Week, Season, SeasonName

