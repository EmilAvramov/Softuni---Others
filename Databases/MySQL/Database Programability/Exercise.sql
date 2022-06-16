-- 1
CREATE PROCEDURE usp_get_employees_salary_above_35000()
BEGIN
    SELECT first_name, last_name
    FROM employees
    WHERE salary > 35000
    ORDER BY first_name, last_name, employee_id;
END

-- 2
CREATE PROCEDURE usp_get_employees_salary_above (num DOUBLE(19, 4))
BEGIN
    SELECT first_name, last_name
    FROM employees
    WHERE salary >= num
    ORDER BY first_name, last_name, employee_id;
END

-- 3
CREATE PROCEDURE usp_get_towns_starting_with (string NVARCHAR(100))
BEGIN
    SELECT name FROM towns
    WHERE name LIKE CONCAT(string, "%")
    ORDER BY name;
END;

-- 4
CREATE PROCEDURE usp_get_employees_from_town (t_name NVARCHAR(100))
BEGIN
    SELECT e.first_name, e.last_name FROM employees AS e
    JOIN addresses AS a on e.address_id = a.address_id
    JOIN towns AS t on a.town_id = t.town_id
    WHERE t.name = t_name
    ORDER BY e.first_name, e.last_name;
END

-- 5
CREATE FUNCTION ufn_get_salary_level (salary DOUBLE(19, 2))
RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
	DECLARE s_level VARCHAR(20);
	IF salary > 50000 THEN SET s_level = "High";
	ELSEIF salary BETWEEN 30000 AND 50000 THEN SET s_level = "Average";
		ELSE SET s_level = "Low";
	END IF;
	RETURN s_level;
END;

-- 6
CREATE PROCEDURE usp_get_employees_by_salary_level (s_level VARCHAR(7))
BEGIN
    SELECT first_name, last_name
    FROM employees
    WHERE ufn_get_salary_level(salary) = s_level
    ORDER BY first_name DESC, last_name DESC;
END;

-- 7
CREATE FUNCTION ufn_is_word_comprised (set_of_letters VARCHAR(50), word VARCHAR(50))
RETURNS BIT
DETERMINISTIC
BEGIN
    DECLARE idx INT;
    DECLARE current_letter VARCHAR(1);
    SET idx = 1;
    WHILE(idx <= LENGTH(word)) DO
		SET current_letter = SUBSTRING(word, idx, 1);
		IF (LOCATE(current_letter, set_of_letters) <= 0) THEN
			RETURN 0;
		END IF;
		SET idx = idx + 1;
	END WHILE;
    RETURN 1;
-- REGEX => RETURN word REGEXP(CONCAT('^[', set_of_letters, ']+$'))
END;

-- 8
CREATE PROCEDURE usp_get_holders_full_name()
BEGIN
    SELECT CONCAT(first_name, " ", last_name) AS full_name
    FROM account_holders
    ORDER BY CONCAT(first_name, " ", last_name), id;
END

-- 9
CREATE PROCEDURE usp_get_holders_with_balance_higher_than (numb DOUBLE(19, 2))
BEGIN
    SELECT ah.first_name, ah.last_name
    FROM account_holders AS ah
    JOIN accounts AS a ON ah.id = a.account_holder_id
    GROUP BY ah.id
    HAVING SUM(balance) > numb
    ORDER BY ah.id;
END

-- 10
CREATE FUNCTION ufn_calculate_future_value (total DECIMAL(19,4), interest DECIMAL(19, 2), years INT)
RETURNS DECIMAL(19, 4)
DETERMINISTIC
BEGIN
    RETURN total * (POWER(1 + interest, years));
END

-- 11
CREATE PROCEDURE usp_calculate_future_value_for_account (target_id INT, interest DECIMAL(19, 4))
BEGIN
    SELECT 
    a.id AS account_id,
    ah.first_name,
    ah.last_name,
    a.balance AS cureent_balance,
    ufn_calculate_future_value(a.balance, interest, 5) AS balance_in_5_years
    FROM account_holders AS ah
    JOIN accounts AS a ON ah.id = a.account_holder_id 
    WHERE a.id = target_id;
END;

-- 12
CREATE PROCEDURE usp_deposit_money(target_id INT, money_amount DECIMAL(19,4))
BEGIN
    START TRANSACTION;
    IF (money_amount > 0) 
    THEN
        UPDATE accounts SET balance = balance + money_amount WHERE target_id = id;
        COMMIT;
    ELSE ROLLBACK;
    END IF;
END

-- 13
CREATE PROCEDURE usp_withdraw_money (target_id INT, money_amount DECIMAL(19, 4))
BEGIN
    START TRANSACTION;
    IF (money_amount > 0 AND
    (SELECT balance FROM accounts WHERE target_id = id) > money_amount) 
    THEN
        UPDATE accounts SET balance = balance - money_amount WHERE target_id = id;
        COMMIT;
    ELSE ROLLBACK;
    END IF;
END

-- 14
CREATE FUNCTION usp_check_id (target_id INT)
RETURNS BIT
DETERMINISTIC
BEGIN
    RETURN (SELECT EXISTS(SELECT id FROM accounts WHERE id = target_id));
END;

CREATE PROCEDURE usp_transfer_money (sender INT, receiver INT, amount DECIMAL(19, 4))
BEGIN
    START TRANSACTION;
    IF (
        usp_check_id(sender) = 1 AND 
        usp_check_id(receiver) = 1 AND
        amount > 0 AND
        (SELECT balance FROM accounts WHERE id = sender) >= amount
        ) 
    THEN 
        UPDATE accounts SET balance = balance + amount WHERE id = receiver;
        UPDATE accounts SET balance = balance - amount WHERE id = sender;
        COMMIT;
    ELSE 
		ROLLBACK;
    END IF;
END;

-- 15
CREATE TABLE logs (
    log_id INT AUTO_INCREMENT NOT NULL,
    account_id INT NOT NULL,
    old_sum DECIMAL(19, 4) NOT NULL,
    new_sum DECIMAL(19, 4) NOT NULL,
    CONSTRAINT pk_logs PRIMARY KEY (log_id)
);

CREATE TRIGGER tr_logs
AFTER UPDATE ON accounts
FOR EACH ROW
BEGIN
    INSERT INTO logs (account_id, old_sum, new_sum)
    VALUES (OLD.id, OLD.balance, NEW.balance);
END;

-- 16
CREATE TABLE notification_emails(
    id INT AUTO_INCREMENT NOT NULL,
    recipient NVARCHAR(100) NOT NULL,
    subject NVARCHAR(200) NOT NULL,
    body NVARCHAR(1000) NOT NULL,
    CONSTRAINT pk_notif PRIMARY KEY (id)
);

CREATE TRIGGER tr_notifications
AFTER INSERT ON logs
FOR EACH ROW
BEGIN
    INSERT INTO notification_emails (recipient, subject, body)
    VALUES 
    (
    NEW.account_id,
    CONCAT('Balance change for account: ', NEW.account_id),
    CONCAT('On ', DATE_FORMAT(NOW(), '%b %d %Y at %r'), ' your balance was changed from ', NEW.old_sum, ' to ', NEW.new_sum)
    );
END;