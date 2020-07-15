"""Unit testing file"""
import sys
import os
import unittest

sys.path.append(os.path.join('\\'.join(os.getcwd().split('\\')[:-1]), 'main'))
import mydbconnection


class TestDatabaseConnection(unittest.TestCase):
    """
    CLASS TO PERFORM UNIT TESTING FOR INITIATING TESTS FOR EACH MODULE
    """

    def test_connection_db(self):
        """

        Test to check if the database connection is getting established
        """
        obj = mydbconnection.Connect()
        self.assertIsNotNone(obj.connection_db('dev'))

    def test_file_path(self):
        """

        Test to check if the file path of the .sql and .csv files are getting fetched
        """
        db = mydbconnection.Connect()
        db1 = db.connection_db('dev')
        obj = mydbconnection.EmployeeDetails(db1)
        file_path = os.path.dirname(os.path.dirname(__file__)) + "\\files"
        file_path1 = os.path.dirname(os.path.dirname(__file__))
        self.assertTrue(file_path, obj.file_path())
        self.assertFalse(file_path1, obj.file_path())

    def test_create_database(self):
        """
        Test to check if a database is created
        """
        db = mydbconnection.Connect()
        db1 = db.connection_db('dev')
        cursor = db1.cursor()
        cursor.execute("SHOW DATABASES")
        db_name_list = cursor.fetchall()
        check_db = "mymodel"
        my_db = ""
        for i in db_name_list:
            for j in i:
                if check_db in j:
                    my_db += j
        fake_db = "abc"

        self.assertEqual(my_db, check_db)
        self.assertNotEqual(fake_db, check_db)

    def test_create_table(self):
        """

        Test to check if tables are getting created in the database
        """
        db = mydbconnection.Connect()
        db1 = db.connection_db('dev')
        cursor = db1.cursor()
        folder_path = os.getcwd()
        file_path = os.path.join('\\'.join(folder_path.split('\\')[:-1]), 'files')
        cursor.execute("SELECT table_name FROM information_schema.tables"
                       " WHERE table_schema='mymodel'")
        table_name = cursor.fetchall()
        table_names = []
        for i in table_name:
            for j in i:
                table_names.append(j)
        num1 = len(table_names)
        for i in range(num1):
            for filename in os.listdir(file_path):
                if filename.split('.')[1] == 'sql' and filename.split('.')[0] == table_names[i]:
                    self.assertEqual(filename.split('.')[0], table_names[i])
                    self.assertNotEqual(filename.split('.')[1], table_names[i])

    def test_query1(self):
        '''

        Test to check if an HTML file report is generated to display execution output of the query
        query: To display an employees working location, branch, facility and department
        '''
        db = mydbconnection.Connect()
        db1 = db.connection_db('dev')
        obj = mydbconnection.EmployeeDetails(db1)
        obj.query1()
        folder_path = os.getcwd()
        true_res = os.path.exists(
            os.path.join('\\'.join(folder_path.split('\\')[:-1]), 'Results', 'emp_branch_facility.html'))
        false_res = os.path.exists(
            os.path.join('\\'.join(folder_path.split('\\')[:-1]), 'main', 'emp_branch_facility.html'))
        self.assertTrue(true_res)
        self.assertFalse(false_res)

    def test_query2(self):
        '''
        Test to check if an HTML file report is generated to display execution output of the query
        query: To display an the count of employees in each skill
        :return:
        '''
        db = mydbconnection.Connect()
        db1 = db.connection_db('dev')
        obj = mydbconnection.EmployeeDetails(db1)
        obj.query2()
        folder_path = os.getcwd()
        true_res = os.path.exists(
            os.path.join('\\'.join(folder_path.split('\\')[:-1]), 'Results', 'employee_count_in_each_skill.html'))
        false_res = os.path.exists(
            os.path.join('\\'.join(folder_path.split('\\')[:-1]), 'main', 'employee_count_in_each_skill.html'))
        self.assertTrue(true_res)
        self.assertFalse(false_res)

    # def test_insert_table(self):
    #     db1 = mydbconnection.Connect.connection_db('dev')
    #     cursor = db1.cursor()
    #     folder_path = os.getcwd()


if __name__ == '__main__':
    unittest.main()
