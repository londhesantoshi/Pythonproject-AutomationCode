*** Settings ***
Documentation    Suite description
Library         SeleniumLibrary
Library         RequestsLibrary
Library         Collections

*** Keywords ***
Get_page2info
    create session      mysession   https://reqres.in/
    ${response}     get on session     mysession  url=api/users?page=2
#    log to console  ${response.status_code}
#    log to console  ${response.content}
#    log to console  ${response.headers}

#    Validations
        ${status_code}=   convert to string    ${response.status_code}
        should be equal     ${status_code}     200

       ${contentTypeValue}=     get from dictionary   ${response.headers}   Content-Type
       should be equal    ${contentTypeValue}    application/json; charset=utf-8


