CREATE FUNCTION ufn_calculate_future_value (total DECIMAL(19,4), interest DECIMAL(19, 2), years INT)
RETURNS DECIMAL(19, 4)
DETERMINISTIC
BEGIN
    RETURN total * (POWER(1 + interest, years));
END;

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