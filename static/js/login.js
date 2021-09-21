var loginUrl = "http://127.0.0.1/api/login/"

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
        
    })

})