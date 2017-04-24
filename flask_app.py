from flask import *

import pandas as pd
app = Flask(__name__)
@app.route("/tables")
def show_tables():
     df1 = pd.read_csv('daily.csv')
     df2 = pd.read_csv('companies.csv')
     df1['date']= pd.to_datetime(df1['date'], format='%m/%d/%y')
     df3 = pd.merge(df1,df2,how='left',on='id')
     dates = pd.DataFrame({"date": pd.date_range("2017-01-01", "2017-01-10")})
     df4 = (df3.groupby(['id', 'name'])['date', 'value']
 .apply(lambda g: g.merge(dates, how="outer"))
 .fillna(0)
 .reset_index(level=[0,1])
 .reset_index(drop=True))
     df4 = df4.sort_values(by=['id','date'])
     df4.value = df4.value.astype(int)
     df4['difference'] = df4.groupby('id')['value'].diff()
     return render_template('view.html',tables=[df4.to_html(classes='Company_data')],
     titles = [ 'Company_data'])

if __name__ == "__main__":
    app.run()
