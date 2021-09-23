var loginUrl = "../api/login/"

$("#submit").click(function() {
    let username = $("#username").val();
    let password = $("#password").val();
    let csrf_token = $("input[name='csrfmiddlewaretoken']").val();

    let response = {
        "username" : username,
        "password" : password,
        "csrf_token" : csrf_token
    }

    $.ajax({
        "url" : loginUrl,
        "type" : "post",
        "data" : response,
        "success" : function(res) {
            window.location.href = "../getCode"
        },
        "error" : function(res) {
            alert(res["msg"]);
        }
    })

})