*** Settings ***
Library         SeleniumLibrary
Resource        PageObject/Amazon_HomePage.robot
Resource        ../Configuration/${ENV}_Env.robot

*** Keywords ***
I Navigate to Amazon website
        open browser    ${Amazon_URL}       ${BROWSER}
        maximize browser window
        capture page screenshot

I Toggle category from dropdown
        ${Category_list}      get webelements     ${dd_Category}

        FOR   ${Category}   IN  @{Category_list}
            ${CategoryValue}    get text    ${Category}
            log    ${CategoryValue}
        END