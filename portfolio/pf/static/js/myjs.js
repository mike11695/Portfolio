//Credit to W3Schools for the guide on creating an image slideshow
//https://www.w3schools.com/howto/howto_js_slideshow.asp

$(document).ready(function() {
  console.log("Yeet");

  var curImage = 1;
  displayImg(curImage);

  //Go to next image to right or left
  document.getElementById("left-arrow-btn").addEventListener("click", imageScrollLeft, false);
  document.getElementById("right-arrow-btn").addEventListener("click", imageScrollRight, false);

  function imageScrollLeft() {
    displayImg(curImage -= 1);
  }

  function imageScrollRight() {
    displayImg(curImage += 1);
  }

  //Display the current image
  function currentImage(n) {
    displayImg(curImage = n);
  }

  function displayImg(n) {
    var i;
    var images = document.getElementsByClassName('ind-project-img');
    var actualImages = document.getElementsByClassName('listit-img');
    var circles = document.getElementsByClassName('circ');

    if (n > images.length) {
      curImage = 1;
    }

    if (n < 1) {
      curImage = images.length;
    }

    for (i = 0; i < images.length; i++) {
        images[i].style.display = "none";
    }

    for (i = 0; i < circles.length; i++) {
        circles[i].className = circles[i].className.replace("active-circ", "");
    }

    images[curImage-1].style.display = "inline-block";
    images[curImage-1].style.margin = "0px -20px 0px -20px";
    images[curImage-1].style.zindex = "-1";
    actualImages[curImage-1].style.width = "90%";
    actualImages[curImage-1].style.height = "80%";
    circles[curImage-1].className += "fas fa-circle circ active-circ";
  }
});
