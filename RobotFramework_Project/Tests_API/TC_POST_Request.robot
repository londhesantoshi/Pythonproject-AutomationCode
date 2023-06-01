*** Settings ***
Documentation    Suite description
Library      SeleniumLibrary
Library      RequestsLibrary


*** Test Cases ***
Make Call to to Reqres.in
        Create New data

*** Keywords ***
Create New data
        create session   