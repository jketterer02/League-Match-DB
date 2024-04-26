USE match_database;

-- Populating with Teams and Players

INSERT INTO TEAM values('Cloud9');
INSERT INTO COACH values('Mithy','Cloud9');
INSERT INTO PLAYER values('Fudge','Cloud9',1);
INSERT INTO PLAYER values('Thanatos','Cloud9',1);
INSERT INTO PLAYER values('Blaber','Cloud9',2);
INSERT INTO PLAYER values('Jojopyun','Cloud9',3);
INSERT INTO PLAYER values('Berserker','Cloud9',4);
INSERT INTO PLAYER values('VULCAN','Cloud9',5);

INSERT INTO TEAM values('T1');
INSERT INTO COACH values('KkOma','T1');
INSERT INTO PLAYER values('Zeus','T1',1);
INSERT INTO PLAYER values('Oner','T1',2);
INSERT INTO PLAYER values('Faker','T1',3);
INSERT INTO PLAYER values('Gumayusi','T1',4);
INSERT INTO PLAYER values('Keria','T1',5);

INSERT INTO TEAM values('G2');
INSERT INTO COACH values('Dylan Falco ','G2');
INSERT INTO PLAYER values('BrokenBlade','G2',1);
INSERT INTO PLAYER values('Yike','G2',2);
INSERT INTO PLAYER values('Caps','G2',3);
INSERT INTO PLAYER values('Hans Sama','G2',4);
INSERT INTO PLAYER values('Mikyx','G2',5);

INSERT INTO TEAM values('FlyQuest');
INSERT INTO COACH values('Nukeduck','FlyQuest');
INSERT INTO PLAYER values('Bwipo','FlyQuest',1);
INSERT INTO PLAYER values('Inspired','FlyQuest',2);
INSERT INTO PLAYER values('Jensen','FlyQuest',3);
INSERT INTO PLAYER values('Massu','FlyQuest',4);
INSERT INTO PLAYER values('Busio','FlyQuest',5);

INSERT INTO TEAM values('Fnatic');
INSERT INTO COACH values('Nightshare','Fnatic');
INSERT INTO PLAYER values('Oscarinin','Fnatic',1);
INSERT INTO PLAYER values('Razork','Fnatic',2);
INSERT INTO PLAYER values('Humanoid','Fnatic',3);
INSERT INTO PLAYER values('Noah','Fnatic',4);
INSERT INTO PLAYER values('Jun','Fnatic',5);

-- Populating with Games

INSERT INTO GAME values(1,45,'Fnatic','Flyquest','FlyQuest');
INSERT INTO GAME values(2,55,'T1','G2','T1');
INSERT INTO GAME values(3,55,'Cloud9','G2','Cloud9');
INSERT INTO GAME values(4,55,'T1','Cloud9','T1');
INSERT INTO GAME values(5,55,'Flyquest','G2','G2');

-- Populating with Objectives

-- Game 1 Objectives
INSERT INTO OBJECTIVE values(0,1,'Fire Dragon','Flyquest','Bwipo');
INSERT INTO OBJECTIVE values(1,1,'Air Dragon','Fnatic','Razork');
INSERT INTO OBJECTIVE values(2,1,'Mountain Dragon','Fnatic','Razork');
INSERT INTO OBJECTIVE values(3,1,'Elder Dragon','Fnatic','Razork');
INSERT INTO OBJECTIVE values(4,1,'Inhibitor','Flyquest','Jensen');
INSERT INTO OBJECTIVE values(5,1,'Nexus','Flyquest','Inspired');

-- Game 2 Objectives
INSERT INTO OBJECTIVE values(0,2,'Void Grub','T1','Zeus');
INSERT INTO OBJECTIVE values(1,2,'Water Dragon','G2','Yike');
INSERT INTO OBJECTIVE values(2,2,'Mountain Dragon','G2','Caps');
INSERT INTO OBJECTIVE values(3,2,'Turret','G2','BrokenBlade');
INSERT INTO OBJECTIVE values(4,2,'Nexus','T1','Faker');

-- Populating with Damage numbers for Game 1

INSERT INTO DAMAGE values(100000,1,'Flyquest','Bwipo');
INSERT INTO DAMAGE values(23576,1,'Flyquest','Busio');
INSERT INTO DAMAGE values(12378,1,'Flyquest','Inspired');
INSERT INTO DAMAGE values(9876,1,'Flyquest','Jensen');
INSERT INTO DAMAGE values(15635,1,'Flyquest','Massu');

INSERT INTO DAMAGE values(10000,1,'Fnatic','Razork');
INSERT INTO DAMAGE values(54321,1,'Fnatic','Noah');
INSERT INTO DAMAGE values(9234,1,'Fnatic','JUN');
INSERT INTO DAMAGE values(6089,1,'Fnatic','Oscarinin');
INSERT INTO DAMAGE values(5367,1,'Fnatic','Humanoid');

-- Populating with Damage numbers for Game 2

INSERT INTO DAMAGE values(15000,2,'T1','Zeus');
INSERT INTO DAMAGE values(12967,2,'T1','Oner');
INSERT INTO DAMAGE values(12341,2,'T1','Faker');
INSERT INTO DAMAGE values(31415,2,'T1','Gumayusi');
INSERT INTO DAMAGE values(10023,2,'T1','Keria');


INSERT INTO DAMAGE values(15000,2,'G2','BrokenBlade');
INSERT INTO DAMAGE values(12967,2,'G2','Yike');
INSERT INTO DAMAGE values(12341,2,'G2','Caps');
INSERT INTO DAMAGE values(2115,2,'G2','Hans Sama');
INSERT INTO DAMAGE values(14323,2,'G2','Mikyx');

-- Populating with Vision Score for Game 1

INSERT INTO VISION values(25,1,'Flyquest','Bwipo');
INSERT INTO VISION values(52,1,'Flyquest','Busio');
INSERT INTO VISION values(11,1,'Flyquest','Inspired');
INSERT INTO VISION values(16,1,'Flyquest','Jensen');
INSERT INTO VISION values(21,1,'Flyquest','Massu');

INSERT INTO VISION values(10,1,'Fnatic','Razork');
INSERT INTO VISION values(7,1,'Fnatic','Noah');
INSERT INTO VISION values(8,1,'Fnatic','JUN');
INSERT INTO VISION values(19,1,'Fnatic','Oscarinin');
INSERT INTO VISION values(20,1,'Fnatic','Humanoid');

-- Populating with Vision Score for Game 2

INSERT INTO VISION values(21,2,'T1','Zeus');
INSERT INTO VISION values(26,2,'T1','Oner');
INSERT INTO VISION values(34,2,'T1','Faker');
INSERT INTO VISION values(42,2,'T1','Gumayusi');
INSERT INTO VISION values(16,2,'T1','Keria');

INSERT INTO VISION values(14,2,'G2','BrokenBlade');
INSERT INTO VISION values(16,2,'G2','Yike');
INSERT INTO VISION values(4,2,'G2','Caps');
INSERT INTO VISION values(7,2,'G2','Hans Sama');
INSERT INTO VISION values(34,2,'G2','Mikyx');


-- Populating with KDA for Game 1

INSERT INTO KDA values(1,1,23,1,'Fnatic','JUN');
INSERT INTO KDA values(13,2,0,1,'Fnatic','Noah');
INSERT INTO KDA values(0,2,0,1,'Fnatic','Razork');
INSERT INTO KDA values(5,5,5,1,'Fnatic','Humanoid');
INSERT INTO KDA values(0,6,12,1,'Fnatic','Oscarinin');

INSERT INTO KDA values(1,6,14,1,'Flyquest','Bwipo');
INSERT INTO KDA values(11,6,0,1,'Flyquest','Jensen');
INSERT INTO KDA values(3,1,4,1,'Flyquest','Inspired');
INSERT INTO KDA values(0,0,30,1,'Flyquest','Massu');
INSERT INTO KDA values(3,1,3,1,'Flyquest','Busio');

-- Populating with KDA for Game 2

INSERT INTO KDA values(23,0,5,2,'T1','Zeus');
INSERT INTO KDA values(0,11,15,2,'T1','Oner');
INSERT INTO KDA values(2,1,1,2,'T1','Faker');
INSERT INTO KDA values(3,1,4,2,'T1','Gumayusi');
INSERT INTO KDA values(4,5,6,2,'T1','Keria');


INSERT INTO KDA values(0,19,5,2,'G2','BrokenBlade');
INSERT INTO KDA values(2,4,6,2,'G2','Yike');
INSERT INTO KDA values(0,1,2,2,'G2','Caps');
INSERT INTO KDA values(24,0,13,2,'G2','Hans Sama');
INSERT INTO KDA values(5,2,1,2,'G2','Mikyx');


