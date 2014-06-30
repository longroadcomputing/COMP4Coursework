#Styling Guidance
Creating an appropriately styled document in an important component of the coursework. Styling ensures that your document is easy to read and that it is possible to find the relevant sections of the document quickly and easily.

It is recommended that you create and write your document using the **LaTeX** mark-up language rather than a word processor due to the size and complexity of the document you will be producing.

##LaTeX
It is expected that you write your coursework using **LaTeX**, which is a document preparation and mark-up language.

Using LaTeX will mean that your document will **automatically** have the appropriate styling, including a **table of contents**, title page and page numbers. In addition, all of your diagrams and tables will automatically **respect margins** and it will be easier to manage **cross-references** and **program listings**.

Finally, because LaTeX is just text, it can be **version controlled** using Git, just like any other source code you produce.

###Getting LaTeX
You can download and install LaTeX for free:

- [OS X][7]
- [Windows][8]

Once installed you can use the provided editor or a text editor of your choice to write your LaTeX documents.

###Templates
Templates are provided for the main coursework document and each section. These templates include all of the headers necessary for each section.

###Diagrams
Because LaTeX is a mark-up language it does not natively support the creating of diagrams or manipulation of images. You should create diagrams using a tool such as [Libre Draw][6] and use the **export to PDF** option to create files that you can include in your LaTeX document.


##Word Processors
It is **strongly recommended** that you use LaTeX but if you decide not to you will most likely use Microsoft Word to write your coursework as this is the word processor available in the college.

You will need to ensure that you have a copy of Microsoft Word on your home computer as well. There are options available to get Microsoft Office (including Word) for free or at a reduced rate - please speak to your teacher to find out more.

Using Microsoft Word in college and another word processor at home is problematic due to the formatting differences that are often introduced and therefore it is **not recommended**.

###Setting up your word processing document
Writing a long piece of coursework is very different from the short reports that you will have written in the past. You need to ensure that your document is structured properly to cope with the demands of the course. A normal piece of coursework can be anything from about 200 to 500 pages. This includes text, diagrams and code listings and unless you structure your document appropriately you will find that a word processor will struggle to cope with this length of document.

####Master document
In order for the word processor to cope you will first need to create a **master document** for the coursework. You can follow instructions to do this on the [Microsoft website][1].

####Styles
You should use [styles][2] for headings and sub-headings in your document. If you add all of the headings in outline view (whilst creating the master document) this will be done for you.

The benefit of using styles over formatting sections of text individually is that you can easily change the formatting of the document - just like using CSS to style a HTML page.

You should ensure that your **headings** have the following formatting:

- **Page title**: sans-serif font, black, 16 pt.
- **Section heading**: sans-serif font, black, 14 pt.
- **Sub-section heading**: sans-serif font, black, 12 pt.
- **Sub-sub-section heading**: sans-serif font, black, 10 pt.

In addition, ensure that your **paragraphs** have the following formatting:

- **Text**: serif font, black, 10 pt.
- **Paragraph separation**: you should separate paragraphs will a blank line, **not** indentation like you would when writing by hand.
- **Paragraph spacing**: should also be set to 0 pt before and after.

Finally, **program code** should have the following formatting:

- **Code**: mono-spaced font, black, 10 pt.
- **Lines**: lines should be numbered sequentially
- **Modules**: modules should be separated with an appropriate heading. Line numbering should restart for a new module.

####Header
Each page of your document should have a header with the following information:

- Candidate name.
- Candidate number.
- Center number (22151).

####Footer
Each page of your document should have a footer containing a **page number** aligned to the **right** of the page.

###Table of contents
Your document should have a [table of contents][5].

###Tracking changes
You should turn on the option to [track changes][3] in the word processing document so that you can shown when particular changes were made in your document.

###Version Control and Back-up
Using a service such as [Dropbox][4] to manage your files will provide you with an **off-site** back-up and up to 30 days worth of versions of your document.

[1]: http://office.microsoft.com/en-gb/word-help/create-a-master-document-and-subdocuments-HP005187002.aspx
[2]: http://office.microsoft.com/en-gb/word-help/style-basics-in-word-HA010230882.aspx
[3]: http://office.microsoft.com/en-us/word-help/track-changes-while-you-edit-HA001218690.aspx
[4]: http://www.dropbox.com
[5]: http://office.microsoft.com/en-gb/word-help/create-a-table-of-contents-or-update-a-table-of-contents-HP001225372.aspx
[6]: http://www.libreoffice.org/discover/draw/
[7]: http://www.tug.org/mactex/
[8]: http://miktex.org







