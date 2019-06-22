'''1。给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。'''
# nums=[2,0,1,0,4,3,0,11,7]
while True:
    nums=input('请输入数组：').split(' ')#输入数组并转化为列表
    nums_new=[]
    #将列表中的字符串转变为整型
    for a in nums:
        nums_new.append(int(float(a)))
        if len(nums_new)==len(nums):#数组中没有0的情况
            list_nums = []
            if nums_new.count(0)==0:
                for i in nums_new:
                        list_nums.append(i)
                        if len(list_nums)==len(nums):
                            print(sorted(list_nums))
            else:#数组中有0时的排序
                list_nums1=[]
                list_nums2=[]
                for j in nums_new:
                    if j!=0:
                        list_nums1.append(j)
                        # if len(list_nums1)==len(nums)-nums.count(0):

                for n in nums_new:
                    if n==0:
                        if n==0:
                            list_nums2.append(0)
                            # if len(list_nums2) == nums.count(0):
                if len(list_nums1+list_nums2)==len(nums_new):
                    print(list_nums1+list_nums2)


