# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Salary_Data.csv')

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#fit the training set to the simple linear regression model
regressor <- lm(formula = Salary ~ YearsExperience,
                data = training_set)

summary(regressor)
#run summary on the regressor to see the various statistical parameters such as p value
# multiple r squared etc. These model parameters can give us important info about the model
#for the below example the variable of experience is marked with 3 stars which shows
# that experience as a variable is statistically significant. The very very small p value
# also supports this. This gives us an indication that the formula we specified Salary ~ Years
# is the right one


#Test the accuracy of the regressor on the test set
predicted_results <- predict(regressor, newdata = test_set)

#Plot the training set 
library(ggplot2)
p_train <- ggplot(data = training_set)
p_train + geom_point(aes(x=YearsExperience, 
                   y=Salary, 
                   color= 'Red')) + 
  geom_line(aes(x=YearsExperience, y=predict(regressor, newdata = training_set)),
            color = 'Blue',
            size = 0.9) +
  xlab("Experience in Years") +
  ylab("Salary") +
  ggtitle("Salary vs Experience")

#Plot the test set 
p_test <- ggplot()
p_test + geom_point(data = test_set,
                    aes(x=test_set$YearsExperience, 
                         y=test_set$Salary, 
                         color= 'Red')) + 
  geom_line(data = training_set,
            aes(x=training_set$YearsExperience, y=predict(regressor, newdata = training_set)),
            color = 'Blue',
            size = 0.9) +
  xlab("Experience in Years") +
  ylab("Salary") +
  ggtitle("Salary vs Experience")

            