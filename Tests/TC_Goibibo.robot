*** Settings ***
Documentation    This Test file contains all TC's related to Goibibo
Resource         ../Resources/Goibibo_Keywords.robot

*** Test Cases ***
Verify for Search Flights
    Given I Navigate to goibibo.com
    When I Select for trip
    When I Select Date
    Then I Select Class
    And I Click on Search flights button


