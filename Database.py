# database of skills and what they're related to
# split string of text (skills) in to see if its in the database
# each skill is assigned to a category: technical/design etc

import sqlite3 as lite
import sys

con = lite.connect('Skills.db')

cur = con.cursor()
# cur.execute("CREATE TABLE Skills(Id INT, Skills TEXT, Category TEXT)")

with con:

    cur.execute("INSERT INTO Skills VALUES(1, 'Programming', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(2, 'Java', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(3, 'Ruby','Technical')")
    cur.execute("INSERT INTO Skills VALUES(4, 'Hardware','Technical')")
    cur.execute("INSERT INTO Skills VALUES(5, 'Robotics', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(6, 'Perl', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(7, 'HTML', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(8, 'CSS', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(9, 'C++', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(10, 'C#', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(11, 'Javascript', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(12, 'OpenCL', 'Technical')")


    cur.execute("INSERT INTO Skills VALUES(13, 'PHP', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(14, 'VisualBasic', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(15, 'SQL', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(16, 'Problem Solving', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(17, 'Critical Thinking', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(18, 'Debugging', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(19, 'C', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(20, 'XML', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(21, 'Python', 'Technical')")


    cur.execute("INSERT INTO Skills VALUES(22, 'Pascal', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(23, 'Haskell', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(24, 'Scala', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(25, 'MongoDB', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(26, 'MySQL', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(27, 'Hadoop', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(28, 'Apachee', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(29, 'Linux', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(30, 'iOS', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(31, 'Android', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(32, 'Git', 'Technical')")


    cur.execute("INSERT INTO Skills VALUES(33, 'NodeJS', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(34, 'MeteorJS', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(35, 'Swift', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(36, 'Objective C', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(37, 'Data Analysis', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(38, 'Communication Protocol', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(39, 'Bluetooth', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(40, 'Raspberry Pi', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(41, 'BASIC', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(42, 'FORTRAN', 'Technical')")


    cur.execute("INSERT INTO Skills VALUES(43, 'Oculus Rift', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(44, 'Myo', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(45, 'Spark Photon', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(46, 'APIs', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(47, 'Scalable system design', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(48, 'Project Management', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(49, 'Development', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(50, 'Communication Skills', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(51, 'Server Operating Systems', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(52, 'Databases', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(53, 'Cloud Computing', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(54, 'Networking', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(55, 'Scripting Languages', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(56, 'Optimization', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(57, 'Client networking', 'Technical')")
    cur.execute("INSERT INTO Skills VALUES(58, 'Server networking', 'Technical')")

    #Design category
    cur.execute("INSERT INTO Skills VALUES(59, 'Marketing', 'Design')")
    cur.execute("INSERT INTO Skills VALUES(60, 'Advertising', 'Design')")
    cur.execute("INSERT INTO Skills VALUES(61, 'Design', 'Design')")
    cur.execute("INSERT INTO Skills VALUES(62, 'Interactive Development', 'Design')")
    cur.execute("INSERT INTO Skills VALUES(63, 'Copywriting', 'Design')")



    con.commit()


con.close()