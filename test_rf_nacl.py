## -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 19:22:03 2022

@author: ma
"""

# Importing the required libraries
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from openpyxl import load_workbook
from sklearn.tree import export_graphviz
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
import random
# Reading the csv file and putting it into 'df' object
df = pd.read_csv('pore_nacl2.csv')
#df = pd.read_csv('pore_na2so4.csv')
df.head()

# Putting feature variable to X
X = df.drop('NaCl',axis=1)
# Putting response variable to y
y = df['NaCl']
#X = df.drop('Na2SO4',axis=1)
### Putting response variable to y
#y = df['Na2SO4']
r_score1,r_score2,r_score3=[],[],[]
random2r=[]
#rmse_score=[]
#rmse_score1,rmse_score2,rmse_score3=[],[],[]
#
#result,result_all=[],[]
#choice=[]
#for i in range(20,160,5):
#    X_train_all, X_test, y_train_all, y_test = train_test_split(X, y, train_size=0.8, random_state=i)#89
#    X_train_all.shape, X_test.shape
#    
#    
## now lets split the data into train and test
##Splitting the data into train and test
##=========================================================================================
#    for j in range(20,200,5):
#        X_train, X_ver, y_train, y_ver = train_test_split(X_train_all, y_train_all, train_size=0.8, random_state=j)
#        X_train.shape, y_ver.shape
#        
#        for k in range(120,200,20):
#            
#            for l in range(5,12,1):
#                
#                rfc = RandomForestRegressor(n_estimators=k+1,                    
#                         max_depth=l, 
#                                                   
#                         random_state=9)
#                rfc.fit(X_train, y_train)
#                 # 对测试集进行预测
#                y_pred = rfc.predict(X_ver)
#                ## evaluate predictions
#                pearson_r=stats.pearsonr(y_ver,y_pred)
#                R2=metrics.r2_score(y_ver,y_pred)
#                RMSE=metrics.mean_squared_error(y_ver,y_pred)**0.5
#                print('Pearson correlation coefficient is {0}, and RMSE is {1}.'.format(pearson_r[0],RMSE))
#                print ('r2_score: %.2f' %R2)
#                result=[]
#                result.append(i)
#                result.append(j)
#                result.append(k)
#                result.append(l)
#                result.append(R2)
#                result.append(RMSE)
#                result_all.append(result)
###########################################################################
#
#
#for i in result_all:
#    if i[-2]>0.8:
#        
#        choice.append(i)
#
#                
#######################################################################            
#test_r,test_rmse=[],[]
#for i in choice:
#    X_train_all, X_test, y_train_all, y_test = train_test_split(X, y, train_size=0.8, random_state=i[0])#89
#    X_train_all.shape, X_test.shape
#    X_train, X_ver, y_train, y_ver = train_test_split(X_train_all, y_train_all, train_size=0.8, random_state=i[1])
#    X_train.shape, y_ver.shape
#    rfc = RandomForestRegressor(n_estimators=i[2],                    
#                         max_depth=i[3], 
#                                                   
#                         random_state=9)
#    rfc.fit(X_train, y_train)
#          
#    y_pred = rfc.predict(X_test)
#    random_forest_error=y_pred-y_test    
#    # evaluate predictions
#    from sklearn import metrics
#    print('Mean Absolute Error: ', metrics.mean_absolute_error(y_test,y_pred))
#    pearson_r=stats.pearsonr(y_test,y_pred)
#    R2=metrics.r2_score(y_test,y_pred)
#    RMSE=metrics.mean_squared_error(y_test,y_pred)**0.5
#    test_r.append(R2)
#    test_rmse.append(RMSE)


#######################################################################################
###66 116
###
X_train_all, X_test, y_train_all, y_test = train_test_split(X, y, train_size=0.8, random_state=30)#nacl_117,na2so4_57,71,mgso4_31,mgcl2_141
X_train_all.shape, X_test.shape
X_train, X_ver, y_train, y_ver = train_test_split(X_train_all, y_train_all, train_size=0.8, random_state=185)#nacl_45,na2so4_193,33,mgso4_169,mgcl2_45
X_train.shape, y_ver.shape
train_X_column_name=list(X_train.columns)
rfc = RandomForestRegressor(n_estimators=180,                    
                         max_depth=11,
                          
                         random_state=7)
rfc.fit(X_train, y_train)

#################################################################################################
random_forest_predict1=rfc.predict(X_ver)
random_forest_error1=random_forest_predict1-y_ver
# Verify the accuracy
from sklearn import metrics
print('Mean Absolute Error: ', metrics.mean_absolute_error(y_ver,random_forest_predict1))
pearson_r1=stats.pearsonr(y_ver,random_forest_predict1)
R21=metrics.r2_score(y_ver,random_forest_predict1)
RMSE1=metrics.mean_squared_error(y_ver,random_forest_predict1)**0.5

#Draw test plot
font = {"color": "darkred",
        "size": 18,
        "family" : "times new roman"}
font1 = {"color": "black",
        "size": 12,
        "family" : "times new roman"}

Text='r='+str(round(pearson_r1[0],2))
plt.figure(3)
plt.clf()
ax=plt.axes(aspect='equal')
plt.scatter(y_ver,random_forest_predict1,color='red')
plt.xlabel('True Values',fontdict=font)
plt.ylabel('Predictions',fontdict=font)
Lims=[0,110]
plt.xlim(Lims)
plt.ylim(Lims)
plt.tick_params(labelsize=10)
plt.plot(Lims,Lims,color='black')
plt.grid(False)
plt.title('ion',fontdict=font)
plt.text(2,10,Text,fontdict=font1)
plt.savefig('figure3.png', dpi=100,bbox_inches='tight') 

################################################################################################
# 对测试集进行预测
y_pred = rfc.predict(X_test)
random_forest_error=y_pred-y_test
# evaluate predictions
from sklearn import metrics
print('Mean Absolute Error: ', metrics.mean_absolute_error(y_test,y_pred))
pearson_r=stats.pearsonr(y_test,y_pred)
R2=metrics.r2_score(y_test,y_pred)
RMSE=metrics.mean_squared_error(y_test,y_pred)**0.5
print('Pearson correlation coefficient is {0}, and RMSE is {1}.'.format(pearson_r[0],RMSE))
print ('r2_score: %.2f' %R2)
   
#Draw test plot
font = {"color": "darkred",
        "size": 18,
        "family" : "times new roman"}
font1 = {"color": "black",
        "size": 12,
        "family" : "times new roman"}

Text='r='+str(round(pearson_r[0],2))
plt.figure(1)
plt.clf()
ax=plt.axes(aspect='equal')
plt.scatter(y_test,y_pred,color='red')
plt.xlabel('True Values',fontdict=font)
plt.ylabel('Predictions',fontdict=font)
Lims=[0,110]
plt.xlim(Lims)
plt.ylim(Lims)
plt.tick_params(labelsize=10)
plt.plot(Lims,Lims,color='black')
plt.grid(False)
plt.title('ion',fontdict=font)
plt.text(2,10,Text,fontdict=font1)
plt.savefig('figure1.png', dpi=100,bbox_inches='tight')   


plt.figure(2)
plt.clf()
plt.hist(random_forest_error,bins=30)
plt.xlabel('Prediction Error',fontdict=font)
plt.ylabel('Count',fontdict=font)
plt.grid(False)
plt.title('ion',fontdict=font)
plt.savefig('figure2.png', dpi=100,bbox_inches='tight')
print('Pearson correlation coefficient is {0}, and RMSE is {1}.'.format(pearson_r[0],RMSE))
#
## 显示重要特征
# Calculate the importance of variables
random_forest_importance=list(rfc.feature_importances_)
random_forest_feature_importance=[(feature,round(importance,8)) 
                                  for feature, importance in zip(train_X_column_name,random_forest_importance)]
random_forest_feature_importance=sorted(random_forest_feature_importance,key=lambda x:x[1],reverse=True)
#Calculate the importance of variables

################################################################################################重复做实验
choice_repeat=[]
for i in range(0,300,1):
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=i)#89
    X_train.shape, X_test.shape
    
    
# now lets split the data into train and test
#Splitting the data into train and test
#=========================================================================================


    rfc1 = RandomForestRegressor(n_estimators=180,                    
                         max_depth=11,
                          
                         random_state=7)
    rfc1.fit(X_train, y_train)
                 # 对测试集进行预测
    y_pred = rfc1.predict(X_test)
    #################################################################################################
    random_forest_predict1=rfc1.predict(X_train)
    random_forest_error1=random_forest_predict1-y_train
    # Verify the accuracy
    from sklearn import metrics
    mae1=metrics.mean_absolute_error(y_train,random_forest_predict1)
    pearson_r1=stats.pearsonr(y_train,random_forest_predict1)
    R21=metrics.r2_score(y_train,random_forest_predict1)
    RMSE1=metrics.mean_squared_error(y_train,random_forest_predict1)**0.5
    ###########################################################################################################
        ## evaluate predictions
    pearson_r=stats.pearsonr(y_test,y_pred)
    mae=metrics.mean_absolute_error(y_test,y_pred)
    R2=metrics.r2_score(y_test,y_pred)
    RMSE=metrics.mean_squared_error(y_test,y_pred)**0.5
    print('Pearson correlation coefficient is {0}, and RMSE is {1}.'.format(pearson_r[0],RMSE))
    print ('r2_score: %.2f' %R2)
    result=[]
    
    result.append(R2)
    result.append(i)
    result.append(mae)
    result.append(RMSE)
    
    random_forest_importance1=list(rfc1.feature_importances_)
    for j in random_forest_importance1:
        result.append(j)
    
    result.append(R21)
    result.append(mae1)
    result.append(RMSE1)    
    choice_repeat.append(result)
    

resule_repeat_choice=sorted(choice_repeat,reverse=True)    
sum_mae,sum_r2,sum_rmse,sum_rd,sum_zeta,sum_bar,sum_con,sum1_mae,sum1_r2,sum1_rmse=[],[],[],[],[],[],[],[],[],[]

for i in resule_repeat_choice[:50]:
    sum_mae.append(i[2])
    sum_r2.append(i[0])
    sum_rmse.append(i[3])
    sum_rd.append(i[4])
    sum_zeta.append(i[5])
    sum_bar.append(i[6])
    sum_con.append(i[7])
    sum1_r2.append(i[8])
    sum1_mae.append(i[9])
    sum1_rmse.append(i[10])
  
all_mae=np.array(sum_mae)
mean_mae=np.mean(all_mae)
std_mae=np.std(all_mae,ddof = 1)

all_r2=np.array(sum_r2)
mean_r2=np.mean(all_r2)
std_r2=np.std(all_r2,ddof = 1)

all_rmse=np.array(sum_rmse)
mean_rmse=np.mean(all_rmse)
std_rmse=np.std(all_rmse,ddof = 1)

all_rd=np.array(sum_rd)
mean_rd=np.mean(all_rd)
std_rd=np.std(all_rd,ddof = 1)

all_zeta=np.array(sum_zeta)
mean_zeta=np.mean(all_zeta)
std_zeta=np.std(all_zeta,ddof = 1)

all_bar=np.array(sum_bar)
mean_bar=np.mean(all_bar)
std_bar=np.std(all_bar,ddof = 1)

all_con=np.array(sum_con)
mean_con=np.mean(all_con)
std_con=np.std(all_con,ddof = 1)

all_mae1=np.array(sum1_mae)
mean_mae1=np.mean(all_mae1)
std_mae1=np.std(all_mae1,ddof = 1)

all_r21=np.array(sum1_r2)
mean_r21=np.mean(all_r21)
std_r21=np.std(all_r21,ddof = 1)

all_rmse1=np.array(sum1_rmse)
mean_rmse1=np.mean(all_rmse1)
std_rmse1=np.std(all_rmse1,ddof = 1)