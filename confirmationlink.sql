CREATE TABLE confirmationlink (
	id INTEGER NOT NULL,
	link TEXT(512),
	active SMALLINT,
	user_id INTEGER NOT NULL,
	expire_on DATE,
	PRIMARY KEY (id),
	FOREIGN KEY(user_id) REFERENCES user (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=197 ;