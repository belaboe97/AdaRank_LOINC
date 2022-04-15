# Program extracting all columns
# name in Python
import xlrd
import csv
glucinbl=[]
def writecsv(res,filename):
    with open(filename, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for sor in res:
            spamwriter.writerow(sor)
    return "ok"

def readcsv(filename):
    reslist=[]
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar=' ')
        for row in spamreader:
            reslist.append(row)
    return reslist

loc = ('loinc_dataset.xlsx')
wb = xlrd.open_workbook(loc)
glucoriginal=[]
glucsheet = wb.sheet_by_index(0)
for i in range(2,glucsheet.nrows):
    glucoriginal.append(glucsheet.row_values(i))
bilioriginal=[]
bilisheet = wb.sheet_by_index(1)
for i in range(2,bilisheet.nrows):
    bilioriginal.append(bilisheet.row_values(i))
whiteoriginal=[]
whitesheet = wb.sheet_by_index(2)
for i in range(2,whitesheet.nrows):
    whiteoriginal.append(whitesheet.row_values(i))
glucfile='glucose in blood.csv'
glucinbl=readcsv(glucfile)
bilifile='bilirubin in plasma.csv'
bilirubin=readcsv(bilifile)
whitefile='White blood cells count.csv'
white=readcsv(whitefile)
ext=readcsv('randomres.csv')
def compare_and_make(query,orilist,extendlist,otherlist,fromi):
    print(query)
    for j in range(len(orilist)):
        for i in range(1,len(extendlist)):
            if str(extendlist[i][0])==str(orilist[j][0]):
                print('hit')
                orilist[j][6]=1
                extendlist[i][0]='hit'
        if orilist[j][6]!=1:
            orilist[j][6]=0
        orilist[j][5]=1
    writecsv(orilist,query+'final.csv')
    extended=orilist
    if len(extendlist)>70:
        extendlist=extendlist[:70]
    for i in range(1,len(extendlist)):
        if glucinbl[i][0]!='hit':
            extended.append([extendlist[i][0],extendlist[i][14],extendlist[i][1],extendlist[i][2],extendlist[i][2],1,1])
    while len(extended)<=201:
        extended.append([otherlist[fromi][0],otherlist[fromi][14],otherlist[fromi][1],otherlist[fromi][2],otherlist[fromi][2],1,0])
        fromi+=1
    writecsv(extended,query+'finalEXT.csv')
    return fromi

firstquery=compare_and_make("glucose_in_blood_",glucoriginal,glucinbl,ext,0)
secondquery=compare_and_make("bilirubin_in_plasma_",bilioriginal,bilirubin,ext,firstquery)
thirdquery=compare_and_make("whit_blood_cells_count_",whiteoriginal,white,ext,secondquery)
