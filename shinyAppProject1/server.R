library(shiny)
library(ggplot2)
library(DT)
library(openxlsx)
library(here)

function(input, output) {
  
  #Prepare Data frame
  data <- read.xlsx(here("data", "Backlog_Master_07-12 Forecast.xlsx"),sheet = 4, colNames = TRUE)
  colnames(data) <- as.character(unlist(data[1,]))
  data <- data[-1, ]
  
  # Filter data based on selections
  output$chart1 <- renderPlotly({
    if(input$`P&L` == "All"){
      chart_data <- data.frame("Category" = unique(data$`P&L`),GP = aggregate(as.numeric(data$GP), by = list(data$`P&L`), FUN = sum)[,2])
    }
    if(input$`P&L` != "All" && input$AM == "none"){
      chart_data <- data[data$`P&L` == input$`P&L`,]
      chart_data <- data.frame("Category" = unique(chart_data$`External Rep`),
                    GP = aggregate(as.numeric(chart_data$GP), by = list(chart_data$`External Rep`), FUN = sum)[,2])
    }
    if(input$AM != "none"){
      chart_data <- data
      if(input$AM != "All"){
        chart_data <- data[data$`External Rep` == input$AM, ]
      }
      chart_data <- data.frame("Category" = unique(chart_data$`Ship to Customer`),
                               GP = aggregate(as.numeric(chart_data$GP), by = list(chart_data$`Ship to Customer`), FUN = sum)[,2])
    }
    plot_ly(chart_data, labels = ~Category, values = ~GP, type = 'pie')
  })
  
  output$secondSelection <- renderUI({
    chart_data <- data
    if(input$`P&L` != "All"){
      chart_data <- data[data$`P&L` == input$`P&L`,]
    }
    selectInput("AM", "AM", c("none","All", unique(as.character((chart_data$`External Rep`)))), selected = "none")
  })
  
  output$thirdSelection <- renderUI({
    selectInput("order_options", label = "Order Options", c("none", "% GP", "Status"))
  })
}