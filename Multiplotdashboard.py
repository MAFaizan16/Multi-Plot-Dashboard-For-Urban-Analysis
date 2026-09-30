import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)

COLOR_A='#1f77b4'
COLOR_B='#ff7f0e'
def generate_population_data():
    years=np.arange(2015,2025)
    city_a=1.0*(1.08**np.arange(10))
    city_b=1.0+0.15*np.arange(10)
    return years,city_a,city_b
def generate_cost_of_living_data():
    categories=["Housing","Food","Transport","Utilities","Health"]
    city_a_costs=[1200,400,300,150,200]
    city_b_costs=[1000,350,250,100,150]
    return categories,city_a_costs,city_b_costs
def generate_climate_data():
    days=365
    city_a_temp=np.random.normal(loc=20,scale=5,size=days)
    city_b_temp=np.random.normal(loc=25,scale=7,size=days)
    return city_a_temp,city_b_temp
def generate_income_happiness_data():
    n = 60
    income_a=np.random.normal(50000, 12000, n)
    happiness_a=3+(income_a/20000)+np.random.normal(0,0.8,n)
    income_b=np.random.normal(55000, 15000, n)
    happiness_b=3+(income_b/20000)+np.random.normal(0,0.8,n)
    return income_a,happiness_a,income_b,happiness_b
def plot_population(ax):
    years,city_a,city_b=generate_population_data()
    ax.plot(years,city_a,marker='o',color=COLOR_A,label='City A')
    ax.plot(years,city_b,marker='s',color=COLOR_B,label='City B')
    ax.set_title('Population Growth 10 years Trend')
    ax.set_xlabel('Year')
    ax.set_ylabel('Population Index (normalised)')
    ax.grid(alpha=0.3)
    ax.legend()
def plot_cost_of_living(ax):
    categories,cost_a,cost_b=generate_cost_of_living_data()
    x=np.arange(len(categories))
    width=0.35
    ax.bar(x-width/2,cost_a,width,color=COLOR_A,label='City A')
    ax.bar(x+width/2,cost_b,width,color=COLOR_B,label='City B')
    ax.set_title('Cost of Living Comparison')
    ax.set_xlabel('Category')
    ax.set_ylabel('Monthly Cost in USD')
    ax.set_xticks(x)
    ax.set_xticklabels(categories,rotation=20)
    ax.legend()
def plot_climate(ax):
    temp_a,temp_b=generate_climate_data()
    ax.hist(temp_a,bins=25,alpha=0.6,color=COLOR_A,label='City A')
    ax.hist(temp_b,bins=25,alpha=0.6,color=COLOR_B,label='City B')
    ax.set_title('Climate Distribution (Temperature °C)')
    ax.set_xlabel('Temperature(°C)')
    ax.set_ylabel('Frequency')
    ax.legend()
def plot_income_happiness(ax):
    income_a,happiness_a,income_b,happiness_b=generate_income_happiness_data()
    ax.scatter(income_a,happiness_a,color=COLOR_A,alpha=0.7,label='City A')
    ax.scatter(income_b,happiness_b,color=COLOR_B,alpha=0.7,label='City B')
    ax.set_title('Income vs Happiness')
    ax.set_xlabel('Income')
    ax.set_ylabel('Happiness')
    ax.legend()
def build_dashboard():
    fig,axes=plt.subplots(2,2,figsize=(14,10))
    fig.suptitle("Urban Analytics Dashboard: City A vs City B",fontsize=16,fontweight="bold")
    plot_population(axes[0,0])
    plot_cost_of_living(axes[0,1])
    plot_climate(axes[1,0])
    plot_income_happiness(axes[1,1])
    plt.tight_layout(rect=[0,0,1,0.96])
    return fig
if __name__=="__main__":
    fig=build_dashboard()
    fig.savefig("urban_dashboard.png",dpi=150)
    plt.show()
    print("Dashboard saved as urban_dashboard.png")

