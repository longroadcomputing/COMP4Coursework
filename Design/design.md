#Design
There are **12 marks** available for this section.

##Introduction
During the Analysis section you gained an understanding of what is going to be involved in solving the problems presented by the project and from this you developed a list of objectives.

The Design phase deals with translating these objectives into a **physical model** of the system.

##Overall System Design
This section focuses on enabling the reader to understand the system. You need to write a clear and concise description that visualises each system function.

###Short description of the main parts of the system
In this section it is important to think about the different areas of your system and then describe each of those areas in reasonable detail. The reader should be able to understand all of the functionality of your system from this description.

It should summarise each aspect of the system's functionality and this section may be anything up to **roughly a page** in length.

For example, if your system were a **booking system for a bed and breakfast** you might start by identifying what the areas of the system as a series of bullets:

- Bed and Breakfast Booking System
    - General User Interface
    - Getting Customer Booking Details
    - Managing Bookings
    - Reporting Information

You might then take each of these areas as a **sub-heading** and describe the functionality contained within the area:

- Getting Customer Booking Details
    - The system will ask for basic details about the booking, such as: what night they plan to arrive, how many nights they plan to stay for, what type of room they wish to have
    - If the booking is possible the system will then ask for customer details, postcode and house number. If the customer has stayed previously the rest of the details will be found automatically and then the customer asked to confirm them, otherwise further customer information will be requested
    - Finally, additional details such as dietary requirements will be asked for and then there will be an opportunity to review the booking details before it is confirmed
    - Once confirmed, the customer can be provided with the booking reference number which can be used to amend or cancel the booking in futur

###System flowcharts showing an overview of the complete system
A system flowchart allows you to represent the functionality of the system in a way that is easily understood. You will need to create a chart which represents all of the functionality of your system. The symbols that you should use in your flowchart are:

![][1]

Much like Data Flow Diagrams, creating a reasonable System Flowchart will take some practice. It is easy for them to become unwieldy and end up spread across many pages in a Word document. Let's look at an example:

![][2]

In the above example a flowchart has been constructed which fully explains the process of creating a booking but the sections for managing a booking and system reporting are unfinished. How can we complete these sections when there is clearly not much more room available?

Instead of trying to make the elements smaller or trying to place them closer together we will do the following:

![][3]

Notice, that instead of continuing the flowchart we have just referenced the page on which you can see the rest of that particular section of the chart. If you were to look at page 4 you would see the following:

![][4]

This enables you to both complete the rest of the diagram on a new page and also see where the rest of the diagram can be located.

####Creating Flow charts
System flowcharts are difficult to do well using the tools available in Word. You will need to use a [**specialist diagramming**][11] application to do this section justice.

You should also consider:

- Separate out the different aspects of your system on different pages if required rather than trying to squeeze everything into one page
- Make sure you provide sub-headings for each flowchart and give some explanation of what it is supposed to be representing

The example flowchart in the A2 textbook is not very good as it does not use all of the symbols available. Be sure to investigate this further on the Internet – especially the decision symbol.

Keep in mind that a process symbol is for processing and not for stating that a particular UI screen is displayed on the monitor.

##User Interface Designs
Here you are providing diagrams which **visualise** the interface and show the **flow of control** i.e. what happens when one interface component is selected.

Designing a good interface is difficult, even for professional software developers. The success of an interface depends on many factors which need to be considered together. There is a good list of these factors in the **A2 Textbook on page 250**.

It is important to consider each one of these factors seriously as by doing so you will be able to come to a conclusion about what is most suitable for your **client** and/or **audience**. For example, imagine you were producing an interface for a touch-screen device. Which of the screenshots below would be most suitable? Why?

![][5]

![][6]

###Designing your Interface
You must create sketches for each interface screen and **annotate** these sketches to **explain your decisions** and also to show **flow of control**. The example below shows this.

![][7]

###Considerations
Be sure to provided **headings** and **figure numbers** for each interface so that the can be **cross-referenced** later. In addition, be sure to annotate the designs to explain or highlight particular features.

##Hardware Specification
This is your opportunity to describe and justify the hardware that is required to enable your design. In the majority of cases the will be the hardware specified by your client as this is the equipment they plan to use to run your solution. However, if a few cases it may be appropriate to select hardware that will need to be purchased by the client to effectively run your system.

You need to **justify** your choices in terms of:

- **cost**
- **suitability for purpose**
- **availability**

You should take each hardware component and justify it individually.

##Program Structure
In this section you are breaking the problem down so that it can be more easily solved and then developing the algorithms and structures necessary to solve these problems.

###Topdown design structure charts
Here you must take your problem and break it down into its component parts. You start be developing a **Hierarchy Chart** for the problem. For example:

![][8]

Once you have created the hierarchy chart you need to add interfaces and control information to turn it into a structure chart. For example:

![][9]

###Algorithms in pseudo-code for each data transformation process
Most students find this the hardest section to complete as it is quite hard to think about all of the algorithms that your system will require **before** you build the system rather than creating them as you are going along. You should make use of the [pseudo-code guide][10] which explains the syntax of pseudo-code.

Here, we are only interested in those algorithms that perform some **data transformation**, not on every single algorithm in the system. You will be able to identify the data transformation algorithms from analysing your structure chart and identifying those sub-problems that **process** data.

For example, in the above structure chart the **search availability** sub-problem takes in the dates and rooms required and outputs whether these rooms are available on these dates.

The search availability algorithm could look as follows:

```python
FUNCTION SearchAvailability (checkDate, checkRooms)
    single ← 0
    double ← 0
    family ← 0
    availability ← FALSE
    Connect(BookingDatabase)
    Bookings ← Search(BookingDatabase,Bookings,CheckDate)
    Rooms ← Search(BookingDatabase,Rooms)
    FOR EACH Room IN Rooms
        CASE Room.Type OF
            "Single": single ← single + 1
            "Double": double ← double + 1
        ELSE
            family ← family + 1
        ENDCASE
    ENDFOR<br/>
    FOR EACH eachBooking IN Bookings
        CASE eachBooking.Room OF
            "Single": single ← single - 1
            "Double": double ← double - 1
        ELSE
            Family ← Family - 1
        ENDCASE
    ENDFOR
    IF checkRooms.single <= single AND checkRooms.double <= Double AND checkRooms.family <= family THEN
        availability  ← TRUE
    ENDIF
    RETURN availability
ENDFUNCTION
```

Make sure you provide algorithms for **all** data processing functions in your system. However, there is no need to include **SQL** in your algorithms - just state that you will get the information from the database. SQL queries are highlighted in a separate section.

##Object diagrams
You have done most of this work already as part of the analysis section. For the most part you should be able to copy and paste the material from there into this section. However, you may need to make alterations if your understanding of the problem has improved.

##Class definitions
You have done most of this work already as part of the analysis section. For the most part you should be able to copy and paste the material from there into this section. However, you may need to make alterations if your understanding of the problem has improved.

##Prototyping
You might find this section difficult as you have little experience of developing large scale solutions to programming problems.

At this stage, there are many areas of your project implementation that you must be unsure about as you may not have the gained the knowledge necessary to have confidence in developing a particular area.

Prototypes can help. Rather than attempting to jump straight into a difficult problem you may decide to solve a smaller scale problem to test out your ideas or to develop your programming knowledge. You can then use the results to inform your decisions on tackling the actual problem.

###Consideration of impact on design and development
In this section you should list the different parts of the implementation you plan to create prototypes for and give reasons as to why you wish to do this. You should explain what you are expecting the prototype to help you find out and also how the results of the prototype will inform the development of the actual system.

For example, you may wish to:

- Prototype the design of a user interface form and get feedback from the client on whether it is appropriate or not.
- Develop an algorithm which enables you to place parameters in a complex SQL query as you are not sure about how to do this

##Definition of Data Requirements
This section is going to be based on your work on the **data source(s) and data destination(s)** section of the Analysis.

###Identification of all data input items
You should list all of you data input items here. If not obvious you could say where these items come from and give a comment/description for more obscurely titled items.

###Identification of all data output items
You should list all of you data output items here. If not obvious you could say where these items come from and give a comment/description for more obscurely titled items.

###Explanation of how data output items are generated
You should explain how data output items are produced and which input items are required to produce them.

It may make sense to complete this entire section in table format.

###Data Dictionary
This is your data dictionary from Analysis updated with any additional data items that have presented themselves at the design phase.

###Identification of appropriate storage media
Describe and explain the kind of secondary storage devices that will be required to store and back-up your data. Be sure to justify your choices.

##Database Design
It is important to spend a good deal of time on this section as without a properly designed database your system will not function as intended.

###Normalisation

####ER Diagrams
Include, with a key, your final normalised ER diagram.

####UNF to 3NF (and Entity Descriptions)
In this section show with annotation how you moved from **UNF** to **3NF**. Ensure that your final **entity descriptions match the ER diagram** in the section above.

###SQL Queries
You will have literally dozens of SQL queries to produce for your implementation. In this section only include those queries that are either **complex** or **complex and parameterised**.

For example, the following type of SQL query is **simple** and **should not** be included:

```sql
SELECT *
FROM Videos
WHERE VideoID = 5
```
This query is also simple:

```sql
SELECT *
FROM Videos
WHERE VideoID = ?
```

This query is complex and parameterised:

```sql
SELECT Video.Title,Genre.Name
FROM Video,Genre
WHERE VideoID = ? AND
Video.VideoID = Genre.VideoID
```

Clearly you will need to annotate and explain where the parameters come from and make clear that you are using Python to format the SQL query text strings.

##Security and Integrity of the System and Data
This section is concerned with explaining how you plan to ensure your system and data are used only by authorised individuals.

###Security and Integrity of Data
Here you will want to discuss any encryption you plan to add to certain data or how you are going to ensure that the data is accurate (may refer to the next section on Validation).

Finally, you will want to discuss how your data needs to be protected in respect to legislation. You may find it possible to copy material from Analysis and amend/improve it based on the changes that have occurred during the design phase.

###System Security
This section deals with the access restrictions you will place on the system and how these relate to legislation.

##Validation
This section will involve references back to the data dictionary where you identified validation techniques to use. Here you will identify each type of check and explain why it is required.

##Testing</h2>
Testing is another important section as producing the plan you will use to actually test your system as you are developing it/once you have finished developing it.

###Outline Plan

####Identification and explanation of suitable test strategies</h4>
This section should be a table which identifies the purpose of each area of testing, the testing strategy and a rationale for using the strategy:

|Test Series|Purpose of test series|Testing Strategy|Strategy Rationale|
|-|-|-|-|
|1|Validation of input data performed corrected|Bottom-up Testing|Each component will be tested as it becomes available|

###Detailed Plan
In this final section you must take the outline plan and identify the tests that will be performed in each area. There is a good example in the textbook on **page 262**.

However, you should use the table format below:
<table>
<tr>
<th>Test Series and number</th>
<th>Purpose</th>
<th>Description</th>
<th>Test Data</th>
<th>Test Data Type (Normal/Erroneous/Extreme)</th>
<th>Expected Result</th>
<th>Actual Result</th>
<th>Evidence in appendix</th>
</tr>
<tr>
<td rowspan="4" class="tcell">2.1</td>
<td rowspan="4" class="tcell">Validate number of seconds input</td>
<td rowspan="4" class="tcell">The input box should accept positive integers and values with once decimal place</td>
<td>15</td>
<td>normal</td>
<td>Accept 15</td>
<td>Accepted</td>
<td>Page 57, Fig.2.1a</td>
</tr>
<tr>
    <td>21.6</td>
    <td>normal</td>
    <td>Accept 21.6</td>
    <td>Accepted</td>
    <td>Page 57, Fig.2.1b</td>
</tr>
<tr>
    <td>3</td>
    <td>erroneous</td>
    <td>Error</td>
    <td>Error</td>
    <td>Page 58, Fig.2.1c</td>
</tr>
<tr>
    <td>'abs'</td>
    <td>erroneous</td>
    <td>Error</td>
    <td>Error</td>
    <td>Page 58, Fig.2.1d</td>
</tr>
</table>

##Mark Scheme
|0-3 marks|4-6 marks|7-9 marks|10-12 marks|
|-|-|-|-|
|not feasible design|less than feasible design|feasible design|effective design|
|poor reporting of criteria for design|detailed reporting of all criteria for design|detailed reporting of all criteria for design|detailed reporting of all criteria for design in the context of the problem being solved|

[1]: images/flowchartsymbols.png
[2]: images/bookingflowchart.png
[3]: images/bookingflowchart2.png
[4]: images/bookingflowchart3.png
[5]: images/desktop.png
[6]: images/metro.jpg
[7]: images/userinterfacesample.png
[8]: images/heirarchychart.png
[9]: images/structurechart.png
[10]: http://filestore.aqa.org.uk/subjects/AQA-GCSE-COMPSCI-W-TRB-PSEU.PDF
[11]: http://www.libreoffice.org/discover/draw/