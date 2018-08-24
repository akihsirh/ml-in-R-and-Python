# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('PositionSalaries.csv')
dataset_model <- dataset[2:3]

#Dont need to split into training and test set since the dataset is small
#Dont need feature scaling since the features of the polynomial regression are basically going
#to be just n degree terms of the main input feature levels

#Build the polynomial regressor
dataset_model$Level2 <- dataset$Level ^ 2
dataset_model$Level3 <- dataset$Level ^ 3
dataset_model$Level4 <- dataset$Level ^ 4
poly_reg = lm(formula = Salary ~ . , 
              data = dataset_model )
summary(poly_reg)

#Plot the results of polynomial regression
library(ggplot2)
p <- ggplot()
p + geom_point(data = dataset_model,
                    aes(x=dataset_model$Level, 
                        y=dataset_model$Salary, 
                        color= 'Red')) + 
  geom_line(data = dataset_model,
            aes(x=dataset_model$Level, y=predict(poly_reg, newdata = dataset_model)),
            color = 'Blue',
            size = 0.9) +
  xlab("Position Level") +
  ylab("Salary") +
  ggtitle("Salary based on position")

#Find the salary for a custom position level
predict(poly_reg, data.frame(Level = 6.5, Level2 = 6.5 ^ 2, Level3 = 6.5 ^ 3, Level4 = 6.5 ^ 4))
