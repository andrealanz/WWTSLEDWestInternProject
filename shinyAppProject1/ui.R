library(shiny)
library(shinydashboard)
library(plotly)
# Load the ggplot2 package which provides
# the 'mpg' dataset.
library(ggplot2)


sidebar <- dashboardSidebar(
      sidebarMenu(
        menuItem("Profit & Loss", tabName = "profit_loss"),
        menuItem("Account Managers", tabName = "acc_man")
      )
)
    
body <- dashboardBody(
  tabItems(
    tabItem(tabName = "profit_loss",
        fluidRow(
          box(
            plotlyOutput("chart1"),
            width = NULL, title = "%GP by P&L"
          )
        ),
        fluidRow(
          box(
              selectInput("P&L1", "P&L", c("All", unique(as.character((data$`P&L`)))), selected = "All")       
          ),
          box(
            uiOutput("secondSelection")       
          ),
          box(
            uiOutput("thirdSelection")
          )
        )
    ),
    tabItem(tabName = "acc_man",
        fluidRow(
          box(
            h2("new tab"),
            #plotlyOutput("chart2"),
            width = NULL, title = "%GP by AM"
          )
        )
    )
  )
)

dashboardPage(skin = "black",
  dashboardHeader(title ="BackLog Summary"),
  sidebar,
  body
)
