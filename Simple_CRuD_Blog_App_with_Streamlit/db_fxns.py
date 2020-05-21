import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS blogtable(author TEXT,title TEXT,article TEXT,postdate,DATE)')


def add_data(author,title,article,postdate):
	c.execute('INSERT INTO blogtable(author,title,article,postdate) VALUES (?,?,?,?)',(author,title,article,postdate))
	conn.commit()


def view_all_notes():
	c.execute('SELECT * FROM blogtable')
	data = c.fetchall()
	# for row in data:
	# 	print(row)
	return data

def view_all_titles():
	c.execute('SELECT DISTINCT title FROM blogtable')
	data = c.fetchall()
	# for row in data:
	# 	print(row)
	return data

def get_single_blog(title):
	c.execute('SELECT * FROM blogtable WHERE title="{}"'.format(title))
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
 

def get_blog_by_msg(article):
	c.execute("SELECT * FROM blogtable WHERE article like '%{}%'".format(article))
	data = c.fetchall()
	return data

def edit_blog_author(author,new_author):
	c.execute('UPDATE blogtable SET author ="{}" WHERE author="{}"'.format(new_author,author))
	conn.commit()
	data = c.fetchall()
	return data

def edit_blog_title(title,new_title):
	c.execute('UPDATE blogtable SET title ="{}" WHERE title="{}"'.format(new_title,title
		))
	conn.commit()
	data = c.fetchall()
	return data


def edit_blog_article(article,new_article):
	c.execute('UPDATE blogtable SET title ="{}" WHERE title="{}"'.format(new_article,article
		))
	conn.commit()
	data = c.fetchall()
	return data

def delete_data(title):
	c.execute('DELETE FROM blogtable WHERE title="{}"'.format(title))
	conn.commit()
