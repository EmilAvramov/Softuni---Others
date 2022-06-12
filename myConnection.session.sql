ALTER TABLE teachers
ADD CONSTRAINT fk_teachers FOREIGN KEY (manager_id) REFERENCES teachers (teacher_id)