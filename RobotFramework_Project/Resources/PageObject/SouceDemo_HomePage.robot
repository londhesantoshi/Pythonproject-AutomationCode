*** Settings ***
Documentation    This file contains Addresses of webelement of home page of Saucedemo used in SD keyword file

*** Variables ***
${UsernameID}               user-name
${PasswordID}               password
${SubmitBtnID}              login-button
${Product_Sort_DropDown}    //select[@class='product_sort_container']
${Price_LowToHigh_Cat}      //select[@class='product_sort_container']/option[text()='Price (low to high)']
${Pro_Sauce_Labs_Onesie}    //div[text()='Sauce Labs Onesie']
${AddTo_Cart_Btn}           //button[text()='Add to cart']
${Shopping_Cart_Menu_Btn}   //div[@id='shopping_cart_container']/a
${Checkout_BtnID}           checkout
${FirstNameID}              first-name
${LastNameID}               last-name
${PostCodeID}               postal-code
${ContinueBtn_ID}           continue
${FinishBtn_ID}             finish
${React_burger_Menu_BtnID}  react-burger-menu-btn
${Logout_Link}              //a[text()='Logout']