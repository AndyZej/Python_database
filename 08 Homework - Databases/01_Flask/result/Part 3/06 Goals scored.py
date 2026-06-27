# SQL

-- Home goals
SELECT SUM(goals_home)
FROM Games g
JOIN Teams t ON g.team_home = t.id
WHERE t.name = 'The Fiery Dragons';

-- Away goals
SELECT SUM(goals_away)
FROM Games g
JOIN Teams t ON g.team_away = t.id
WHERE t.name = 'The Fiery Dragons';