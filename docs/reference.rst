Reference
=========

.. module:: aioschedule

This part of the documentation covers all the interfaces of schedule.

Main Interface
--------------

.. autodata:: default_scheduler
.. autodata:: jobs

.. autofunction:: every
.. autofunction:: run_pending
.. autofunction:: run_all
.. autofunction:: get_jobs
.. autofunction:: clear
.. autofunction:: cancel_job
.. autofunction:: next_run
.. autofunction:: idle_seconds


Classes
-------

.. autoclass:: aioschedule.Scheduler
   :members:
   :undoc-members:

.. autoclass:: aioschedule.Job
   :members:
   :undoc-members:


Exceptions
----------

.. autoexception:: aioschedule.CancelJob
