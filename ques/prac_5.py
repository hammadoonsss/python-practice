lis_main = ["l1","l2","l3","l4"]
dic = {
    "l1" : [1,2,3,4],
    "l2" : [2,4,6,8],
    "l3" : [1,3,5,7],
    "l4" : [0,9,8,7],
}
print(dic)
lis_temp = []
for ele in lis_main:
    print("ele",ele)
    lis_temp = lis_temp + dic[ele]
print("lis_temp:", lis_temp)


lis_main2 = "White"
dic2 = {
    "White" : "B02001002",
    "Black" : "B02001003",
    "Native Indian" : "B02001004",
    "Asian" : "B02001005",
    "Native Hawaiian" : "B02001006"
}
print(dic2)
print(lis_main2)
a = dic2[lis_main2]
print("a--a",a)

    