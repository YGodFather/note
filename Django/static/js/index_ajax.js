// 按钮发送ajax请求
$(document).ready(function() {
    $("#submit_button").click(function () {
        var url_para=$("#data_input").val();
        console.log(url_para)
        $.ajax({
            type: 'GET',
            url:'/get_ctbpm',
            cache: false,
            data:url_para,
            // dataType:'string',
            success:function (result) {
                console.log(result['code'])
                // if (result['code']==1){
                //     alert(result['message'])
                // }
                $("#data_input").val(result['code'])

            }
        })

    })
})


