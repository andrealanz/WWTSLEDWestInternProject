library(shiny)
library(shinydashboard)
library(plotly)
library(ggplot2)

sidebar <- dashboardSidebar(
      #create sidebar with the given tabs
      sidebarMenu(
        menuItem("Profit & Loss", tabName = "profit_loss"),
        menuItem("Account Managers", tabName = "acc_man")
      )
)

#create dashboard main body   
body <- dashboardBody(
  #fill tabs
  tabItems(
    #first tab
    tabItem(tabName = "profit_loss",
        fluidRow(
          box(
            checkboxGroupInput("metric", "Choose Statistic", c("%GP"))
          )
        ),
        #output for pie chart
        fluidRow(
          box(
            plotlyOutput("chart1"),
            width = NULL, title = "%GP by P&L"
          )
        ),
        #create drop-down menus
        fluidRow(
          box(
              selectizeInput("P&L1", "P&L", c("All", unique(as.character((data$`P&L`)))), selected = "All")       
          ),
          box(
            uiOutput("secondSelection")       
          ),
          box(
            uiOutput("thirdSelection")
          )
        )
    ),
    #second tab
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

#create dashboard
dashboardPage(skin = "black",
  dashboardHeader(title ="BackLog Summary"),
  sidebar,
  body
)
