from blinker import signal


def test_should_receive_signal_when_send_signal():
    send_data = signal('send-data')

    @send_data.connect
    def receive_data(sender, **kw):
        print("Caught signal from %r, data %r" % (sender, kw))
        return 'received!'

    result = send_data.send('anonymous', abc=123)
    assert result is not None
