## Feaure Scaling

##### why we need to do it
for a sample, in the dataset, age scal and salary scal are not on the same the same scal. such as the age is 27-50, salary is 40k to 90k  
it causes problems.  

feature scaling  
- standardisation  
- normalisation  

##### goal is put them on the same scal  
///feature scaling  
from sklearn.preprocessing import StandardScaler  
sc_X = StandardScaler()  
X_train = sc_X.transform(X_test)  


