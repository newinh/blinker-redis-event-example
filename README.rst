=======================
Event-Driven Cascading
=======================

해당 카타 프로젝트는 DDD(Domain Driven Development)에서 파이썬에서 Aggregate 간의 연계된 연산을 어떻게 전달한지에 대한 방법을 시도한 것이다.
유저스토리는 게시판의 기능 중 공지사항 삭제 기능과 관련된다.


User Story
==========
공지사항 작성자가 공지사항을 삭제할 경우에 댓글과 첨부파일이 같이 삭제되어야한다

.. code-block:: shell

    .
    └── Notice(공지사항)
        ├── Comment(댓글)
        └── Attachment(첨부파일)

해당 구현을 위한 기술 스택은 다음과 같다. 자세한 내용은 `Redis`_ and `Blinker`_ 참고하면 된다

.. _Redis: https://redis.io/documentation
.. _Blinker: https://pythonhosted.org/blinker/



Dependencies Installation
=========================

* Redis install

.. code-block:: shell

    $ docker run --name some-redis -d -p 6379:6379 redis





Architecture
============
* DDD Aggregator domain logic
* Dispatcher
* Event Source

여기에 그림을 추가하여 사용함(TODO)


Event Generation
----------------


Event Subscription
------------------


LICENSE
=======

MIT License.