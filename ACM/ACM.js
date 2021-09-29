var signUpButton = document.getElementById('signUp')
var signInButton = document.getElementById('signIn')
var container = document.getElementById('dowebok')

// API URL
var loginUrl = "../api/login/"
var regUrl = "../api/register/"
var checkUsernameUrl = "../api/checkusername/"
var verEmailUrl = "../api/getemailcode/"

signUpButton.addEventListener('click', function () {
  container.classList.add('right-panel-active')
})

signInButton.addEventListener('click', function () {
  container.classList.remove('right-panel-active')
})

const slider = document.querySelector('[data-slider]');
var timer = 300;

slider.addEventListener('input', e => {
  timer = 500 - slider.value;
});

addCircles();

function addCircles() {
  setTimeout(() => {
    addCircle(...randomPosition());
    addCircles();
  }, timer);
}

function addCircle(x, y) {
  var circle = document.createElement('div');
  var animationTime = Math.round(Math.random() * 10);
  circle.classList.add('circle');
  circle.style.left = x + 'vw';
  circle.style.top = y + 'vh';
  circle.style.backgroundColor = randomColor();
  circle.style.setProperty('--grow-time', `${animationTime}s`);

  requestAnimationFrame(() => {
    document.body.appendChild(circle);
    setTimeout(removeCircle.bind(this, circle), animationTime * 1000);
  });
}

function removeCircle(circle) {
  document.body.removeChild(circle);
}

function randomPosition() {
  return [
    Math.random() * 100 + 1,
    Math.random() * 100 + 1];

}

function randomColor() {
  const colors = [
    '#81ecec',
    '#74b9ff',
    '#a29bfe',
    '#ffeaa7',
    '#fab1a0',
    '#ff7675',
    '#fd79a8'];

  return colors[Math.round(Math.random() * colors.length)];
}

function showMessage(message, type) {
  let messageJQ = $("<div class='showMessage'>" + message + "</div>");
  if (type == 0) {
    messageJQ.addClass("showMessageError");
  } else if (type == 1) {
    messageJQ.addClass("showMessageSuccess");
  }
  /**先将原始隐藏，然后添加到页面，最后以600秒的速度下拉显示出来*/
  messageJQ.hide().appendTo("body").slideDown(300);
  /**3秒之后自动删除生成的元素*/
  window.setTimeout(function () {
    messageJQ.fadeOut("slow");
  }, 2200);
}

$("#adveri").hide();
// 登录块
$(function () {
  $(".btn1").click(function () {
    var usernameText = $("#username").val();
    var usernamePat = /^[0-9]{10}$/;
    if (usernameText == "") {
      showMessage("请输入用户名！",0);
      //$(".errorMsg").text("请输入用户名！");
      $("#username").css("border-color", "red");
      return false;
    // } else if (!usernamePat.test(usernameText)) {
    //   $(".errorMsg").text("用户名不合法");
    //   $("#username").css("border-color", "red");
    //   return false;
    } else {
      $("#username").css("border-color", "aquamarine");
    }

    var passwordText = $("#password").val();
    if (passwordText == "") {
      showMessage("请输入密码！",0);
      //$(".errorMsg").text("请输入密码！");
      $("#password").css("border-color", "red");
      return false;
    } else {
      $("#password").css("border-color", "aquamarine");
    }

    //$(".errorMsg").text("");
    $.ajax({
      method: 'post',
      url: loginUrl,
      data: {
        username: $("input#username").val(),
        password: $("input#password").val(),
        csrf_token: $("input[name='csrfmiddlewaretoken']").val()
      },
      success:function(res){
        if (res["status"] == "success") {
          window.location.href="##";
        } else {
          showMessage(res["msg"],0);
        }
      },
      error:function(res){
        showMessage(res["msg"],0);
      }
    })
    // .then(response => {
    //   console.log(response);
    // })
  })

  // 用户名检测
  $("#StuID").blur(function () {
    var studentID = $("#StuID").val();
    var studentIDPat = /^[0-9]{10}$/;
    if (studentID == "") {
      showMessage("请输入用户名！",0);
      //$(".errorMsg2").text("请输入用户名！");
      $("#StuID").css("border-color", "red");
      return false;
    } else if (!studentIDPat.test(studentID)) {
      showMessage("学号命名不合法",0);
      //$(".errorMsg2").text("学号命名不合法");
      $("#StuID").css("border-color", "red");
      return false;
    } else {
      $("#StuID").css("border-color", "aquamarine");
    }
    //$(".errorMsg2").text("");
    $.ajax({
      method: 'POST',
      url: checkUsernameUrl,
      data: {
        username: $("input#StuID").val(),
        csrf_token: $("input[name='csrfmiddlewaretoken']").val()
      },
      success:function(res){
        if (res["status"] == "success") {
          if (!res["data"]["usable"]) {
            showMessage("用户名已被占用",0);
          }
        } else {
          showMessage(res["msg"],0);
        }
      },
      error:function(res){
        showMessage(res["msg"],0);
      }
    })
    // .then(response => {
    //   console.log(response);
    // })
  })

  // 姓名检查
  $("#Username").blur(function () {
    var studentName = $("#Username").val();
    var studentNamePat = /^[\u4E00-\u9FA5A-Za-z]+$/;
    if (studentName == "") {
      showMessage("请输入姓名！",0);
      //$(".errorMsg2").text("请输入姓名！");
      $("#Username").css("border-color", "red");
      return false;
    } else if (!studentNamePat.test(studentName)) {
      showMessage("姓名不合法！",0);
      //$(".errorMsg2").text("姓名不合法");
      $("#Username").css("border-color", "red");
      return false;
    } else {
      $("#Username").css("border-color", "aquamarine");
    }
    //$(".errorMsg2").text("");
  })

  // 邮箱检查
  $("#Email").blur(function () {
    var email = $("#Email").val();
    var emailPat = /^\w+@[a-zA-Z0-9]{2,10}(?:\.[a-z]{2,4}){1,3}$/;
    if (email == "") {
      showMessage("请输入邮箱！",0);
      //$(".errorMsg2").text("请输入邮箱！");
      $("#Email").css("border-color", "red");
      return false;
    } else if (!emailPat.test(email)) {
      showMessage("邮箱地址不合法！",0);
      //$(".errorMsg2").text("邮箱地址不合法");
      $("#Email").css("border-color", "red");
      return false;
    } else {
      $("#Email").css("border-color", "aquamarine");
    }
    //$(".errorMsg2").text("");
  })

  // 密码检查
  $("#Password").blur(function () {
    var Password = $("#Password").val();
    var PasswordPat = /^\w+$/;
    if (Password == "") {
      showMessage("请输入密码！",0);
      //$(".errorMsg2").text("请输入密码！");
      $("#Password").css("border-color", "red");
      return false;
    } else if (!PasswordPat.test(Password)) {
      showMessage("密码不合法！",0);
      //$(".errorMsg2").text("密码不合法");
      $("#Password").css("border-color", "red");
      return false;
    } else {
      $("#Password").css("border-color", "aquamarine");
    }
    //$(".errorMsg2").text("");
  })

  // 密码重复检查
  $("#Password2").blur(function () {
    var Password = $("#Password").val();
    var repassword = $("#Password2").val();
    if (repassword == "") {
      showMessage("请输入密码！",0);
      //$(".errorMsg2").text("请输入密码！");
      $("#Password2").css("border-color", "red");
      return false;
    } else if (repassword != Password) {
      showMessage("两次密码不相同！",0);
      //$(".errorMsg2").text("两次密码不相同！");
      $("#Password2").css("border-color", "red");
      return false;
    } else {
      $("#Password2").css("border-color", "aquamarine");
    }
    //$(".errorMsg2").text("");
  })

  $("#EnqueueTime").blur(function () {
    var date = $("#EnqueueTime").val();
    if (date == "") {
      showMessage("请选择时间！",0);
      //$(".errorMsg2").text("请选择时间！");
      $("#EnqueueTime").css("border-color", "red");
      return false;
    } else {
      $("#EnqueueTime").css("border-color", "aquamarine");
    }
    //$(".errorMsg2").text("");
  })

  // 管理员邀请码切换
  let s = 0;
  $("#control").click(function(){
    if(s==0){
      $("#adveri").fadeIn("slow");
      s =1;
      $("a#control").html("您不是管理员吗？");
    }else if(s == 1){
      $("#adveri").fadeOut("slow");
      s = 0;
      $("a#control").html("您是管理员吗？") ;
    }
    console.log(s);
  })

  // 注册
  $(".btn2").click(function () {
    var verification = $("#yan").val();
    if (verification == "") {
      showMessage("请输入验证码！",0);
      //$(".errorMsg2").text("请输入验证码");
    } else {
      $.ajax({
        method: 'post',
        url: regUrl,
        data: {
          username: $("input#StuID").val(),
          password: $("#Password").val(),
          name: $("#Username").val(),
          email: $("#Email").val(),
          department: $("department").val(),
          // joinTime: () => $("#EnqueueTime").val() == '' ? "None" : $("#EnqueueTime").val(),
          emailVerify: $("#yan").val(),
          admin:s,
          adminVerify: $("adver").val(),
          csrf_token: $("input[name='csrfmiddlewaretoken']").val()
        },
        success:function(res){
          if (res["status"] == "success") {
            showMessage("注册成功，您是第"+res["data"]["userId"]+"个用户",1);
          } else {
            showMessage(res["msg"],0);
          }
        },
        error:function(res){
          showMessage(res["msg"],0);
        }
      })
    }
    return false;
  })

  // 邮箱验证码发送
  $("#wert").click(function () {
    var btnget = document.getElementById("wert");
    btnget.disabled = true;
    var email = $("#Email").val();
    var emailPat = /^\w+@[a-zA-Z0-9]{2,10}(?:\.[a-z]{2,4}){1,3}$/;
    if (email == "") {
      showMessage("请输入邮箱！",0);
      //$(".errorMsg2").text("请输入邮箱！");
      $("#Email").css("border-color", "red");
      btnget.disabled = false;
      return false;
    } else if (!emailPat.test(email)) {
      showMessage("邮箱地址不合法！",0);
      //$(".errorMsg2").text("邮箱地址不合法");
      $("#Email").css("border-color", "red");
      btnget.disabled = false;
      return false;
    } else {
      $("#Email").css("border-color", "aquamarine");
      btnget.disabled = true;
      useChangeBTN();
      $.ajax({
        method: 'post',
        url: verEmailUrl,
        data: {
          username: $("input#StuID").val(),
          email: $("#Email").val(),
          csrf_token: $("input[name='csrfmiddlewaretoken']").val()
        },
        success:function(response){
          if (res["status"] == "success") {
            showMessage(res["邮件发送成功请注意查收"],1);
          } else {
            showMessage(res["msg"],0);
          }
        },
        error:function(res){
          showMessage(res["msg"],0);
        }
      })
      // .then(response => {
      //   console.log(response);
      // })
    }
    //$(".errorMsg2").text("");
  })
})

var time0 = 60;
var time = time0;
var t;
function changeBTN() {
  if (time > 0) {
    $("#wert").val("(" + time + "s)" + "重新获取");
    time = time - 1;
  }
  else {
    var btnGet = document.getElementById("wert");
    btnGet.disabled = false;
    $("#wert").val("获取验证码");
    clearInterval(t);
    time = time0;
  }
}
function useChangeBTN() {
  $("#wert").val("(" + time + "s)" + "重新获取");
  time = time - 1;
  t = setInterval("changeBTN()", 1000);  // 1s调用一次
}