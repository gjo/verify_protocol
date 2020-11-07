================================
Verify Protocol
================================



Install::

  $ pip install verity_protocol

Usage::

  from verify_protocol import verify_object

  def test_proto():
      from your_protocols import YourProtocol
      from your_implemements import YourClass

      obj = YourClass()
      assert verify_object(YourProtocol, obj)


development
-----------

setup::

  $ python3.8 -m venv .env
  $ . .env/bin/activate
  (.env)$ pip install -e '.[develop]'

run tests::

  (.env)$ tox
