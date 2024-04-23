-- completely changed my queries as my original database was too complicated to be implemented

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
    
-- Q3: Show every Objective name taken from Games 1 and 2, leave off Objective number and Team as they are unnecessary

	SELECT O_game_number AS Game, Objective_Type as Objective, O_player_name AS Player_Name
	FROM OBJECTIVE
	WHERE O_game_number = 1 ||O_game_number = 2;
    
-- Q4: Show the actual KDA stat from each game, for each player, and label the game they were in, ordered by game.
-- KDA = (kills + assists)/ deaths, unless deaths are 0, in which case KDA is Kills + Assists
    SELECT  KDA.K_game_number AS Game_Number, PLAYER.Display_name AS Player_Name, KDA.Kills, KDA.Assists, KDA.Deaths, 
    CASE 
        WHEN KDA.Deaths = 0 THEN ROUND(KDA.Kills + KDA.Assists,1)
        ELSE ROUND(((KDA.Kills + KDA.Assists) / KDA.Deaths),1)
        -- KDA is typically rounded to 1 decimal point
	END AS KDA
    FROM PLAYER
    JOIN KDA ON PLAYER.Display_name = KDA.K_player_name
    ORDER BY KDA.K_game_number;
    
-- Q5: Display each game number, and which team won that specific game

	SELECT GAME.Game_number AS Game, Game.Winning_team_name AS Winner
    FROM GAME
