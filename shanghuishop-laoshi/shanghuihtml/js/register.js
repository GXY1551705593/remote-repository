// alert('ok')

function uuid() {
    /* 这是生成uuid的函数*/
    var s = [];
    var hexDigits = "0123456789abcdef";
    for (var i = 0; i < 36; i++) {
        s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
    }
    s[14] = "4";  // bits 12-15 of the time_hi_and_version field to 0010
    s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1);  // bits 6-7 of the clock_seq_hi_and_reserved to 01
    s[8] = s[13] = s[18] = s[23] = "-";

    var uuid = s.join("");
    return uuid;
};

// var prefix_id = ''
var current_id = '';


function getImageCode() {
       // 这个函数生成新的uuid，并且在前端中将验证码对应的src替换掉
    var uuid_data = uuid();
    current_id = uuid_data;
    $('#img_code').attr('src','http://127.0.0.1:8000/image_code/'+uuid_data+'/')

}

$(function () {
    getImageCode();
    $('#msg_req').click(function () {
        // alert(current_id)
        // 1、拼接请求路径路径 GET  /msg_code/?image_id=uuid&image_text=mytext&phone=12345678
        // 1.0获取 uuid 输入的文字验证码、电话号码
        image_id = current_id;

        image_text  = $('#mytext').val();
        phone = $('#phone').val();




        // 1.1 将获取到的数据进行正则的校验
        var reg = new RegExp('1[3456789]\\d{9}')



        var reg_uuid = /^[\w]{8}-[\w]{4}-[\w]{4}-[\w]{4}-[\w]{12}$/;
        var reg_text = /^[\w]{4}$/;
        var reg_phone = /^1[3456789]\d{9}$/;
        console.log(reg_uuid.exec(image_id));
        console.log(reg_uuid.test(image_id));


        // 1.2利用正则进行校验,如果校验不通过，则返回弹窗
        if(!reg_uuid.test(image_id)){
            alert('图片地址校验未通过');
            return;
        }
        if(!reg_text.test(image_text)){
            alert('验证码校验未通过');
            return;
        }

        if(!reg_phone.test(phone)){
            alert('手机号码校验未通过');
            return;
        }

        //拼接的是向后端提交申请短信验证码的url
        msg_url = 'http://127.0.0.1:8000/msg_code/?image_id='+image_id+'&image_text='+image_text+'&phone='+phone
        // alert(msgurl)
        console.log(msg_url);


        // 2、通过ajax发送请求
        $.ajax({
            url:msg_url,
            method:'GET',
            contentType:'application/json',
            success:function (data) {
                alert(data)
            },
            error:function (data) {
                // alert('异常处理')
                alert(data)
                console.log(data)
            }


        })


    })
})