// fetches and prints how to say “Hello” depending on the language
$(document).ready(() => {
  $('input#btn_translate').on('click', () => {
    $.get('http://stefanbohacek.com/hellosalut', { lang: $('input#language_code').val() },
      function (returnVal) {
        $('div#hello').text(returnVal);
      }
    );
  });
  $('input#btn_translate').on('keydown', (event) => {
    if (event.which === 13) {
      $.get('http://stefanbohacek.com/hellosalut', { lang: $('input#language_code').val() },
        function (returnVal) {
          $('div#hello').text(returnVal);
        }
      );
    }
  });
}
);
