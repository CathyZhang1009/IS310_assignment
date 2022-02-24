from prettytable import PrettyTable

myTable = PrettyTable(["Tool", "2015", "2016", "2017", "2018", "2019"])
myTable.add_row(["Python", 9, 22, 27, 32, 35])
myTable.add_row(["JavaScript", 8, 18, 12, 6, 15])
myTable.add_row(["Twitter", 10, 18, 26, 16, 12])
myTable.add_row(["Github", 2, 6, 17, 5, 10])
myTable.add_row(["Gephi", 11, 16, 14, 10, 9])
myTable.add_row(["GeoNames", 2, 4, 3,1, 8])
myTable.add_row(["Transkribus", 0, 1, 2, 1, 8])
myTable.add_row(["Excel", 5, 9, 3, 6, 7])
myTable.add_row(["MySQL", 0, 6, 9, 5, 7])

print(myTable)
sum2015 = 0
sum2019 = 0
for i in range(9):
    sum2015 += myTable.rows[i][1]
    sum2019 += myTable.rows[i][5]

sumPython = 0
sumJavaScript = 0
sumTwitter = 0
sumGithub = 0
sumGephi = 0
sumGeoNames = 0
sumTranskribus = 0
sumExcel = 0
sumMySQL = 0
for i in range(1,6):
    sumPython += myTable.rows[0][i]
    sumJavaScript += myTable.rows[1][i]
    sumTwitter += myTable.rows[2][i]
    sumGithub += myTable.rows[3][i]
    sumGephi += myTable.rows[4][i]
    sumGeoNames += myTable.rows[5][i]
    sumTranskribus += myTable.rows[6][i]
    sumExcel += myTable.rows[7][i]
    sumMySQL += myTable.rows[8][i]

print(sum2015)
print(sum2019)
print(sumPython)
print(sumJavaScript)
print(sumTwitter)
print(sumGithub)
print(sumGephi)
print(sumGeoNames)
print(sumTranskribus)
print(sumExcel)
print(sumMySQL)