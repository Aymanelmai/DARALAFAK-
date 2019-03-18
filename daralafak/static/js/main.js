$(document).ready(function(){
  $('.carousel1').owlCarousel();
  $('.owl-carousel').owlCarousel();
  var year = new Date().getFullYear();
  $('#year').html(year+'');
});
