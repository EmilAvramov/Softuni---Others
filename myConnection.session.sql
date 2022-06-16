CREATE TRIGGER tr_notifications
AFTER INSERT ON logs
FOR EACH ROW
BEGIN
    INSERT INTO notification_emails (recipient, subject, body)
    VALUES 
    (NEW.account_id,
    CONCAT('Balance change for account: ', NEW.account_id),
    CONCAT('On ', DATE_FORMAT(NOW(), '%b %d %Y at %r'), 
    ' your balance was changed from '),
    NEW.old_sum, ' to ', NEW.new_sum
    );
END;