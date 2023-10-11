# my_list = []

# words = input("parasyti penkis zdozius atskirtais kableliais: ").split(",")
# my_list.append(words)

# st="abcabcabc" 
# s=set(st) 
# for i in s: 
#     print(i+" occur "+str(st.count(i))+" times") 

# sally = "sally sells sea shells by the sea shore" 
words = input("parasyti penkis zodzius atskirtais kableliais: ")
words1 = words.replace(",", "")
def characters(best_char): 
    dict = {} 
    for n in best_char: 
        keys = dict.keys() 
        if n in keys: 
            dict[n] += 1 
        else: 
            dict[n] = 1 
    return dict 
print(characters(words1)) 