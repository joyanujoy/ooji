ooji
====

My url shortener



@todo

                                    /-------- encoder.py
                                   /
    ooji.py    -------------------/---------- filestore.py
    controller                    \
      |                            \
      |                             \-------- postgrestore.py
      |                              \------- redistore.py
      |
      |
      |
      |
      |
      |------- @/index   - index page
      |------- @/shorten - shorten url
      |------- @/expand  - expand url
      |------- @/options - list api allowed methods
      |------- @/summary - print store statistics
      |------- @/urlinfo - print stats for a url
