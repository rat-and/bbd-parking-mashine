# Created by ${USER} at ${DATE}
Feature: Parkomat Cash

User story for this feature:
Parkometr/Parkomat

    15 min:           1,70 zł
    1 godz:           7,00 zł
    Druga godzina:    7,40 zł
    Trzecia godzina:  7,90 zł
    Każda następna:   7,00 zł

pon-pt w godz. 8:00 - 20:00 sob w godz. 8:00 - 18:00
**Weekendy nie są obsługiwane

 @park_cash
  Scenario Outline: Not enough money to buy a ticket
    Given money amount is <money_amount>
    And current time is <current_time>
    When end time is calculated
    Then error message is <result>

    Examples:
      # Not enough money
      |money_amount|current_time       |result            |
      |1.00       |2021-11-08T00:00:00|Not enough money   |
      |1.00       |2021-11-08T08:15:00|Not enough money   |
      |1.00       |2021-11-08T19:45:00|Not enough money   |
      |1.00       |2021-11-08T19:50:00|Not enough money   |
      |1.00       |2021-11-08T23:50:00|Not enough money   |


  @park_cash
  Scenario Outline: Compute end parking timestamp
    Given money amount is <money_amount>
    And current time is <current_time>
    When end time is calculated
    Then result is <result>

    Examples:
      |money_amount|current_time       |result             |
      # Exact amount for 15min
      |1.70       |2021-11-08T00:00:00|2021-11-08T08:15:00|
      |1.70       |2021-11-08T08:15:00|2021-11-08T08:30:00|
      |1.70       |2021-11-08T19:45:00|2021-11-09T08:00:00|
      |1.70       |2021-11-08T19:50:00|2021-11-09T08:05:00|
      |1.70       |2021-11-08T23:50:00|2021-11-09T08:15:00|
      # Amount between 15min and 1h - same result as above
      |5.50       |2021-11-08T00:00:00|2021-11-08T08:15:00|
      |5.50       |2021-11-08T08:15:00|2021-11-08T08:30:00|
      |5.50       |2021-11-08T19:45:00|2021-11-09T08:00:00|
      |5.50       |2021-11-08T19:50:00|2021-11-09T08:05:00|
      |5.50       |2021-11-08T23:50:00|2021-11-09T08:15:00|
      # Exact amount for 1h
      |7.00       |2021-11-08T00:00:00|2021-11-08T09:00:00|
      |7.00       |2021-11-08T08:15:00|2021-11-08T09:15:00|
      |7.00       |2021-11-08T19:45:00|2021-11-09T08:45:00|
      |7.00       |2021-11-08T19:50:00|2021-11-09T08:50:00|
      |7.00       |2021-11-08T23:50:00|2021-11-09T09:00:00|
      # Amount between 1h and 2h - same result as above
      |14.00      |2021-11-08T00:00:00|2021-11-08T09:00:00|
      |14.00      |2021-11-08T08:15:00|2021-11-08T09:15:00|
      |14.00      |2021-11-08T19:45:00|2021-11-09T08:45:00|
      |14.00      |2021-11-08T19:50:00|2021-11-09T08:50:00|
      |14.00      |2021-11-08T23:50:00|2021-11-09T09:00:00|
      # Exact amount for 2h
      |14.40      |2021-11-08T00:00:00|2021-11-08T10:00:00|
      |14.40      |2021-11-08T08:15:00|2021-11-08T10:15:00|
      |14.40      |2021-11-08T19:45:00|2021-11-09T09:45:00|
      |14.40      |2021-11-08T19:50:00|2021-11-09T09:50:00|
      |14.40      |2021-11-08T23:50:00|2021-11-09T10:00:00|
      # Amount between 2h and 3h - same result as above
      |20.00      |2021-11-08T00:00:00|2021-11-08T10:00:00|
      |20.00      |2021-11-08T08:15:00|2021-11-08T10:15:00|
      |20.00      |2021-11-08T19:45:00|2021-11-09T09:45:00|
      |20.00      |2021-11-08T19:50:00|2021-11-09T09:50:00|
      |20.00      |2021-11-08T23:50:00|2021-11-09T10:00:00|
      # Exact amount for 3h
      |22.30      |2021-11-08T00:00:00|2021-11-08T11:00:00|
      |22.30      |2021-11-08T08:15:00|2021-11-08T11:15:00|
      |22.30      |2021-11-08T19:45:00|2021-11-09T10:45:00|
      |22.30      |2021-11-08T19:50:00|2021-11-09T10:50:00|
      |22.30      |2021-11-08T23:50:00|2021-11-09T11:00:00|
      # Amount between 3h and 4h - same result as above
      |26.66      |2021-11-08T00:00:00|2021-11-08T11:00:00|
      |26.66      |2021-11-08T08:15:00|2021-11-08T11:15:00|
      |26.66      |2021-11-08T19:45:00|2021-11-09T10:45:00|
      |26.66      |2021-11-08T19:50:00|2021-11-09T10:50:00|
      |26.66      |2021-11-08T23:50:00|2021-11-09T11:00:00|
      # Exact amount for 4h
      |29.30      |2021-11-08T00:00:00|2021-11-08T12:00:00|
      |29.30      |2021-11-08T08:15:00|2021-11-08T12:15:00|
      |29.30      |2021-11-08T19:45:00|2021-11-09T11:45:00|
      |29.30      |2021-11-08T19:50:00|2021-11-09T11:50:00|
      |29.30      |2021-11-08T23:50:00|2021-11-09T12:00:00|
      # Amount between 6h and 7h
      |45.00      |2021-11-08T00:00:00|2021-11-08T14:00:00|
      |45.00      |2021-11-08T08:15:00|2021-11-08T14:15:00|
      |45.00      |2021-11-08T19:45:00|2021-11-09T13:45:00|
      |45.00      |2021-11-08T19:50:00|2021-11-09T13:50:00|
      |45.00      |2021-11-08T23:50:00|2021-11-09T14:00:00|
      # Exact amount for 12h
      |92.30      |2021-11-08T00:00:00|2021-11-09T08:00:00|
      |92.30      |2021-11-08T08:15:00|2021-11-09T08:15:00|
      |92.30      |2021-11-08T19:45:00|2021-11-09T19:45:00|
      |92.30      |2021-11-08T19:50:00|2021-11-09T19:50:00|
      |92.30      |2021-11-08T23:50:00|2021-11-10T08:00:00|
      # Exact amount for 15h
      |114.30     |2021-11-08T00:00:00|2021-11-09T11:00:00|
      |114.30     |2021-11-08T08:15:00|2021-11-09T11:15:00|
      |114.30     |2021-11-08T19:45:00|2021-11-10T10:45:00|
      |114.30     |2021-11-08T19:50:00|2021-11-10T10:50:00|
      |114.30     |2021-11-08T23:50:00|2021-11-10T11:00:00|