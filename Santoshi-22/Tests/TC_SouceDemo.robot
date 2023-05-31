*** Settings ***
Documentation       This Test file contains all TC's related to SouceDemo
Resource            ../Resources/SouceDemo_Keywords.robot

*** Test Cases ***
Login to the SouceDemo website
    Given I Navigate to saucedemo.com
    When I Enter all login details & Login to SouceDemo
    Then I Add first product to cart
    And I Fill all checkout details
    And I Logout from SouceDemo
