import configparser

con=configparser.ConfigParser()
con.read('C:\\Users\\Sri Athishya\\Desktop\\Python\\4-4.30\\My_dbproject\\config\\dev.ini')

def config(env):
    #env=input("Enter the environment:")
    dbase=con.get(env,'db')
    return(dbase)
#config('dev')
