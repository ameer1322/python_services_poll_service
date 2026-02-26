DROP TABLE IF EXISTS poll_question;
DROP TABLE IF EXISTS poll_answers;


CREATE TABLE poll_questions(
    id INT NOT NULL AUTO_INCREMENT,
    question VARCHAR(300) NOT NULL DEFAULT "",
    answer_a VARCHAR(300) NOT NULL DEFAULT "",
    answer_b VARCHAR(300) NOT NULL DEFAULT "",
    answer_c VARCHAR(300) NOT NULL DEFAULT "",
    answer_d VARCHAR(300) NOT NULL DEFAULT "",
    PRIMARY KEY (id)
);

CREATE TABLE poll_answers(
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    question_id INT NOT NULL,
    answer_id INT DEFAULT 0,
    PRIMARY KEY (id),
    FOREIGN KEY (question_id) REFERENCES poll_questions(id) ON DELETE CASCADE
);