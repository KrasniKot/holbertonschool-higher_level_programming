-- Lists all the cities of California

SELECT cities.id, cities.name, states.name FROM cities, states WHERE cities.state_id = states.id;