const login_btn = document.getElementById("sign-up-btn")
login_btn.addEventListener("click", function(){
    var userEmail = document.getElementById("login-email").value
    var userPassword = document.getElementById("login-password").value

    if (!userEmail || !userPassword){
        alert("This can't be empty!")
    }
    var user = {
        email:userEmail,
        password: userPassword
    }
    console.log(user)

    fetch("http://127.0.0.1:8000/login", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(user)
})
    .then(response => response.json())
    .then(data => {
        if (data.success === true){
            window.location.href = "qr.html"
        }
        else{
            alert("Wrong password or username")   
        }
    })
    .catch(error => {
        console.error("Network error!", error);
    })


})