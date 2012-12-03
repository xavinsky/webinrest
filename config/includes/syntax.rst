#####
Parts
#####

********
Chapters
********

Sections
========

Subsections
-----------

Separation Line :

----------


*****
Texts
*****


*italics words*
**bolds words** 
``monospaced text words``

Escape  \*not italic\*.  
Escape Backslash \\
``no escape \* with monospaced text``

text base

    text indent

the text continue
in the same ligne

Term
    Term description.

:Term2:
    Term2 description.


Insert code :

>>> print 'pseudo interractive'
pseudo interractive 


::

    This is a code source.
    This is a code source.
    no escape \* with bloc ::


*****
LIENS
*****

http://lien1

`text2 <http://lien2>`_

`text3`_
 
.. _text3 : <http://lien3>

Footnotes [1]_

.. [1] Footnote text.

.. _ref-internal:

`Name Internal <#ref-internal>`_  or `ref-internal`_

Replacement text : |text4| & |text4|_

.. |text4| replace:: newtext4
.. _text4 : lien4


*****
Lists
*****
* elem 1 

    * elem 1.1
    * elem 1.2

* elem 2
* elem 3

1. elem 1

    1. elem 1.1
    2. elem 1.2

2. elem 2

   #. elem 2.1
   #. elem 2.2


******
Tables
******
Simple table

=====  =======  =======
Id     Type     Value
=====  =======  =======
i      int      2
a      str      toto
l      list     [1, 2]
=====  =======  =======

Complex Grid

+--------------+------------+----------+----------+
| Header 1     | Header 2   | Header 3 | Header 4 |
+--------------+------------+----------+----------+
| span header is possible   |          |          |
+==============+============+==========+==========+
| *italic*     |            span columns.         |
+--------------+------------+---------------------+
| *bold*       | span rows  | code syntax::       |
+--------------+            |                     |
| simple cell  |            |     code datas      |
|              | - elem 1   |     blabla          |
|              | - elem 2   |     truc truc       |
|              |            |                     |
+--------------+------------+---------------------+

