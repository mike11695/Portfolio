//Credit to W3Schools for the guide on creating an image slideshow
//https://www.w3schools.com/howto/howto_js_slideshow.asp

$(document).ready(function() {
  var curImageLI = 1;
  displayImgLI(curImageLI);

  //Go to next image to right or left
  document.getElementById("left-arrow-btn-li").addEventListener("click", imageScrollLeftLI, false);
  document.getElementById("right-arrow-btn-li").addEventListener("click", imageScrollRightLI, false);

  function imageScrollLeftLI() {
    displayImgLI(curImageLI -= 1);
  }

  function imageScrollRightLI() {
    displayImgLI(curImageLI += 1);
  }

  //Display the current image
  function currentImageLI(n) {
    displayImgLI(curImageLI = n);
  }

  function displayImgLI(n) {
    var i;
    var images = document.getElementsByClassName('ind-project-img-li');
    var actualImages = document.getElementsByClassName('listit-img');
    var circles = document.getElementsByClassName('circ-li');

    if (n > images.length) {
      curImageLI = 1;
    }

    if (n < 1) {
      curImageLI = images.length;
    }

    for (i = 0; i < images.length; i++) {
        images[i].style.display = "none";
    }

    for (i = 0; i < circles.length; i++) {
        circles[i].className = circles[i].className.replace("active-circ", "");
    }

    images[curImageLI-1].style.display = "inline-block";
    images[curImageLI-1].style.margin = "0px -20px 0px -20px";
    images[curImageLI-1].style.zindex = "-1";
    actualImages[curImageLI-1].style.width = "90%";
    actualImages[curImageLI-1].style.height = "80%";
    circles[curImageLI-1].className += "fas fa-circle circ-li active-circ";
  }

  //PetTP image slideshow functions
  var curImagePT = 1;
  displayImgPT(curImagePT);

  //Go to next image to right or left
  document.getElementById("left-arrow-btn-pt").addEventListener("click", imageScrollLeftPT, false);
  document.getElementById("right-arrow-btn-pt").addEventListener("click", imageScrollRightPT, false);

  function imageScrollLeftPT() {
    displayImgPT(curImagePT -= 1);
  }

  function imageScrollRightPT() {
    displayImgPT(curImagePT += 1);
  }

  //Display the current image
  function currentImagePT(n) {
    displayImgPT(curImagePT = n);
  }

  function displayImgPT(n) {
    var i;
    var images = document.getElementsByClassName('ind-project-img-pt');
    var actualImages = document.getElementsByClassName('pettp-img');
    var circles = document.getElementsByClassName('circ-pt');

    if (n > images.length) {
      curImagePT = 1;
    }

    if (n < 1) {
      curImagePT = images.length;
    }

    for (i = 0; i < images.length; i++) {
        images[i].style.display = "none";
    }

    for (i = 0; i < circles.length; i++) {
        circles[i].className = circles[i].className.replace("active-circ", "");
    }

    images[curImagePT-1].style.display = "inline-block";
    images[curImagePT-1].style.margin = "0px -20px 0px -20px";
    images[curImagePT-1].style.zindex = "-1";
    actualImages[curImagePT-1].style.width = "90%";
    actualImages[curImagePT-1].style.height = "80%";
    circles[curImagePT-1].className += "fas fa-circle circ-pt active-circ";
  }
});
