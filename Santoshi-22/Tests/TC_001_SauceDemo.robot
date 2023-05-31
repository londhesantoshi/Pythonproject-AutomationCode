*** Settings ***
Documentation    This Test file contains all TC's related to SouceDemo website
Resource         ../Resources/SD_Keywords.robot

*** Test Cases ***
Verify for User Login to SauceDemo website
    Given User navigate to SauceDemo Website
    When User enter valid username
    Then user enter valid password
    And user click on login button

Verify for User sort the product by price low to high
    Given User navigate to SauceDemo Website
    When User enter valid username
    Then user enter valid password
    Then user click on login button
    And user click on product sort container dropdown
	And user select category price low to high

Verify for User add first product to cart & place order
    Given User navigate to SauceDemo Website
    When User enter valid username
    When user enter valid password
    Then user click on login button
    And user click on product sort container dropdown
	And user select category price low to high
    Then user click on first product
	And user click on add to cart button
	And user clcik on Shopping cart container menu
	And user click on checkout button
	And user fill all information
	And user click on continue button
	And user click on finish button

Verify for User Logout from SauceDemo website
    Given User navigate to SauceDemo Website
    When User enter valid username
    When user enter valid password
    Then user click on login button
    And user click on react burger menu button
	And click on logout link