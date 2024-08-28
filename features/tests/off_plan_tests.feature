# Created by faris at 8/27/2024
Feature: Tests for Off_plan


  Scenario: User can see titles and pictures on each product inside the off plan page
    Given Open Reelly main page
    And Click Sign In
    And Log in to the page
    When Click on “off plan” at the left side menu
    Then Verify the right page opens
    Then Verify each product on this page contains a title and picture visible

