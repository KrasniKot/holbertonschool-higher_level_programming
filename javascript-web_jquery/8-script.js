$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: function(result){
    for (result of result.results) { $('#list_movies').append(`<li>${result.title}</li>`); };
  }
});
