*** Settings ***
Documentation   This Keyword file contains implementation of goibibo TC's
Library         SeleniumLibrary
#Resource        ../Configuration/${ENV}_Env.robot
Library         ../Library/TimeStamp.py

*** Keywords ***
I Navigate to goibibo.com
        open browser      https://www.goibibo.com       Chrome
        maximize browser window
        click element   //span[@class='logSprite icClose']
        ${timestamp}    get_Timestamp
        log to console  ${timestamp}

#I Select for trip
#        wait until element is enabled      //span[text()='From']/following-sibling::p           10s
#        click element       //span[text()='From']/following-sibling::p
#        Input text          //input[@type='text']                                               Pune
#        press keys          //input[@type='text']                                               ENTER
#        wait until element is visible       //p[text()='Enter city or airport']/preceding-sibling::span[text()='To']      10s
#        click element       //p[text()='Enter city or airport']/preceding-sibling::span[text()='To']
#        Input text          //input[@type='text']                                               Bengaluru
#        press keys          //input[@type='text']                                               ENTER
#
#I Select Date
#        click element       //span[text()='Departure']
#        wait until element is visible     //div[@aria-label='Sun May 14 2023']                  10s
#        click element       //div[@aria-label='Sun May 14 2023']
#        wait until element is enabled       //span[text()='Done']       10s
#        click element       //span[text()='Done']
#
#I Select Class
#        wait until element is enabled       //span[text()='Travellers & Class']                 10s
#        click element       //span[text()='Travellers & Class']
#        click element       //li[text()='economy']
#        click element       //a[text()='Done']
#
#I Click on Search flights button
#        wait until element is enabled       //span[text()='SEARCH FLIGHTS']                      10s
#        click element   //span[text()='SEARCH FLIGHTS']