*** Settings ***
Documentation    This test file contains TC's related to Customer Creation website
Resource         ../Resources/CustomerCreation_Keywords.robot

*** Test Cases ***
Verify for User Create a Lead
   Given I Navigate to Microsoftonline.com
   When I Enter all Login Details           ${EmailID}     pcubeworkforce@gmail.com
   Then I click on submit button
   Then I click on Dynamics 365-custom app
   Then I click on new & select Lead
   And I Enter all lead details & click on save & close
   And I click on View Record & click on save & close


