import os
import pandas as pd
class Query():
    def Create(self):
        for filename in os.listdir('../csv'):
            tab_name=filename.split('.')[0]
            b=os.path.join(os.getcwd(), 'csv', filename)
            with open(b,'r+') as file:
                col=""
                for data in pd.read_csv(file):
                    data = "".join(data).replace('\n', '')
                    col=col+data+","
                col=col.strip(",")
                print(col)


        print("Hello")

obj=Query()
obj.Create()