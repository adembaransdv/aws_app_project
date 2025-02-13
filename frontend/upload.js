function uploadImage() {
    let fileInput = document.getElementById("fileInput").files[0];
    let formData = new FormData();
    formData.append("file", fileInput);

    fetch("http://44.211.225.249:5000/upload", {
        method: "POST",
        body: formData
    }).then(response => response.json())
      .then(data => alert(data.message));
}