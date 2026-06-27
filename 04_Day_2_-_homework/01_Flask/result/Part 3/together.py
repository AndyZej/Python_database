-- 1. Table leader
SELECT name
FROM Teams
ORDER BY points DESC
LIMIT 1;


-- 2. Full table sorted by points
SELECT name, points
FROM Teams
ORDER BY points DESC;


-- 3. Home matches of The Fiery Dragons
SELECT t1.name, t2.name, g.goals_home, g.goals_away
FROM Games g
JOIN Teams t1 ON g.team_home = t1.id
JOIN Teams t2 ON g.team_away = t2.id
WHERE t1.name = 'The Fiery Dragons';


-- 4. Away matches
SELECT t1.name, t2.name, g.goals_home, g.goals_away
FROM Games g
JOIN Teams t1 ON g.team_home = t1.id
JOIN Teams t2 ON g.team_away = t2.id
WHERE t2.name = 'The Fiery Dragons';


-- 5. All matches
SELECT t1.name, t2.name, g.goals_home, g.goals_away
FROM Games g
JOIN Teams t1 ON g.team_home = t1.id
JOIN Teams t2 ON g.team_away = t2.id
WHERE t1.name = 'The Fiery Dragons'
   OR t2.name = 'The Fiery Dragons';


-- 6. Goals scored (home and away)
SELECT SUM(goals_home)
FROM Games g
JOIN Teams t ON g.team_home = t.id
WHERE t.name = 'The Fiery Dragons';

SELECT SUM(goals_away)
FROM Games g
JOIN Teams t ON g.team_away = t.id
WHERE t.name = 'The Fiery Dragons';