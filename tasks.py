import matplotlib
from matplotlib import pyplot as plt
import pandas as pd
import datetime as dt
from data import check

matplotlib.use('TkAgg')

@check()
def task1(df):
    print("TASK 1")
    print(df.head(10))
    print(f"Rows: {1}\nColumns: {2}", df.shape[0], df.shape[1])

@check(cols=['City'])
def task2(df):
    print("TASK 2")
    print(df.City.unique())

@check(cols=['Category', 'ProductID'])
def task3(df):
    print("TASK 3")
    print(df.groupby(['Category'])['ProductID'].count())

@check(cols=['Category', 'UnitsInStock'])
def task4(df):
    print("TASK 4")
    print(df.groupby(['Category'])['UnitsInStock'].mean())

@check(cols=['Product', 'Category', 'UnitPrice (Products)'])
def task5(df):
    print("TASK 5")
    print(df[['Product', 'Category', 'UnitPrice (Products)']].max())

@check(cols=['Country', 'Profit'])
def task6(df):
    print("TASK 6")
    print(df.groupby(['Country'])['Profit'].sum())

@check(cols=['Country', 'Sales'])
def task7(df):
    print("TASK 7")
    print(df.groupby(['Country'])['Sales'].sum().plot(kind='pie'))

@check(cols=['City and Counry'])
def task8(df):
    print("TASK 8")
    print(pd.Series(df['City and Counry'].unique()))

@check(cols=['Category', 'UnitPrice'])
def task9(df):
    print("TASK 9")
    print(df.groupby(['Category'])['UnitPrice'].mean())

@check(cols=['Customer Company', 'Profit'])
def task10(df):
    print("TASK 10")
    print(df.groupby(['Customer Company'])['Profit'].sum().nlargest(n=3))

@check(cols=['Quantity'])
def task11(df):
    print("TASK 11")
    print(df[df['Quantity'] > 30])

@check(cols=['Product', 'UnitsOnOrder'])
def task12(df):
    print("TASK 12")
    print(df.groupby(['Product'])['UnitsOnOrder'].sum().nlargest(n=5))

@check(cols=['Customer', 'Quantity'])
def task13(df):
    print("TASK 13")
    print(df.groupby(['Customer'])['Quantity'].sum())

@check(cols=['City', 'Category'])
def task14(df):
    print("TASK 14")
    print(df.groupby('City')['Category'].unique().apply(len))

@check(cols=['UnitPrice', 'UnitCost'])
def task15(df):
    print("TASK 15")
    print(df.assign(Margin = df['UnitPrice'] - df['UnitCost']).sort_values('Margin', ascending=False).head(5))

@check(cols=['Profit', 'Quantity'])
def task16(df):
    print("TASK 16")
    for category, group in df.groupby('Category'):
        plt.scatter(group['Quantity'], group['Profit'], label=category)
    plt.title('Profit by category')
    plt.xlabel('Amount of sales')
    plt.ylabel('Profit')
    plt.legend()
    plt.show()

@check(cols=['Customer', 'UnitPrice (Products)'])
def task17(df):
    print("TASK 17")
    print(pd.DataFrame({'Mean': df.groupby(['Customer'])['UnitPrice (Products)'].mean(), 'Median': df.groupby(['Customer'])['UnitPrice (Products)'].median()}))

@check(cols=['OrderDate', 'Sales'])
def task18(df):
    print("TASK 18")
    df['Month'] = df['OrderDate'].dt.to_period('M')
    sales_by_month = df.groupby('Month')['Sales'].sum()
    sales_by_month.plot()
    plt.title('Sales by month')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.show()

@check(cols=['Customer Company', 'Customer'])
def task19(df):
    print("TASK 19")
    customers_amount = df.groupby(['Customer Company'])['Customer'].nunique().reset_index().rename(columns = {'Customer': 'UniqueCustomers'})
    max_customers = customers_amount.loc[customers_amount["UniqueCustomers"].idxmax()]
    print(max_customers)

@check()
def task20(df):
    print("TASK 20")
    print(df.loc[df.groupby('Category')['Quantity'].idxmax()])

@check(cols=['Profit', 'Category', 'City'])
def task21(df):
    print("TASK 21")
    table = pd.pivot_table(df, values='Profit', index=['Category'], columns=['City'], aggfunc='sum', fill_value=0)
    print(table)

@check(cols=['City', 'Sales', 'OrderDate'])
def task22(df):
    print("TASK 22")
    df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')
    city_sales = df[df['OrderDate'] >= df['OrderDate'].max() - pd.DateOffset(months=6)].groupby('City')['Sales'].sum().nlargest(3)
    print(city_sales)

@check(cols=['Profit', 'Category'])
def task23(df):
    print('TASK 23')
    df['ProfitDif'] = df['Profit'] - df['Category'].map(df.groupby('Category')['Profit'].mean())
    print(df.nlargest(5, 'ProfitDif'))