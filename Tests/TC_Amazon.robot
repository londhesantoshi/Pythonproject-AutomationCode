*** Settings ***
Documentation    This Tests file contains TC's related to Amazon
Resource         ../Resources/Amazon_Keywords.robot

*** Test Cases ***
User Verify for dropdown category selection is working fine
        Given I Navigate to Amazon website
        When I Toggle category from dropdown
#        Then I Verify category is selected