#System Maintenance
There are **7 marks** available for this section.

##Introduction
In this section you must produce documentation that will enable another programmer to maintain your system.

To do this you will need to include:

- A brief discussion of the environment used to solve the problem, its capabilities and special features and a clear description of the features you have used
- A system overview
- An explanation of the modular structure of all the code
- Annotated variable lists with reference to the data dictionary in the design section
- Screenshots of all tables, forms, queries, relationships windows in design view
- A discussion of test results with reference to the testing section
- Explanation of any parts of the code that are difficult to understand plus samples of detailed algorithms developed by you
- Reference to the program listing (in implementation section)
- A list of system settings and the system configuration
- Acknowledgement of any automatically generated code or code incorporated from other sources

##The Environment
In this section you must describe which software you have used to create your system, why you have used this software and highlight the features of that software you have used.

Clearly, you may have used additional software but most of you will have used the following:

- Python 3
- IDLE (to write Python scripts)
- PyQt (to produce user interface elements)
- SQLite 3 (for databases)
- Apache (web server - server-side projects only)
- MySQL (for databases - server-side projects only)
- Any other modules

###Usage
In addition to listing the software used you must provide some justification for using the particular packages. It is okay to state that the reason a particular package was used is that it is the only one of that type you are familiar with but try and give **detailed explanations** where possible.

###Features Used
You also need to discuss the features used in each package. For instance the ability to **import modules** in Python, **syntax highlighting** in IDLE, ability to debug/execute SQL in SQLite Inspector.

##System Overview
Because the programmer would not necessarily see the rest the documentation you have produced for the project you must provide them with a **clear overview** of the main functionality of the system.

You should be able to take material from previous sections and adapt it for here. Be sure to use **appropriate technical language**.

##Code Structure
Once you have an appropriate code listing you can then explain the the code structure. Topics you could discuss include:

- Why did you make a particular section of code a function?
- Why are parameters passed in a particular way?
- (If relevant) why have is a particular section of code an object and why do the methods go with it?

###Code Snippets [CodeSnippets]
It is important in this section to quote snippets of code from your listing so that it is possible to explain the structure properly. When quoting code be sure to add **cross-referencing** so that the marker can easier find the snippet of code in the full listing.

##Variable List
The Data Dictionary from the Design section will form the basis of this list. However, you are referring only to variable in the code here - not data from the database. Be sure to include a reference back to the **data dictionary** as well.

You will then need to make sure that any additional variables creating during the implementation phase are included in the revised table.

Finally, you may need to indicate on the table the purpose of the variable if it is not immediately obvious and also where the variable is referenced in the code (this is somewhat time consuming).

##System Evidence
This section is basically an overview of both the user interface of the system and the database behind it (if used). You should include:

- Screenshots of all user interfaces in your system
- You have already taken these for the implementation section. You should amend your coursework document so that these screenshot become part of the system maintenance section
- An ER diagram of your finished database
- Screenshots of each entities in your database in table view
- The SQL code required to create the entities
- SQL for all queries of the database

For each component here you should include **appropriate headings** and **commentary** where necessary.

###SQL Queries
It is especially important to ensure that you explain complex SQL statements so that you can show your understanding to the marker.

##Testing
Here you should provide a **summary** of your test results and comment on what you discovered from the process.

It is key that you **clearly highlight** any problems you discovered during testing and provide suggestions as to how they could be fixed (if known).

Finally, you should **reference** the main testing section so that the programmer can look at your testing plan etc. if required.

###Known Issues
In addition to summarising the testing you should discuss how you could resolve known issues (or state that your are unsure).

##Code Explanation
Again, you must refer to your code listing.

Ask yourself the following questions:

- Are there any sections of your code that are particularly difficult to understand?
- Do you have any self-created algorithms?

For each section of code you identify you should:

- Annotate item
- Provide a detailed explanation of its operation
- Present this explanation in an easy to read format

###Code Snippets
Again you will need to make use of code snippets in the section - refer to [previous guidance][CodeSnippets] given above.

##Settings
Here you will need to highlight any particular settings that need to be altered in the software you are using to enable the functionality of your system. Examples might include:

- Particular modules that need to be available in Python for your system to function
- Server settings to allow for CGI scripting on a web server
- Creating user accounts with particular privileges for the SQLite/MySQL database

##Acknowledgements
This section should highlight any code or APIs you have used from additional sources. Think of it like a **bibliography**. You should state clearly and highlight any code that is not yours and explain why you used it and where it can be found on the Internet.

##Code Listing
Here you should include all of your program code. The listing should be separated by module and each listing should include line numbers.

##Mark Scheme

|0-1 marks|2-3 marks|4-5 marks|6-7 marks|
|-|-|-|-|
|Complete code listings which are not self-documenting or fully annotated|Self-documenting code listings or fully annotated code listings|Self-documenting code listings or fully annotated code listings|Candidate-written code/scripts listing that is self-documenting and/or well annotated, easy to follow (very easy to comprehend).
| | |Some technical aspects described|Explanation of the modular structure of all the code|
| | | |Reference to the design section|
| | | |Reference to testing|
| | | |Explanation of difficult-to-understand parts of code|
| | | |List or description of system settings/configuration|

