#   /$$$$$$  /$$   /$$ /$$   /$$ /$$   /$$        /$$$$$$  /$$$$$$$$                                         
#  /$$__  $$| $$  | $$| $$  | $$| $$  /$$/       /$$__  $$|_____ $$                                          
# | $$  \__/| $$  | $$| $$  | $$| $$ /$$/       | $$  \__/     /$$/                                          
# | $$      | $$  | $$| $$$$$$$$| $$$$$/ /$$$$$$|  $$$$$$     /$$/                                           
# | $$      | $$  | $$| $$__  $$| $$  $$|______/ \____  $$   /$$/                                            
# | $$    $$| $$  | $$| $$  | $$| $$\  $$        /$$  \ $$  /$$/                                             
# |  $$$$$$/|  $$$$$$/| $$  | $$| $$ \  $$      |  $$$$$$/ /$$$$$$$$                                         
#  \______/  \______/ |__/  |__/|__/  \__/       \______/ |________/                                         
#                                                                                                        
# $$\       $$\ $$\                                                                                         
# $$ |      \__|$$ |                                                                                        
# $$ |      $$\ $$$$$$$\   $$$$$$\  $$$$$$\   $$$$$$\  $$\   $$\                               _____          _         _              __ ___  ____   ___   ___   ___   ___ ______ ___  
# $$ |      $$ |$$  __$$\ $$  __$$\ \____$$\ $$  __$$\ $$ |  $$ |                             / ____|        | |       | |            /_ |__ \|___ \ / _ \ / _ \ / _ \ / _ \____  / _ \ 
# $$ |      $$ |$$ |  $$ |$$ |  \__|$$$$$$$ |$$ |  \__|$$ |  $$ |                            | |     ___   __| | ___   | |__  _   _    | |  ) | __) | | | | (_) | | | | | | |  / / (_) |
# $$ |      $$ |$$ |  $$ |$$ |     $$  __$$ |$$ |      $$ |  $$ |                            | |    / _ \ / _` |/ _ \  | '_ \| | | |   | | / / |__ <| | | |\__, | | | | | | | / / \__, |
# $$$$$$$$\ $$ |$$$$$$$  |$$ |     \$$$$$$$ |$$ |      \$$$$$$$ |                            | |___| (_) | (_| |  __/  | |_) | |_| |   | |/ /_ ___) | |_| |  / /| |_| | |_| |/ /    / / 
# \________|\__|\_______/ \__|      \_______|\__|       \____$$ |                             \_____\___/ \__,_|\___|  |_.__/ \__, |   |_|____|____/ \___/  /_/  \___/ \___//_/    /_/  
#                                                      $$\   $$ |                                                              __/ |                                                    
#                                                      \$$$$$$  |                                                             |___/                                                                                 
#                                                       \______/                                            
# $$\      $$\                                                                                      $$\     
# $$$\    $$$ |                                                                                     $$ |    
# $$$$\  $$$$ | $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$$$$$$\ $$$$$$\   
# $$\$$\$$ $$ | \____$$\ $$  __$$\  \____$$\ $$  __$$\ $$  __$$\ $$  _$$  _$$\ $$  __$$\ $$  __$$\\_$$  _|  
# $$ \$$$  $$ | $$$$$$$ |$$ |  $$ | $$$$$$$ |$$ /  $$ |$$$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |$$ |  $$ | $$ |    
# $$ |\$  /$$ |$$  __$$ |$$ |  $$ |$$  __$$ |$$ |  $$ |$$   ____|$$ | $$ | $$ |$$   ____|$$ |  $$ | $$ |$$\ 
# $$ | \_/ $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |\$$$$$$$ |\$$$$$$$\ $$ | $$ | $$ |\$$$$$$$\ $$ |  $$ | \$$$$  |
# \__|     \__| \_______|\__|  \__| \_______| \____$$ | \_______|\__| \__| \__| \_______|\__|  \__|  \____/ 
#                                            $$\   $$ |                                                     
#                                            \$$$$$$  |                                                     
#                                             \______/                                                      
#  $$$$$$\                        $$\                                                                       
# $$  __$$\                       $$ |                                                                      
# $$ /  \__|$$\   $$\  $$$$$$$\ $$$$$$\    $$$$$$\  $$$$$$\$$$$\                                            
# \$$$$$$\  $$ |  $$ |$$  _____|\_$$  _|  $$  __$$\ $$  _$$  _$$\                                           
#  \____$$\ $$ |  $$ |\$$$$$$\    $$ |    $$$$$$$$ |$$ / $$ / $$ |                                          
# $$\   $$ |$$ |  $$ | \____$$\   $$ |$$\ $$   ____|$$ | $$ | $$ |                                          
# \$$$$$$  |\$$$$$$$ |$$$$$$$  |  \$$$$  |\$$$$$$$\ $$ | $$ | $$ |                                          
#  \______/  \____$$ |\_______/    \____/  \_______|\__| \__| \__|                                          
#           $$\   $$ |                                                                                      
#           \$$$$$$  |                                                                                      
#            \______/                 
import sys
import sqlite3
import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import font, ttk
import hashlib
import random
import string
# from PIL import Image, ImageDraw, ImageFont, ImageTk  
import pandas as pd
import matplotlib.pyplot as plt


# Setup User Database
def setup_user_database():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
        ''')
        conn.commit()

def setup_library_database():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            nationality TEXT NOT NULL,
            isbn TEXT UNIQUE NOT NULL,
            shelf_number TEXT NOT NULL,
            total_quantity INTEGER NOT NULL CHECK (total_quantity > 0),
            available_quantity INTEGER NOT NULL CHECK (available_quantity >= 0 AND available_quantity <= total_quantity)
        )
        ''')
        conn.commit()
# Insert User into User Database
def insert_user(username, password, role):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    try:
        with sqlite3.connect('library.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO Users (username, password, role) VALUES (?, ?, ?)
            ''', (username, hashed_password, role))
            conn.commit()
    except sqlite3.IntegrityError:
        print("User already exists.")

# Validate Login User
def login_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT role FROM Users WHERE username = ? AND password = ?
        ''', (username, hashed_password))
        user = cursor.fetchone()
    return user[0] if user else None
        
def logout_and_return_to_login(current_window):
    current_window.destroy()  # 关闭当前窗口
    login_screen()  # 返回登录界面
    
# Setup Borrowed Books Database
def setup_borrowed_books_database():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS BorrowedBooks (
            borrowed_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            book_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            quantity INTEGER NOT NULL CHECK (quantity > 0),
            borrow_date DATE NOT NULL,
            return_date DATE NOT NULL,
            status TEXT DEFAULT 'borrowed',  
            FOREIGN KEY (book_id) REFERENCES Books(book_id),
            UNIQUE(username, book_id)
        )
        ''')
        conn.commit()

# Display Books
def show_books(order_by=None, order_direction="ASC"):
    query = "SELECT * FROM Books"
    if order_by:
        query += f" ORDER BY {order_by} {order_direction}"
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()


# Display Borrowed Books for a User
def show_borrowed_books(username):
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM BorrowedBooks WHERE username = ? AND status='borrowed' ", (username,))
        return cursor.fetchall()

# Display Borrowed Books for All Users
def show_all_borrowed_books():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM BorrowedBooks')
        return cursor.fetchall()

# Display Users Who Borrowed a Specific Book
def show_users_for_book(book_id):
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM BorrowedBooks WHERE book_id = ?', (book_id,))
        return cursor.fetchall()
    
def show_borrow_history(username=None):
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        if username:
            # Fetch history for a specific user
            cursor.execute('''
                SELECT title, borrow_date, return_date, status 
                FROM BorrowedBooks 
                WHERE username = ?
                ORDER BY borrow_date DESC
            ''', (username,))
        else:
            # Fetch history for all users
            cursor.execute('''
                SELECT username, title, borrow_date, return_date, status 
                FROM BorrowedBooks
                ORDER BY borrow_date DESC
            ''')
        return cursor.fetchall()



def view_all_borrow_history():
    history_window = tk.Toplevel()
    history_window.title("All Borrow Histories")
    history_window.geometry("900x600")

    columns = ('Username', 'Title', 'Borrow Date', 'Return Date', 'Due Date', 'Status')
    history_tree = ttk.Treeview(history_window, columns=columns, show='headings', height=15)

    for col in columns:
        history_tree.heading(col, text=col)
        history_tree.column(col, width=120 if col != 'Title' else 200)

    history_tree.pack(pady=20)
    history = show_borrow_history()

    for record in history:
        username, title, borrow_date, return_date, status = record
        if status == 'returned':
            due_date = "-"
        else:  # 书籍未归还
            due_date = return_date
            return_date = "-"
        history_tree.insert('', 'end', values=(username, title, borrow_date, return_date, due_date, status))
    history_window.mainloop()


def add_book(title, author, nationality, isbn, shelf_number, total_quantity, available_quantity):
    if total_quantity <= 0 or available_quantity < 0:
        raise ValueError("Total quantity must be greater than 0 and available quantity must be non-negative.")
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO Books (title, author, nationality, isbn, shelf_number, total_quantity, available_quantity)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (title, author, nationality, isbn, shelf_number, total_quantity, available_quantity))
        conn.commit()

def update_book(book_id, title, author, nationality, isbn, shelf_number, total_quantity, available_quantity):
    if total_quantity <= 0 or available_quantity < 0 or available_quantity > total_quantity:
        raise ValueError("Total quantity must be greater than 0, available quantity must be non-negative, and available quantity cannot exceed total quantity.")
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE Books SET title = ?, author = ?, nationality = ?, isbn = ?, shelf_number = ?, 
                        total_quantity = ?, available_quantity = ? WHERE book_id = ?
        ''', (title, author, nationality, isbn, shelf_number, total_quantity, available_quantity, book_id))
        conn.commit()

# Delete Book
def delete_book(book_id):
    if book_id <= 0:
        raise ValueError("Book ID must be a positive integer.")
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Books WHERE book_id = ?', (book_id,))
        conn.commit()

# Search Books
def search_books(query, search_by_title=False, search_by_author=False, search_by_isbn=False, search_by_nationality=False):
    conditions = []
    params = []

    # 根据用户的复选框选择和输入来设置查询条件
    if not query.strip():  # 查询为空时返回所有书籍
        query_string = "SELECT * FROM Books"
    else:
        # 根据勾选的复选框添加条件
        if search_by_title:
            conditions.append("title LIKE ?")
            params.append(f"%{query}%")
        if search_by_author:
            conditions.append("author LIKE ?")
            params.append(f"%{query}%")
        if search_by_isbn:
            conditions.append("isbn LIKE ?")
            params.append(f"%{query}%")
        if search_by_nationality:
            conditions.append("nationality LIKE ?")
            params.append(f"%{query}%")

        # 没有选择任何复选框时，默认搜索所有四个字段
        if not conditions:
            conditions.append("title LIKE ? OR author LIKE ? OR isbn LIKE ? OR nationality LIKE ?")
            params.extend([f"%{query}%"] * 4)
            
        # 创建查询语句，多个条件使用 OR 连接
        query_string = "SELECT * FROM Books WHERE " + " OR ".join(conditions)

    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query_string, params)
        return cursor.fetchall()


def open_data_analytics_window(analysis_type):
    def fetch_data(query):
        with sqlite3.connect('library.db') as conn:
            return pd.read_sql_query(query, conn)

    if analysis_type == "most_borrowed":
        df = fetch_data(
            '''
            SELECT title, COUNT(*) as borrow_count 
            FROM BorrowedBooks 
            GROUP BY title 
            ORDER BY borrow_count DESC LIMIT 10'''
        )
        if not df.empty:
            plt.figure(figsize=(10, 6))
            plt.bar(df['title'], df['borrow_count'])
            plt.title("Most Borrowed Books")
            plt.xlabel("Book Title")
            plt.ylabel("Borrow Count")
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()

    elif analysis_type == "borrowing_trends":
        df = fetch_data(
            'SELECT strftime("%Y-%m", borrow_date) as month, COUNT(*) as borrow_count FROM BorrowedBooks GROUP BY month ORDER BY month'
        )
        if not df.empty:
            plt.figure(figsize=(10, 6))
            plt.plot(df['month'], df['borrow_count'], marker='o')
            plt.title("Borrowing Trends Over Time")
            plt.xlabel("Month")
            plt.ylabel("Number of Borrows")
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.tight_layout()
            plt.show()

    elif analysis_type == "top_borrowers":
        df = fetch_data(
            'SELECT username, COUNT(*) as borrow_count FROM BorrowedBooks GROUP BY username ORDER BY borrow_count DESC LIMIT 10'
        )
        if not df.empty:
            plt.figure(figsize=(10, 6))
            plt.bar(df['username'], df['borrow_count'])
            plt.title("Top Borrowers")
            plt.xlabel("Username")
            plt.ylabel("Borrow Count")
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()

    elif analysis_type == "inventory_analysis":
        df = fetch_data(
            'SELECT title, available_quantity FROM Books WHERE available_quantity < 5 ORDER BY available_quantity ASC'
        )
        if not df.empty:
            plt.figure(figsize=(10, 6))
            plt.bar(df['title'], df['available_quantity'], color='orange')
            plt.title("Low Inventory Books")
            plt.xlabel("Book Title")
            plt.ylabel("Available Quantity")
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()




def check_due_dates(username):
    """
    检查用户的借阅记录，查找即将到期的书籍（7天内）。
    """
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        # 获取当前日期
        today = datetime.date.today()
        # 计算提醒日期范围（7天内）
        reminder_date = today + datetime.timedelta(days=7)
        
        # 查询用户的借阅记录，查找还书日期在未来7天内的书籍
        cursor.execute('''
            SELECT title, return_date FROM BorrowedBooks 
            WHERE username = ? AND return_date BETWEEN ? AND ?
        ''', (username, today, reminder_date))
        
        # 获取即将到期的书籍
        due_books = cursor.fetchall()
    
    return due_books

def add_status_column():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("ALTER TABLE BorrowedBooks ADD COLUMN status TEXT DEFAULT 'borrowed'")
            print("Status column added successfully.")
        except sqlite3.OperationalError:
            print("Status column already exists.")
        conn.commit()


def setup_reservations_database():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Reservations (
            reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            book_id INTEGER NOT NULL,
            reservation_date DATE NOT NULL,
            notified INTEGER DEFAULT 0,
            FOREIGN KEY (book_id) REFERENCES Books(book_id)
        )
        ''')
        conn.commit()
def check_reservations(username):
    available_reservations = []
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        # 查询当前用户的预约书籍，若有库存则获取
        cursor.execute('''
        SELECT Reservations.book_id, Books.title 
        FROM Reservations 
        JOIN Books ON Reservations.book_id = Books.book_id 
        WHERE Reservations.username = ? AND Books.available_quantity > 0 AND Reservations.notified = 0
        ''', (username,))
        available_reservations = cursor.fetchall()
        
        # 将通知标记为已提醒
        if available_reservations:
            cursor.execute('''
            UPDATE Reservations SET notified = 1 WHERE username = ? AND book_id IN ({})
            '''.format(','.join([str(res[0]) for res in available_reservations])), (username,))
            conn.commit()
    
    return available_reservations
def confirm_borrow_reserved_book(username, book_id):
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        
        # 减少库存并插入到 BorrowedBooks 表中
        cursor.execute('SELECT title, available_quantity FROM Books WHERE book_id = ?', (book_id,))
        book_info = cursor.fetchone()
        title, available_quantity = book_info if book_info else (None, 0)
        
        if title and available_quantity > 0:
            new_quantity = available_quantity - 1
            borrow_date = datetime.date.today()
            return_date = borrow_date + datetime.timedelta(days=28)
            
            # 更新书籍库存
            cursor.execute('UPDATE Books SET available_quantity = ? WHERE book_id = ?', (new_quantity, book_id))
            # 添加到 BorrowedBooks 表
            cursor.execute('''
            INSERT INTO BorrowedBooks (username, book_id, title, quantity, borrow_date, return_date) 
            VALUES (?, ?, ?, 1, ?, ?)
            ''', (username, book_id, title, borrow_date, return_date))
            # 删除预约记录
            cursor.execute('DELETE FROM Reservations WHERE username = ? AND book_id = ?', (username, book_id))
            conn.commit()
            
            messagebox.showinfo("Borrow Book", f"'{title}' borrowed successfully.")

# User Dashboard
def user_dashboard(username):
    def display_books(books):
        # 清空现有数据
        for row in book_tree.get_children():
            book_tree.delete(row)
        # 插入每本书的信息，包括所有新字段
        for book in books:
            book_tree.insert('', 'end', values=(book[0], book[1], book[2], book[3], book[4], book[5], book[6], book[7]))
        print("Books displayed:", books)  # 调试输出
  
    def sort_by_column(col, reverse=False):
        # col 为列名，reverse 为布尔值，True 时表示降序，False 时表示升序
        order_direction = "DESC" if reverse else "ASC"
        display_books(show_books(order_by=col, order_direction=order_direction))

    def display_borrowed_books(borrowed_books):
        for row in borrowed_book_tree.get_children():
            borrowed_book_tree.delete(row)
        for book in borrowed_books:
            borrowed_book_tree.insert('', 'end', values=(book[1], book[2], book[3], book[4], book[5], book[6]))  # 借阅日期和到期日期
        print("Borrowed books displayed:", borrowed_books)

    def borrow_selected_book():
        try:
            selected_item = book_tree.selection()[0]
            book_id = int(book_tree.item(selected_item)['values'][0])
            title = book_tree.item(selected_item)['values'][1]
            available_quantity = int(book_tree.item(selected_item)['values'][7])

            if available_quantity > 0:
                # 获取当前日期
                borrow_date = datetime.date.today()
                # 设置应还日期为借书日期后的28天
                return_date = borrow_date + datetime.timedelta(days=28)

                new_quantity = available_quantity - 1
                with sqlite3.connect('library.db') as conn:
                    cursor = conn.cursor()
                    # 更新 Books 表中的 available_quantity
                    cursor.execute('''
                    UPDATE Books SET available_quantity = ? WHERE book_id = ?
                    ''', (new_quantity, book_id))

                    # 插入或更新 BorrowedBooks 表，包括 borrow_date 和 return_date
                    cursor.execute('''
                    INSERT INTO BorrowedBooks (username, book_id, title, quantity, borrow_date, return_date) 
                    VALUES (?, ?, ?, 1, ?, ?)
                    ON CONFLICT(username, book_id) 
                    DO UPDATE SET quantity = quantity + 1
                    ''', (username, book_id, title, borrow_date, return_date))

                    conn.commit()
                display_books(show_books())  # 刷新书籍列表
                display_borrowed_books(show_borrowed_books(username))  # 刷新借阅的书籍列表
                
            else:
                # messagebox.showerror("Error", "No copies available to borrow.")
                            # 无库存，提示预约
                if messagebox.askyesno("Out of Stock", "This book is currently unavailable. Would you like to reserve it?"):
                    with sqlite3.connect('library.db') as conn:
                        cursor = conn.cursor()
                        reservation_date = datetime.date.today()
                        cursor.execute('''
                        INSERT INTO Reservations (username, book_id, reservation_date)
                        VALUES (?, ?, ?)
                        ''', (username, book_id, reservation_date))
                        conn.commit()
                    messagebox.showinfo("Reservation", "Book reserved successfully. You will be notified when it becomes available.")

        except IndexError:
            messagebox.showerror("Error", "Please select a book to borrow.")
   
    def return_selected_book():
        try:
            # 获取选中的借阅记录
            selected_item = borrowed_book_tree.selection()[0]
            selected_values = borrowed_book_tree.item(selected_item)['values']
            
            # 从选中的行中提取所需信息
            username = selected_values[0]
            book_id = int(selected_values[1])
            quantity = int(selected_values[3])
            return_date = datetime.date.today()

            with sqlite3.connect('library.db') as conn:
                cursor = conn.cursor()

                # 获取当前的 total_quantity 和 available_quantity
                cursor.execute('SELECT total_quantity, available_quantity FROM Books WHERE book_id = ?', (book_id,))
                book_info = cursor.fetchone()
                if not book_info:
                    messagebox.showerror("Error", "Book not found.")
                    return
                
                total_quantity, available_quantity = book_info

                # 检查是否可以增加 available_quantity
                if available_quantity >= total_quantity:
                    messagebox.showerror("Error", "Cannot return book. Available quantity already at maximum.")
                    return

                # 如果借阅数量为 1，则删除这条记录
                if quantity == 1:
                    cursor.execute('DELETE FROM BorrowedBooks WHERE username = ? AND book_id = ?', (username, book_id))
                else:
                    # 否则，只减少数量并更新 return_date
                    cursor.execute('''
                        UPDATE BorrowedBooks 
                        SET quantity = quantity - 1, return_date = ?, status = 'returned'
                        WHERE username = ? AND book_id = ?
                    ''', (return_date, username, book_id))

                # 更新 Books 表中的 available_quantity
                cursor.execute('''
                    UPDATE Books SET available_quantity = available_quantity + 1 WHERE book_id = ?
                ''', (book_id,))

                conn.commit()

            # 从 TreeView 中移除该条记录
            borrowed_book_tree.delete(selected_item)
            messagebox.showinfo("Success", "Book returned successfully!")

        except IndexError:
            messagebox.showerror("Error", "Please select a book to return.")

      
    def renew_selected_book():
        try:
            selected_item = borrowed_book_tree.selection()
            if not selected_item:
                messagebox.showerror("Error", "Please select a record to renew.")
                return

            selected_values = borrowed_book_tree.item(selected_item[0], 'values')
            if not selected_values:
                messagebox.showerror("Error", "Failed to retrieve selected record data.")
                return

            current_due_date = datetime.datetime.strptime(selected_values[5], '%Y-%m-%d').date()
            new_due_date = current_due_date + datetime.timedelta(days=28)

            with sqlite3.connect('library.db') as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE BorrowedBooks SET return_date = ? WHERE username = ? AND book_id = ?
                ''', (new_due_date, username, selected_values[1]))
                conn.commit()

            borrowed_book_tree.item(selected_item, values=(
                selected_values[0], selected_values[1], selected_values[2],
                selected_values[3], selected_values[4], new_due_date.strftime('%Y-%m-%d')
            ))
            messagebox.showinfo("Renew Book", "Book renewed successfully!")
        except IndexError:
            messagebox.showerror("Error", "Please select a valid record to renew.")
    
    def open_trend_books_window():
        # 显示流行图书和趋势分析窗口
        analysis_window = tk.Toplevel(user_window)
        analysis_window.title("Trend Books")
        analysis_window.geometry("300x250")
        analysis_options = [
            ("Most Borrowed Books", "most_borrowed"),
            ("Borrowing Trends", "borrowing_trends"),
            ("Top Borrowers", "top_borrowers"),
            ("Inventory Analysis", "inventory_analysis")
        ]
        
        tk.Label(analysis_window, text="Select Analysis", font=default_font).pack(pady=10)
        
        for option_text, option_value in analysis_options:
            tk.Button(analysis_window, text=option_text, font=default_font, width=20,
                      command=lambda opt=option_value: open_data_analytics_window(opt)).pack(pady=5)

    def view_borrow_history(username):
        history_window = tk.Toplevel()
        history_window.title("Borrow History")
        history_window.geometry("800x600")

        columns = ('Title', 'Borrow Date', 'Return Date', 'Status')
        history_tree = ttk.Treeview(history_window, columns=columns, show='headings', height=15)
        
        for col in columns:
            history_tree.heading(col, text=col)
            history_tree.column(col, width=150)

        history_tree.pack(pady=20)

        try:
            # Fetch the user's borrow history from the database
            history = show_borrow_history(username)

            # Insert each record into the treeview
            for record in history:
                history_tree.insert('', 'end', values=record)

            if not history:
                messagebox.showinfo("Info", "No borrow history available for this user.")

        except Exception as e:
            print(f"Error displaying borrow history: {e}")
            messagebox.showerror("Error", "Failed to retrieve borrow history. Please try again.")

        history_window.mainloop()
# Fetch borrow history from the BorrowedBooks table
  
    def show_borrow_history(username=None):
        with sqlite3.connect('library.db') as conn:
            cursor = conn.cursor()
            if username:
                # Fetch history for a specific user
                cursor.execute('''
                    SELECT title, borrow_date, return_date, status 
                    FROM BorrowedBooks 
                    WHERE username = ?
                    ORDER BY borrow_date DESC
                ''', (username,))
            else:
                # Fetch history for all users
                cursor.execute('''
                    SELECT username, title, borrow_date, return_date, status 
                    FROM BorrowedBooks
                    ORDER BY borrow_date DESC
                ''')
            return cursor.fetchall()


    user_window = tk.Tk()
    user_window.title("User Dashboard")
    user_window.geometry("900x800")
    user_window.resizable(False, False)

    title_font = font.Font(size=24, weight="bold")
    tk.Label(user_window, text="User Dashboard", font=title_font).pack(pady=20)

    # 定义复选框变量
    title_var = tk.BooleanVar()
    author_var = tk.BooleanVar()
    isbn_var = tk.BooleanVar()
    default_font = font.Font(size=14)

    # Search Books Section
    default_font = font.Font(size=14)
    search_frame = tk.Frame(user_window)
    search_frame.pack(pady=20)
        
    tk.Label(search_frame, text="Search Books", font=default_font).grid(row=0, column=0, padx=10, pady=5)
    search_entry = tk.Entry(search_frame, font=default_font)
    search_entry.grid(row=0, column=1, padx=10, pady=5)

    # 在右上角添加 "Log out" 按钮
    logout_button = tk.Button(user_window, text="Log out", command=lambda: logout_and_return_to_login(user_window), font=default_font)
    logout_button.place(x=700, y=10)  # 右上角位置
    tk.Button(search_frame, text="Search", command=lambda: display_books(search_books(search_entry.get(), title_var.get(), author_var.get(), isbn_var.get())), font=default_font).grid(row=0, column=2, padx=10, pady=5)
    tk.Checkbutton(search_frame, text="Title", variable=title_var, font=default_font).grid(row=1, column=0, padx=5, pady=5, sticky="w")
    tk.Checkbutton(search_frame, text="Author", variable=author_var, font=default_font).grid(row=1, column=1, padx=5, pady=5, sticky="w")
    tk.Checkbutton(search_frame, text="ISBN", variable=isbn_var, font=default_font).grid(row=1, column=2, padx=5, pady=5, sticky="w")

    # Book List Display using Treeview
    columns = ('ID', 'Title', 'Author', 'Nationality', 'ISBN', 'Shelf Number', 'Total Quantity', 'Available Quantity')
    book_tree = ttk.Treeview(user_window, columns=columns, show='headings', height=10)
    for col in columns:
        book_tree.heading(col, text=col, command=lambda _col=col: sort_by_column(_col, reverse=False))
        if col == 'ID':
            book_tree.column(col, minwidth=0, width=40)  # 调整 ID 列的宽度
        else:
            book_tree.column(col, minwidth=0, width=100)
    book_tree.pack(pady=10)

    display_books(show_books())  # Display all books initially


    button_frame1 = tk.Frame(user_window)
    button_frame1.pack(pady=10)
    tk.Button(button_frame1, text="Borrow Selected Book", command=borrow_selected_book, font=default_font).grid(row=0, column=0, padx=10)
    tk.Button(button_frame1, text="View Trend Books", command=lambda: open_data_analytics_window("most_borrowed"), font=default_font).grid(row=0, column=1, padx=10)

    # Borrowed Books Display using Treeview
    borrowed_columns = ('Username', 'Book ID', 'Title', 'Quantity', 'Borrow Date', 'Due Date')
    borrowed_book_tree = ttk.Treeview(user_window, columns=borrowed_columns, show='headings', height=5)
    for col in borrowed_columns:
        borrowed_book_tree.heading(col, text=col)
        borrowed_book_tree.column(col, minwidth=0, width=120)
    borrowed_book_tree.pack(pady=10)

    display_borrowed_books(show_borrowed_books(username))  # Display all borrowed books initially

    button_frame2 = tk.Frame(user_window)
    button_frame2.pack(pady=10)
    tk.Button(button_frame2, text="Return Selected Book", command=return_selected_book, font=default_font).grid(row=0, column=0, padx=10)
    tk.Button(button_frame2, text="Renew Selected Book", command=renew_selected_book, font=default_font).grid(row=0, column=1, padx=10)
    tk.Button(button_frame2, text="My Borrow History", command=lambda: view_borrow_history(username), font=default_font).grid(row=0, column=2, padx=10)

    user_window.mainloop()

# Admin Dashboard
def admin_dashboard():
    def display_books(books):
        # 清空现有数据
        for row in book_tree.get_children():
            book_tree.delete(row)
        # 插入每本书的信息，包括所有新字段
        for book in books:
            book_tree.insert('', 'end', values=(book[0], book[1], book[2], book[3], book[4], book[5], book[6], book[7]))
    
    def sort_by_column(col, reverse=False):
        order_direction = "DESC" if reverse else "ASC"
        display_books(show_books(order_by=col, order_direction=order_direction))

    def open_add_book_window():
        add_window = tk.Toplevel(admin_window)
        add_window.title("Add New Book")
        add_window.geometry("500x400")
        add_window.resizable(False, False)

        def add_new_book():
            title = title_entry.get()
            author = author_entry.get()
            nationality = nationality_entry.get()
            isbn = isbn_entry.get()
            shelf_number = shelf_entry.get()
            total_quantity = total_quantity_entry.get()
            available_quantity = available_quantity_entry.get()
                
            # ISBN 长度检查
            if len(isbn) != 13:
                messagebox.showerror("Error", "ISBN must be 13 characters long.")
                return
            
            print(f"Adding book with: title={title}, isbn={isbn}, author={author}, nationality={nationality}, "
                f"shelf_number={shelf_number}, total_quantity={total_quantity}, available_quantity={available_quantity}")

            if title and author and nationality and isbn and shelf_number and total_quantity.isdigit() and available_quantity.isdigit():
                total_quantity = int(total_quantity)
                available_quantity = int(available_quantity)
                if total_quantity > 0 and available_quantity >= 0 and available_quantity <= total_quantity:
                    add_book(title, author, nationality, isbn, shelf_number, total_quantity, available_quantity)
                    print("Add Book", "Book added successfully!")
                    display_books(show_books())  # 刷新书籍列表
                    add_window.destroy()
                else:
                    messagebox.showerror("Error", "Total quantity must be greater than 0, available quantity must be non-negative, and available quantity cannot exceed total quantity.")
            else:
                messagebox.showerror("Error", "Please fill in all fields correctly.")

        default_font = font.Font(size=14)

        tk.Label(add_window, text="Title", font=default_font).grid(row=0, column=0, padx=10, pady=5)
        title_entry = tk.Entry(add_window, font=default_font)
        title_entry.grid(row=0, column=1, padx=10, pady=7)

        tk.Label(add_window, text="Author", font=default_font).grid(row=1, column=0, padx=10, pady=5)
        author_entry = tk.Entry(add_window, font=default_font)
        author_entry.grid(row=1, column=1, padx=10, pady=7)
        tk.Label(add_window, text="Nationality", font=default_font).grid(row=2, column=0, padx=10, pady=5)
        nationality_entry = tk.Entry(add_window, font=default_font)
        nationality_entry.grid(row=2, column=1, padx=10, pady=7)
    
        tk.Label(add_window, text="ISBN", font=default_font).grid(row=3, column=0, padx=10, pady=5)
        isbn_entry = tk.Entry(add_window, font=default_font)
        isbn_entry.grid(row=3, column=1, padx=10, pady=7)      
        tk.Label(add_window, text="Shelf Number", font=default_font).grid(row=4, column=0, padx=10, pady=5)
        shelf_entry = tk.Entry(add_window, font=default_font)
        shelf_entry.grid(row=4, column=1, padx=10, pady=7)
        tk.Label(add_window, text="Total Quantity", font=default_font).grid(row=5, column=0, padx=10, pady=5)
        total_quantity_entry = tk.Entry(add_window, font=default_font)
        total_quantity_entry.grid(row=5, column=1, padx=10, pady=7)

        tk.Label(add_window, text="Available Quantity", font=default_font).grid(row=6, column=0, padx=10, pady=5)
        available_quantity_entry = tk.Entry(add_window, font=default_font)
        available_quantity_entry.grid(row=6, column=1, padx=10, pady=7)

        tk.Button(add_window, text="Add Book", command=add_new_book, font=default_font).grid(row=8, column=0, columnspan=2, pady=20)

    def open_update_book_window():
        try:
            selected_item = book_tree.selection()[0]
            book_id = int(book_tree.item(selected_item)['values'][0])
            selected_book = book_tree.item(selected_item)['values']
        except IndexError:
            messagebox.showerror("Error", "Please select a book to update.")
            return

        update_window = tk.Toplevel(admin_window)
        update_window.title("Update Book")
        update_window.geometry("500x450")
        update_window.resizable(False, False)

        def update_selected_book():
            title = title_entry.get()
            author = author_entry.get()
            nationality = nationality_entry.get()
            isbn = isbn_entry.get()
            shelf_number = shelf_entry.get()
            total_quantity = total_quantity_entry.get()
            available_quantity = available_quantity_entry.get()

            # ISBN length validation
            if len(isbn) != 13:
                messagebox.showerror("Error", "ISBN must be 13 characters long.")
                return

            if title and author and nationality and isbn and shelf_number and total_quantity.isdigit() and available_quantity.isdigit():
                total_quantity = int(total_quantity)
                available_quantity = int(available_quantity)
                if total_quantity > 0 and available_quantity >= 0 and available_quantity <= total_quantity:
                    update_book(book_id, title, author, nationality, isbn, shelf_number, total_quantity, available_quantity)
                    print("Update Book", "Book updated successfully!")
                    display_books(show_books())  # Refresh book list
                    update_window.destroy()
                else:
                    messagebox.showerror("Error", "Total quantity must be greater than 0, available quantity must be non-negative, and available quantity cannot exceed total quantity.")
            else:
                messagebox.showerror("Error", "Please fill in all fields correctly.")

        def delete_selected_book():
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this book?"):
                delete_book(book_id)
                print("Delete Book", "Book deleted successfully!")
                display_books(show_books())
                update_window.destroy()

        default_font = font.Font(size=14)

        # Layout for update book entries
        tk.Label(update_window, text="Title", font=default_font).grid(row=0, column=0, padx=10, pady=5)
        title_entry = tk.Entry(update_window, font=default_font)
        title_entry.insert(0, selected_book[1])
        title_entry.grid(row=0, column=1, padx=10, pady=7)

        tk.Label(update_window, text="Author", font=default_font).grid(row=1, column=0, padx=10, pady=5)
        author_entry = tk.Entry(update_window, font=default_font)
        author_entry.insert(0, selected_book[2])
        author_entry.grid(row=1, column=1, padx=10, pady=7)

        tk.Label(update_window, text="Nationality", font=default_font).grid(row=2, column=0, padx=10, pady=5)
        nationality_entry = tk.Entry(update_window, font=default_font)
        nationality_entry.insert(0, selected_book[3])
        nationality_entry.grid(row=2, column=1, padx=10, pady=7)

        tk.Label(update_window, text="ISBN", font=default_font).grid(row=3, column=0, padx=10, pady=5)
        isbn_entry = tk.Entry(update_window, font=default_font)
        isbn_entry.insert(0, selected_book[4])
        isbn_entry.grid(row=3, column=1, padx=10, pady=7)

        tk.Label(update_window, text="Shelf Number", font=default_font).grid(row=4, column=0, padx=10, pady=5)
        shelf_entry = tk.Entry(update_window, font=default_font)
        shelf_entry.insert(0, selected_book[5])
        shelf_entry.grid(row=4, column=1, padx=10, pady=7)

        tk.Label(update_window, text="Total Quantity", font=default_font).grid(row=5, column=0, padx=10, pady=5)
        total_quantity_entry = tk.Entry(update_window, font=default_font)
        total_quantity_entry.insert(0, selected_book[6])
        total_quantity_entry.grid(row=5, column=1, padx=10, pady=7)

        tk.Label(update_window, text="Available Quantity", font=default_font).grid(row=6, column=0, padx=10, pady=5)
        available_quantity_entry = tk.Entry(update_window, font=default_font)
        available_quantity_entry.insert(0, selected_book[7])
        available_quantity_entry.grid(row=6, column=1, padx=10, pady=7)

        # Buttons for Update and Delete
        tk.Button(update_window, text="Update Book", command=update_selected_book, font=default_font).grid(row=7, column=0, columnspan=2, pady=20)
        tk.Button(update_window, text="Delete Book", command=delete_selected_book, font=default_font).grid(row=8, column=0, columnspan=2, pady=10)
    
    def view_users_for_selected_book():
        try:
            selected_item = book_tree.selection()[0]
            book_id = int(book_tree.item(selected_item)['values'][0])
        except IndexError:
            messagebox.showerror("Error", "Please select a book to view borrowed users.")
            return

        # 创建一个新窗口来显示借阅此书的用户
        borrowed_users_window = tk.Toplevel(admin_window)
        borrowed_users_window.title("Users Who Borrowed This Book")
        borrowed_users_window.geometry("600x450")
        borrowed_users_window.resizable(False, False)

        borrowed_users_columns = ('Username', 'Book ID', 'Title', 'Borrow Date', 'Due Date')
        borrowed_users_tree = ttk.Treeview(borrowed_users_window, columns=borrowed_users_columns, show='headings', height=10)
        
        borrowed_users_tree.heading('Username', text='Username')
        borrowed_users_tree.heading('Book ID', text='Book ID')
        borrowed_users_tree.heading('Title', text='Title')
        borrowed_users_tree.heading('Borrow Date', text='Borrow Date')
        borrowed_users_tree.heading('Due Date', text='Due Date')
        
        borrowed_users_tree.column('Username', width=120)
        borrowed_users_tree.column('Book ID', width=40)
        borrowed_users_tree.column('Title', width=200)
        borrowed_users_tree.column('Borrow Date', width=120)
        borrowed_users_tree.column('Due Date', width=120)

        borrowed_users_tree.pack(pady=10)

        # 获取并显示借阅此书的用户信息，包括借阅日期和到期日期
        with sqlite3.connect('library.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT username, book_id, title, borrow_date, return_date 
                FROM BorrowedBooks 
                WHERE book_id = ?
            ''', (book_id,))
            borrowed_users = cursor.fetchall()

        for user in borrowed_users:
            borrowed_users_tree.insert('', 'end', values=user)
        
        def return_selected_book():
            try:
                # 获取选中的借阅记录
                selected_item = borrowed_users_tree.selection()[0]
                selected_values = borrowed_users_tree.item(selected_item)['values']
                # 提取所需信息
                username = selected_values[0]
                book_id = int(selected_values[1])
                title = selected_values[2]
                quantity = int(selected_values[3])
                
                return_date = datetime.date.today()

                with sqlite3.connect('library.db') as conn:
                    cursor = conn.cursor()
                    
                    cursor.execute('SELECT total_quantity, available_quantity FROM Books WHERE book_id = ?', (book_id,))
                    book_info = cursor.fetchone()
            
                    # 检查书籍是否存在
                    if not book_info:
                        messagebox.showerror("Error", "Books not found.")
                        return

                    total_quantity, available_quantity = book_info

                    # 检查库存是否已满
                    if available_quantity >= total_quantity:
                        messagebox.showerror("Error", "Cannot return book. Available quantity already at maximum.")
                        return


                    # 更新 `BorrowedBooks` 表的 `status` 和 `return_date`
                    cursor.execute('''
                        UPDATE BorrowedBooks 
                        SET status = 'returned', return_date = ? 
                        WHERE username = ? AND book_id = ? AND status = 'borrowed'
                    ''', (datetime.date.today(), username, book_id))

                    # 更新 `Books` 表的 `available_quantity`
                    cursor.execute('''
                        UPDATE Books 
                        SET available_quantity = available_quantity + 1 
                        WHERE book_id = ?
                    ''', (book_id,))

                    conn.commit()
                    
                # Refresh the table view
                borrowed_users_tree.delete(selected_item)
                messagebox.showinfo("Return Book", "Book returned successfully!")

            except IndexError:
                messagebox.showerror("Error", "Please select a record to return.")

        # 创建并添加 "Return Books" 按钮
        return_button = tk.Button(borrowed_users_window, text="Return Books", command=return_selected_book, font=font.Font(size=12))
        return_button.pack(pady=10)
    
    def view_borrowed_books():
        
        borrowed_books_window = tk.Toplevel(admin_window)
        borrowed_books_window.title("Borrowed Books")
        borrowed_books_window.geometry("800x500")
        borrowed_books_window.resizable(False, False)

        borrowed_books_columns = ('Username','Book ID', 'Book Name','Quantity', 'Borrow Date', 'Due Date')
        borrowed_books_tree = ttk.Treeview(borrowed_books_window, columns=borrowed_books_columns, show='headings', height=10)
        
        # 设置表头和列宽度
        borrowed_books_tree.heading('Username', text='Username')
        borrowed_books_tree.heading('Book ID', text='Book ID')
        borrowed_books_tree.heading('Book Name', text='Book Name')
        borrowed_books_tree.heading('Quantity', text='Quantity')
        borrowed_books_tree.heading('Borrow Date', text='Borrow Date')
        borrowed_books_tree.heading('Due Date', text='Due Date')

        # 调整列的宽度
        borrowed_books_tree.column('Username', width=80)
        borrowed_books_tree.column('Book ID', width=60)
        borrowed_books_tree.column('Book Name', width=200)
        borrowed_books_tree.column('Quantity', width=70)
        borrowed_books_tree.column('Borrow Date', width=100)
        borrowed_books_tree.column('Due Date', width=100)
        
        # 从数据库中获取借阅的书籍信息
        borrowed_books_tree.pack(pady=10)

        borrowed_books = show_all_borrowed_books()
        for book in borrowed_books:
            username = book[1]
            book_id = book[2]
            book_name=book[3]
            quantity = book[4]
            borrow_date = book[5]
            return_date = book[6]
            # 按照新的表头顺序插入数据
            borrowed_books_tree.insert('', 'end', values=(username, book_id,book_name, quantity, borrow_date, return_date))
        '''
        borrowed_books_tree.heading('Book ID', text='Book ID')
        borrowed_books_tree.heading('Username', text='Username')
        borrowed_books_tree.heading('Title', text='Title')
        borrowed_books_tree.heading('Quantity', text='Quantity')
        borrowed_books_tree.heading('Borrow Date', text='Borrow Date')
        borrowed_books_tree.heading('Due Date', text='Due Date')
        
        borrowed_books_tree.column('Book ID', width=40)
        borrowed_books_tree.column('Username', width=120)
        borrowed_books_tree.column('Title', width=200)
        borrowed_books_tree.column('Quantity', width=60)
        borrowed_books_tree.column('Borrow Date', width=120)
        borrowed_books_tree.column('Due Date', width=120)        
        
        borrowed_books_tree.pack(pady=10)

        # Retrieve borrowed books and insert them into the tree view in the correct order
        borrowed_books = show_all_borrowed_books()
        for book in borrowed_books:
            # Adjust the order of `book` tuple to match the column order
            borrowed_books_tree.insert('', 'end', values=(book[1], book[0], book[2], book[3], book[4], book[5]))
        '''
        def return_selected_book():
            try:
                selected_item = borrowed_books_tree.selection()[0]
                selected_values = borrowed_books_tree.item(selected_item)['values']
                book_id = selected_values[0]
                username = selected_values[1]
                quantity = selected_values[3]
                
                with sqlite3.connect('library.db') as conn:
                    cursor = conn.cursor()
                    # 获取当前的 total_quantity 和 available_quantity
                    cursor.execute('SELECT total_quantity, available_quantity FROM Books WHERE book_id = ?', (book_id,))
                    book_info = cursor.fetchone()
                    if not book_info:
                        messagebox.showerror("Error", "Book not found.")
                        return
                    
                    total_quantity, available_quantity = book_info

                    # 检查是否可以增加 available_quantity
                    if available_quantity >= total_quantity:
                        messagebox.showerror("Error", "Cannot return book. Available quantity already at maximum.")
                        return

                    # Delete the record from BorrowedBooks table if quantity is 1
                    if quantity == 1:
                        cursor.execute('DELETE FROM BorrowedBooks WHERE username = ? AND book_id = ?', (username, book_id))
                        cursor.execute('''
                            UPDATE BorrowedBooks 
                            SET status = 'returned', return_date = ? 
                            WHERE username = ? AND book_id = ?
                        ''', (datetime.date.today(), username, book_id))
                    else:
                        # Otherwise, reduce quantity by 1
                        cursor.execute('''
                            UPDATE BorrowedBooks 
                            SET quantity = quantity - 1 
                            WHERE username = ? AND book_id = ?
                        ''', (username, book_id))

                    # Update the available_quantity in Books table
                    cursor.execute('''
                        UPDATE Books SET available_quantity = available_quantity + 1 WHERE book_id = ?
                    ''', (book_id,))
                    
                    conn.commit()
                
                borrowed_books_tree.delete(selected_item)
                messagebox.showinfo("Return Book", "Book returned successfully!")
            except IndexError:
                messagebox.showerror("Error", "Please select a record to return.")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        def renew_selected_book():
            try:
                # 获取选中的行
                selected_item = borrowed_books_tree.selection()
                if not selected_item:
                    messagebox.showerror("Error", "Please select a record to renew.")
                    return

                # 获取选中的行的数据
                selected_values = borrowed_books_tree.item(selected_item[0], 'values')

                # 验证是否成功获取到数据
                if not selected_values:
                    messagebox.showerror("Error", "Failed to retrieve selected record data.")
                    return

                # 从选中的行中提取所需数据
                username = selected_values[0]
                book_id = selected_values[1]

                # 获取当前的还书日期，并延长 28 天
                current_due_date = datetime.datetime.strptime(selected_values[5], '%Y-%m-%d').date()
                new_due_date = current_due_date + datetime.timedelta(days=28)

                # 更新数据库中的 return_date
                with sqlite3.connect('library.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute('''
                        UPDATE BorrowedBooks SET return_date = ? WHERE username = ? AND book_id = ?
                    ''', (new_due_date, username, book_id))
                    conn.commit()

                # 更新 Treeview 显示
                borrowed_books_tree.item(selected_item, values=(
                    selected_values[0], selected_values[1], selected_values[2],
                    selected_values[3], selected_values[4], new_due_date.strftime('%Y-%m-%d')
                ))
                messagebox.showinfo("Renew Book", "Book renewed successfully!")
            except IndexError:
                messagebox.showerror("Error", "Please select a valid record to renew.")

        # 添加按钮
        tk.Button(borrowed_books_window, text="Return Book", command=return_selected_book, font=font.Font(size=12)).pack(pady=10)
        tk.Button(borrowed_books_window, text="Renew Book", command=renew_selected_book, font=font.Font(size=12)).pack(pady=10)
    def show_all_borrowed_books():
        with sqlite3.connect('library.db') as conn:
            cursor = conn.cursor()
            # 确保查询包含所有状态的记录
            cursor.execute('SELECT * FROM BorrowedBooks')
            return cursor.fetchall()

    def show_borrow_history(username=None):
        with sqlite3.connect('library.db') as conn:
            cursor = conn.cursor()
            if username:
                cursor.execute('''
                    SELECT title, borrow_date, return_date, status 
                    FROM BorrowedBooks 
                    WHERE username = ?
                    ORDER BY borrow_date DESC
                ''', (username,))
            else:
                cursor.execute('''
                    SELECT username, title, borrow_date, return_date, status 
                    FROM BorrowedBooks
                    ORDER BY borrow_date DESC
                ''')
            return cursor.fetchall()

    def view_users_for_selected_book():
        try:
            selected_item = book_tree.selection()[0]
            book_id = int(book_tree.item(selected_item)['values'][0])
        except IndexError:
            messagebox.showerror("Error", "Please select a book to view borrowed users.")
            return

        # 创建一个新窗口来显示借阅此书的用户
        borrowed_users_window = tk.Toplevel(admin_window)
        borrowed_users_window.title("Users Who Borrowed This Book")
        borrowed_users_window.geometry("700x500")
        borrowed_users_window.resizable(False, False)

        borrowed_users_columns = ('Username', 'Book ID', 'Title', 'Borrow Date', 'Due Date')
        borrowed_users_tree = ttk.Treeview(borrowed_users_window, columns=borrowed_users_columns, show='headings', height=10)
        
        borrowed_users_tree.heading('Username', text='Username')
        borrowed_users_tree.heading('Book ID', text='Book ID')
        borrowed_users_tree.heading('Title', text='Title')
        borrowed_users_tree.heading('Borrow Date', text='Borrow Date')
        borrowed_users_tree.heading('Due Date', text='Due Date')
        
        borrowed_users_tree.column('Username', width=120)
        borrowed_users_tree.column('Book ID', width=40)
        borrowed_users_tree.column('Title', width=200)
        borrowed_users_tree.column('Borrow Date', width=120)
        borrowed_users_tree.column('Due Date', width=120)
        
        borrowed_users_tree.pack(pady=10)

        # 设置Return和Renew的按钮
        borrow_button = tk.Button(button_frame, text="Rerurn Book", command=return_selected_book(), font=font.Font(size=12))
        borrow_button.grid(row=1, column=0, padx=10)

        renew_button = tk.Button(button_frame, text="Renew Book", command=renew_selected_user_book(), font=font.Font(size=12))
        renew_button.grid(row=1, column=1, padx=10)


        # 获取并显示借阅此书的用户信息，包括借阅日期和到期日期
        with sqlite3.connect('library.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT username, book_id, title, borrow_date, return_date 
                FROM BorrowedBooks 
                WHERE book_id = ?
            ''', (book_id,))
            borrowed_users = cursor.fetchall()

        for user in borrowed_users:
            borrowed_users_tree.insert('', 'end', values=user)
            
        
        # 将 return_selected_book 函数移到循环外部
        def return_selected_book():
            try:
                selected_item = borrowed_users_tree.selection()[0]
                selected_values = borrowed_users_tree.item(selected_item)['values']

                username = selected_values[0]
                book_id = selected_values[1]
                title = selected_values[2]
                quantity = int(selected_values[3])
                return_date = datetime.date.today()

                with sqlite3.connect('library.db') as conn:
                    cursor = conn.cursor()

                    # 检查书籍库存是否可以增加
                    cursor.execute('SELECT total_quantity, available_quantity FROM Books WHERE book_id = ?', (book_id,))
                    
                    book_info = cursor.fetchone()
                    
                    if not book_info:
                        messagebox.showerror("Error", "Book not found.")
                        return

                    total_quantity, available_quantity = book_info

                    if available_quantity >= total_quantity:
                        messagebox.showerror("Error", "Cannot return book. Available quantity already at maximum.")
                        return

                    # 更新 BorrowedBooks 表的 status 和 return_date
                    cursor.execute('''
                        UPDATE BorrowedBooks 
                        SET status = 'returned', return_date = ? 
                        WHERE username = ? AND book_id = ? AND status = 'borrowed'
                    ''', (return_date, username, book_id))

                    # 更新 Books 表中的 available_quantity
                    cursor.execute('''
                        UPDATE Books SET available_quantity = available_quantity + 1 WHERE book_id = ?
                    ''', (book_id,))

                    conn.commit()
                    
                    # borrowed_books_tree.delete(selected_item)

                messagebox.showinfo("Success", "Book returned successfully!")
                
                # 刷新列表
                borrowed_users_tree.delete(selected_item)

            except IndexError:
                messagebox.showerror("Error", "Please select a record to return.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

        def renew_selected_user_book():
            try:
                # 获取选中的行
                selected_item = borrowed_users_tree.selection()
                if not selected_item:
                    messagebox.showerror("Error", "Please select a record to renew.")
                    return

                # 获取选中的行的数据
                selected_values = borrowed_users_tree.item(selected_item[0], 'values')
                
                # 验证是否成功获取到数据
                if not selected_values:
                    messagebox.showerror("Error", "Failed to retrieve selected record data.")
                    return
                
                # 从选中的行中提取所需数据
                username = selected_values[0]
                book_id = selected_values[1]

                # 获取当前的还书日期，并延长 28 天
                current_due_date = datetime.datetime.strptime(selected_values[4], '%Y-%m-%d').date()
                new_due_date = current_due_date + datetime.timedelta(days=28)

                # 更新数据库中的 return_date
                with sqlite3.connect('library.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute('''
                        UPDATE BorrowedBooks SET return_date = ? WHERE username = ? AND book_id = ?
                    ''', (new_due_date, username, book_id))
                    conn.commit()

                # 更新 Treeview 显示
                borrowed_users_tree.item(selected_item, values=(
                    selected_values[0], selected_values[1], selected_values[2],
                    selected_values[3], selected_values[4], new_due_date.strftime('%Y-%m-%d')
                ))
                messagebox.showinfo("Renew Book", "Book renewed successfully!")
                # 刷新表格以显示更新后的数据
                refresh_borrowed_users_tree(book_id)
            except IndexError as e:
                print(f"Error: {e}")
                messagebox.showerror("Error", "Please select a valid record to renew.")

        def refresh_borrowed_users_tree(book_id):
            """刷新 'Users Who Borrowed This Book' 窗口中的表格数据"""
            # 清空表格中的现有数据
            for row in borrowed_users_tree.get_children():
                borrowed_users_tree.delete(row)
            
            # 重新从数据库中获取数据
            with sqlite3.connect('library.db') as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT username, book_id, title, borrow_date, return_date 
                    FROM BorrowedBooks 
                    WHERE book_id = ?
                ''', (book_id,))
                borrowed_users = cursor.fetchall()

            # 重新插入数据到表格
            for user in borrowed_users:
                borrowed_users_tree.insert('', 'end', values=user)

    def open_borrow_book_window():
        '''
        if hasattr(open_borrow_book_window, "borrow_window") and open_borrow_book_window.borrow_window.winfo_exists():
            open_borrow_book_window.borrow_window.lift()  # 将已经打开的窗口置于前台
            return  # 直接返回，不再创建新窗口
        '''
        try:
            # 获取选中的书籍
            selected_item = book_tree.selection()[0]
            book_id = int(book_tree.item(selected_item)['values'][0])
            title = book_tree.item(selected_item)['values'][1]
            available_quantity = int(book_tree.item(selected_item)['values'][7])
            
            # 检查书籍是否可借
            if available_quantity <= 0:
                messagebox.showerror("Error", "No copies available to lend.")
                return

        except IndexError:
            messagebox.showerror("Error", "Please select a book to lend.")
            return

        # 打开借书窗口
        borrow_window = tk.Toplevel(admin_window)
        borrow_window.title("Lend Book")
        borrow_window.geometry("400x300")
        borrow_window.resizable(False, False)

        tk.Label(borrow_window, text="Lend Book", font=font.Font(size=18, weight='bold')).pack(pady=20)
        tk.Label(borrow_window, text=f"Book Title: {title}", font=font.Font(size=14)).pack(pady=10)

        tk.Label(borrow_window, text="Enter Username:", font=font.Font(size=12)).pack(pady=10)
        username_entry = tk.Entry(borrow_window, font=font.Font(size=12))
        username_entry.pack(pady=10)

        def confirm_borrow():
            username = username_entry.get().strip()

            if not username:
                messagebox.showerror("Error", "Username is required.")
                return

            # 检查用户是否存在
            with sqlite3.connect('library.db') as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT username FROM Users WHERE username = ?", (username,))
                user = cursor.fetchone()
            
            if not user:
                messagebox.showerror("Error", "User does not exist.")
                return

            # 借书操作
            borrow_date = datetime.date.today()
            return_date = borrow_date + datetime.timedelta(days=28)
            new_available_quantity = available_quantity - 1

            with sqlite3.connect('library.db') as conn:
                cursor = conn.cursor()
                
                # 更新 Books 表中的可用数量
                cursor.execute('''
                    UPDATE Books SET available_quantity = ? WHERE book_id = ?
                ''', (new_available_quantity, book_id))
                
                # 在 BorrowedBooks 表中插入借书记录
                cursor.execute('''
                    INSERT INTO BorrowedBooks (username, book_id, title, quantity, borrow_date, return_date)
                    VALUES (?, ?, ?, 1, ?, ?)
                    ON CONFLICT(username, book_id)
                    DO UPDATE SET quantity = quantity + 1
                ''', (username, book_id, title, borrow_date, return_date))
                
                conn.commit()

            # 刷新书籍列表
            display_books(show_books())
            messagebox.showinfo("Success", f"Book '{title}' successfully lent to {username}.")
            borrow_window.destroy()

        tk.Button(borrow_window, text="Confirm Lending", command=confirm_borrow, font=font.Font(size=12)).pack(pady=20)

        try:
            # 获取选中的书籍
            selected_item = book_tree.selection()[0]
            book_id = int(book_tree.item(selected_item)['values'][0])
            title = book_tree.item(selected_item)['values'][1]
            available_quantity = int(book_tree.item(selected_item)['values'][7])
            
            # 检查书籍是否可借
            if available_quantity <= 0:
                messagebox.showerror("Error", "No copies available to lend.")
                return

        except IndexError:
            messagebox.showerror("Error", "Please select a book to lend.")
            return

        # # 创建并添加 "Return Books" 按钮
        # return_button = tk.Button(borrow_window, text="Return Books", command=return_selected_book, font=font.Font(size=12))
        # renew_button=tk.Button(borrow_window, text="Renew Book", command=renew_selected_user_book, font=font.Font(size=12))
        # return_button.pack(pady=10)
        # renew_button.pack(pady=10) 
        
    # Delete Book Section
    '''   
    def delete_selected_book():
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this book?")
        if confirm:  # 如果用户选择 'Yes'
            delete_book(book_id)  # 调用删除函数
            print("Delete Book", "Book deleted successfully!")
            display_books(show_books())  # 刷新书籍列表
            update_window.destroy()  # 关闭 Update 窗口
    '''
    admin_window = tk.Tk()
    admin_window.title("Admin Dashboard")
    admin_window.geometry("900x800")
    admin_window.resizable(False, False)
    
    # 设置大标题字体
    title_font = font.Font(size=24, weight="bold")

    # 在顶部添加大标题
    title_label = tk.Label(admin_window, text="Admin Dashboard", font=title_font)
    title_label.pack(pady=20)
    

    default_font = font.Font(size=14)
    # 在右上角添加 "Log out" 按钮
    logout_button = tk.Button(admin_window, text="Log out", command=lambda: logout_and_return_to_login(admin_window), font=default_font)
    logout_button.place(x=700, y=10)  # 右上角位置
    
    
    # 定义复选框变量
    title_var = tk.BooleanVar()
    author_var = tk.BooleanVar()
    isbn_var = tk.BooleanVar()

    # Search Books Section
    search_frame = tk.Frame(admin_window)
    search_frame.pack(pady=20)

    tk.Label(search_frame, text="Search Books", font=default_font).grid(row=0, column=0, padx=10, pady=5)
    search_entry = tk.Entry(search_frame, font=default_font)
    search_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(search_frame, text="Search", command=lambda: display_books(search_books(search_entry.get(), title_var.get(), author_var.get(), isbn_var.get())), font=default_font).grid(row=0, column=2, padx=10, pady=5)
    tk.Checkbutton(search_frame, text="Title", variable=title_var, font=default_font).grid(row=1, column=0, padx=5, pady=5, sticky="w")
    tk.Checkbutton(search_frame, text="Author", variable=author_var, font=default_font).grid(row=1, column=1, padx=5, pady=5, sticky="w")
    tk.Checkbutton(search_frame, text="ISBN", variable=isbn_var, font=default_font).grid(row=1, column=2, padx=5, pady=5, sticky="w")

    # Book List Display using Treeview
    columns = ('ID', 'Title', 'Author', 'Nationality', 'ISBN', 'Shelf Number', 'Total Quantity', 'Available Quantity')
    book_tree = ttk.Treeview(admin_window, columns=columns, show='headings', height=10)
    for col in columns:
        book_tree.heading(col, text=col, command=lambda _col=col: sort_by_column(_col, reverse=False))
        if col == 'ID':
            book_tree.column(col, minwidth=0, width=40)  # 调整 ID 列的宽度
        else:
            book_tree.column(col, minwidth=0, width=100)
    book_tree.pack(pady=10)


    display_books(show_books())  # Display all books initially

    # 创建按钮的三个列布局
    button_frame = tk.Frame(admin_window)
    button_frame.pack(pady=20)

    # 第一列按钮布局
    column1 = tk.Frame(button_frame)
    column1.grid(row=0, column=0, padx=20)

    tk.Button(column1, text="Add Book", command=open_add_book_window, font=default_font, width=20).pack(pady=10)
    tk.Button(column1, text="Edit Selected Book", command=open_update_book_window, font=default_font, width=20).pack(pady=10)
    tk.Button(column1, text="Lend Selected Book", command=open_borrow_book_window, font=default_font, width=20).pack(pady=10)

    # 第二列按钮布局
    column2 = tk.Frame(button_frame)
    column2.grid(row=0, column=1, padx=20)

    tk.Button(column2, text="View All Lending Books ", command=view_borrowed_books, font=default_font, width=25).pack(pady=10)
    tk.Button(column2, text="Users Borrowing This Book", command=view_users_for_selected_book, font=default_font, width=25).pack(pady=10)

    # 第三列按钮布局 (Data Analytics)
    column3 = tk.Frame(button_frame)
    column3.grid(row=0, column=2, padx=20)

    tk.Button(column3, text="Most Borrowed Books", command=lambda: open_data_analytics_window("most_borrowed"), font=default_font, width=20).pack(pady=10)
    tk.Button(column3, text="Borrowing Trends", command=lambda: open_data_analytics_window("borrowing_trends"), font=default_font, width=20).pack(pady=10)
    tk.Button(column3, text="Top Borrowers", command=lambda: open_data_analytics_window("top_borrowers"), font=default_font, width=20).pack(pady=10)
    tk.Button(column3, text="Low Inventory Books", command=lambda: open_data_analytics_window("inventory_analysis"), font=default_font, width=20).pack(pady=10)
    
    # 添加 "View All Borrow Histories" 按钮
    view_all_history_button = tk.Button(admin_window, text="View All Borrow Histories",
                                        command=view_all_borrow_history, font=font.Font(size=14))
    view_all_history_button.pack(pady=20)

    admin_window.mainloop()

def IT_admin_dashboard():
    def display_users(users):
        for row in user_tree.get_children():
            user_tree.delete(row)
        for user in users:
            user_tree.insert('', 'end', values=(user[0], user[1], user[3]))  # 不显示密码
 
    def sort_by_column(col, reverse=False):
        order_direction = "DESC" if reverse else "ASC"
        display_users(fetch_all_users(order_by=col, order_direction=order_direction))

    def fetch_all_users():
        with sqlite3.connect('library.db') as conn:
            cursor = conn.cursor()
            # cursor.execute("SELECT * FROM Users WHERE role != 'IT_admin'")
            cursor.execute("SELECT * FROM Users")
            
            return cursor.fetchall()

    def open_add_user_window():
        add_user_window = tk.Toplevel(it_admin_window)
        add_user_window.title("Add New User")
        add_user_window.geometry("400x300")
        add_user_window.resizable(False, False)

        def add_user():
            username = username_entry.get().strip()
            password = password_entry.get().strip()
            role = role_var.get().strip()  # 获取角色值
            
            # 打印调试信息，确保获取了正确的角色
            print("Adding user with details:")
            print(f"Username: '{username}', Password: '{password}', Role: '{role}'")

            # 检查每个字段是否已填写
            if not username or not password or not role:
                messagebox.showerror("Error", "All fields are required")
                return

            try:
                insert_user(username, password, role)
                messagebox.showinfo("Success", "User added successfully!")
                display_users(fetch_all_users())
                add_user_window.destroy()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Username already exists")

        # 创建用户名、密码和角色输入框
        tk.Label(add_user_window, text="Username").grid(row=0, column=0, padx=10, pady=10)
        username_entry = tk.Entry(add_user_window)
        username_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(add_user_window, text="Password").grid(row=1, column=0, padx=10, pady=10)
        password_entry = tk.Entry(add_user_window, show="*")
        password_entry.grid(row=1, column=1, padx=10, pady=10)

        # 设置角色选择的 Combobox
        tk.Label(add_user_window, text="Role").grid(row=2, column=0, padx=10, pady=10)
        role_var = tk.StringVar(value="Admin")  # 设置默认值为 "Admin"
        role_options = ["Admin", "User", "IT_admin"]
        role_menu = ttk.Combobox(add_user_window, textvariable=role_var, values=role_options, state="readonly")
        role_menu.grid(row=2, column=1, padx=10, pady=10)

        tk.Button(add_user_window, text="Add User", command=add_user).grid(row=3, column=0, columnspan=2, pady=20)

    def open_update_user_window():
        try:
            selected_item = user_tree.selection()[0]
            user_id = int(user_tree.item(selected_item)['values'][0])
            selected_user = user_tree.item(selected_item)['values']
        except IndexError:
            messagebox.showerror("Error", "Please select a user to update.")
            return

        update_user_window = tk.Toplevel(it_admin_window)
        update_user_window.title("Update User")
        update_user_window.geometry("400x350")
        update_user_window.resizable(False, False)

        def update_user():
            new_username = username_entry.get()
            new_password = password_entry.get()
            new_role = role_var.get()

            if not new_username or not new_role:
                messagebox.showerror("Error", "Username and Role are required")
                return

            if new_password and len(new_password) < 6:
                messagebox.showerror("Error", "Password must be at least 6 characters long.")
                return

            try:
                hashed_password = hashlib.sha256(new_password.encode()).hexdigest() if new_password else selected_user[2]
                with sqlite3.connect('library.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute('''
                        UPDATE Users SET username = ?, password = ?, role = ? WHERE user_id = ?
                    ''', (new_username, hashed_password, new_role, user_id))
                    conn.commit()
                messagebox.showinfo("Success", "User updated successfully!")
                display_users(fetch_all_users())
                update_user_window.destroy()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Username already exists")

        tk.Label(update_user_window, text="Username").grid(row=0, column=0, padx=10, pady=10)
        username_entry = tk.Entry(update_user_window)
        username_entry.insert(0, selected_user[1])
        username_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(update_user_window, text="Password (leave blank to keep unchanged)").grid(row=1, column=0, padx=10, pady=10)
        password_entry = tk.Entry(update_user_window, show="*")
        password_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(update_user_window, text="Role").grid(row=2, column=0, padx=10, pady=10)
        role_var = tk.StringVar()
        role_options = ["Admin", "User", "IT_Admin"]
        role_menu = ttk.Combobox(update_user_window, textvariable=role_var, values=role_options, state="readonly")
        role_menu.grid(row=2, column=1, padx=10, pady=10)
        role_menu.set(selected_user[2])

        tk.Button(update_user_window, text="Update User", command=update_user).grid(row=3, column=0, columnspan=2, pady=20)

        def delete_user():
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this user?"):
                with sqlite3.connect('library.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute('DELETE FROM Users WHERE user_id = ?', (user_id,))
                    conn.commit()
                display_users(fetch_all_users())
                messagebox.showinfo("Delete User", "User deleted successfully!")
                update_user_window.destroy()

        tk.Button(update_user_window, text="Delete User", command=delete_user).grid(row=4, column=0, columnspan=2, pady=10)

    it_admin_window = tk.Tk()
    it_admin_window.title("IT Admin Dashboard")
    it_admin_window.geometry("900x800")
    it_admin_window.resizable(False, False)

    title_font = font.Font(size=24, weight="bold")
    tk.Label(it_admin_window, text="IT Admin Dashboard", font=title_font).pack(pady=20)

    default_font = font.Font(size=14)
    logout_button = tk.Button(it_admin_window, text="Log out", command=lambda: logout_and_return_to_login(it_admin_window), font=default_font)
    logout_button.place(x=700, y=10)

    columns = ('User ID', 'Username', 'Role')
    user_tree = ttk.Treeview(it_admin_window, columns=columns, show='headings', height=10)
    for col in columns:
        user_tree.heading(col, text=col, command=lambda _col=col: sort_by_column(_col, reverse=False))
        if col == 'User ID':
            user_tree.column(col, minwidth=0, width=50)  # 调整 User ID 列的宽度
        else:
            user_tree.column(col, minwidth=0, width=150)

    user_tree.pack(pady=20)

    tk.Button(it_admin_window, text="Add User", command=open_add_user_window, font=default_font).pack(pady=10)
    tk.Button(it_admin_window, text="Edit Selected User", command=open_update_user_window, font=default_font).pack(pady=10)

    display_users(fetch_all_users())
    it_admin_window.mainloop()

# Login Screen
def login_screen():
    def attempt_login():
        username = username_entry.get()
        password = password_entry.get()
        role = login_user(username, password)
        
        if role:
            print("Login Success", f"Logged in successfully as {role}")
            login_window.withdraw()  # 使用 withdraw() 隐藏窗口
            if role == 'User':
                due_books = check_due_dates(username)
                available_reservations = check_reservations(username)
                if available_reservations:
                    reservation_message = "\n".join([f"'{res[1]}' is now available for borrowing." for res in available_reservations])
                    if messagebox.askyesno("Reservation Notification", f"The following reserved books are available:\n{reservation_message}\nWould you like to borrow them now?"):
                        for res in available_reservations:
                            confirm_borrow_reserved_book(username, res[0])
                if due_books:
                    due_message = "\n".join([f"'{book[0]}' (Due: {book[1]})" for book in due_books])
                    messagebox.showinfo("Due Date Reminder", f"The following books are due soon:\n{due_message}")
            
            # 根据角色进入相应的界面
            if role == 'Admin':
                admin_dashboard()
            elif role == 'IT_admin':
                IT_admin_dashboard()
            else:
                user_dashboard(username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    login_window = tk.Tk()
    login_window.title("Library Login")
    login_window.geometry("900x800")
    login_window.resizable(False, False)

    default_font = font.Font(size=14)
    title_font = font.Font(size=24, weight="bold")

    tk.Label(login_window, text="Library Management System", font=title_font).pack(pady=40)
    tk.Label(login_window, text="Username", font=default_font).pack(pady=10)
    username_entry = tk.Entry(login_window, font=default_font)
    username_entry.pack(pady=10)
    tk.Label(login_window, text="Password", font=default_font).pack(pady=10)
    password_entry = tk.Entry(login_window, show="*", font=default_font)
    password_entry.pack(pady=10)
    tk.Button(login_window, text="Login", command=attempt_login, font=default_font).pack(pady=20)

    login_window.mainloop()



# Add Sample Books
def add_sample_books():
    sample_books = [
        ("The Great Gatsby", "F. Scott Fitzgerald", "American", "9780743273565", "A1", 5, 5),
        ("1984", "George Orwell", "British", "9780451524935", "B2", 10, 10),
        ("To Kill a Mockingbird", "Harper Lee", "American", "9780060935467", "C3", 10, 10),
        ("Moby Dick", "Herman Melville", "American", "9781503280786", "D4", 3, 3),
        ("Pride and Prejudice", "Jane Austen", "British", "9781503290563", "E5", 6, 6),
        ("War and Peace", "Leo Tolstoy", "Russian", "9780199232765", "F1", 8, 8),
        ("The Odyssey", "Homer", "Greek", "9780140268867", "G2", 7, 7),
        ("The Catcher in the Rye", "J.D. Salinger", "American", "9780316769488", "H3", 4, 4),
        ("Ulysses", "James Joyce", "Irish", "9780199535675", "I4", 5, 5),
        ("Don Quixote", "Miguel de Cervantes", "Spanish", "9780060934347", "J5", 6, 6),
        ("Crime and Punishment", "Fyodor Dostoevsky", "Russian", "9780486415871", "K6", 5, 5),
        ("The Brothers Karamazov", "Fyodor Dostoevsky", "Russian", "9780374528379", "L7", 8, 8),
        ("Brave New World", "Aldous Huxley", "British", "9780060850524", "M8", 9, 9),
        ("Wuthering Heights", "Emily Bronte", "British", "9780141439556", "N9", 6, 6),
        ("The Divine Comedy", "Dante Alighieri", "Italian", "9780140448955", "O10", 7, 7),
        ("Les Misérables", "Victor Hugo", "French", "9780451419439", "P11", 6, 6),
        ("Jane Eyre", "Charlotte Bronte", "British", "9780141441146", "Q12", 5, 5),
        ("Anna Karenina", "Leo Tolstoy", "Russian", "9780143035008", "R13", 6, 6),
        ("The Iliad", "Homer", "Greek", "9780140275360", "S14", 8, 8),
        ("One Hundred Years of Solitude", "Gabriel Garcia Marquez", "Colombian", "9780060883287", "T15", 10, 10)
    ]

    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()

        for title, author, nationality, isbn, shelf_number, total, available in sample_books:
            try:
                cursor.execute('''
                INSERT INTO Books (title, author, nationality, isbn, shelf_number, total_quantity, available_quantity) VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (title, author, nationality, isbn, shelf_number, total, available))
            except sqlite3.IntegrityError:
                pass
        conn.commit()

def generate_borrowed_books_data():
    usernames = ["user6", "user7", "user8", "user9"]
    book_titles = [
        "The Great Gatsby", "1984", "To Kill a Mockingbird", "Moby Dick",
        "Pride and Prejudice", "War and Peace", "The Odyssey",
        "The Catcher in the Rye", "Ulysses", "Don Quixote",
        "Crime and Punishment", "Brave New World", "Wuthering Heights",
        "The Divine Comedy", "Les Misérables", "Jane Eyre",
        "Anna Karenina", "The Iliad", "One Hundred Years of Solitude"
    ]
    
    data = []
    start_date = datetime.date(2023, 12, 1)
    end_date = datetime.date(2024, 11, 12)
    delta = datetime.timedelta(days=3)

    current_date = start_date
    while current_date <= end_date:
        username = random.choice(usernames)
        title = random.choice(book_titles)
        book_id = random.randint(1, 20)  # 假设书籍ID在1到20之间
        borrow_date = current_date
        return_date = borrow_date + datetime.timedelta(days=28)
        status = "returned"

        data.append((username, book_id, title, 1, borrow_date, return_date, status))
        current_date += delta

    return data


# 插入生成的借阅记录到数据库中，忽略重复项
def insert_borrowed_books_data(data):
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.executemany('''
            INSERT INTO BorrowedBooks (username, book_id, title, quantity, borrow_date, return_date, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', data)
        conn.commit()
    print(f"{len(data)} records inserted successfully.")


# Main Program
if __name__ == "__main__":
    setup_user_database()
    setup_library_database()
    setup_borrowed_books_database()
    setup_reservations_database()  # 用户的预约书籍表
    insert_user("admin", "admin123", "Admin")
    insert_user("admin1", "admin123", "Admin")
    insert_user("admin2", "admin123", "Admin")
    insert_user("admin3", "admin123", "Admin")
    insert_user("user1", "user123", "User")
    insert_user("user2", "user123", "User")
    insert_user("user3", "user123", "User")
    insert_user("user4", "user123", "User")
    insert_user("user5", "user123", "User")
    insert_user("user6", "user123", "User")
    insert_user("itadmin", "itadmin123", "IT_admin") 
    insert_user("itman", "itman123", "IT_admin") 
    insert_user("itman1", "itman123", "IT_admin") 
    add_sample_books()

    '''
    data = generate_borrowed_books_data(num_records=100)  # 生成100条记录
    insert_borrowed_books_data(data)
    '''
    
    login_screen()
