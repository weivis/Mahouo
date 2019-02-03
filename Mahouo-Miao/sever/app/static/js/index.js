function hot_uc(data) {
    $('#module-hota_content').prepend('<div class="module-hota_content-li"><a href="'+ data['url'] +'" target="_blank" class="module-hota_content-a">'+ data['name'] +'</a></div>')
}

function bangumi_animeico(data,day) {
    dataday = '#bangumiapi-' + day;
    $(dataday).prepend('<a href="'+ data['url'] +'">'+
    '<div class="module-bangumi_anime-a">'+
        '<div class="module-bangumi_anime-img">'+
            '<img src="static/img/bangumi-cover/'+ data['cover'] +'" width="100%">'+
        '</div>'+
        '<div class="module-bangumi_anime-title mi">'+
            data['name'] +
        '</div>'+
'</div></a>');
}

window.onload = function() {
    var oLi = document.getElementById("module-bangumi-title-r-sel").getElementsByTagName("div");
    var oUl = document.getElementById("module-bangumi_content").getElementsByTagName("lu");

    for (var i = 0; i < oLi.length; i++) {
      oLi[i].index = i;
      oLi[i].onclick = function() {
        for (var n = 0; n < oLi.length; n++) oLi[n].className = "module-bangumi-tab-a";
        this.className = "module-bangumi-tab-a module-bangumi-tab-a_hot";
        for (var n = 0; n < oUl.length; n++) oUl[n].style.display = "none";
        oUl[this.index].style.display = "block";
      }
    }
    getbangumi()
  }

function commonly_com(data) {
    $('#commonly_com-ico').prepend('<a href="'+ data['url'] +'" target="">'+
    '<div class="commonly_com a"><img class="commonly_com img" src="static/img/ico/'+ data['ico'] +'"><div class="commonly_com name">'+ data['name'] +'</div></div>'+
    '</a>')
}

function classification1(data) {
    $('#cf-data1').prepend('<a href="'+ data['url'] +'" target="_blank"><div class="classification_com a">'+ data['name'] +'</div></a>')
}
function classification2(data) {
    $('#cf-data2').prepend('<a href="'+ data['url'] +'" target="_blank"><div class="classification_com a">'+ data['name'] +'</div></a>')
}
function classification3(data) {
    $('#cf-data3').prepend('<a href="'+ data['url'] +'" target="_blank"><div class="classification_com a">'+ data['name'] +'</div></a>')
}
function classification4(data) {
    $('#cf-data4').prepend('<a href="'+ data['url'] +'" target="_blank"><div class="classification_com a">'+ data['name'] +'</div></a>')
}

function getbangumi() {
    $.ajax({
        type: "POST",
        url: "index-api/bangumi",
        dataType: 'json',
        success: function (msg) {
            all = msg['all'];day1 = msg['day1'];day2 = msg['day2'];day3 = msg['day3'];day4 = msg['day4'];day5 = msg['day5'];day6 = msg['day6'];day7 = msg['day7'];
            $.each((all),
                function () {
                    bangumi_animeico(this,day='all')
            });
            $.each((day1),
                function () {
                    bangumi_animeico(this,day='day1')
            });
            $.each((day2),
                function () {
                    bangumi_animeico(this,day='day2')
            });
            $.each((day3),
                function () {
                    bangumi_animeico(this,day='day3')
            });
            $.each((day4),
                function () {
                    bangumi_animeico(this,day='day4')
            });
            $.each((day5),
                function () {
                    bangumi_animeico(this,day='day5')
            });
            $.each((day6),
                function () {
                    bangumi_animeico(this,day='day6')
            });
            $.each((day7),
                function () {
                    bangumi_animeico(this,day='day7')
            });
        }
    });
}

$.ajax({
    type: "POST",
    url: "index-api/hot-uc",
    dataType: 'json',
    success: function (msg) {
        $.each((msg),
            function () {
                hot_uc(this);
        });
    }
});

$.ajax({
    type: "POST",
    url: "index-api/commonly-com",
    dataType: 'json',
    success: function (msg) {
        $.each((msg),
            function () {
                commonly_com(this);
        });
    }
});

$.ajax({
    type: "POST",
    url: "/index-api/classification-comlist",
    dataType: 'json',
    success: function (msg) {
        data1 = msg['data1'];data2 = msg['data2'];data3 = msg['data3'];data4 = msg['data4'];
        $.each((data1),
            function () {
                classification1(this);
        });
        $.each((data2),
            function () {
                classification2(this);
        });
        $.each((data3),
            function () {
                classification3(this);
        });
        $.each((data4),
            function () {
                classification4(this);
        });
    }
});