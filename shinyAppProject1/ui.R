library(shiny)
library(shinydashboard)
library(plotly)
# Load the ggplot2 package which provides
# the 'mpg' dataset.
library(ggplot2)

fluidPage(
  dashboardPage(
    dashboardHeader(title ="BackLog Summary"),
    dashboardSidebar(),
    dashboardBody(
      # Create a new Row in the UI for selectInputs
        fluidRow(
          box(
              plotlyOutput("chart1"),
              verbatimTextOutput("event"), width = NULL, title = "%GP by P&L"
          )
        ),
        fluidRow(
          box(
              selectInput("P&L", "P&L", c("All", unique(as.character((data$`P&L`)))))       
          )
        )
    )
  )
)