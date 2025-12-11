const generate_button = document.getElementById("qr-code-btn")
const qr_image = document.getElementById("qr-code-image")

generate_button.addEventListener("click", function(){
    const url_link = document.getElementById("url-input").value

    if(!url_link){
        alert("Please enter URL")
        return
    }

    fetch("http://127.0.0.1:8000/generate_qr",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body: JSON.stringify({url:url_link})
    })
    .then(response => response.blob())
    .then(blob => {
        const imageURL = URL.createObjectURL(blob)
        qr_image.src = imageURL
        qr_image.style.display = 'block';
    })
    .catch(error => {
        console.error('Error:', error);
        alert("Error generating QR code");
    });
})