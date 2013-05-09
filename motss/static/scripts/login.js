$(document).ready(function(){
  // 注册转换
  $("#lb22").click(function(){
    $("#loginbox").css({"display":"none"});
  });

  $("#lb22").click(function(){
    $("#rgbox").css({"display":"block"});
  });
  
  $("#btn_login").click(login);

  // 登录转换
  $("#lginr").click(function(){
    $("#rgbox").css({"display":"none"});
  });

  $("#lginr").click(function(){
    $("#loginbox").css({"display":"block"});
  });

  
  // 其他帐号登录图标
  $("#lb21").click(function(){
    $(".olgl").toggle(100);
  });

  // 注册成功
  $("#btn_rg").click(function(){
    $(".rp").show(100);
  });
});

function login() {
  var username = $("#login_username").val();
  var password = $("#login_password").val();
  var csrftoken = $.cookie('csrftoken');
 
  $.ajax({
    url : "/member/dologin",
    data : {
      'username' : username,
      'password' : password,
      'csrfmiddlewaretoken' : csrftoken
    },
    dataType : 'json',
    success : function(data) {
      if (data.code == 0) {
        window.location.href='/home/'
      };
    },
    error : function(xhr) {
      alert("error:"+$.parseJSON(xhr.responseText).msg)
    } 
  });

 /*
  $.post("/member/dologin", {
      'username' : username,
      'password' : password,
      'csrfmiddlewaretoken' : csrftoken
    }, function(data) {

    });*/
}
