# Created by sehij at 12/20/23
Feature: Verification on the Contact Page

  Scenario: Verify user can open the Contact us page
    Given Open the Sign In page
    Then Log in to the Sign In page
    And Click on settings option
    And Click on Contact us option
    And Verify the Contact us page opens