###################
ReStructured Syntax
###################

This is only some ReST syntax tested with Rest2Web. 
You can see `official specification <http://docutils.sourceforge.net/rst.html>`_ or
`syntax Documenting python <http://docs.python.org/devguide/documenting.html>`_ for others usages.

.. _ref-summary:

*******
Summary
*******

* `Document Structure <#ref-structure>`_
* `Text formating <#ref-text>`_
* `Media <#ref-media>`_
* `Code Source <#ref-code>`_
* `Links <#ref-links>`_
* `Lists <#ref-lists>`_
* `Tables <#ref-tables>`_

.. _ref-structure:

******************
Document Structure
******************
[back to `Summary <#ref-summary>`_]

Syntax::

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


.. _ref-text:

**************
Text formating
**************
[back to `Summary <#ref-summary>`_]

+-------------------------------------------------+----------------------------------------------+
| Syntax                                          | Visual                                       |
+=================================================+==============================================+
| ::                                              |                                              |
|                                                 |                                              |
|    *italics words* **bolds words**              | *italics words* **bolds words**              |
|    & ``monospaced text words``                  | & ``monospaced text words``                  |
|                                                 |                                              |
|    Escape with backslashes \*not italic\*.      | Escape with backslashes \*not italic\*.      |
|    Backslash is possible: \\                    | Backslash is possible: \\                    |
|                                                 |                                              |
|    ``no escape \* with monospaced text``        | ``no escape \* with monospaced text``        |
|                                                 |                                              |
|    text base                                    | text base                                    |
|                                                 |                                              |
|        text indentation 1                       |     text indentation 1                       |
|                                                 |                                              |
|            text indentation 2                   |         text indentation 2                   |
|                                                 |                                              |
|    text base                                    | text base                                    |
|                                                 |                                              |
|            text indentation 2                   |         text indentation 2                   |
|                                                 |                                              |
|        text indentation 1                       |     text indentation 1                       |
|                                                 |                                              |
|    Text 1                                       | Text 1                                       |
|    Text 2                                       | Text 2                                       |
|                                                 |                                              |
|    Text 3                                       | Text 3                                       |
|    Text 4                                       | Text 4                                       |
|                                                 |                                              |
|    Term                                         | Term                                         |
|        Term description.                        |     Term description.                        |
|        The description continue.                |     The description continue.                |
|                                                 |                                              |
|    :Term2: Term2 description.                   | :Term2: Term2 description.                   |
|            The description continue.            |         The description continue.            |
+-------------------------------------------------+----------------------------------------------+

.. _ref-media:

*****
Media
*****

+--------------------------------------------------+------------------------------------------------+
| Syntax                                           | Visual                                         |
+==================================================+================================================+
| image::                                          |                                                |
|                                                  |                                                |
|   .. image:: /includes/images/by-sa.png          | .. image:: /includes/images/by-sa.png          |
|                                                  |                                                |
| image in a line ::                               |                                                |
|                                                  |                                                |
|   before |image1| after                          | before |image1| after                          |
|                                                  |                                                |
|   .. |image1| image:: /includes/images/by-sa.png | .. |image1| image:: /includes/images/by-sa.png |
|                                                  |                                                |
+--------------------------------------------------+------------------------------------------------+

.. _ref-code:

***********
Code Source
***********
[back to `Summary <#ref-summary>`_]

+-------------------------------------------------+----------------------------------------------+
| Syntax                                          | Visual                                       |
+=================================================+==============================================+
| ::                                              |                                              |
|                                                 |                                              |
|    >>> print 'pseudo interractive'              | >>> print 'pseudo interractive'              |
|    pseudo interractive                          | pseudo interractive                          |
|                                                 |                                              |
|    ::                                           | ::                                           |
|                                                 |                                              |
|        This is a code source.                   |     This is a code source.                   |
|        No escape with \ here.                   |     No escape with \ here.                   |
|        No interpretation <html> here.           |     No interpretation <html> here.           |
|        No links : http://www.google.com         |     No links : http://www.google.com         |
+-------------------------------------------------+----------------------------------------------+

.. _ref-links:

*****
Links
*****
[back to `Summary <#ref-summary>`_]

+-------------------------------------------------+----------------------------------------------+
| Syntax                                          | Visual                                       |
+=================================================+==============================================+
| ::                                              |                                              |
|                                                 |                                              |
|    http://docutils.sourceforge.net/rst.html     | http://docutils.sourceforge.net/rst.html     |
|                                                 |                                              |
|    `RST site <http://goo.gl/YQYjq>`_            | `RST site <http://goo.gl/YQYjq>`_            |
|                                                 |                                              |
|    `RST site2`_                                 | `RST site2`_                                 |
|                                                 |                                              |
|     .. _RST site2 : <http://goo.gl/YQYjq>       |  .. _RST site2 : <http://goo.gl/YQYjq>       |
|                                                 |                                              |
|    Footnotes [1]_                               | Footnotes [1]_                               |
|                                                 |                                              |
|    .. [1] Footnote text.                        | .. [1] Footnote text.                        |
|                                                 |                                              |
|    .. _ref-internal:                            | .. _ref-internal:                            |
|                                                 |                                              |
|    Invisible Ref internal                       | Invisible Ref internal                       |
|                                                 |                                              |
|    Link the internal reference :                | Link the internal reference :                |
|    `LinkName <#ref-internal>`_                  | `LinkName <#ref-internal>`_                  |
|     or `ref-internal`_                          | or `ref-internal`_                           |
|                                                 |                                              |
|    Replacement text : |RST|  |RST|_ .           | Replacement text : |RST|  |RST|_ .           |
|                                                 |                                              |
|    .. |RST| replace:: reStructuredText          | .. |RST| replace:: reStructuredText          |
|    .. _RST: http://goo.gl/YQYjq                 | .. _RST: http://goo.gl/YQYjq                 |
+-------------------------------------------------+----------------------------------------------+


.. _ref-lists:

*****
Lists
*****
[back to `Summary <#ref-summary>`_]


+-------------------------------------------------+----------------------------------------------+
| Syntax                                          | Visual                                       |
+=================================================+==============================================+
| ::                                              |                                              |
|                                                 |                                              |
|    * elem 1                                     | * elem 1                                     |
|      second line elem 1                         |   second line elem 1                         |
|    * elem 2                                     | * elem 2                                     |
|                                                 |                                              |
|      * elem 2.1                                 |      * elem 2.1                              |
|                                                 |                                              |
|    1. elem 1                                    |  1. elem 1                                   |
|                                                 |                                              |
|      a. elem 1.1                                |      a. elem 1.1                             |
|      b. elem 1.2                                |      b. elem 1.2                             |
|                                                 |                                              |
|    2. elem 2                                    |  2. elem 2                                   |
|                                                 |                                              |
|      #. elem 2.1                                |      #. elem 2.1                             |
|      #. elem 2.2                                |      #. elem 2.2                             |
+-------------------------------------------------+----------------------------------------------+

.. _ref-tables:

******
Tables
******
[back to `Summary <#ref-summary>`_]

Syntax::

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

----------

visual result :

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

.. _ref-end:

###
End
###
[back to `Summary <#ref-summary>`_]
