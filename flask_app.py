from flask import *
import csv

import pandas as pd
app = Flask(__name__)
@app.route("/tables")
def show_tables():
     with open('daily.csv', 'w') as csvfile:
     filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
     filewriter.writerow(['id', 'date','value'])
     filewriter.writerow(['C1','1/1/17','31'])
     filewriter.writerow(['C1','1/2/17','35'])
     filewriter.writerow(['C1','1/3/17','32'])
     filewriter.writerow(['C1','1/6/17','36'])
     filewriter.writerow(['C1','1/7/17','35'])
     filewriter.writerow(['C1','1/8/17','34'])
     filewriter.writerow(['C1','1/10/17','33'])
     filewriter.writerow(['C2','1/1/17','225'])
     filewriter.writerow(['C2','1/2/17','223'])
     filewriter.writerow(['C2','1/3/17','223'])
     filewriter.writerow(['C2','1/6/17','220'])
     filewriter.writerow(['C2','1/7/17','222'])
     filewriter.writerow(['C2','1/8/17','225'])
     filewriter.writerow(['C2','1/10/17','224'])
     filewriter.writerow(['C3','1/8/17','340'])
     with open('companies.csv', 'w') as csvfile:
     filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
     filewriter.writerow(['id', 'name'])
     filewriter.writerow(['C1','Company 1'])
     filewriter.writerow(['C2','Company 2'])
     filewriter.writerow(['C3','Company 3'])
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
