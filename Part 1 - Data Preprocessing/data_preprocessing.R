#Import the dataset
dataset = read.csv("Data.csv")
head(dataset)

#Handle missing data 
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age , FUN = function(x) median(x, na.rm = TRUE)),
                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
                     ave(dataset$Salary , FUN = function(x) median(x, na.rm = TRUE)),
                     dataset$Salary)

#Encode categorical data
dataset$Country = factor(dataset$Country, 
                         levels = c("France","Germany","Spain"),
                         labels= c(1,2,3))

dataset$Purchased = factor(dataset$Purchased,
                           levels = c("Yes","No"),
                           labels = c(1,0))

#install.packages('caTools')
library(caTools)
set.seed(123)

split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#Feature scaling
training_set[,2:3] = scale(training_set[,2:3])
test_set[,2:3] = scale(test_set[,2:3])
