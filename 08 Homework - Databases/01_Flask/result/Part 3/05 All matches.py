# SQL

SELECT t1.name, t2.name, g.goals_home, g.goals_away
FROM Games g
JOIN Teams t1 ON g.team_home = t1.id
JOIN Teams t2 ON g.team_away = t2.id
WHERE t1.name = 'The Fiery Dragons'
   OR t2.name = 'The Fiery Dragons';