dolt config --global --add user.email dhimes@gmail.com
dolt config --global --add user.name "dhimes"

https://www.youtube.com/watch?v=vWBEn1bfyoc

make a new repo in this folder
	dolt init
	
Build table
	dolt sql -q "create table state_populations(state varchar(14), population int, primary key(state))"
	
See tables
	dolt sql -q "show tables"
	
populate table (Not working on windows)
	dolt sql -q 'INSERT INTO state_populations (state, population)VALUES ("bob", 12)'

	dolt sql -q 'INSERT INTO state_populations (state, population)VALUES ("ted", 15)'

	
Run query
	dolt sql -q "select * from state_populations where state = 'ted'"
	
Commit/save data (git ishly)
	dolt add .
	dolt commit -m "Added shit populations"

See if changes have been made
	 dolt status
