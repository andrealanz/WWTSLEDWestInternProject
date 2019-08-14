library(shiny)
library(ggplot2)
library(DT)

function(input, output) {
  
  # Filter data based on selections
  output$chart1 <- renderPlotly({
    if(input$`P&L1` == "All" && input$AM == "none"){
      chart_data <- data.frame(
        "Category" = unique(data$`P&L`),
        GP = aggregate(as.numeric(data$GP), by = list(data$`P&L`), FUN = sum)[,2]
      )
    }
    if(input$`P&L1` != "All" && input$AM == "none"){
      chart_data <- data[data$`P&L` == input$`P&L1`,]
      chart_data <- data.frame(
        "Category" = unique(chart_data$`External Rep`),
        GP = aggregate(as.numeric(chart_data$GP), by = list(chart_data$`External Rep`), FUN = sum)[,2]
      )
    }
    if(input$AM != "none"){
      if(input$AM != "All"){
        chart_data <- data[data$`External Rep` == input$AM, ]
      }
      chart_data <- data.frame(
        "Category" = unique(chart_data$`Ship to Customer`),
        GP = aggregate(as.numeric(chart_data$GP), by = list(chart_data$`Ship to Customer`), FUN = sum)[,2]
      )
    }
    plot_ly(chart_data, labels = ~Category, values = ~GP, type = 'pie')
  })
  
  output$chart2 <- renderPlotly({
    
  })
  
  output$secondSelection <- renderUI({
    if(input$`P&L1` != "All"){
      chart_data <- data[data$`P&L` == input$`P&L1`,]
    }
    selectizeInput("AM", "AM", c("none","All", unique(as.character((chart_data$`External Rep`)))))
  })
  
  output$thirdSelection <- renderUI({
    selectizeInput("order_options", label = "Order Options", c("none", "% GP", "Status"))
  })
}