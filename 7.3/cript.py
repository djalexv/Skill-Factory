# def encrypt(instring):
#
#     alf = ('а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я')
#     new = []
#     print(instring.__len__())
#     for i in instring:
#        if i not in alf:
#            new.append(i)
#        else:
#          if i == 'я':
#            new.append('а')
#          else:
#            new.append(alf[alf.index(i)+1])
#     return new #"".join(new)
#
# word = input('Введите слово для шифрования - ')
# print(encrypt(word))

# dict_sample = {
# 1: {'student1': 'Nicholas', 'student2': 'John', 'student3': 'Mercy'},
# 2: {'course1': 'Computer Science', 'course2': 'Mathematics', 'course3': 'Accounting'}
# }
# dict_sample[1]['student4'] = 'Tomas'
# # get(1).get('student2'))
# dict_sample[1].pop('student1')
# # Nicholas.
# # print(dict_sample[1]['student2'])
# print(dict_sample)

# numbers = [1,2,4,3,6,8,4,5,9,1]
# print(len(set(numbers)))

string1 = 'jghsdjkhgsjkd'
string2 = 'dskj hsduihl'
print(set(string1).intersection(set(string2)))