schedule
========

.. image:: https://api.travis-ci.org/geoff-carve-systems/python-aioschedule.svg?branch=master
        :target: https://travis-ci.org/geoff-carve-systems/python-aioschedule

.. image:: https://coveralls.io/repos/geoff-carve-systems/python-aioschedule/badge.svg?branch=master
        :target: https://coveralls.io/r/geoff-carve-systems/python-aioschedule


Python job scheduling for humans.

Forked from github.com/ibrb/python-aioschedule and rebased from a recent version of github.com/dbader/schedule.

Bug fixes for code in both source repos.

- A simple to use API for scheduling jobs, made for humans.
- In-process scheduler for periodic jobs. No extra processes needed!
- Very lightweight and no external dependencies.
- Excellent test coverage.
- Tested on Python 3.7, 3.8, 3.9, 3.10, 3.11


:doc:`Example <examples>`
-------------------------

.. code-block:: bash

    $ pip install aioschedule

.. code-block:: python

    import asyncio
    import aioschedule as schedule
    import time

    async def job(message='stuff', n=1):
        print("Asynchronous invocation (%s) of I'm working on:" % n, message)
        asyncio.sleep(1)

    for i in range(1,3):
        schedule.every(1).seconds.do(job, n=i)
    schedule.every(5).to(10).days.do(job)
    schedule.every().hour.do(job, message='things')
    schedule.every().day.at("10:30").do(job)
    schedule.every().monday.do(job)
    schedule.every().wednesday.at("13:15").do(job)
    schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
    schedule.every().minute.at(":17").do(job)

    loop = asyncio.get_event_loop()
    while True:
        loop.run_until_complete(schedule.run_pending())
        time.sleep(0.1)


More :doc:`examples`

When **not** to use Schedule
----------------------------
Let's be honest, Schedule is not a 'one size fits all' scheduling library.
This library is designed to be a simple solution for simple scheduling problems.
You should probably look somewhere else if you need:

* Job persistence (remember schedule between restarts)
* Exact timing (sub-second precision execution)
* Concurrent execution (multiple threads)
* Localization (workdays or holidays)


**Schedule does not account for the time it takes for the job function to execute.**
To guarantee a stable execution schedule you need to move long-running jobs off the main-thread (where the scheduler runs).
See :doc:`parallel-execution` for a sample implementation.


Read More
---------
.. toctree::
   :maxdepth: 2

   installation
   examples
   background-execution
   parallel-execution
   timezones
   exception-handling
   logging
   multiple-schedulers
   faq
   reference
   development

.. toctree::
   :maxdepth: 1

   changelog


Issues
------

If you encounter any problems, please `file an issue <http://github.com/dbader/schedule/issues>`_ along with a detailed description.
Please also use the search feature in the issue tracker beforehand to avoid creating duplicates. Thank you 😃

About Schedule
--------------

Created by `Daniel Bader <https://dbader.org/>`__ - `@dbader_org <https://twitter.com/dbader_org>`_

Inspired by `Adam Wiggins' <https://github.com/adamwiggins>`_ article `"Rethinking Cron" <https://adam.herokuapp.com/past/2010/4/13/rethinking_cron/>`_ and the `clockwork <https://github.com/Rykian/clockwork>`_ Ruby module.


Distributed under the MIT license. See ``LICENSE.txt`` for more information.

.. include:: ../AUTHORS.rst
