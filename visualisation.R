library(readxl)
library(dplyr)
library(tidyr)
library(ggplot2)
library(reshape2)
# Load the Excel file
df <- read.csv("C:/Users/Dell/Downloads/Nouveau dossier/data.csv")

# View the first few rows of the data
head(df)
tail(df)
View(df)

#vissss ###############

# Convert relevant columns to numeric, forcing conversion and handling potential issues
df <- df %>%
  mutate(across(c(Electricité, Analyse.2, Algèbre.2, Math, LT, Note.du.Semestre2), as.numeric))

# Calculate the correlation matrix, ignoring NA values
cor_matrix <- cor(df[, c("Electricité", "Analyse.2", "Algèbre.2", "Math", "LT", "Note.du.Semestre2")], use = "complete.obs")

# Melt the correlation matrix into a format suitable for ggplot
melted_cor <- melt(cor_matrix)

# Create the heatmap
ggplot(data = melted_cor, aes(x=Var1, y=Var2, fill=value)) + 
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", 
                       midpoint = 0, limit = c(-1,1), space = "Lab", 
                       name="Correlation") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, vjust = 1, 
                                   size = 12, hjust = 1)) +
  coord_fixed() +
  labs(title = "Heatmap of Score Correlations Across Subjects", x = "Subject", y = "Subject")

##boxplot 
  # Reshape the data into long format for ggplot
  df_long <- df %>%
    select( Electricité, Analyse.2, Algèbre.2, Math, LT, Note.du.Semestre2) %>%
    pivot_longer(cols = c(Electricité, Analyse.2, Algèbre.2, Math, LT, Note.du.Semestre2), 
                 names_to = "Subject", 
                 values_to = "Score")
  
  # Create the boxplot
  ggplot(df_long, aes(x = Subject, y = Score, fill = Subject)) +
    geom_boxplot() +
    theme_minimal() +
    labs(title = "Boxplot of Scores Across Subjects", x = "Subject", y = "Score") +
    theme(axis.text.x = element_text(angle = 45, vjust = 1, hjust = 1))
  



