USE nhlsalarycap;
CREATE TABLE BasicCapInfo (
	Player varchar(80),
    Pos varchar(5),
    RemainingYearsofContract INT,
    AAV_2023_24 INT,
    AAV_2024_25 INT,
    AAV_2025_26 INT,
    ExpStatust varchar(80),
    Clause varchar(80)
);

SELECT default_character_set_name FROM information_schema.SCHEMATA 
WHERE schema_name = "nhlsalarycap";


