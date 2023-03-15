aioschedule
===========


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

Usage
-----

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

    loop = asyncio.get_event_loop()
    while True:
        loop.run_until_complete(schedule.run_pending())
        time.sleep(0.1)

Documentation
-------------

Schedule's documentation lives at `schedule.readthedocs.io <https://schedule.readthedocs.io/>`_.


Development
-----------
Run `vagrant up` to spawn a virtual machine containing the development
environment. Make sure to set the `IBR_GIT_COMMITTER_NAME` and
`IBR_GIT_COMMITTER_EMAIL` environment variables.


Meta
----

- Geoff Robinson - geoff.robinson@carvesystems.com
- Daniel Bader - `@dbader_org <https://twitter.com/dbader_org>`_ - mail@dbader.org
- Cochise Ruhulessin - `@magicalcochise <https://twitter.com/magicalcochise>`_ - c.ruhulessin@ibrb.org

Inspired by `Adam Wiggins' <https://github.com/adamwiggins>`_ article `"Rethinking Cron" <https://adam.herokuapp.com/past/2010/4/13/rethinking_cron/>`_ and the `clockwork <https://github.com/Rykian/clockwork>`_ Ruby module.

Distributed under the MIT license. See `LICENSE.txt <https://github.com/dbader/schedule/blob/master/LICENSE.txt>`_ for more information.

https://github.com/geoff-carve-systems/python-aioschedule
