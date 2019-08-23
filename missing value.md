## missing value

//one way to fix hte missing value is replace the missing value by the mean of the column  
// the library that we're going to use for this one is sikat learn pre-processing  
from sklearn.preprocessing import imputer [sample](https://scikit-learn.org/stable/modules/impute.html#impute)   
imputer = Imputer(missing_values = 'NaN',strategy = 'mean', axis = 0)  
 ##we are only going to fit it to the columns where there is some missing data  
imputer = imputer.fit(x[:,1:3])  
 #we need to replace the missing data of the metrics X by the mean of the column  
X[:,1:3] = imputer.transform(X[:,1:3])  


### R:

dataset$age = ifelse(is.na(dataset$age), ave(dataset$age, FUN = function(x) mean(x, na.rm = TRUE)),dataset$age)
