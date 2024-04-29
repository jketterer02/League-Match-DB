-- Q1: Show every Professional player and coach in the database, ordered by team
    SELECT 'Player' AS Job, Display_name AS Name, P_team_name AS Team
    FROM PLAYER
    UNION
    SELECT 'Coach' AS Job, Coach_display_name AS Name, C_Team_name AS Team
    FROM COACH
    ORDER BY Team;
    
-- Q2: Display each Team's maximum kills, deaths, and assists, as well as their average kills, deaths and assists, only if their average Kills are greater than 3.7. Sort by maximum kills in ascending order
-- Team FlyQuest should not show here as their average kills are below 3.7
    SELECT PLAYER.P_team_name AS Team, MAX(KDA.Kills) AS Maximum_Kills, MAX(KDA.Deaths) AS Maximum_Deaths, MAX(KDA.Assists) AS Maximum_Assists, 
    ROUND(AVG(KDA.Kills),1) AS Average_Kills, ROUND(AVG(KDA.Deaths),1) AS Average_Deaths, ROUND(AVG(KDA.Assists),1) AS Average_Assists
    -- Round to 1 decimal point
	FROM PLAYER
    JOIN KDA ON PLAYER.Display_name = KDA.K_player_name
	GROUP BY PLAYER.P_team_name
	HAVING AVG(KDA.Kills) > 3.7
	ORDER BY Maximum_Kills ASC;
    
-- Q3: Show every Objective name taken from Games 1,2 and 3 leave off Objective number as it is unnecessary

	SELECT O_game_number AS Game, Objective_Type as Objective, O_player_name AS Player_Name, O_team_name AS Team
	FROM OBJECTIVE;
    
-- Q4: Show the actual KDA stat from each game, for each player, and label the game they were in, ordered by game and KDA.
-- KDA = (kills + assists)/ deaths, unless deaths are 0, in which case KDA is Kills + Assists
    SELECT  KDA.K_game_number AS Game_Number, PLAYER.Display_name AS Player_Name, KDA.Kills, KDA.Assists, KDA.Deaths, 
    CASE 
        WHEN KDA.Deaths = 0 THEN ROUND(KDA.Kills + KDA.Assists,1)
        ELSE ROUND(((KDA.Kills + KDA.Assists) / KDA.Deaths),1)
        -- KDA is typically rounded to 1 decimal point
	END AS KDA
    FROM PLAYER
    JOIN KDA ON PLAYER.Display_name = KDA.K_player_name
    ORDER BY KDA.K_game_number, KDA DESC;
    
-- Q5: Display each game number, and which team won that specific game
	SELECT GAME.Game_number AS Game, Game.Winning_team_name AS Winner
    FROM GAME;
    
-- Q6: For each game, display each player and their team, and their calucated Vision Score Per Minute stat
	SELECT
    V_game_number AS Game,
    V_player_name AS Player,
    V_team_name AS Team,
    ROUND(Vision_score / Game_length_min,1) AS VSPM
	FROM VISION
	INNER JOIN GAME ON V_game_number = Game_number
    -- Have to join in order to access game length
    ORDER BY V_game_number, V_team_name, VSPM DESC;
    
    
-- Q7: Display the damage values for each player in each game
	SELECT 
		D_game_number,
		Damage_number,
		D_player_name,
		D_team_name
	FROM DAMAGE
	ORDER BY D_game_number, D_team_name, Damage_number DESC;

-- Q8: Show every player with at least 1 objective taken in a game 
	SELECT 
		O_game_number AS Game,
        COUNT(*) AS Objectives_Taken,
		O_player_name AS Player,
        O_team_name AS Team
	FROM OBJECTIVE
	GROUP BY O_game_number, O_team_name, O_player_name
	ORDER BY O_game_number, Objectives_taken DESC;

-- Q9: Show only the player(s) with the most number of objectives taken per game
	WITH count AS(
		SELECT 
			O_game_number AS Game,
			O_player_name AS Player,
            O_team_name AS Team,
			COUNT(*) AS Objectives_Taken
		FROM OBJECTIVE
		GROUP BY O_game_number, O_team_name, O_player_name
		ORDER BY O_game_number, Objectives_taken DESC
	)
    SELECT
		count.Game,
        count.Objectives_Taken,
        count.Player,
        count.Team
	FROM count
    -- Filters new tuples from list of objectives, and allows for ties
    WHERE count.Objectives_Taken =(
        SELECT MAX(current_count.Objectives_Taken)
        FROM count current_count
        WHERE current_count.Game = count.Game
        -- Compares the current count to the max count per game over all players to see if it is filtered
    );

-- Q10: Display every player with their actual position name
	SELECT
		Display_name AS Player,
        P_team_name AS Team,
        CASE Position 
        WHEN 1 THEN 'Toplane'
        WHEN 2 THEN 'Jungle'
        WHEN 3 THEN 'Midlaner'
        WHEN 4 THEN 'ADC'
        WHEN 5 THEN 'Support'
        END AS Role
	FROM PLAYER
	ORDER BY Team, Position, Display_name;
    
-- Trigger display

	SELECT Message AS DB_Insert_Timestamp FROM LOG;