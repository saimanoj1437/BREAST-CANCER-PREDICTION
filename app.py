<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Maker Dashboard</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', sans-serif;
        }

        body {
            background: #f5f7fb;
            color: #333;
            display: flex;
            min-height: 100vh;
        }

        /* =================== Sidebar =================== */
        .sidebar {
            width: 220px;
            background: #fff;
            padding: 20px;
            box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
            position: fixed;
            top: 0;
            left: 0;
            height: 100%;
            z-index: 200;
        }

        .sidebar .logo {
            text-align: center;
            margin-bottom: 30px;
        }

        .sidebar .logo img {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            object-fit: cover;
        }

        .sidebar nav a {
            display: flex;
            justify-content: space-between;
            align-items: center;
            text-decoration: none;
            color: #333;
            padding: 10px 15px;
            border-radius: 6px;
            margin-bottom: 10px;
            transition: 0.3s;
        }

        .sidebar nav a.active,
        .sidebar nav a:hover {
            background: #07b132;
            color: #fff;
        }

        .sidebar nav .badge {
            background: red;
            color: #fff;
            font-size: 12px;
            padding: 2px 6px;
            border-radius: 12px;
        }

        /* =================== Content Wrapper =================== */
        .content-wrapper {
            margin-left: 220px;
            width: calc(100% - 220px);
            flex: 1;
            display: flex;
            flex-direction: column;
            background: #f5f7fb;
        }

        /* Navbar */
        .navbar {
            background: #fff;
            display: flex;
            justify-content: flex-end;
            align-items: center;
            padding: 12px 40px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            position: sticky;
            top: 0;
            z-index: 100;
            border-left: 1px solid transparent;
        }

        .nav-right {
            display: flex;
            align-items: center;
            gap: 20px;
        }

        .notif {
            position: relative;
            font-size: 1.3rem;
            color: #0078d7;
            cursor: pointer;
        }

        .notif-badge {
            position: absolute;
            top: -6px;
            right: -8px;
            background: red;
            color: white;
            font-size: 10px;
            border-radius: 50%;
            padding: 2px 5px;
        }

        .profile {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .profile img {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: #ccc;
        }

        .user-details h4 {
            font-size: 14px;
        }

        .user-details p {
            font-size: 12px;
            color: #777;
        }

        /* Banner */
        .banner {
            background: url("https://sustainability-news.net/wp-content/uploads/2024/08/SC-head-office-2022-scaled-1.jpg") no-repeat center center;
            background-size: cover;
            height: 30vh;
            position: relative;
        }

        /* Floating Cards */
        .stats-cards {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: -50px;
            position: relative;
            z-index: 10;
        }

        .card {
            background: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            text-align: center;
            width: 250px;
        }

        .card h3 {
            font-size: 14px;
            color: #555;
        }

        .count {
            font-size: 22px;
            font-weight: 700;
            margin: 6px 0;
        }

        .success {
            color: #1e7c4c;
        }

        .warning {
            border-left: 4px solid #e97724;
        }

        .success-card {
            border-left: 4px solid #1e7c4c;
        }

        .danger {
            border-left: 4px solid #e34242;
        }

        /* Main Content */
        .main {
            padding: 40px 60px;
        }

        .applications {
            background: #fff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }

        .section-header h2 {
            font-size: 18px;
            color: #0078d7;
        }

        .section-header p {
            font-size: 13px;
            color: #888;
        }

        /* Filters */
        .filters {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 16px 20px;
            background: #fff;
            justify-content: space-between;
            border-bottom: 1px solid #e5e7eb;
            margin-top: 10px;
            border-radius: 8px;
        }

        .filters input {
            flex: 1;
            padding: 10px;
            border: 1px solid #d1d5db;
            border-radius: 8px;
            outline: none;
        }

        .filters select {
            padding: 10px;
            border: 1px solid #d1d5db;
            border-radius: 8px;
            outline: none;
        }

        .filter-btn {
            background: #2563eb;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            transition: 0.3s;
        }

        .filter-btn:hover {
            background: black;
            color: white;
        }

        /* Table */
        .app-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        .app-table th,
        .app-table td {
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid #eee;
            font-size: 14px;
        }

        .tag {
            padding: 4px 8px;
            border-radius: 6px;
            font-size: 12px;
            color: white;
        }

        .blue {
            background: #3b82f6;
        }

        .green {
            background: #16a34a;
        }

        .purple {
            background: #8b5cf6;
        }

        .status {
            padding: 4px 8px;
            border-radius: 6px;
            font-size: 12px;
            color: white;
        }

        .pending {
            background: #facc15;
            color: #333;
        }

        .approved {
            background: #16a34a;
        }

        .rejected {
            background: #e34242;
        }

        /* Pagination Buttons */
        .pagination {
            display: flex;
            justify-content: flex-end;
            gap: 10px;
            margin-top: 15px;
        }

        .pagination button {
            padding: 6px 12px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            background: #f0f2f5;
            transition: 0.3s;
        }

        .pagination button:hover {
            background: #0078d7;
            color: white;
        }
    </style>
</head>

<body>
    <!-- Sidebar -->
    <aside class="sidebar">
        <div class="logo">
            <img src="SC.jpg" alt="Logo" class="logo-img">
        </div>
        <nav class="nav">
            <a class="active" href="#">Dashboard</a>
            <a href="#">Applications <span class="badge">12</span></a>
            <a href="#">Approved</a>
            <a href="#">Rejected</a>
            <a href="#">Pending</a>
            <a href="#">Reports</a>
            <a href="#">Settings</a>
        </nav>
    </aside>

    <!-- Content Wrapper -->
    <div class="content-wrapper">
        <!-- Top Navbar (logo removed) -->
        <nav class="navbar">
            <div class="nav-right">
                <div class="notif">
                    <i class="fa-solid fa-bell"></i>
                    <span class="notif-badge">3</span>
                </div>
                <div class="profile">
                    <img src="" alt="user" />
                    <div class="user-details">
                        <h4>Account Settings</h4>
                        <p>Loan Officer</p>
                    </div>
                </div>
            </div>
        </nav>

        <!-- Banner -->
        <section class="banner"></section>

        <!-- Stats Cards -->
        <section class="stats-cards">
            <div class="card">
                <h3>Total Applications</h3>
                <p class="count">24</p>
                <span class="success">↑ 12% from last month</span>
            </div>
            <div class="card warning">
                <h3>Pending Review</h3>
                <p class="count">8</p>
                <span class="alert">⚠ Requires attention</span>
            </div>
            <div class="card success-card">
                <h3>Approved Today</h3>
                <p class="count">6</p>
                <span class="success">✅ Great progress!</span>
            </div>
            <div class="card danger">
                <h3>Rejected</h3>
                <p class="count">2</p>
                <span class="alert">❌ This month</span>
            </div>
        </section>

        <!-- Main -->
        <main class="main">
            <section class="applications">
                <div class="section-header">
                    <h2>Recent Applications</h2>
                    <p>Review and process loan applications</p>
                </div>

                <div class="filters">
                    <input type="text" placeholder="Search by customer name, loan type, or application ID" />
                    <select>
                        <option>All Loan Types</option>
                        <option>Personal Loan</option>
                        <option>Home Loan</option>
                        <option>Vehicle Loan</option>
                    </select>
                    <select>
                        <option>All Statuses</option>
                        <option>Verified</option>
                        <option>Pending Docs</option>
                    </select>
                    <button class="filter-btn">Filter</button>
                </div>

                <table class="app-table">
                    <thead>
                        <tr>
                            <th>Applicant</th>
                            <th>Loan Type</th>
                            <th>Amount</th>
                            <th>Status</th>
                            <th>Applied Date</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr data-status="pending">
                            <td>Sarah Johnson<br><span>sarah.j@email.com</span></td>
                            <td><span class="tag blue">Home Loan</span></td>
                            <td>₹25,00,000</td>
                            <td><span class="status pending">Pending Review</span></td>
                            <td>Dec 15, 2024</td>
                            <td><a href="#">Open</a></td>
                        </tr>
                        <tr data-status="approved">
                            <td>Michael Chen<br><span>m.chen@email.com</span></td>
                            <td><span class="tag green">Personal Loan</span></td>
                            <td>₹5,00,000</td>
                            <td><span class="status approved">Approved</span></td>
                            <td>Dec 14, 2024</td>
                            <td><a href="#">Open</a></td>
                        </tr>
                        <tr data-status="pending">
                            <td>David Wilson<br><span>d.wilson@email.com</span></td>
                            <td><span class="tag purple">Vehicle Loan</span></td>
                            <td>₹8,50,000</td>
                            <td><span class="status pending">Pending Review</span></td>
                            <td>Dec 13, 2024</td>
                            <td><a href="#">Open</a></td>
                        </tr>
                        <tr data-status="rejected">
                            <td>Emma Brown<br><span>e.brown@email.com</span></td>
                            <td><span class="tag blue">Home Loan</span></td>
                            <td>₹12,00,000</td>
                            <td><span class="status rejected">Rejected</span></td>
                            <td>Dec 12, 2024</td>
                            <td><a href="#">Open</a></td>
                        </tr>
                    </tbody>
                </table>

                <div class="pagination">
                    <button id="prev-btn">Previous</button>
                    <button id="next-btn">Next</button>
                </div>
            </section>
        </main>
    </div>
</body>

</html>oi
