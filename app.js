const forma = document.getElementById("form-id")
const submitBtn = document.getElementById("btn-id")
//waiting for submit button to be pressed
forma.addEventListener("submit", function (event){
    event.preventDefault()
    //getting values from form
    var user_name = document.getElementById("name-id").value
    var user_email = document.getElementById("email-id").value
    var user_password = document.getElementById("password-id").value
    //creating js object with these values
    var person = {
        username:user_name,
        email:user_email,
        password:user_password
    }
    //fetch the data
    fetch("http://127.0.0.1:8000/register",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify(person)
    })
    
    //handling the result
    .then(response => response.json())
    .then(data => {
        if (data.success === true){
            window.location.href = "login.html"
        }
        else{
            alert("That account already exists!")   
        }
    })
    .catch(error => {
        console.error("Network error!");
    } )
})

