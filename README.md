# Breast_Cancer_Perdiction


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Name & Message App</title>
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">

<div class="container py-5">
  <h2 class="mb-4 text-center">Name & Message App</h2>

  <!-- Input form -->
  <div class="card p-3 shadow-sm">
    <div class="mb-3">
      <input type="text" id="nameInput" class="form-control" placeholder="Enter your name">
    </div>
    <div class="mb-3">
      <textarea id="messageInput" class="form-control" placeholder="Enter your message"></textarea>
    </div>
    <button class="btn btn-primary" onclick="addMessage()">Add</button>
  </div>

  <!-- Messages list -->
  <ul id="messageList" class="list-group mt-4"></ul>
</div>

<!-- Bootstrap JS -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
<script>
let editingIndex = null;

function addMessage() {
  const name = document.getElementById('nameInput').value.trim();
  const message = document.getElementById('messageInput').value.trim();
  if (!name || !message) {
    alert("Please enter both name and message.");
    return;
  }

  if (editingIndex !== null) {
    // Update existing message
    document.querySelectorAll('#messageList li')[editingIndex].querySelector('.message-text').textContent = name + ": " + message;
    editingIndex = null;
  } else {
    // Create new message item
    const li = document.createElement('li');
    li.className = "list-group-item d-flex justify-content-between align-items-center";

    const span = document.createElement('span');
    span.className = "message-text";
    span.textContent = name + ": " + message;

    const btnGroup = document.createElement('div');

    const editBtn = document.createElement('button');
    editBtn.className = "btn btn-sm btn-warning me-2";
    editBtn.textContent = "Edit";
    editBtn.onclick = () => editMessage(li, name, message);

    const deleteBtn = document.createElement('button');
    deleteBtn.className = "btn btn-sm btn-danger";
    deleteBtn.textContent = "Delete";
    deleteBtn.onclick = () => li.remove();

    btnGroup.appendChild(editBtn);
    btnGroup.appendChild(deleteBtn);

    li.appendChild(span);
    li.appendChild(btnGroup);

    document.getElementById('messageList').appendChild(li);
  }

  document.getElementById('nameInput').value = "";
  document.getElementById('messageInput').value = "";
}

function editMessage(li, name, message) {
  document.getElementById('nameInput').value = name;
  document.getElementById('messageInput').value = message;
  editingIndex = Array.from(document.querySelectorAll('#messageList li')).indexOf(li);
}
</script>
</body>
</html>
