-- converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
ALTER DATABASE utf8mb4
CHARACTER SET utf8mb4,
ALTER TABLE hbtn_0c_0.first_table
DEFAULT CHARACTER SET utf8mb4,
  MODIFY name varchar(256)
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL;
