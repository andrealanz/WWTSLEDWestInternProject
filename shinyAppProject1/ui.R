library(shiny)
# Load the ggplot2 package which provides
# the 'mpg' dataset.
library(ggplot2)

fluidPage(
  titlePanel("Basic DataTable"),
  
  # Create a new Row in the UI for selectInputs
  fluidRow(
    column(4,
           selectInput("program",
                       colnames(data)[2],
                       c("All",
                         unique(as.character(data$`Financial Rptg Program`))))
    ),
    column(4,
           selectInput("P&L",
                       "P&L",
                       c("All",
                         unique(as.character(data$`P L`))))
    ),
    column(4,
           selectInput("channel",
                       "Sales Channel",
                       c("All",
                         unique(as.character(data$`Sales Channel`))))
    )
  ),
  # Create a new row for the table.
  DT::dataTableOutput("table")
)