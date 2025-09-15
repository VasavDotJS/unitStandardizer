#DataSet created for explanatory and standardization testing purpose.
import pandas
import unitStandardizer
data={
    "Name": ["Akshay","Vishnu","Abhi","Zayan","Tessa"],
    "Age": [21,19,18,16,17],
    "Gender": ['Male','Male','Male','Male','Female'],
    "Height": [168,1.8,1590,5.3,145]
}
dataSet=pandas.DataFrame(data)
dataSet["HeightStandard"]=dataSet.apply(lambda row: unitStandardizer.scaleUnits.unitStandard(row["Height"]),axis=1)
print(dataSet)
