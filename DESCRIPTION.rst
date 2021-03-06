# tweetprep
-----------

A simple python library for preprocessing tweets to make them training
ready. Use it to preprocess the tweets before feeding them to Machine
Learning or Deep Learning models.

The code is Python 2 and 3 compatible.

# Installation
--------------

Fast install:
-------------

::

        pip install tweetprep

For a manual install get this package:
--------------------------------------

.. code:: bash

        $wget https://github.com/garain/tweetprep/archive/master.zip
        $unzip master.zip
        $rm master.zip
        $cd tweetprep-master

Install the package:
--------------------

::

        python setup.py install    

# Example
---------

.. code:: python

        import tweetprep
        from tweetprep import lang_translator

        tweet = "#COVID-19 is the worst pandemic @2020!! :,("
        # get translated tweet
        lang="es"
        print(lang_translator.translate(tweet,dest=lang).text)

        # Get processed version of tweet
        print(tweetprep.clean(tweet))

Here is the output:
-------------------

::

    # COVID-19 es la peor pandemia @ 2020!! :,(
    covid19 is the worst pandemic crying smiley

