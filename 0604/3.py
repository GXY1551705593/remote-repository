'''# 1.学校在拍年度纪念照时，一般要求学生按照
# 非递减的高度顺序排列。
# 请你返回至少有多少个学生没有站在正确位置数量。该人数指的是：能让所有学生以
# 非递减
# 高度排列的必要移动人数。
# 示例：
# 输入：[1 1 4 2 1 3]
# 输出：3
# 解释：
# 高度为4、3和最后一个1的学生，没有站在正确的位置。'''
while True:
    nums=input('请输入数组：').split(' ')#输入数组并转化为列表
    # print(nums)
    nums_new=[]
    list_pepople=[]
    list_wrong=[]
    #将列表中的字符串转变为整型
    for a in nums:
        nums_new.append(int(float(a)))
        if len(nums_new)==len(nums):#数组中没有0的情况
            for index,i in enumerate(nums_new):
                    if nums_new[index]==sorted(nums_new)[index]:
                        list_pepople.append(i)
                    else:
                        list_wrong.append(i)
                    if len(list_wrong)+len(list_pepople)==len(nums_new):
                        print('有%s个学生没有站在正确位置，他们分别是%s'%(len(list_wrong),list_wrong))

