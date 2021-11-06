Feature: Least Recently Used list

  Scenario: a new list is empty
    When a new list is created
    Then the list is empty

  Scenario: add a new file to an empty list
    Given an empty list exists
    When we open a new file
    Then the list has one element
    And the new file is first

  Scenario: add a new file to not empty list
    Given not empty list exists
    When new file is opened
    Then the new file is first
    And the rest of elements go to next positions

  Scenario: a list contain at most 5 elements
    Given a list with 5 elements exists
    When new file is opened
    Then the new file is first
    And the rest of elements go to next positions
    And the oldest one is deleted from the list

  Scenario: the list does not contain duplicates
    Given a list with three elements
    When we open the second file from the list again
    Then the file is moved to the first place on the list
