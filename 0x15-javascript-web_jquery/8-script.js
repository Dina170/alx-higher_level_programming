$.get('https://swapi.co/api/films/?format=json', (data) => {
  data.results.forEach((result) => {
    $('UL#list_movies').append($('<li></li>').text(result.title));
  });
});
