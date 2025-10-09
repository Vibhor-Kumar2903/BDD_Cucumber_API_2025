Feature:  Login into swag labs
  As a valid user
  I want to be able to log in to the SauceDemo web application
  So that I can access the product dashboard
  ** With Inputs **

  Scenario Outline: Data Driven Scenario of Login
    Given   Go to login page
    When    Enter the username <username> and password <password> in textbox
    And     Click on login button
    Then    Verify the dashboard


  Examples:
    |         username      |  password  |
    |standard_user          |secret_sauce|
    |locked_out_user        |secret_sauce|
    |problem_user           |secret_sauce|
    |performance_glitch_user|secret_sauce|
    |       invalid         |   invalid  |




