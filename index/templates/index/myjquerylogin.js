$(document).ready(function(){
// 注册转换
  $("#lb22").click(function(){
    $("#loginbox").css({"display":"none"});
  });

   $("#lb22").click(function(){
    $("#rgbox").css({"display":"block"});
  });
  

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