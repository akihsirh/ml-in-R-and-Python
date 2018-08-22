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
regressor <- lm(formula = Profit ~ . , #efficient way to say Profit depends on all variables
                data = training_set)

summary(regressor)
#The above shows that the RandD spend is the bit that affects the independent variable Profit most
#predicting the test set with our trained regressor
y_predicted <- predict(regressor, newdata = test_set)

#Plot the data to better understand the regressor accuracy