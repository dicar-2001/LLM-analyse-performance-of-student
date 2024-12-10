setwd("C:/Users/FHM/Downloads")
data <- read.csv("C:/Users/FHM/Downloads/SMP-SMC-SMA-SMI-S2-17-18.csv")
library(dplyr)
library(ggplot2)
library(tidyr)
library(magrittr)

data$Electricité <- as.numeric(data$Electricité)
data$Analyse.2 <- as.numeric(data$Analyse.2)
data$Algèbre.2 <- as.numeric(data$Algèbre.2)
data$Math <- as.numeric(data$Math)
data$LT <- as.numeric(data$LT)
data$Note.du.Semestre2 <- as.numeric(data$Note.du.Semestre2)

#screen this:
summary(data)

#dont screen this:
for (colname in names(data)[4:length(names(data))]){
  
  if(is.numeric(data[[colname]])){
    cat("Quantiles for", colname, ":\n")
    print(quantile(data[[colname]], probs = c(0.25, 0.5, 0.75), na.rm = TRUE))
    cat("\n") 

  }
}

#screen each histogram
hist(data$Age.,
     col='steelblue',
     main = 'Histogram of Age',
     xlab = 'Age')

# Histogram for Electricité
hist(data$Electricité,
     col= "lightblue",
     main = 'Histogram of Electricité',
     xlab = 'Electricité')


# Histogram for Analyse.2
hist(data$Analyse.2,
     col = 'lightgreen',
     main = 'Histogram of Analyse.2',
     xlab = 'Analyse.2',
     border = 'black')

# Histogram for Math
hist(data$Math,
     col = 'lightyellow',
     main = 'Histogram of Math',
     xlab = 'Math',
     border = 'black')



# Histogram for Note.du.Semestre2
hist(data$Note.du.Semestre2,
     col = 'lightcyan',
     main = 'Histogram of Note du Semestre2',
     xlab = 'Note du Semestre2',
     border = 'black')







cov(data$Age., data$Note.du.Semestre2)
cov(data$Math, data$Electricité, use = "complete.obs")
cov(data$Math, data$Analyse.2, use = "complete.obs")

# Scatter plot to visualize the relationship
plot(data$Age., data$Note.du.Semestre2,
     main = "Relation entre l'Âge et Note du Semestre2",
     xlab = "Âge",
     ylab = "Note du Semestre2",
     col = 'blue', pch = 19)
abline(lm(data$Note.du.Semestre2 ~ data$Age.), col = 'red')  # Adding a regression line



# Scatter plot to visualize the relationship
plot(data$Electricité, data$Math,
     main = "Relation entre Electricité et Math ",
     xlab = "Âge",
     ylab = "Note du Semestre2",
     col = 'blue', pch = 19)
abline(lm(data$Electricité ~ data$Math), col = 'red')  # Adding a regression line

plot(data$Analyse.2, data$Electricité,
     main = "Relation entre Electricité et Analyse.2 ",
     xlab = "Âge",
     ylab = "Note du Semestre2",
     col = 'blue', pch = 19)
abline(lm(data$Electricité ~ data$Math), col = 'red')  # Adding a regression line

boxplot(Math ~ filiere., data = data,
        main = "Boxplot of Math Scores by Filière",
        xlab = "Filière",
        ylab = "Math Scores",
        col = 'lightblue')

boxplot(Electricité ~ filiere., data = data,
        main = "Boxplot of Math Scores by Filière",
        xlab = "Filière",
        ylab = "Math Scores",
        col = 'lightblue')

boxplot(Analyse.2 ~ filiere., data = data,
        main = "Boxplot of Math Scores by Filière",
        xlab = "Filière",
        ylab = "Math Scores",
        col = 'lightblue')

