# while True:
#     t=input('请输入t：')
#     p=input('请输入p：')
#     def naive_matching(t,p):
#         m,n=len(p),len(t)
#         i,j=0,0
#         while i<m and j<n:
#             if p[i]==p[j]:
#                 i,j=i+1,j+1
#             else:
#                 i,j=0,j-i+1
#         if i==m:
#             return j-1
#         return -1
#     if __name__ == '__main__':
#         ret=naive_matching(t,p)
#         print(
import pymysql
