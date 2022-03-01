import pandas
import ssl

#read the file
ssl._create_default_https_context = ssl._create_unverified_context
df = pandas.read_csv('https://zoeleblanc.com/is310-computing-humanities/assets/files/tools_dh_proceedings.csv')

#2015, 2019, and overall counts for each tool
df["sum"] = df.sum(axis=1)
for i, row in df.iterrows():
    print(row['Tool'],": 2015:", row['2015'], ", 2019:", row['2019'], ", sum:", row['sum'])

#reworking my code into a function
def dataTable(data, name):
    data["sum"] = data.sum(axis=1)
    print(data.loc[data['Tool'] == name])

#bonus
def inputData():
    name = input("Tool name: ")
    print(df.loc[df['Tool'] == name])
