import random

def run_simulation(order_amount, SimTime, Weeks, fixed_order_cost, backlog_cost_per,Distributor):
    # Name variables for everything in process
    Demand = 0
    holding_cost = 25
    items_backloged = 0

    #Add variables for customer fatisfaction and leaving as well as sales
    customerloss = 1.0
    backlog_time = 0
    sale_gain = 9.99

    #Get Demand Perks
    if Distributor == "Original":
        delay_chance = 100
        demand_multiple = 1
    elif Distributor == "ReliableRetails":
        delay_chance = 200
        demand_multiple = 1
        fixed_order_cost = fixed_order_cost*1.5
    elif Distributor == "PremiuimProcess":
        sale_gain = 8.99
        delay_chance = 50
        demand_multiple = 2
    fixed_order_amount = order_amount



    # Create Indexing for all Weekly Values, and alerts list
    results = []
    alerts = []

    #Have variables for totals
    total_costs = 0
    total_holding = 0
    total_made = 0

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
        "demand": ((int(Demand/(customerloss*52))*demand_multiple)),
        "total_cost": total_costs,
        "inventory": total_holding,
        "season": SeasonName,
        "order_amount": order_amount,
        "Gross Revenue": total_made,
        "Net Revenue": total_made - total_costs
        })
        delay = random.randint(1,delay_chance)
        if delay < 5:
            order_amount = 0
            alerts.append(f"There was a delay and no products shipped to inventory warehouse in week {Weeks}")
        else:
            order_amount = fixed_order_amount
        if Season == 1:
            Demand, Weeks, Season, SeasonName = Winter_Demand(Weeks)
        elif Season == 2:
            Demand, Weeks, Season, SeasonName = Spring_Demand(Weeks)
        elif Season == 3:
            Demand, Weeks, Season, SeasonName = Summer_Demand(Weeks)
        elif Season == 4:
            Demand, Weeks, Season, SeasonName = Fall_Demand(Weeks)

        if items_backloged > 0:
            backlog_time += 1
            if backlog_time >= 4:
                customerloss +=0.25
        else:
            backlog_time =0
            if customerloss > 1:
                customerloss -= 0.25

        total_costs = total_costs + fixed_order_cost
        total_holding = total_holding + (order_amount - (int((Demand/(customerloss*52))*demand_multiple)))
        if total_holding < 0:
            items_backloged = abs(total_holding)
            total_costs = total_costs + items_backloged*(backlog_cost_per/52)
            if total_holding > -(int(Demand/(customerloss*52))):
                total_made = total_made + sale_gain*(total_holding + (((int(Demand/(customerloss*52)*demand_multiple)))))
        elif total_holding > 0:
            total_costs = total_costs + total_holding*(holding_cost/52)
            total_made = total_made + sale_gain*(int((Demand/(customerloss*52)*demand_multiple)))
            items_backloged = 0
    return results, alerts



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

