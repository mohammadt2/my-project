$(document).ready(function () {

  // PopUp For Image
  $(".info-icon").on("click", function () {
    $(".popup").addClass("open-popup");
    $(".close-overlay").addClass("open-popup");
  });

  $(".close-overlay").on("click", function () {
    $(".popup").removeClass("open-popup");
    $(this).removeClass("open-popup");
  });

  // // PopUp For Pagination
  // $(".open-popup-pagination").on("click", function () {
  //   $(".popup-pagination").addClass("open-popup");
  //   $(".close-overlay").addClass("open-popup");
  // });

  // $(".close-overlay, .close-popup-pagination").on("click", function () {
  //   $(".popup-pagination").removeClass("open-popup");
  //   $(".close-overlay").removeClass("open-popup");
  // });

  // Get Date Of Now And Print It In Html
  var today = new Date();
  var dd = today.getDate();

  var mm = today.getMonth() + 1;
  var yyyy = today.getFullYear();
  if (dd < 10) {
    dd = "0" + dd;
  }

  if (mm < 10) {
    mm = "0" + mm;
  }
  today = dd + "/" + mm + "/" + yyyy;

  $(".date-of-now").text(today);
});
