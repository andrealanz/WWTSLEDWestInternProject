library(shiny)
library(ggplot2)
library(DT)
library(openxlsx)
library(here)

function(input, output) {
  
  # Filter data based on selections
  output$table <- DT::renderDataTable(DT::datatable({
    #Prepare Data frame
    data <- read.xlsx(here("shinyAppProject1","data", "Backlog Order Summary.xlsx"), colNames = TRUE)
    colnames(data) <- as.character(unlist(data[1,]))
    data <- data[-1, ]
    if (input$program != "All") {
      data <- data[data$`Financial Rptg Program` == input$program,]
    }
    if (input$`P&L` != "All") {
      data <- data[data$`P L` == input$`P&L`,]
    }
    if (input$channel != "All") {
      data <- data[data$`Sales Channel` == input$channel,]
    }
    data
  }))
  
}