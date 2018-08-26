# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset_model <- dataset[2:3]

#Dont need to split into training and test set since the dataset is small
#Dont need feature scaling since the decision trees dont depend on Euclidean distances of the 
#data points

#Build the decision tree regressor
#install.packages('rpart')
library(rpart)
regressor = rpart(formula = Salary ~ .,
                  data = dataset_model ,
                  control = rpart.control(minsplit = 1))

summary(regressor)

#Find the salary for a custom position level
predict(regressor, data.frame(Level = 6.5))

#Plot the results of decision tree regression in higher resolution
x_plot <- seq(min(dataset_model$Level), max(dataset_model$Level), 0.01)

library(ggplot2)
p <- ggplot()
p + geom_point(aes(x=dataset_model$Level, 
                   y=dataset_model$Salary, 
                   color= 'Red')) + 
  geom_line(aes(x=x_plot, y=predict(regressor, newdata = data.frame(Level= x_plot))),
            color = 'Blue',
            size = 0.9) +
  xlab("Position Level") +
  ylab("Salary") +
  ggtitle("Salary based on position")

