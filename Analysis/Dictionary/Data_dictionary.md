|Name|Data Type|Length|Validation|Example Data|Comment|
|:--:|:-------:|:----:|:--------:|:----------:|:-----:|
|ItemID|Integer|1-435|Range|184|-|
|ItemName|Text|5 - 40 Characters|Length|Mac Pro|-|
|Value|Real|2-5 figures|Range|1,300|-|
|Quantity|Integer|1-150|Range|8|-|
|Total Value|Real|2-8 figures|Range|133,204.86||
|OnLoan|Boolean|-|Status Check|True|If an item is on loan or not|
|LoanRate|Real|1-3 figures|Range|75||
|LoanStartDate|Date|-|Format|25/09/2014||
|LoanEndDate|Date|-|Format|27/09/2014||
|LoanTime|Integer|-|Date Range|7 Days||
|LoanCost|Real|1-4 Integers|Range|250||
|LastTest|Date|-|Format|01/10/2014||
|NextTest|Date|-|Format|20/10/2014|Calculated 12 months from LastTest date|