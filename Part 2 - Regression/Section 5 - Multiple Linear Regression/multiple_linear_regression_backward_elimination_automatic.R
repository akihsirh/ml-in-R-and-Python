# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('50_Startups.csv')

#Encode the categorical data state
dataset$State <- factor(x = dataset$State, 
                        levels = c("New York","California","Florida"),
                        labels = c(1,2,3))


# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Intercepts are considered by the lm function unlike Python where we had to add an extra column
# Feature Scaling wont be applied since the linear regression libraries support feature scaling
# R also created the dummy variable for the encoded variable and like Python automatically 
#handles the dummy variable trap

#Fit the multiple linear regression model to the training set
regressor = lm(formula = Profit ~ ., data = training_set)
backwardElimination <- function(x, siglevel) {
  numPredictors = length(x) # equivalent to ncol
  
  for (i in c(1:numPredictors)){
    regressor = lm(formula = Profit ~ ., data = x)
    maxVar = max(coef(summary(regressor))[c(2:numPredictors), "Pr(>|t|)"]) #matrix of stats
    if (maxVar > siglevel){
      j = which(coef(summary(regressor))[c(2:numPredictors), "Pr(>|t|)"] == maxVar) #Location or variable number
      x = x[, -j] # remove max p value predictor
    }
    numPredictors = numPredictors - 1
  }
  return(summary(regressor))
}

SL = 0.05
training_set_opt = training_set[, c(1,2,3,4,5)]
backwardElimination(training_set_opt, SL)

#predicting the test set with our trained regressor
y_predicted <- predict(regressor, newdata = test_set)

#Plot the data to better understand the regressor accuracy