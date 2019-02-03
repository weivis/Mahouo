var sUserAgent = navigator.userAgent;
var ip = returnCitySN['cip'];

$.ajax({
    type: "GET",
    url: "https://api.mahouo.com/gps/",
    dataType: 'json',
    success: function (data) {
        region = data['country'] +'-'+ data['province'] +'-'+ data['city']
    }
});

$('#auth_account').click(function(){
    var account = $( "input[id=input-account]" ).val();
    if(account){
        $.ajax({
            type: "POST",
            url: "account-auth",
            data: {"key": account},
            dataType: 'json',
            success: function (msg) {
                if(msg['type']=='ok'){
                    account_key = account;
                    nextpassword_page(account);
                }else if(msg['type']=='-1'){
                    alert('账户不存在')
                }
            }
        });
    }else{
        alert('请输入账户')
    }
})

function nextpassword_page(account){
    $('#account_auth-ok_key').html(account)
    $('#auth-account').css('display','none')
    $('#auth-password').css('display','block')
}

   function getUrlParam(name) {
       var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
       var r = window.location.search.substr(1).match(reg);  //匹配目标参数

       if (r != null)
           return unescape(r[2]);
       return null; //返回参数值
   }

$('#sign_post').click(function (){
    var password = $( "input[id=input-password]" ).val();
    var sign_long = $('#login_long').is(':checked')
    if(account_key){
        if(password){
            authdata = {
                "key":account_key,
                "pass":password,
                "wp":sUserAgent,
                "ip":ip,
                "city":region,
                "long":sign_long,
            }
            $.ajax({
                type: "POST",
                url: "auth",
                data: authdata,
                dataType: 'json',
                success: function (msg) {
                    if (msg['type'] == 'ok'){
                        var referer = getUrlParam('referer');
                        if (referer == null){
                            $(window).attr('location','https://www.mahouo.com/');
                        }else{
                            $(window).attr('location',referer);
                        }
                    }else{
                        return false;
                    }
                    //return false;
                }
            });
        }else{
            alert('密码不存在')
        }
    }else{
        alert('账户不存在')
    }

})