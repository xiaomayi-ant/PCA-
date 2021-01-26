import  pandas  as  pd
import  numpy as  np
import  matplotlib.pyplot  as plt
plt.style.use('seaborn-whitegrid')
plt.rc('font',**{'family':'Microsoft YaHei,SimHei'})  #设置中文字体
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

#探索性分析
df=pd.read_excel(r'C:\Desktop\dataset\PCA\La-ID.xls',sheet_name='second')
print(df)

import seaborn as  sns
sns.heatmap(df.corr(),annot=True)
plt.show()

#数据零均值化
from  sklearn.preprocessing  import scale
data=scale(df)
print(data)

from  sklearn.decomposition import PCA
pca=PCA(n_components=5)  #首次模拟与变量相同的主成分
print(pca.fit(data))

#累计贡献方差  >0.85
print(pca.explained_variance_ratio_)
print(sum(pca.explained_variance_ratio_))
plt.plot(np.cumsum(pca.explained_variance_ratio_),linewidth=3)
plt.xlabel('成份数')
plt.ylabel('累计解释方差')
plt.grid(True)
plt.show()

#根据模拟结果,重新选择主成分个数进行二次建模
pca=PCA(n_components=2).fit(data)
new_data=pca.fit_transform(data) #fit_transform  表示将生成降维后的数据

#主成分中各变量权重分析
coefficient=pd.DataFrame(pca.components_).T

#输出第一主成分表达式
x=pd.DataFrame(df).columns.values.tolist()
coe=coefficient.loc[:,0]
print('---------------------------------------------------------')
equ=[]
for  i  in  range(len(coe)):
    equ.append(str(round(coe[i],3))+'*'+str(x[i]))
st='+'
print("第一主成分="+str(st.join(equ)))
print('---------------------------------------------------------')
coe=coefficient.loc[:,1]
equ=[]
for  i  in  range(len(coe)):
    equ.append(str(round(coe[i],3))+'*'+str(x[i]))
st='+'
print("第二主成分="+str(st.join(equ)))
print('---------------------------------------------------------')

#结果分值
print(pd.DataFrame(new_data[:,0],columns=['PCA']))
df=pd.DataFrame(df)
results=df.join(pd.DataFrame(new_data[:,0],columns=['PCA']))

#排序
results.sort_values(by='PCA',ascending=False,inplace=True)
print(results)
print(type(results))

#写入excel表格
results.to_excel(r'C:\Users\Desktop\dataset\PCA\ID.xls',sheet_name='second')
print('写入完成')

