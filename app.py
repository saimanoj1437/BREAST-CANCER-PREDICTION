
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Presenting the Use Case</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        .testimonial-box {
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 10px;
        }
        .btn-custom {
            background-color: #28a745;
            color: #fff;
        }
    </style>
</head>
<body class="p-4">
    <div class="container" style="max-width: 700px;">
        <h4>Presenting the Use Case</h4>
        <form id="testimonialForm" class="mb-4">
            <div class="form-group row">
                <label for="name" class="col-sm-2 col-form-label font-weight-bold">Name</label>
                <div class="col-sm-10">
                    <input type="text" class="form-control" id="name" placeholder="Your Name" required>
                </div>
            </div>
            <div class="form-group row">
                <label for="message" class="col-sm-2 col-form-label font-weight-bold">Message</label>
                <div class="col-sm-10">
                    <input type="text" class="form-control" id="message" placeholder="Enter your Message" required>
                </div>
            </div>
            <div class="form-group text-center">
                <button type="submit" class="btn btn-success" id="submitBtn">Submit</button>
            </div>
        </form>

        <div>
            <h5>Testimonials</h5>
            <div id="testimonials"></div>
        </div>
    </div>

    <script>
        let testimonials = [];
        let editIndex = null;

        function renderTestimonials() {
            const container = document.getElementById('testimonials');
            container.innerHTML = '';
            testimonials.forEach((item, index) => {
                container.innerHTML += `
                    <div class="testimonial-box">
                        <strong>${item.name}</strong>
                        <p>${item.message}</p>
                        <button class="btn btn-custom btn-sm mr-2" onclick="editTestimonial(${index})">Edit</button>
                        <button class="btn btn-danger btn-sm" onclick="deleteTestimonial(${index})">Delete</button>
                    </div>
                `;
            });
        }

        document.getElementById('testimonialForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const name = document.getElementById('name').value.trim();
            const message = document.getElementById('message').value.trim();
            if (editIndex === null) {
                testimonials.push({ name, message });
            } else {
                testimonials[editIndex] = { name, message };
                editIndex = null;
                document.getElementById('submitBtn').textContent = 'Submit';
            }
            this.reset();
            renderTestimonials();
        });

        window.editTestimonial = function(index) {
            document.getElementById('name').value = testimonials[index].name;
            document.getElementById('message').value = testimonials[index].message;
            editIndex = index;
            document.getElementById('submitBtn').textContent = 'Update';
            document.getElementById('name').focus();
        };

        window.deleteTestimonial = function(index) {
            testimonials.splice(index, 1);
            if (editIndex === index) {
                editIndex = null;
                document.getElementById('testimonialForm').reset();
                document.getElementById('submitBtn').textContent = 'Submit';
            }
            renderTestimonials();
        };

        // Initial render
        renderTestimonials();
    </script>
</body>
</html>
