$(document).ready(function () {
  const btn = $('#btn_translate');

  btn.click(function () {
    const lang = $('#language_code').val();
    console.log(lang);
    $.ajax({
      url: `https://hellosalut.stefanbohacek.dev/?lang=${lang}`,
      dataType: 'json',
      success: function (response) {
        $('#hello').text(response.hello);
      }
    });
  });
});
