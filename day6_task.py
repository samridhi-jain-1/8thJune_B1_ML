#Q1.Installation done

#Q2.Basic Mathematical Operations
print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6==6)
a=20
a+=30
a%=3
print(a)
print(True * False)
print(True & False)
print(True and False)
print(((6>3) and (7<4) or (18==3)) and (9>3))
print(True is False)
#print(False in 'False')--> gives error
print(((True == False) or (False > True)) and (False <= True))

#Q3.Try to get expected output
s1 ='Nice to have it'
s2 ='here'
print(s1,s2)

#Q4.Use index to grab 'hello' word
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])

#Q5.Insert s1 ans s2 in list a
a=[s1]+a+[s2]
print(a)

#Q6.Set question
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1-color_list_2)

#Q7.String Pangram or not
string="the quick brown fox jumps over the lazy dog"
l=[False]*26
for i in string.lower():
    if not i==' ':
        l[ord(i)-ord('a')]=True
for i in l:
    if(i==False):
        print('Not Pangram')
        break
else:
    print('Pangram')

#Q8.compute n+nn+nnn
n=int(input('Enter an integer between 0 to 9: '))
print(eval('{0}+{0}{0}+{0}{0}{0}'.format(n)))

#Q9.list
items = input("Input comma separated sequence of words: ")
words = [word for word in items.split(",")]
print(",".join(sorted(list(words))))
4
#Q10.dictionary
d = {'Student': ['Rahul','Kishore','Vidhya','Raakhi'],'Marks': [57,87,67,79]}
print(d['Student'][d['Marks'].index(max(d['Marks']))])
