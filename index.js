function search() {
    var vin = document.getElementById("vinInput").value;
    var url = "http://localhost:5000/get-info?vin=" + vin;

    fetch(url)
      .then(response => response.json())
      .then(data => {
        if (data.error) {
          document.getElementById("carData").innerHTML = "<h1 class='error'>" + data.error + "</h1>";
        } else {
          var carData = data.cardata;
          var carInfo = "<h1>" + carData.make + " " + carData.model + "</h1>";

          // Display car specs
          carInfo += "<ul>";
          for (var key in carData.specs) {
            carInfo += "<li><strong>" + key.replace(/_/g, ' ') + ":</strong> " + carData.specs[key] + "</li>";
          }
          carInfo += "</ul>";

          // Display car photos
          var photos = data.photos;
          for (var i = 0; i < Math.min(photos.length, 10); i++) {
            carInfo += "<img src='" + photos[i] + "'>";
          }

          document.getElementById("carData").innerHTML = carInfo;
        }
      })
      .catch(error => console.log("Error:", error));
  }
