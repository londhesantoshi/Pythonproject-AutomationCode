*** Settings ***
Documentation    This keyword file contains implementation of TC's for SouceDemo website
Library          SeleniumLibrary
Resource         ../Configuration/SouceDemoConfig_Env.robot
Resource         PageObject/SouceDemo_HomePage.robot

*** Variables ***
${Username}         standard_user
${Password}         secret_sauce
${FirstName}        Roshni
${LastName}         Patil
${PostalCode}       411012

*** Keywords ***
User navigate to SauceDemo Website
    open browser        ${URL}              ${Browser}
    maximize browser window

User enter valid username
    input text          ${UsernameID}       ${Username}

user enter valid password
    input text          ${PasswordID}       ${Password}

user click on login button
    click element       ${SubmitBtnID}
    capture page screenshot

user click on product sort container dropdown
    click element       ${Product_Sort_DropDown}

user select category price low to high
    click element       ${Price_LowToHigh_Cat}
    capture page screenshot

user click on first product
    click element       ${Pro_Sauce_Labs_Onesie}

user click on add to cart button
    click element       ${AddTo_Cart_Btn}

user clcik on Shopping cart container menu
    click element       ${Shopping_Cart_Menu_Btn}

user click on checkout button
    click element       ${Checkout_BtnID}

user fill all information
    input text          ${FirstNameID}      ${FirstName}
    input text          ${LastNameID}       ${LastName}
    input text          ${PostCodeID}       ${PostalCode}

user click on continue button
    click element       ${ContinueBtn_ID}

user click on finish button
    click element       ${FinishBtn_ID}
    capture page screenshot

user click on react burger menu button
    click element       ${React_burger_Menu_BtnID}
    sleep               5s

click on logout link
    click element       ${Logout_Link}
    capture page screenshot
    close all browsers