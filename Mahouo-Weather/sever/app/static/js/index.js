function css3anime_load(){
    $("#content").addClass("content-wp content_anime");
    $("#data-li1").addClass("weather-datali content_top-css3");
    $("#data-li2").addClass("weather-datali content-css3");
    $("#data-li3").addClass("weather-datali content-css3");
    $("#data-li4").addClass("weather-datali content-css3");
    $("#api-background-pic").addClass("background-css3");
};

//nowdata
function nowdata(data){
    $("#api-wendu").text(data.temperature + "℃");
    $("#api-wind_direction").text(data.wind_direction);
    $("#api-text").text(data.text);
    $("#api-wind_scale").text(data.wind_scale);
    $("#api-wind_speed").text(data.wind_speed + "级");
    $("#api-pressure").text(data.pressure + "hPa");
    $("#api-visibility").text(data.visibility + "KM");
};

function pmdata(data){
    $("#api-pm25").text(data.pm25);
    $("#api-pm10").text(data.pm10);
    $("#api-so2").text(data.so2);
    $("#api-no2").text(data.no2);
    $("#api-co").text(data.co);
    $("#api-o3").text(data.o3);
};

function apihtml(data){
    var nwehtml = "空气质量   " + data.aqi + "   " + data.quality
    $("#api-aqi").text(nwehtml);
};

function rcdata(data){
    $("#api-sunrise").text(data.sunrise);
    $("#api-sunset").text(data.sunset);
};

function todaydata_outhtml(data){
    var weather_text = data['text'];
    var text_data = weather_text.replace('\/','~');
    $("#api-today").prepend('<div class="today a opy-2">'+
    '<div class="today_a li today_a date">'+ data['day'] +'</div>'+
        '<div class="today_a li">'+
            '<div class="today_a ico">'+
                '<img src="http://p6ykp0exp.bkt.clouddn.com/'+ data['code1'] +'.png" class="today_a img" width="50%">'+
            '</div>'+
        '</div>'+
    '<div class="today_a li today_a wendu">'+ data['high'] +'°'+ data['low'] +'°</div>'+
    '<div class="today_a li">'+ text_data +'</div>'+
    '</div>');
};

function suggestiondata(data){
    $("#api-dressing").text(data.dressing['brief'] + " - " + data.dressing['details']);
    $("#api-uv").text(data.uv['brief'] + " - " + data.uv['details']);
    $("#api-car_washing").text(data.car_washing['brief'] + " - " + data.car_washing['details']);
    $("#api-travel").text(data.travel['brief'] + " - " + data.travel['details']);
    $("#api-flu").text(data.flu['brief'] + " - " + data.flu['details']);
    $("#api-sport").text(data.sport['brief'] + " - " + data.sport['details']);
};

function getweatherdata(city_data) {
    $.getJSON('http://weather.mahouo.com/api/weather=' + city_data,
    function(data, textStatus) {
        var weather = data['weather'];
        var now = weather[0]['now'];
        var pmget = now['air_quality']['city'];
        var today = weather[0]['today'];
        var suggestion = today['suggestion'];
        var future = weather[0]['future'];
        
        var newico = 'http://p6ykp0exp.bkt.clouddn.com/' + now['code'] + '.png'
        $("#weather-ico").attr('src',newico);
        $("#api-city").text("中国 " + data['weather'][0]['city_name']);
        $("#api-daywendu").text(future[0]['high']+"℃ ~ "+future[0]['low']+"℃");
        $("#api-date").text(future[0]['date']+' '+future[0]['day']);

        nowdata(now);
        pmdata(pmget);
        apihtml(pmget);
        rcdata(today);

        $("#api-today").empty();
        
        future.reverse()
        $.each((future),
            function () {
                todaydata_outhtml(this);
        });

        suggestiondata(suggestion);

        loginanimepofls();
        css3anime_load();
    });
};

function left_citytab_out(data) {
    $("#left-citytab").prepend('<li class="left-citytab a">' + data['areaname'] + '</li>');
}

function city_list(data) {
    $("#right-citycontent").prepend('<div class="right-citycontent a" data-cityid="' + data['cityid'] + '">' + data[
        'cityname'] + '</div>');
}

function countryget(country) {
    $.getJSON('http://weather.mahouo.com/api/country=' + country,
        function (data, textStatus) {
            $("#left-citytab").empty();
            data.reverse();
            $.each((data),
                function () {
                    //alert(data);
                    left_citytab_out(this);
                });
        });
};

function cityget(cityname) {
    $.getJSON('http://weather.mahouo.com/api/city=' + cityname,
        function (data, textStatus) {
            data.reverse();
            $.each((data),
                function () {
                    //alert(data);
                    city_list(this);
                });
        });
};

$(".weather-county.a").click(function (event) {
    //alert(event.target.innerHTML);
    countryget(event.target.innerHTML);
    $(".weather-county.a").css("background-color", "");
    $(event.target).css("background-color", "#000");
});

$("#left-citytab").on("click", ".left-citytab.a", function () {
    //alert($(this).html());
    cityget($(this).html());
    $(".left-citytab.a").css("background-color", "");
    $(event.target).css("background-color", "#000");
})

$("#right-citycontent").on("click", ".right-citycontent.a", function () {
    //alert($(this).data("cityid"));
    $("#load-anime-po").addClass("");
    $("#load-anime-po").removeClass("load-pa-po");
    $("#weather-more-por").hide();
    getweatherdata($(this).data("cityid"));
    $(".right-citycontent.a").css("background-color", "");
    $(event.target).css("background-color", "#000");
})

//$(this).click(function(event){
//    alert(event.target.innerHTML);
//$(".right-citycontent.a").css("background-color","");
//$(event.target).css("background-color","#000")
//});

$("#moremap").click(
    function () {
        $("#weather-more-por").show();
        $("#load-anime-po").css("height", "100%");
    }
);

$("#more-weather_powin-closs").click(
    function () {
        $("#weather-more-por").hide();
        $("#load-anime-po").css("height", "0px");
    }
);