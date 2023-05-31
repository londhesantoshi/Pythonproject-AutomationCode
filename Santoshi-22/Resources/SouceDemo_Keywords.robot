*** Settings ***
Documentation    This Resource file contains implementaion of SouceDemo TC's
Library          SeleniumLibrary
Resource         ../Configuration/${ENV}_Env.robot

*** Keywords ***
I Navigate to saucedemo.com
        open browser        ${SouceDemo_URL}      ${BROWSER}
        maximize browser window
        capture page screenshot

I Enter all login details & Login to SouceDemo
        input text  id:user-name    standard_user
        input text  id:password     secret_sauce
        click element   id=login-button

I Add first product to cart
        click element   id:add-to-cart-sauce-labs-backpack
        click element   //div[@id='shopping_cart_container']/a
        click element   id:checkout

I Fill all checkout details
        input text      id:first-name      Santoshi
        input text      id:last-name       Londhe
        input text      id:postal-code     413503
        click element   id:continue
        click element   id:finish
        capture page screenshot

I Logout from SouceDemo
        click element   id:react-burger-menu-btn
        sleep           5s
        click element   //a[text()='Logout']
        close browser