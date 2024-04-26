import mysql.connector
import os

# Connect to the MySQL database
conn = mysql.connector.connect(host="localhost", user="root", password="password",ssl_disabled=True)

# Check if connection is established to the database
if conn.is_connected(): print("Connection established...")
# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Creates database 
#cursor.execute("CREATE DATABASE match_database")
#cursor.execute("USE match_database")
#cursor.execute("CREATE TABLE TEAM( Team_name VARCHAR(20) NOT NULL,PRIMARY KEY (Team_name))")
#cursor.execute("CREATE TABLE COACH( Coach_display_name	VARCHAR(20) NOT NULL,C_Team_name VARCHAR(20) NOT NULL,PRIMARY KEY (Coach_display_name),FOREIGN KEY(C_Team_name) REFERENCES TEAM(Team_name))")
#cursor.execute("CREATE TABLE PLAYER( Display_name		VARCHAR(20) NOT NULL,P_team_name		VARCHAR(20) NOT NULL,Position 			INT NOT NULL CHECK (Position >= 0 AND Position <= 6),PRIMARY KEY (Display_name),FOREIGN KEY(P_team_name) REFERENCES TEAM(Team_name));")
#cursor.execute("CREATE TABLE GAME( Game_number 			INT NOT NULL,Game_length_min		FLOAT NOT NULL,Red_team_name			VARCHAR(20) NOT NULL,Blue_team_name		VARCHAR(20) NOT NULL,Winning_team_name		VARCHAR(20) NOT NULL,PRIMARY KEY (Game_number),FOREIGN KEY(Red_team_name) REFERENCES TEAM(Team_name),FOREIGN KEY(Blue_team_name) REFERENCES TEAM(Team_name))")
#cursor.execute("CREATE TABLE OBJECTIVE( Objective_number 		INT NOT NULL,O_game_number			INT NOT NULL,Objective_type		VARCHAR(20) NOT NULL,O_team_name			VARCHAR(20) NOT NULL,O_player_name			VARCHAR(20) NOT NULL,PRIMARY KEY (O_game_number, Objective_number),FOREIGN KEY(O_team_name) REFERENCES TEAM(Team_name),FOREIGN KEY(O_player_name) REFERENCES PLAYER(Display_name),FOREIGN KEY(O_game_number) REFERENCES GAME(Game_number))")
#cursor.execute("CREATE TABLE DAMAGE( Damage_number 		INT NOT NULL,D_game_number			INT NOT NULL,D_team_name			VARCHAR(20) NOT NULL,D_player_name			VARCHAR(20) NOT NULL,PRIMARY KEY (D_game_number, D_player_name),FOREIGN KEY(D_team_name) REFERENCES TEAM(Team_name),FOREIGN KEY(D_player_name) REFERENCES PLAYER(Display_name),FOREIGN KEY(D_game_number) REFERENCES GAME(Game_number))")
#cursor.execute("CREATE TABLE Vision( Vision_score 			INT NOT NULL,V_game_number			INT NOT NULL,V_team_name			VARCHAR(20) NOT NULL,V_player_name			VARCHAR(20) NOT NULL,PRIMARY KEY (V_game_number, V_player_name),FOREIGN KEY(V_team_name) REFERENCES TEAM(Team_name),FOREIGN KEY(V_player_name) REFERENCES PLAYER(Display_name),FOREIGN KEY(V_game_number) REFERENCES GAME(Game_number))")
#cursor.execute("CREATE TABLE KDA( Kills					INT NOT NULL,Deaths				INT NOT NULL,Assists				INT NOT NULL,K_game_number			INT NOT NULL,K_team_name			VARCHAR(20) NOT NULL,K_player_name			VARCHAR(20) NOT NULL,PRIMARY KEY (K_game_number, K_player_name),FOREIGN KEY(K_team_name) REFERENCES TEAM(Team_name),FOREIGN KEY(K_player_name) REFERENCES PLAYER(Display_name),FOREIGN KEY(K_game_number) REFERENCES GAME(Game_number))")
#cursor.execute("CREATE TABLE Log (LogID INT AUTO_INCREMENT PRIMARY KEY,Message VARCHAR(50))")
#cursor.execute("CREATE TRIGGER PlayerInserted AFTER INSERT ON PLAYER FOR EACH ROW BEGIN DECLARE log_message VARCHAR(50); SET log_message = CONCAT('New player inserted with display name: ', NEW.Display_name); INSERT INTO Log (Message) VALUES (log_message); END;")
sql_statements = [
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
    "CREATE TABLE Log (LogID INT AUTO_INCREMENT PRIMARY KEY, Message VARCHAR(50));",
    "CREATE TRIGGER PlayerInserted AFTER INSERT ON PLAYER FOR EACH ROW BEGIN DECLARE log_message VARCHAR(50); SET log_message = CONCAT('New player inserted with display name: ', NEW.Display_name); INSERT INTO Log (Message) VALUES (log_message); END;"
]
        
# Execute each SQL statement
for statement in sql_statements: cursor.execute(statement)

# Commit the transaction
conn.commit()

# Close the cursor
cursor.close()
# Close the connection
conn.close()