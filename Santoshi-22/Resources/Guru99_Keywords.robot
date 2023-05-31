*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary
Resource    ../Configuration/Guru99_Env.robot
Resource    PageObject/Guru99_HomePage.robot
Library     ../Library/Decode.py
Library     RequestsLibrary


*** Keywords ***
User Navigate to Guru99.com
    open browser        ${URL}          ${Browser}
    maximize browser window
    capture page screenshot

User Enter all login Details
    [Arguments]        ${UserID}
    wait until element is visible   ${BankProject_Link_Xpath}
    click element       ${BankProject_Link_Xpath}
    ${status}       run keyword and return status       element should be visible  //iframe[contains(@title,'ad ')]
    sleep           5s
    IF       ${status}== True
        select frame        //iframe[contains(@title,'ad ')]
        select frame        //iframe[@id='ad_iframe']
        sleep               5s
        click element       //div[@id='dismiss-button']
        unselect frame
    END
    sleep           10s
    input text          ${UserID_xpath}      ${UserID}
    ${Password}  decode password        ${Password}
    wait until element is enabled       ${Password_xpath}
    input text          ${Password_xpath}     ${Password}

User Click on submit button
    wait until element is visible       ${Login_Btn}
    click element       ${Login_Btn}
    capture page screenshot

Make a call to Reqres.in
    create session      Test        https://reqres.in/
    ${response}     get on session     Test        url=api/users?page=2
    log to console      ${response.status_code}
    log to console      ${response.text}