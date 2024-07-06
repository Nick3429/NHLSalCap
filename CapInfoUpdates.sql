SET SQL_SAFE_UPDATES = 0;

-- Perform the update
UPDATE nhlsalarycap.`cf cost per point 2016-17`
SET PLAYER = 'Burakovsky, Andre'
WHERE PLAYER = 'Burakovsky, AndrÃ©';

-- Re-enable safe update mode
SET SQL_SAFE_UPDATES = 1;