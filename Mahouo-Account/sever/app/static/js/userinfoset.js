//生日修改控件
//#api-birthday-open(打开) #api-birthday-close(关闭) #api-birthday-module
//#api-birthday-input(控件)
//触发 #api-birthday-post(发送内容) #api-birthday-imput(状态提示)

//打开修改
$('#api-birthday-open').click(function(){
    $('#api-birthday-module').css('display','block');
});
// 关闭修改
$('#api-birthday-close').click(function(){
    $('#api-birthday-module').css('display','none');
});

//获取值发送
$('#api-birthday-post').click(function(){
    var date = $('#api-birthday-input').val()
    if (date == ''){
        alert('请选择日期')
    }else{
        $.ajax({
            type: "POST",
            url: "https://account.mahouo.com/api/profile/birthday",
            data: {"brd": date},
            dataType: 'json',
            success: function (data) {
                if(data['type'] == 1){
                    $('#api-birthday-shon').html(date);
                    $('#api-birthday-module').css('display','none');
                    history.go(0)
                }else{
                    alert('提交失败, 请重试');
                }
                
            }
        });
    }
});


//打开修改
$('#api-gender-open').click(function(){
    $('#api-gender-module').css('display','block');
});
// 关闭修改
$('#api-gender-close').click(function(){
    $('#api-gender-module').css('display','none');
});

//获取值发送
$('#api-gender-post').click(function(){
    var sel = $('#api-gender-input').val()
    if (sel == ''){
        alert('请选择日期')
    }else{
        $.ajax({
            type: "POST",
            url: "https://account.mahouo.com/api/profile/gender",
            data: {"brd": sel},
            dataType: 'json',
            success: function (data) {
                if(data['type'] == 1){
                    $('#api-gender-shon').html(sel);
                    $('#api-gender-module').css('display','none');
                    history.go(0) 
                }else{
                    alert('提交失败, 请重试');
                }
            }
        });
    }
});


//打开修改
$('#api-region-open').click(function(){
    $('#api-region-module').css('display','block');
});
// 关闭修改
$('#api-region-close').click(function(){
    $('#api-region-module').css('display','none');
});

//获取值发送
$('#api-region-post').click(function(){
    var reg = $('#api-region-input').val()
    if (reg == ''){
        alert('请选择日期')
    }else{
        $.ajax({
            type: "POST",
            url: "https://account.mahouo.com/api/profile/region",
            data: {"brd": reg},
            dataType: 'json',
            success: function (data) {
                if(data['type'] == 1){
                    $('#api-region-shon').html(reg);
                    $('#api-region-module').css('display','none');
                    history.go(0) 
                }else{
                    alert('提交失败, 请重试');
                }
            }
        });
    }
});