// updates the text color of the <header> element to red
/* Method 1
$('#red_header').on('click', function(){
    $('header').css('color', 'red');
});
*/

// Method2
const change = $('#red_header');
change.on('click', function () {
  $('header').css('color', 'red');
});
