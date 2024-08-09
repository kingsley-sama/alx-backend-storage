-- Task: Create a trigger to reset the valid_email attribute when the email is changed

-- Drop the trigger if it already exists
DROP TRIGGER IF EXISTS reset_valid_email;

-- Create the trigger that fires before an update on the users table
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if the email has been changed
    IF NEW.email <> OLD.email THEN
        -- Reset valid_email to 0 if the email is changed
        SET NEW.valid_email = 0;
    END IF;
END;

-- Explanation:
-- The trigger is defined to execute before an UPDATE operation on the users table.
-- It compares the OLD.email (existing email) with the NEW.email (updated email).
-- If the email has been changed, it resets the NEW.valid_email to 0.
