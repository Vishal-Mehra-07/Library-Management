<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <h1>📚 Library Management System</h1>

  <p>This is a simple <strong>Library Management System</strong> built using Python.
  It allows users to <strong>add</strong>, <strong>view</strong>, <strong>issue</strong>, and <strong>return</strong> books through a text-based console interface. </p>

  <h2>🧩 Features</h2>
  <ul>
    <li>➕ <strong>Add Book</strong> – Add new books or increase their quantity.</li>
    <li>📖 <strong>Display Books</strong> – View all available books with their quantities.</li>
    <li>📤 <strong>Issue Book</strong> – Borrow a book (reduces stock by 1).</li>
    <li>📥 <strong>Return Book</strong> – Return a borrowed book or add it if new.</li>
    <li>🚪 <strong>Exit</strong> – Quit the program safely.</li>
  </ul>

  <h2>⚙️ How It Works</h2>
  <p>All books are stored in a Python <strong>dictionary</strong>, where the key is the book name and the value is its quantity.
  The program uses a <strong>menu-driven interface</strong> for interaction.</p>

  <h2>🛠️ Requirements</h2>
  <ul>
    <li>Python 3.x</li>
    <li>No external libraries needed</li>
  </ul>

  <h2>▶️ How to Run</h2>
  <ol>
    <li>Clone or download this repository</li>
    <li>Open a terminal in the project folder</li>
    <li>Run the script:</li>
  </ol>
  <pre><code>python library_management.py</code></pre>

  <h2>💡 Example Usage</h2>
  <pre><code>Library Management System
1. Add Book
2. Display Books
3. Issue Book
4. Return Book
5. Exit
Enter your choice (1-5): 1
Enter book name: Python Programming
Enter quantity: 3
'Python Programming' added successfully. Quantity: 3
</code></pre>

  <h2>🚀 Future Enhancements Can be done</h2>
  <ul>
    <li>Add file/database storage for permanent book records</li>
    <li>Include user authentication</li>
    <li>Implement fine tracking for late returns</li>
  </ul>
</body>
</html>
