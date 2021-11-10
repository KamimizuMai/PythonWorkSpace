DATA_FILENAME = '1110/test.csv'
person_data =[]

with open(DATA_FILENAME,'r',encoding='utf-8') as f:
    title = f.readline().strip().split(',')     #1行目を読込み
    for line in f :                             #残りの行を読込み
        person_data.append(line.strip().split(','))
    # title = []
    # for title_line in f.readline().split(','):
    #     title.append(title_line.strip())
print('person dataは',person_data)
col = 1                                         #[0]は名前なのでSkip[1]から
avg =[0]*len(title)                             #平均を格納するリスト

# col=1のとき、 (50/4)+(70/4)+(90/4)+(60/4)=67.5
while col < len(title):
    for score in person_data:
        avg[col] += int(score[col])/len(person_data)
    col += 1

print(title[1:])
print(avg[1:])