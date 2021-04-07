import pandas as pd

"""
The data in the dataframe represents scores for test. The  possible scores are 0-3.  Each exam completes a stage based on the scores
for the questions.
The code must check the dataframe to find the scores to the questions then compare to the dictionary.
The script will sum the scores for the questions attibuted to each stage.  If the score is equal to or less than the number in the
 dictionary then that number is used. For example if question_1 = 2 in the dataframe then when summing the scores for stage 1 will use 2.
 If the question_2 = 2 in the dataframe, when summing the score for stage1 it will use 1. The total scores are the calculated
 as a percentage using the 'total_possible' and placed in columns ie 'stage1%', 'stage2%'
"""

# dictionary of scores
primary = {
    'stage1' : {
       'question_1': 3,
       'question_2': 1,
       'total_possible':  4
    },

    'stage2': {
        'question_1': 2,
        'question_2': 2,
        'question_3': 1,
        'question_4': 2,
        'question_5': 3,
        'question_6': 1,
        'total_possible': 11
    }
}

#dataframe of test scores
data = {'first_name': ['John', 'Luke', 'Jaime', 'Tom', 'Amy'],
        'question_1': ['0', '2', '3', '2', '0'],
        'question_2': ['2', '3', '0', '3', '1'],
        'question_3': ['1', '1', '1', '2', '3'],
        'question_4': ['3', '2', '2', '3', '3'],
        'question_5': ['2', '0', '1', '2', '1'],
        'question_6': ['0', '2', '0', '3', '1']
        }
df = pd.DataFrame(data, columns = ['first_name', 'question_1','question_2','question_3','question_4','question_5','question_6'])
df1 = pd.DataFrame(data, columns = ['first_name', 'question_1','question_2'])
df2 = pd.DataFrame(data, columns = ['first_name', 'question_1','question_2','question_3','question_4','question_5','question_6'])
#df


#write code below:

#I am making this dictionary to easy it
stage1 = {'question_1':3,'question_2':1}
stage2 = {'question_1': 2,'question_2': 2,'question_3': 1,'question_4': 2,'question_5': 3,'question_6': 1,'total_possible': 11}


#for questions,total_marks in stage1.items():
for total_marks in [3]:
    for scores in df1.question_1:
        if int(scores)<=total_marks:
            pass
        else:
            df1['question_1'].replace(scores,total_marks,inplace=True)


for total_marks in [1]:
    for scores in df1.question_2:
        if int(scores)<=total_marks:
            pass
        else:
            df1['question_2'].replace(scores,total_marks,inplace=True)


for total_marks in [2]:
    for scores in df2.question_1:
        if int(scores)<=total_marks:
            pass
        else:
            df2['question_1'].replace(scores,total_marks,inplace=True)

for total_marks in [2]:
    for scores in df2.question_2:
        if int(scores)<=total_marks:
            pass
        else:
            df2['question_2'].replace(scores,total_marks,inplace=True)

for total_marks in [1]:
    for scores in df2.question_3:
        if int(scores)<=total_marks:
            pass
        else:
            df2['question_3'].replace(scores,total_marks,inplace=True)

for total_marks in [2]:
    for scores in df2.question_4:
        if int(scores)<=total_marks:
            pass
        else:
            df2['question_4'].replace(scores,total_marks,inplace=True)

for total_marks in [3]:
    for scores in df2.question_5:
        if int(scores)<=total_marks:
            pass
        else:
            df2['question_5'].replace(scores,total_marks,inplace=True)

for total_marks in [1]:
    for scores in df2.question_6:
        if int(scores)<=total_marks:
            pass
        else:
            df2['question_6'].replace(scores,total_marks,inplace=True)


def per2(num):
    numb = num*100/11
    return numb


def per(num):
    numb = num*100/4
    return numb




question_1 = []
for number in df1['question_1']:
    question_1.append(number)
question_2 = []
for numbers in df1['question_2']:
    question_2.append(numbers)


a = int(question_1[0])+int(question_2[0])
b = int(question_1[1])+int(question_2[1])
c = int(question_1[2])+int(question_2[2])
d = int(question_1[3])+int(question_2[3])
e = int(question_1[4])+int(question_2[4])

ab = per(a)
ad = per(b)
ar = per(c)
aw = per(d)
aq = per(e)

stage1 = {'stage1%':[ab,ad,ar,aw,aq]}
df_stage1 = pd.DataFrame(stage1)



question_1 = []
for number in df2['question_1']:
    question_1.append(number)
question_2 = []
for numbers in df2['question_2']:
    question_2.append(numbers)
question_3 = []
for numbers in df2['question_3']:
    question_3.append(numbers)
question_4 = []
for numbers in df2['question_4']:
    question_4.append(numbers)
question_5 = []
for numbers in df2['question_5']:
    question_5.append(numbers)
question_6 = []
for numbers in df2['question_6']:
    question_6.append(numbers)

a = int(question_1[0])+int(question_2[0])+int(question_3[0])+int(question_4[0])+int(question_5[0])+int(question_6[0])
b = int(question_1[1])+int(question_2[1])+int(question_3[1])+int(question_4[1])+int(question_5[1])+int(question_6[1])
c = int(question_1[2])+int(question_2[2])+int(question_3[2])+int(question_4[2])+int(question_5[2])+int(question_6[2])
d = int(question_1[3])+int(question_2[3])+int(question_3[3])+int(question_4[3])+int(question_5[3])+int(question_6[3])
e = int(question_1[4])+int(question_2[4])+int(question_3[4])+int(question_4[4])+int(question_5[4])+int(question_6[4])

_1=per2(a)
_2=per2(b)
_3=per2(c)
_4=per2(d)
_5=per2(e)

stage2 = {'stage2%':[_1,_2,_3,_4,_5]}
df_stage2 = pd.DataFrame(stage2)


df3 = pd.concat([df,df_stage1], axis=1)

final_df = pd.concat([df3,df_stage2], axis=1)
print(final_df)

user_input = input("If you want this dataframe into csv file then write 'yes' other wise press any key to continue")
if user_input=="yes":
    final_df.to_csv('scores.csv', index=False)







    
                
    


        


















    

