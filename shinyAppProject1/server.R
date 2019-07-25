library(shiny)
library(ggplot2)
library(DT)
library(openxlsx)
library(here)

function(input, output) {
  
  # Filter data based on selections
  output$chart1 <- renderPlotly({
    #Prepare Data frame
    data <- read.xlsx(here("data", "Backlog_Master_07-12 Forecast.xlsx"),sheet = 4, colNames = TRUE)
    colnames(data) <- as.character(unlist(data[1,]))
    data <- data[-1, ]
    
    if(input$`P&L` == "All"){
      chart_data <- data.frame("Category" = unique(data$`P&L`),GP = aggregate(as.numeric(data$GP), by = list(data$`P&L`), FUN = sum)[,2])
      p <- plot_ly(chart_data, labels = ~Category, values = ~GP, type = 'pie')
    }
    if(input$`P&L` != "All"){
      chart_data <- data[data$`P&L` == input$`P&L`,]
      chart_data <- data.frame("Category" = unique(chart_data$`External Rep`),
                    GP = aggregate(as.numeric(chart_data$GP), by = list(chart_data$`External Rep`), FUN = sum)[,2])
      p <- plot_ly(chart_data, labels = ~Category, values = ~GP, type = 'pie')
    }
    p
  })
}