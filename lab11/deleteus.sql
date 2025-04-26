CREATE PROCEDURE delete_user(nami) 
LANGUAGE plpgsql
AS $$
BEGIN
IF EXISTS (
	SELECT 1 FROM phonebook 
	WHERE name = nami
) THEN
	DELETE FROM phonebook 
    WHERE name = nami;
ELSE
	RAISE NOTICE 'user % does not exist', nami;
END IF;
END;
$$;