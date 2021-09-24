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

// 登录块
$(function () {

  $(".btn1").click(function () {
    var usernameText = $("#username").val();
    var usernamePat = /^[0-9]{10}$/;
    if (usernameText == "") {
      $(".errorMsg").text("请输入用户名！");
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
      $(".errorMsg").text("请输入密码！");
      $("#password").css("border-color", "red");
      return false;
    } else {
      $("#password").css("border-color", "aquamarine");
    }

    $(".errorMsg").text("");
    $.ajax({
      method: 'post',
      url: loginUrl,
      data: {
        username: $("input#username").val(),
        password: $("input#password").val(),
        csrf_token: $("input[name='csrfmiddlewaretoken']").val()
      },
      success: function() {
        $.ajax({
          method: 'post',
          url: '../api/getuserinfo/'
        })
        $.ajax({
          method: 'post',
          url: '../api/getrecord/'
        })
        $.ajax({
          method: 'post',
          url: '../api/getall/'
        })
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
      $(".errorMsg2").text("请输入用户名！");
      $("#StuID").css("border-color", "red");
      return false;
    } else if (!studentIDPat.test(studentID)) {
      $(".errorMsg2").text("学号命名不合法");
      $("#StuID").css("border-color", "red");
      return false;
    } else {
      $("#StuID").css("border-color", "aquamarine");
    }
    $(".errorMsg2").text("");
    $.ajax({
      method: 'POST',
      url: checkUsernameUrl,
      data: {
        username: $("input#StuID").val(),
        csrf_token: $("input[name='csrfmiddlewaretoken']").val()
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
      $(".errorMsg2").text("请输入姓名！");
      $("#Username").css("border-color", "red");
      return false;
    } else if (!studentNamePat.test(studentName)) {
      $(".errorMsg2").text("姓名不合法");
      $("#Username").css("border-color", "red");
      return false;
    } else {
      $("#Username").css("border-color", "aquamarine");
    }
    $(".errorMsg2").text("");
  })

  // 邮箱检查
  $("#Email").blur(function () {
    var email = $("#Email").val();
    var emailPat = /^\w+@[a-zA-Z0-9]{2,10}(?:\.[a-z]{2,4}){1,3}$/;
    if (email == "") {
      $(".errorMsg2").text("请输入邮箱！");
      $("#Email").css("border-color", "red");
      return false;
    } else if (!emailPat.test(email)) {
      $(".errorMsg2").text("邮箱地址不合法");
      $("#Email").css("border-color", "red");
      return false;
    } else {
      $("#Email").css("border-color", "aquamarine");
    }
    $(".errorMsg2").text("");
  })

  // 密码检查
  $("#Password").blur(function () {
    var Password = $("#Password").val();
    var PasswordPat = /^\w+$/;
    if (Password == "") {
      $(".errorMsg2").text("请输入密码！");
      $("#Password").css("border-color", "red");
      return false;
    } else if (!PasswordPat.test(Password)) {
      $(".errorMsg2").text("密码不合法");
      $("#Password").css("border-color", "red");
      return false;
    } else {
      $("#Password").css("border-color", "aquamarine");
    }
    $(".errorMsg2").text("");
  })

  // 密码重复检查
  $("#Password2").blur(function () {
    var Password = $("#Password").val();
    var repassword = $("#Password2").val();
    if (repassword == "") {
      $(".errorMsg2").text("请输入密码！");
      $("#Password2").css("border-color", "red");
      return false;
    } else if (repassword != Password) {
      $(".errorMsg2").text("两次密码不相同！");
      $("#Password2").css("border-color", "red");
      return false;
    } else {
      $("#Password2").css("border-color", "aquamarine");
    }
    $(".errorMsg2").text("");
  })

  $("#EnqueueTime").blur(function () {
    var date = $("#EnqueueTime").val();
    if (date == "") {
      $(".errorMsg2").text("请选择时间！");
      $("#EnqueueTime").css("border-color", "red");
      return false;
    } else {
      $("#EnqueueTime").css("border-color", "aquamarine");
    }
    $(".errorMsg2").text("");
  })


  // 注册
  $(".btn2").click(function () {
    var verification = $("#yan").val();
    if (verification == "") {
      $(".errorMsg2").text("请输入验证码");
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
          // admin : false, -> boolean
          adminVerify: "",
          csrf_token: $("input[name='csrfmiddlewaretoken']").val()
        }
      })
      // .then(response => {
      //   console.log(response);
      // })

      $(".errorMsg2").text("");
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
      $(".errorMsg2").text("请输入邮箱！");
      $("#Email").css("border-color", "red");
      btnget.disabled = false;
      return false;
    } else if (!emailPat.test(email)) {
      $(".errorMsg2").text("邮箱地址不合法");
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
        }
      })
      // .then(response => {
      //   console.log(response);
      // })
    }
    $(".errorMsg2").text("");
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
