# PCA  
[![PCA](https://img.shields.io/badge/PCA-%E4%B8%BB%E6%88%90%E5%88%86%E5%88%86%E6%9E%90-red)](http://blog.sina.com.cn/s/blog_59d470310100j7f1.html)
![方差贡献率](https://img.shields.io/badge/%E6%96%B9%E5%B7%AE%E8%B4%A1%E7%8C%AE%E7%8E%87-%3E0.85-yellowgreen)
![指数](https://img.shields.io/badge/%E6%8C%87%E6%95%B0-%E8%A1%A8%E8%BE%BE%E5%BC%8F-orange)
PCA算法常用于对存在相关性的高维数据进行降维处理，本文按照方差贡献率>0.85选择主成分  
对广告数据进行分析，试图测定其间关系和建立评分或指数评估体系  
项目选取CPM,CPC,CTR,CPA,CVR等5个指标，进行建模，根据一次建模选择第一，第二主成分  
我们可以得到系数以及相应变量的线性表达式  
其中:第一主成分中所有系数都为正,则y1表达广告的强度，同，y2表达广告的难度  
