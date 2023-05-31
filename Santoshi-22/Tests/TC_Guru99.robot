*** Settings ***
Documentation    Suite description
Resource        ../Resources/Guru99_Keywords.robot

*** Variables ***
${UserID}       mngr504610

*** Test Cases ***
Verify for User Login to Guru99 website
#    Given User Navigate to Guru99.com
#    When User Enter all login Details       ${UserID}
#    Then User Click on submit button
    Make a call to Reqres.in