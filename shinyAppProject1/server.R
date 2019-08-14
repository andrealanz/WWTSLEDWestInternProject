library(shiny)
library(ggplot2)
library(DT)

function(input, output) {
  
  #create pie chart output
  output$chart1 <- renderPlotly({
    #handle if all P&L selected
    if(input$`P&L1` == "All" && input$AM == "none"){
      #prepare dataframe for plot_ly
      chart_data <- data.frame(
        "Category" = unique(data$`P&L`),
        #add up GP by P&L
        GP = aggregate(as.numeric(data$GP), by = list(data$`P&L`), 
        FUN = sum)[,2]
      )
    }
    #handle if a P&L is selected with no AM 
    if(input$`P&L1` != "All" && input$AM == "none"){
      chart_data <- data[data$`P&L` == input$`P&L1`,] #get data for specific P&L
      #prepare dataframe for plot_ly
      chart_data <- data.frame(
        "Category" = unique(chart_data$`External Rep`),
        #add GP by AM
        GP = aggregate(as.numeric(chart_data$GP), by = list(chart_data$`External Rep`), 
        FUN = sum)[,2]
      )
    }
    #handle if an AM is selected
    if(input$AM != "none"){
      #handle if specific AM selected
      if(input$AM != "All"){
        chart_data <- data[data$`External Rep` == input$AM, ] #get data for specific AM
      }
      #prepare dataframe for plot_ly
      chart_data <- data.frame(
        "Category" = unique(chart_data$`Ship to Customer`),
        #add GP grouped by customer
        GP = aggregate(as.numeric(chart_data$GP), by = list(chart_data$`Ship to Customer`), 
        FUN = sum)[,2]
      )
    }
    plot_ly(chart_data, labels = ~Category, values = ~GP, type = 'pie')
  })
  
  #possible second chart
  output$chart2 <- renderPlotly({
    
  })
  
  #create AM selection which depends on P&L selection
  output$secondSelection <- renderUI({
    if(input$`P&L1` != "All"){
      chart_data <- data[data$`P&L` == input$`P&L1`,]
    }
    selectizeInput("AM", "AM", c("none","All", unique(as.character((chart_data$`External Rep`)))))
  })
  
  #create order option selection which will depend on AM selection
  output$thirdSelection <- renderUI({
    selectizeInput("order_options", label = "Order Options", c("none", "% GP", "Status"))
  })
}