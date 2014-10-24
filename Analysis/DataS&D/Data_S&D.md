|Source|Data|Data Type|Destination|
|:----:|:--:|:-------:|:---------:|
|Josh|ItemID|Integer|Database - Item Records
|Josh|ItemName|String|Database - Item Records|
|Josh|ItemType|String|Database - Item Records|
|Josh|Value|Real|Database - Item Records|
|Josh|Quantity|Integer|Database - Item Records|
|Josh|SubTotal|Real|Database - Item Records|
|Josh|OnLoan|Text|Database - Item Records|
|Josh|LoanID|Integer|Database - Loan Records|
|Database - Item Records|ItemID|Integer|Database - Loan Records|
|Database - Item Records|ItemName|Text|Database - Loan Records|
|Josh|LoanRate|Real|Database - Loan Records|
|Josh|LoanStart Date|Date|Database - Loan Records|
|Josh|LoanEnd Date|Date|Database - Loan Records|
|Josh|LoanTime|Time|Database - Loan Records|
|Josh|LoanCost|Real|Database - Loan Records|
|Josh|TestID|Integer|Database - PAT test records|
|Database - Item Records|ItemID|Integer|Database - PAT test Records|
|Database - Item Records|ItemName|Text|Database - PAT test Records|
|Database - Item Records|LastTest|Date|Next PAT test Calculation, Database PAT test Records|
|Next PAT Test Calculation|NextTest|Date|Database - PAT test Records|
|Josh|TestResult|Text|Database - PAT test Records|