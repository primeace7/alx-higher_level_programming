/* fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello
*/
$(document).on('load', function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr',
    function (data) {
      $('#hello').html(data.hello);
    },
    'json'
  );
}
);
