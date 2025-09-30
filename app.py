
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Testimonials</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-white">

<div class="container py-4">
  <h4 class="mb-3">Presenting the Use Case</h4>

  <!-- Input Form -->
  <div class="border p-3">
    <div class="row mb-2">
      <div class="col-2 bg-primary text-white d-flex align-items-center justify-content-center fw-bold">
        Name
      </div>
      <div class="col-10">
        <input type="text" id="nameInput" class="form-control" placeholder="Your Name">
      </div>
    </div>
    <div class="row mb-2">
      <div class="col-2 bg-primary text-white d-flex align-items-center justify-content-center fw-bold">
        Message
      </div>
      <div class="col-10">
        <textarea id="messageInput" class="form-control" placeholder="Enter your Message"></textarea>
      </div>
    </div>
    <button class="btn btn-success fw-bold" onclick="addTestimonial()">Submit</button>
  </div>

  <!-- Testimonials -->
  <div class="mt-4">
    <h5>Testimonials</h5>
    <div id="testimonialList"></div>
  </div>
</div>

<script>
let editIndex = null;

function addTestimonial() {
  const name = document.getElementById("nameInput").value.trim();
  const message = document.getElementById("messageInput").value.trim();

  if (!name || !message) {
    alert("Please enter both name and message.");
    return;
  }

  const testimonialList = document.getElementById("testimonialList");

  if (editIndex !== null) {
    // Update existing testimonial
    const card = testimonialList.children[editIndex];
    card.querySelector(".testimonial-name").textContent = name;
    card.querySelector(".testimonial-message").textContent = message;
    editIndex = null;
  } else {
    // Create new testimonial card
    const card = document.createElement("div");
    card.className = "border rounded p-3 mb-2";

    const header = document.createElement("div");
    header.className = "d-flex justify-content-between align-items-center";

    const nameEl = document.createElement("h6");
    nameEl.className = "testimonial-name mb-0";
    nameEl.textContent = name;

    const btnGroup = document.createElement("div");

    const editBtn = document.createElement("button");
    editBtn.className = "btn btn-success btn-sm me-1";
    editBtn.textContent = "Edit";
    editBtn.onclick = () => editTestimonial(card, name, message);

    const deleteBtn = document.createElement("button");
    deleteBtn.className = "btn btn-success btn-sm";
    deleteBtn.textContent = "Delete";
    deleteBtn.onclick = () => card.remove();

    btnGroup.appendChild(editBtn);
    btnGroup.appendChild(deleteBtn);

    header.appendChild(nameEl);
    header.appendChild(btnGroup);

    const msg = document.createElement("p");
    msg.className = "testimonial-message mt-2 mb-0";
    msg.textContent = message;

    card.appendChild(header);
    card.appendChild(msg);

    testimonialList.appendChild(card);
  }

  // Clear inputs
  document.getElementById("nameInput").value = "";
  document.getElementById("messageInput").value = "";
}

function editTestimonial(card, name, message) {
  document.getElementById("nameInput").value = name;
  document.getElementById("messageInput").value = message;
  editIndex = Array.from(card.parentNode.children).indexOf(card);
}
</script>
</body>
</html>
