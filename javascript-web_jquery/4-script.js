$('#toggle_header').click(function () {
  if ($('header .green')) {
    $('header').replaceClass('green', 'red');
  } else {
    $('header').replaceClass('red', 'green');
  }
});
