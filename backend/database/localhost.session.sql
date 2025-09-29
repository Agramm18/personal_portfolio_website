ALTER TABLE contactform
MODIFY gender ENUM('male', 'female', 'other', 'none') NOT NULL DEFAULT 'none',
