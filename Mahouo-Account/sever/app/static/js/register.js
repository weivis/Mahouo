password_username_type = 0
password_emailname_type = 0
password_phone_type = 0
password_auth_type = 0
password_useremail_type = 0

function auth_username_input(){
    var username = $( "input[id=auth_username_input]" ).val();
    var username_length = $( "input[id=auth_username_input]" ).val().length;
    if(username){
        if(username_length>20){
            $("#js_auth_username_error").html("用户名过长")
            $("#js_auth_username_error").css("color","#f00")
        }else{
            $.ajax({
                type: "POST",
                url: "https://account.mahouo.com/api/search-username",
                data: {"username": username},
                dataType: 'json',
                success: function (msg) {
                    if (msg['type'] == '0'){
                        $("#js_auth_username_error").html("OK")
                        $("#js_auth_username_error").css("color","#218a00")
                        password_username_type = 1
                    }else{
                        $("#js_auth_username_error").html("该用户名已被使用")
                        $("#js_auth_username_error").css("color","#f00")
                    }
                }
            });
        }
    }else{
        $("#js_auth_username_error").html("必填")
        $("#js_auth_username_error").css("color","#f00")
    }
};

function auth_mahouoemail_input(){
    var mahouoemail = $( "input[id=auth_mahouoemail_input]" ).val();
    var mahouoemail_length = $( "input[id=auth_mahouoemail_input]" ).val().length;
    if(mahouoemail){
        if(mahouoemail_length>25){
            $("#js_auth_mahouoemail_error").html("邮箱名过长")
            $("#js_auth_mahouoemail_error").css("color","#f00")
        }else{
            $.ajax({
                type: "POST",
                url: "https://account.mahouo.com/api/search-mahouoemail",
                data: {"emailname": mahouoemail},
                dataType: 'json',
                success: function (msg) {
                    if (msg['type'] == '0'){
                        $("#js_auth_mahouoemail_error").html("OK")
                        $("#js_auth_mahouoemail_error").css("color","#218a00")
                        password_emailname_type = 1
                    }else{
                        $("#js_auth_mahouoemail_error").html("该邮箱名已被使用")
                        $("#js_auth_mahouoemail_error").css("color","#f00")
                    }
                }
            });
        }
    }else{
        $("#js_auth_mahouoemail_error").html("必填")
        $("#js_auth_mahouoemail_error").css("color","#f00")
    }
};

function auth_phone_input(){
    var phone = $( "input[id=auth_phone_input]" ).val();
    var phone_length = $( "input[id=auth_phone_input]" ).val().length;
    if(phone){
        if(phone_length>25){
            $("#js_auth_phone_error").html("手机号格式不正确")
            $("#js_auth_phone_error").css("color","#f00")
        }else{
            $.ajax({
                type: "POST",
                url: "https://account.mahouo.com/api/search-phone",
                data: {"phone": phone},
                dataType: 'json',
                success: function (msg) {
                    if (msg['type'] == '0'){
                        $("#js_auth_phone_error").html("OK")
                        $("#js_auth_phone_error").css("color","#218a00")
                        password_phone_type = 1
                    }else{
                        $("#js_auth_phone_error").html("该手机号已被注册")
                        $("#js_auth_phone_error").css("color","#f00")
                    }
                }
            });
        }
    }else{
        $("#js_auth_phone_error").html("必填")
        $("#js_auth_phone_error").css("color","#f00")
    }
};

function password_1(){
    var passwrod = $( "input[id=input_password]" ).val();
    var passwrod_length = $( "input[id=input_password]" ).val().length;
    if(passwrod){
        if(passwrod_length<8){
            $('#js_auth_password_error').html('密码太短')
            $("#js_auth_password_error").css("color","#f00")
        }else{
            $('#js_auth_password_error').html('请重复输入一遍')
            $("#js_auth_password_error").css("color","#0070ff")
            function r(){
                password_2();
            }
        }
    }else{
        $('#js_auth_password_error').html('必填')
        $("#js_auth_password_error").css("color","#f00")
    }
}

function password_2(){
    var passwrod = $( "input[id=input_password]" ).val();
    var R_passwrod = $( "input[id=input_R_password]" ).val();
    if(R_passwrod){
        if(passwrod == R_passwrod){
            $('#js_auth_password_error').html('OK')
            password_auth_type = 1
        }else{
            $('#js_auth_password_error').html('密码不一致')
            $("#js_auth_password_error").css("color","#f00")
        }
    }else{function r(){
        password_1();
        }
    }
}

function auth_useremail_input(){
    var useremail = $( "input[id=auth_useremail_input]" ).val();
    var useremail_length = $( "input[id=auth_useremail_input]" ).val().length;
    var emailreg = /^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/;
    var isok = emailreg.test(useremail);
    if(isok){
        if(useremail){
            if(useremail_length>50){
                $("#js_auth_useremail_error").html("邮箱过长")
                $("#js_auth_useremail_error").css("color","#f00")
            }else{
                $.ajax({
                    type: "POST",
                    url: "https://account.mahouo.com/api/search-email",
                    data: {"email": useremail},
                    dataType: 'json',
                    success: function (msg) {
                        if (msg['type'] == '0'){
                            $("#js_auth_useremail_error").html("OK")
                            $("#js_auth_useremail_error").css("color","#218a00")
                            password_useremail_type = 1
                        }else{
                            $("#js_auth_useremail_error").html("该邮箱已被使用")
                            $("#js_auth_useremail_error").css("color","#f00")
                        }
                    }
                });
            }
        }else{
            $("#js_auth_useremail_error").html("必填")
            $("#js_auth_useremail_error").css("color","#f00")
        }
    }else{
        $("#js_auth_useremail_error").html("邮箱格式有误")
        $("#js_auth_useremail_error").css("color","#f00")
    }
};

var usermdcheckedtype = $('input').prop("checked");

$('#reg_post').click(
    function register_ajax(){
        var username = $( "input[id=auth_username_input]" ).val();
        var mahouoemail = $( "input[id=auth_mahouoemail_input]" ).val();
        var phone = $( "input[id=auth_phone_input]" ).val();
        var passwrod = $( "input[id=input_password]" ).val();
        var useremail = $( "input[id=auth_useremail_input]" ).val();
        var usermdcheckedtype = $('#account_md_checkbox').is(':checked');
        var regdata = {
            "reg_name": username,
            "reg_emailname": mahouoemail,
            "reg_phone": phone,
            "reg_pass": passwrod,
            "reg_useremail": useremail,
        }

        if(password_username_type + password_useremail_type + password_emailname_type + password_phone_type + password_auth_type == 5){
            $.ajax({
                type: "POST",
                url: "https://account.mahouo.com/register/post",
                data: regdata,
                dataType: 'json',
                success: function (msg) {
                    if (msg['out_type'] == 'ok'){
                        window.location.replace("/sign-in/");
                    }else{
                        alert(msg['out'])
                    };
                    //alert(msg['out_type'])
                }
            });
        }
    }
)