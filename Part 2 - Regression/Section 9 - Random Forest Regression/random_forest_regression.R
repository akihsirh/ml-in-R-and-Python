# Random Forest Regression

# Importing the dataset
dataset <-  read.csv('Position_Salaries.csv')
dataset <- dataset[2:3]

#Dont need to split into training and test set since the dataset is small
#Dont need feature scaling since the decision trees dont depend on Euclidean distances of the 
#data points

# Fitting Random Forest Regression to the dataset
#install.packages('randomForest')
library(randomForest)
set.seed(1234)
regressor <- randomForest(x = dataset_model[1], #we need a dataframe hence brackets 
                          y = dataset_model$Salary, # dollar sign because this needs vector
                          ntree = 450)

summary(regressor)
# Predicting a new result with Random Forest Regression
y_pred <- predict(regressor, data.frame(Level = 6.5))

# Visualising the Random Forest Regression results (higher resolution)
# install.packages('ggplot2')
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             colour = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))),
            colour = 'blue') +
  ggtitle('Truth or Bluff (Random Forest Regression)') +
  xlab('Level') +
  ylab('Salary')