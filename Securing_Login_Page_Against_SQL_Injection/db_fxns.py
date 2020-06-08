# DB
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Functions

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS blogtable(author TEXT,title TEXT,article TEXT,postdate DATE)')

def add_data(author,title,article,postdate):
	c.execute('INSERT INTO blogtable(author,title,article,postdate) VALUES (?,?,?,?)',(author,title,article,postdate))
	conn.commit()

def view_all_notes():
	c.execute('SELECT * FROM blogtable')
	data = c.fetchall()
	return data

def view_all_titles():
	c.execute('SELECT DISTINCT title FROM blogtable')
	data = c.fetchall()
	return data


def get_blog_by_title(title):
	c.execute('SELECT * FROM blogtable WHERE title="{}"'.format(title))
	data = c.fetchall()
	return data

def get_blog_by_author(author):
	c.execute('SELECT * FROM blogtable WHERE author="{}"'.format(author))
	data = c.fetchall()
	return data


def delete_data(title):
	c.execute('DELETE FROM blogtable WHERE title="{}"'.format(title))
	conn.commit()



def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data

def login_user_safe2(username,password):
	c.execute("SELECT * FROM userstable WHERE username= '%s' AND password = '%s'"),(username, password);
	data = c.fetchall()
	return data

# Works but not safe agains SQL injections

def login_user_unsafe(username,password):
	c.execute("SELECT * FROM userstable WHERE username='{}' AND password = '{}'".format(username,password))
	data = c.fetchall()
	return data

def login_user_unsafe2(username,password):
	c.execute(f"SELECT * FROM userstable WHERE username= '{username}' AND password= '{password}'")
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data
