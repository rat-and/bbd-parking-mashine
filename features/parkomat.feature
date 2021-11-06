Feature: Parkomat

  @park
  Scenario: parking time less or equal 15 mins
    When parking time = 10 min
    Then parking cost = 1.70 PLN

  @park
  Scenario: parking time more than 15min less or equal 1h
    When parking time = 50 min
    Then parking cost = 7.00 PLN

  @park
  Scenario: parking time more than 1h less or equal 2h
    When parking time = 1:25 hours:mins
    Then parking cost = 14.40 PLN

  @park
  Scenario: parking time more than 2h less or equal 3h
    When parking time = 2:15 hours:mins
    Then parking cost = 22.30 PLN

  @park
  Scenario: parking time more than 3h
    When parking time = 3:40 hours:mins
    Then parking cost = 29.30 PLN

  @park
  Scenario: parking time is 12 h
    When parking time = 12 hours
    Then parking cost = 92.3 PLN