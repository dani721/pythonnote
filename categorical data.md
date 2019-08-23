# Categorical data

##### why we need to do it?
- In the sample dataset, there two variables are categorical variables because simply they contain categories.  
Encoding categorical data  
from sklearn.preprocessing import LabelEncoder
labelendcoder_X = LabelEncoder( )
X[:,0] = labelendcoder_X.fit_transform(X[:,0]) // we are going to apply this method on X but not the whole matrix X we just want the first column  
//for fix problems, we need dummy variable  
from sklearn.preprocessing import LabelEncoder,OnehotEncoder  
onehotencoder = OneHotEncoder(categoricl_features = [0])
X= onehotencoder.fit_transform(x)
