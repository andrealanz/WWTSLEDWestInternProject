library(openxlsx)

#Read in data
data <- read.xlsx("Backlog_Master_07-12 Forecast.xlsx",sheet = 4, colNames = TRUE)

#Prepare data frame
colnames(data) <- as.character(unlist(data[1,]))
data <- data[-1, ]
groups <- c("SLED California", "SLED Southwest", "SLED Northwest", "SLED HI/Comm", "Federal USACE", "SLED House")
data <- data[data$`P&L` %in% groups, ]
chart_data <- data   #initialize chart data
