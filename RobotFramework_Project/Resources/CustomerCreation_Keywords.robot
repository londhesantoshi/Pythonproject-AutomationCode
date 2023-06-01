*** Settings ***
Documentation    This keyword file contains implementaion of TC's of Customer Creation
Library          SeleniumLibrary
Resource         ../Configuration/CustomerCreation_Env.robot
Resource         PageObject/CustomerCreation_HP.robot
Library          ../Library/Decode.py

*** Keywords ***
I Navigate to Microsoftonline.com
    open browser    ${URL}      ${Browser}
    maximize browser window
    capture page screenshot

I Enter all Login Details
    [Arguments]     ${EmailID}
    wait until element is visible       ${Email_Xpath}
    input text      ${Email_Xpath}      ${EmailID}
    click element   ${Next_Button}
    wait until element is enabled       ${Password_Xpath}
    ${Password}     decode password      ${Password}
    input text      ${Password_Xpath}   ${Password}
    wait until element is visible       ${SignIn_Btn}
    click element   ${SignIn_Btn}

I click on submit Button
    wait until element is visible   ${Yes_btn}
    click element   ${Yes_btn}

I click on Dynamics 365-custom app
    wait until element is enabled   //iframe[@id='AppLandingPage']
    select frame        //iframe[@id='AppLandingPage']
    click element       //div[@title='Dynamics 365 — custom']

I click on new & select Lead
    click element       //div[@title='Leads']
    click element       //button[@aria-label='New']

I Enter all lead details & click on save & close
