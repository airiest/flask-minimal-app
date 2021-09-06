// Status 受信処理（websocket処理）
$(function () {

    (function () {
        var ws = new WebSocket('ws://localhost:9000/ws/clock');

        ws.onmessage = function (message) {
            var message_data = JSON.parse(message.data);
            $('#clock').html(message_data['now'])
        };
    }());

    $('#get').on({
        'click': function () {
            $.ajax({
                type: 'GET',
                url: '/v1/echo/',
                data: null,
                contentType: 'application/json',
                dataType: 'json',
            }).done(function (data) {
                $('#get-ret').html(data.result);
            })
        }
    });

    $('#post').on({
        'click': function () {
            send_data = { 'msg': $('#post-msg').val() }
            $.ajax({
                type: 'POST',
                url: '/v1/echo/',
                data: JSON.stringify(send_data),
                contentType: 'application/json',
                dataType: 'json',
            }).done(function (data) {
                $('#post-ret').html(data.result);
            })
        }
    });

});
