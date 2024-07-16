import mysql.connector
import pandas

# Connect to the MySQL database
conn = mysql.connector.connect(host="localhost", user="root", password="password",ssl_disabled=True)

# Check if connection is established to the database
if conn.is_connected(): print("Connection to MySQL established...\n")

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Creates DB with same lines as dbDLL.sql, formatting needs to be different due to mysql connector
create_statements = [
    "CREATE DATABASE match_database;",
    "USE match_database;",
    "CREATE TABLE TEAM (Team_name VARCHAR(20) NOT NULL, PRIMARY KEY (Team_name));",
    "CREATE TABLE COACH (Coach_display_name VARCHAR(20) NOT NULL, C_Team_name VARCHAR(20) NOT NULL, PRIMARY KEY (Coach_display_name), FOREIGN KEY (C_Team_name) REFERENCES TEAM(Team_name));",
    "CREATE TABLE PLAYER (Display_name VARCHAR(20) NOT NULL, P_team_name VARCHAR(20) NOT NULL, Position INT NOT NULL CHECK (Position >= 0 AND Position <= 6), PRIMARY KEY (Display_name), FOREIGN KEY (P_team_name) REFERENCES TEAM(Team_name));",
    "CREATE TABLE GAME (Game_number INT NOT NULL, Game_length_min FLOAT NOT NULL, Red_team_name VARCHAR(20) NOT NULL, Blue_team_name VARCHAR(20) NOT NULL, Winning_team_name VARCHAR(20) NOT NULL, PRIMARY KEY (Game_number), FOREIGN KEY (Red_team_name) REFERENCES TEAM(Team_name), FOREIGN KEY (Blue_team_name) REFERENCES TEAM(Team_name));",
    "CREATE TABLE OBJECTIVE (Objective_number INT NOT NULL, O_game_number INT NOT NULL, Objective_type VARCHAR(20) NOT NULL, O_team_name VARCHAR(20) NOT NULL, O_player_name VARCHAR(20) NOT NULL, PRIMARY KEY (O_game_number, Objective_number), FOREIGN KEY (O_team_name) REFERENCES TEAM(Team_name), FOREIGN KEY (O_player_name) REFERENCES PLAYER(Display_name), FOREIGN KEY (O_game_number) REFERENCES GAME(Game_number));",
    "CREATE TABLE DAMAGE (Damage_number INT NOT NULL, D_game_number INT NOT NULL, D_team_name VARCHAR(20) NOT NULL, D_player_name VARCHAR(20) NOT NULL, PRIMARY KEY (D_game_number, D_player_name), FOREIGN KEY (D_team_name) REFERENCES TEAM(Team_name), FOREIGN KEY (D_player_name) REFERENCES PLAYER(Display_name), FOREIGN KEY (D_game_number) REFERENCES GAME(Game_number));",
    "CREATE TABLE Vision (Vision_score INT NOT NULL, V_game_number INT NOT NULL, V_team_name VARCHAR(20) NOT NULL, V_player_name VARCHAR(20) NOT NULL, PRIMARY KEY (V_game_number, V_player_name), FOREIGN KEY (V_team_name) REFERENCES TEAM(Team_name), FOREIGN KEY (V_player_name) REFERENCES PLAYER(Display_name), FOREIGN KEY (V_game_number) REFERENCES GAME(Game_number));",
    "CREATE TABLE KDA (Kills INT NOT NULL, Deaths INT NOT NULL, Assists INT NOT NULL, K_game_number INT NOT NULL, K_team_name VARCHAR(20) NOT NULL, K_player_name VARCHAR(20) NOT NULL, PRIMARY KEY (K_game_number, K_player_name), FOREIGN KEY (K_team_name) REFERENCES TEAM(Team_name), FOREIGN KEY (K_player_name) REFERENCES PLAYER(Display_name), FOREIGN KEY (K_game_number) REFERENCES GAME(Game_number));",
    "CREATE TABLE LOG (LogID INT AUTO_INCREMENT PRIMARY KEY, Message VARCHAR(100));",
    "CREATE TRIGGER PlayerInserted AFTER INSERT ON PLAYER FOR EACH ROW BEGIN DECLARE log_message VARCHAR(100); SET log_message = CONCAT('Player: ', NEW.Display_name, ' inserted at ', DATE_FORMAT(NOW(), '%Y-%m-%d %H:%i:%s')); INSERT INTO Log (Message) VALUES (log_message); END;"
]
        
# Execute each SQL command
for line in create_statements: cursor.execute(line)

# Populates DB with same lines as dbDML.sql, formatting needs to be different due to mysql connector
populate_statements = [

    #Select match_database
    "USE match_database;",

    #Inserting players/teams

    "INSERT INTO TEAM values('Cloud9');",
    "INSERT INTO COACH values('Mithy','Cloud9');",
    "INSERT INTO PLAYER values('Fudge','Cloud9',1);",
    "INSERT INTO PLAYER values('Blaber','Cloud9',2);",
    "INSERT INTO PLAYER values('Jojopyun','Cloud9',3);",
    "INSERT INTO PLAYER values('Berserker','Cloud9',4);",
    "INSERT INTO PLAYER values('VULCAN','Cloud9',5);",

    "INSERT INTO TEAM values('T1');",
    "INSERT INTO COACH values('KkOma','T1');",
    "INSERT INTO PLAYER values('Zeus','T1',1);",
    "INSERT INTO PLAYER values('Oner','T1',2);",
    "INSERT INTO PLAYER values('Faker','T1',3);",
    "INSERT INTO PLAYER values('Gumayusi','T1',4);",
    "INSERT INTO PLAYER values('Keria','T1',5);",

    "INSERT INTO TEAM values('G2');",
    "INSERT INTO COACH values('Dylan Falco','G2');",
    "INSERT INTO PLAYER values('BrokenBlade','G2',1);",
    "INSERT INTO PLAYER values('Yike','G2',2);",
    "INSERT INTO PLAYER values('Caps','G2',3);",
    "INSERT INTO PLAYER values('Hans Sama','G2',4);",
    "INSERT INTO PLAYER values('Mikyx','G2',5);",

    #Sleep necessary to display timestamp differences in LOG when triggered
    "DO SLEEP(2);",

    "INSERT INTO TEAM values('FlyQuest');",
    "INSERT INTO COACH values('Nukeduck','FlyQuest');",
    "INSERT INTO PLAYER values('Bwipo','FlyQuest',1);",
    "INSERT INTO PLAYER values('Inspired','FlyQuest',2);",
    "INSERT INTO PLAYER values('Jensen','FlyQuest',3);",
    "INSERT INTO PLAYER values('Massu','FlyQuest',4);",
    "INSERT INTO PLAYER values('Busio','FlyQuest',5);",

    "INSERT INTO TEAM values('Fnatic');",
    "INSERT INTO COACH values('Nightshare','Fnatic');",
    "INSERT INTO PLAYER values('Oscarinin','Fnatic',1);",
    "INSERT INTO PLAYER values('Razork','Fnatic',2);",
    "INSERT INTO PLAYER values('Humanoid','Fnatic',3);",
    "INSERT INTO PLAYER values('Noah','Fnatic',4);",
    "INSERT INTO PLAYER values('Jun','Fnatic',5);",

    #Populating with Games

    "INSERT INTO GAME values(1,45,'Fnatic','Flyquest','FlyQuest');",
    "INSERT INTO GAME values(2,55,'T1','G2','T1');",
    "INSERT INTO GAME values(3,55,'Cloud9','G2','Cloud9');",
    "INSERT INTO GAME values(4,55,'T1','Cloud9','T1');",
    "INSERT INTO GAME values(5,55,'Flyquest','G2','G2');",

    #Populating with Objectives for Game 1

    "INSERT INTO OBJECTIVE values(0,1,'Infernal Dragon','Flyquest','Bwipo');",
    "INSERT INTO OBJECTIVE values(1,1,'Cloud Dragon','Fnatic','Razork');",
    "INSERT INTO OBJECTIVE values(2,1,'Mountain Dragon','Fnatic','Razork');",
    "INSERT INTO OBJECTIVE values(3,1,'Mountain Dragon','FlyQuest','Inspired');",
    "INSERT INTO OBJECTIVE values(4,1,'Elder Dragon','Fnatic','Razork');",
    "INSERT INTO OBJECTIVE values(5,1,'Inhibitor','Flyquest','Inspired');",
    "INSERT INTO OBJECTIVE values(6,1,'Inhibitor','Flyquest','Bwipo');",
    "INSERT INTO OBJECTIVE values(7,1,'Inhibitor','Flyquest','Jensen');",
    "INSERT INTO OBJECTIVE values(8,1,'Nexus','Flyquest','Inspired');",

    #Populating with Objectives for Game 2

    "INSERT INTO OBJECTIVE values(0,2,'Void Grub','T1','Zeus');",
    "INSERT INTO OBJECTIVE values(1,2,'Void Grub','G2','Yike');",
    "INSERT INTO OBJECTIVE values(2,2,'Void Grub','G2','Caps');",
    "INSERT INTO OBJECTIVE values(3,2,'Mountain Dragon','G2','BrokenBlade');",
    "INSERT INTO OBJECTIVE values(4,2,'Ocean Dragon','T1','Faker');",
    "INSERT INTO OBJECTIVE values(5,2,'Hextech Dragon','T1','Faker');",
    "INSERT INTO OBJECTIVE values(6,2,'Hextech Dragon','T1','Oner');",
    "INSERT INTO OBJECTIVE values(7,2,'Elder Dragon','T1','Oner');",
    "INSERT INTO OBJECTIVE values(8,2,'Baron','T1','Oner');",
    "INSERT INTO OBJECTIVE values(9,2,'Inhibitor','T1','Oner');",
    "INSERT INTO OBJECTIVE values(10,2,'Inhibitor','G2','Yike');",
    "INSERT INTO OBJECTIVE values(11,2,'Nexus','T1','Zeus');",

    #Populating with Objectives for Game 3

    "INSERT INTO OBJECTIVE values(0,3,'Void Grub','Cloud9','Blaber');",
    "INSERT INTO OBJECTIVE values(1,3,'Void Grub','G2','Yike');",
    "INSERT INTO OBJECTIVE values(2,3,'Void Grub','G2','Caps');",
    "INSERT INTO OBJECTIVE values(3,3,'Ocean Dragon','Cloud9','Fudge');",
    "INSERT INTO OBJECTIVE values(4,3,'Mountain Dragon','G2','BrokenBlade');",
    "INSERT INTO OBJECTIVE values(5,3,'Hextech Dragon','Cloud9','Blaber');",
    "INSERT INTO OBJECTIVE values(6,3,'Hextech Dragon','Cloud9','Blaber');",
    "INSERT INTO OBJECTIVE values(7,3,'Rift Herald','Cloud9','Blaber');",
    "INSERT INTO OBJECTIVE values(8,3,'Baron','Cloud9','Jojopyun');",
    "INSERT INTO OBJECTIVE values(9,3,'Inhibitor','Cloud9','Blaber');",
    "INSERT INTO OBJECTIVE values(10,3,'Elder Dragon','Cloud9','Berserker');",
    "INSERT INTO OBJECTIVE values(11,3,'Inhibitor','Cloud9','Berserker');",
    "INSERT INTO OBJECTIVE values(12,3,'Nexus','Cloud9','VULCAN');",

    #Populating with Damage numbers for Game 1

    "INSERT INTO DAMAGE values(100000,1,'Flyquest','Bwipo');",
    "INSERT INTO DAMAGE values(23576,1,'Flyquest','Busio');",
    "INSERT INTO DAMAGE values(12378,1,'Flyquest','Inspired');",
    "INSERT INTO DAMAGE values(9876,1,'Flyquest','Jensen');",
    "INSERT INTO DAMAGE values(15635,1,'Flyquest','Massu');",

    "INSERT INTO DAMAGE values(10000,1,'Fnatic','Razork');",
    "INSERT INTO DAMAGE values(54321,1,'Fnatic','Noah');",
    "INSERT INTO DAMAGE values(9234,1,'Fnatic','JUN');",
    "INSERT INTO DAMAGE values(6089,1,'Fnatic','Oscarinin');",
    "INSERT INTO DAMAGE values(5367,1,'Fnatic','Humanoid');",

    #Populating with Damage numbers for Game 2

    "INSERT INTO DAMAGE values(15000,2,'T1','Zeus');",
    "INSERT INTO DAMAGE values(12967,2,'T1','Oner');",
    "INSERT INTO DAMAGE values(12341,2,'T1','Faker');",
    "INSERT INTO DAMAGE values(31415,2,'T1','Gumayusi');",
    "INSERT INTO DAMAGE values(10023,2,'T1','Keria');",

    "INSERT INTO DAMAGE values(15000,2,'G2','BrokenBlade');",
    "INSERT INTO DAMAGE values(12967,2,'G2','Yike');",
    "INSERT INTO DAMAGE values(12341,2,'G2','Caps');",
    "INSERT INTO DAMAGE values(2115,2,'G2','Hans Sama');",
    "INSERT INTO DAMAGE values(14323,2,'G2','Mikyx');",

    #Populating with Damage numbers for Game 3

    "INSERT INTO DAMAGE values(13020,3,'G2','BrokenBlade');",
    "INSERT INTO DAMAGE values(11608,3,'G2','Yike');",
    "INSERT INTO DAMAGE values(8941,3,'G2','Caps');",
    "INSERT INTO DAMAGE values(6115,3,'G2','Hans Sama');",
    "INSERT INTO DAMAGE values(12999,3,'G2','Mikyx');",

    "INSERT INTO DAMAGE values(15000,3,'Cloud9','Fudge');",
    "INSERT INTO DAMAGE values(12967,3,'Cloud9','Blaber');",
    "INSERT INTO DAMAGE values(2115,3,'Cloud9','Jojopyun');",
    "INSERT INTO DAMAGE values(12341,3,'Cloud9','Berserker');",
    "INSERT INTO DAMAGE values(14323,3,'Cloud9','VULCAN');",

    #Populating with Vision Score for Game 1

    "INSERT INTO VISION values(25,1,'Flyquest','Bwipo');",
    "INSERT INTO VISION values(52,1,'Flyquest','Busio');",
    "INSERT INTO VISION values(11,1,'Flyquest','Inspired');",
    "INSERT INTO VISION values(16,1,'Flyquest','Jensen');",
    "INSERT INTO VISION values(21,1,'Flyquest','Massu');",

    "INSERT INTO VISION values(10,1,'Fnatic','Razork');",
    "INSERT INTO VISION values(7,1,'Fnatic','Noah');",
    "INSERT INTO VISION values(8,1,'Fnatic','JUN');",
    "INSERT INTO VISION values(19,1,'Fnatic','Oscarinin');",
    "INSERT INTO VISION values(20,1,'Fnatic','Humanoid');",

    #Populating with Vision Score for Game 2

    "INSERT INTO VISION values(21,2,'T1','Zeus');",
    "INSERT INTO VISION values(26,2,'T1','Oner');",
    "INSERT INTO VISION values(34,2,'T1','Faker');",
    "INSERT INTO VISION values(42,2,'T1','Gumayusi');",
    "INSERT INTO VISION values(16,2,'T1','Keria');",

    "INSERT INTO VISION values(14,2,'G2','BrokenBlade');",
    "INSERT INTO VISION values(16,2,'G2','Yike');",
    "INSERT INTO VISION values(4,2,'G2','Caps');",
    "INSERT INTO VISION values(7,2,'G2','Hans Sama');",
    "INSERT INTO VISION values(34,2,'G2','Mikyx');",

    #Populating with Vision Score for Game 3

    "INSERT INTO VISION values(68,3,'G2','BrokenBlade');",
    "INSERT INTO VISION values(34,3,'G2','Yike');",
    "INSERT INTO VISION values(15,3,'G2','Caps');",
    "INSERT INTO VISION values(20,3,'G2','Hans Sama');",
    "INSERT INTO VISION values(21,3,'G2','Mikyx');",

    "INSERT INTO VISION values(46,3,'Cloud9','Fudge');",
    "INSERT INTO VISION values(52,3,'Cloud9','Blaber');",
    "INSERT INTO VISION values(25,3,'Cloud9','Jojopyun');",
    "INSERT INTO VISION values(35,3,'Cloud9','Berserker');",
    "INSERT INTO VISION values(30,3,'Cloud9','VULCAN');",

    #Populating with KDA for Game 1

    "INSERT INTO KDA values(1,1,23,1,'Fnatic','JUN');",
    "INSERT INTO KDA values(13,2,0,1,'Fnatic','Noah');",
    "INSERT INTO KDA values(0,2,0,1,'Fnatic','Razork');",
    "INSERT INTO KDA values(5,5,5,1,'Fnatic','Humanoid');",
    "INSERT INTO KDA values(0,6,12,1,'Fnatic','Oscarinin');",

    "INSERT INTO KDA values(1,6,14,1,'Flyquest','Bwipo');",
    "INSERT INTO KDA values(11,6,0,1,'Flyquest','Jensen');",
    "INSERT INTO KDA values(3,1,4,1,'Flyquest','Inspired');",
    "INSERT INTO KDA values(0,0,30,1,'Flyquest','Massu');",
    "INSERT INTO KDA values(3,1,3,1,'Flyquest','Busio');",

    #Populating with KDA for Game 2

    "INSERT INTO KDA values(23,0,5,2,'T1','Zeus');",
    "INSERT INTO KDA values(0,11,15,2,'T1','Oner');",
    "INSERT INTO KDA values(2,1,1,2,'T1','Faker');",
    "INSERT INTO KDA values(3,1,4,2,'T1','Gumayusi');",
    "INSERT INTO KDA values(4,5,6,2,'T1','Keria');",

    "INSERT INTO KDA values(0,19,5,2,'G2','BrokenBlade');",
    "INSERT INTO KDA values(2,4,6,2,'G2','Yike');",
    "INSERT INTO KDA values(0,1,2,2,'G2','Caps');",
    "INSERT INTO KDA values(24,0,13,2,'G2','Hans Sama');",
    "INSERT INTO KDA values(5,2,1,2,'G2','Mikyx');",

    #Populating with KDA for Game 3

    "INSERT INTO KDA values(2,10,7,3,'G2','BrokenBlade');",
    "INSERT INTO KDA values(4,6,2,3,'G2','Yike');",
    "INSERT INTO KDA values(2,0,1,3,'G2','Caps');",
    "INSERT INTO KDA values(9,11,6,3,'G2','Hans Sama');",
    "INSERT INTO KDA values(2,1,5,3,'G2','Mikyx');",

    "INSERT INTO KDA values(10,0,0,3,'Cloud9','Fudge');",
    "INSERT INTO KDA values(0,5,15,3,'Cloud9','Blaber');",
    "INSERT INTO KDA values(14,7,3,3,'Cloud9','Jojopyun');",
    "INSERT INTO KDA values(6,6,6,3,'Cloud9','Berserker');",
    "INSERT INTO KDA values(2,0,2,3,'Cloud9','VULCAN');"

]

# Execute each SQL command
for line in populate_statements: cursor.execute(line)

# Commit the transaction
conn.commit()

# Executes the SQL Query and prints the resulting table
def execute_and_display_func(SQL_Query):
    print("\n")
    cursor.execute(SQL_Query)
    # Get the row numbers
    rows = cursor.fetchall()
    # Get the column names
    columns = [desc[0] for desc in cursor.description]
    # Create the DataFrame
    df = pandas.DataFrame(rows, columns=columns)
    # Prints the Dataframe
    print(df.to_string(index=False,))
    print("\n")

# Drops the DB and closes the connection
def cleanup():
    # Creates DB with same lines as dbDROP.sql, formatting needs to be different due to mysql connector
    drop_statements = [
    "DROP TRIGGER  PlayerInserted;",
    "drop table KDA;",
    "drop table VISION;",
    "drop table DAMAGE;",
    "drop table OBJECTIVE;",
    "drop table GAME;",
    "drop table PLAYER;",
    "drop table COACH;",
    "drop table TEAM;",
    "DROP DATABASE match_database;"
    ]

    # Execute each SQL command
    for line in drop_statements: cursor.execute(line)

    # Commit the transaction
    conn.commit()

    # Close the cursor
    cursor.close()

    # Close the connection
    conn.close()
    # Exit Program
    quit("Exiting Program")
    

# Command Line Interface
while(1==1):
    # Prints options for user after every Query chosen
    print("Please select an SQL Query to display:")
    print("1: Display every player and coach, ordered by team")
    print("2: Display each team's maximum kills, deaths, and assists, average kills, deaths and assists, only if average kills > 3.7, sorted by maximum kills in ascending order")
    print("3: Show every Objective taken from Games 1, 2, and 3 along with the player that took them")
    print("4: Display each player's calculated KDA stat and the game they were in, ordered by game and KDA in descending order")
    print("5: Display the winning team of each game")
    print("6: For each game, display each player and their team, and their caclulated vision score per minute stat")
    print("7: Display players and their associated damage values and teams for each game")
    print("8: Show every player with at least one objective taken for each game")
    print("9: Show only the player(s) with the most number of objectives taken per game")
    print("10: Display every player with their team and actual game position")
    # Gets user input for which query to display
    choice = input("Enter 'Q1'-'Q10', 'Trigger' for Trigger Display, or 'Q' to quit: ")
    if choice == ('Q') or choice == ('q'): cleanup()
    elif choice == "1" or choice == "Q1":
        execute_and_display_func("SELECT 'Player' AS Job, Display_name AS Name, P_team_name AS Team FROM PLAYER UNION SELECT 'Coach' AS Job, Coach_display_name AS Name, C_Team_name AS Team FROM COACH ORDER BY Team")
    elif choice == "2" or choice == "Q2": 
        execute_and_display_func("SELECT PLAYER.P_team_name AS Team, MAX(KDA.Kills) AS Maximum_Kills, MAX(KDA.Deaths) AS Maximum_Deaths, MAX(KDA.Assists) AS Maximum_Assists,ROUND(AVG(KDA.Kills),1) AS Average_Kills, ROUND(AVG(KDA.Deaths),1) AS Average_Deaths, ROUND(AVG(KDA.Assists),1) AS Average_Assists FROM PLAYER JOIN KDA ON PLAYER.Display_name = KDA.K_player_name GROUP BY PLAYER.P_team_name HAVING AVG(KDA.Kills) > 3.7 ORDER BY Maximum_Kills ASC")
    elif choice == "3" or choice == "Q3":
        execute_and_display_func("SELECT O_game_number AS Game, Objective_Type as Objective, O_player_name AS Player_Name, O_team_name AS Team FROM OBJECTIVE")
    elif choice == "4" or choice == "Q4":
        execute_and_display_func("SELECT  KDA.K_game_number AS Game_Number, PLAYER.Display_name AS Player_Name, KDA.Kills, KDA.Assists, KDA.Deaths, CASE WHEN KDA.Deaths = 0 THEN ROUND(KDA.Kills + KDA.Assists,1) ELSE ROUND(((KDA.Kills + KDA.Assists) / KDA.Deaths),1) END AS KDA FROM PLAYER JOIN KDA ON PLAYER.Display_name = KDA.K_player_name ORDER BY KDA.K_game_number, KDA DESC")
    elif choice == "5" or choice == "Q5":
        execute_and_display_func("SELECT GAME.Game_number AS Game, Game.Winning_team_name AS Winner FROM GAME")
    elif choice == "6" or choice == "Q6":
        execute_and_display_func("SELECT V_game_number AS Game, V_player_name AS Player, V_team_name AS Team, ROUND(Vision_score / Game_length_min,1) AS VSPM FROM VISION INNER JOIN GAME ON V_game_number = Game_number ORDER BY V_game_number, V_team_name, VSPM DESC")
    elif choice == "7" or choice == "Q7": 
        execute_and_display_func("SELECT D_game_number, Damage_number,D_player_name,D_team_name FROM DAMAGE ORDER BY D_game_number, D_team_name, Damage_number DESC")
    elif choice == "8" or choice == "Q8":
        execute_and_display_func("SELECT O_game_number AS Game,COUNT(*) AS Objectives_Taken,O_player_name AS Player,O_team_name AS Team FROM OBJECTIVE GROUP BY O_game_number, O_team_name, O_player_name ORDER BY O_game_number, Objectives_taken DESC")
    elif choice == "9" or choice == "Q9": 
        execute_and_display_func("WITH count AS(SELECT O_game_number AS Game,O_player_name AS Player,O_team_name AS Team, COUNT(*) AS Objectives_Taken FROM OBJECTIVE GROUP BY O_game_number, O_team_name, O_player_name ORDER BY O_game_number, Objectives_taken DESC) SELECT count.Game,count.Objectives_Taken,count.Player,count.Team FROM count WHERE count.Objectives_Taken =( SELECT MAX(current_count.Objectives_Taken) FROM count current_count WHERE current_count.Game = count.Game)")
    elif choice == "10" or choice == "Q10": 
        execute_and_display_func("SELECT Display_name AS Player,P_team_name AS Team,CASE Position WHEN 1 THEN 'Toplane' WHEN 2 THEN 'Jungle' WHEN 3 THEN 'Midlaner' WHEN 4 THEN 'ADC' WHEN 5 THEN 'Support' END AS Role FROM PLAYER ORDER BY Team, Position, Display_name")
    elif choice == "Trigger" or choice == "trigger": 
        execute_and_display_func("SELECT Message AS DB_Insert_Timestamp FROM LOG")
