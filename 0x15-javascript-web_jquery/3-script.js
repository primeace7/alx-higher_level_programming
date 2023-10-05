// adds the class red to the <header> element when the user clicks on the tag DIV#red_header
const change = $('#red_header');
change.on('click', function () {
  $('header').addClass('red');
});
