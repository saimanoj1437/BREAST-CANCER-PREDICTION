src/common/Header/Navbar.jsx

jsx
import React, { useState } from "react";
import { Link, useLocation } from "react-router-dom";

const NavItem = ({ to, children, active }) => {
    const [hover, setHover] = useState(false);
    return (
        <Link
            to={to}
            className={`nav-item${active ? " active" : ""}`}
            onMouseEnter={() => setHover(true)}
            onMouseLeave={() => setHover(false)}
        >
            <span>{children}</span>
        </Link>
    );
};

const Navbar = () => {
    const location = useLocation();
    return (
        <nav className="fixed-navbar navbar">
            <div className="navbar-logo-section">
                <div className="logo-circle">SCB</div>
            </div>
            <div className="nav-middle">
                <NavItem to="/" active={location.pathname === "/"}>Dashboard</NavItem>
                <NavItem to="/approved" active={location.pathname === "/approved"}>Approved</NavItem>
                <NavItem to="/rejected" active={location.pathname === "/rejected"}>Rejected</NavItem>
                <NavItem to="/pending" active={location.pathname === "/pending"}>Pending</NavItem>
            </div>
            <div className="nav-end">
                <div className="nav-notify">
                    <i className="fa-solid fa-bell"></i>
                    <span className="nav-notify-count">3</span>
                </div>
                <img
                    src="https://ui-avatars.com/api/?name=User"
                    alt="user"
                    className="nav-user-avatar"
                />
                <div>
                    <h4 className="nav-account-title">Account Settings</h4>
                    <p className="nav-account-role">Loan Officer</p>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;
src/common/Footer/Footer.jsx

jsx
import React from "react";

const Footer = () => (
    <footer className="fixed-footer">
        © 2025 Your Company Name
    </footer>
);

export default Footer;
src/common/Filters/Filters.jsx

jsx
import React from "react";

const Filters = () => (
    <div className="filters-bar">
        <input
            className="filters-bar-input"
            placeholder="Search by name, loan type, or application ID"
        />
        <select className="filters-bar-select">
            <option>All Loan Types</option>
            <option>Personal Loan</option>
            <option>Home Loan</option>
            <option>Vehicle Loan</option>
        </select>
        <select className="filters-bar-select">
            <option>All Statuses</option>
            <option>Verified</option>
            <option>Pending Docs</option>
        </select>
        <button className="filters-bar-button">Filter</button>
    </div>
);

export default Filters;
src/common/ApplicationsTable/ApplicationsTable.jsx

jsx
import React from "react";

const getAppsData = (filter) => {
    const data = [
        { name: "Sarah Johnson", email: "sarah@email.com", loanType: "Home", amount: "₹25,00,000", status: "Pending", appliedDate: "Dec 15, 2024" },
        { name: "Michael Chen", email: "m.chen@email.com", loanType: "Personal", amount: "₹5,00,000", status: "Approved", appliedDate: "Dec 14, 2024" },
        { name: "David Wilson", email: "d.wilson@email.com", loanType: "Vehicle", amount: "₹8,50,000", status: "Pending", appliedDate: "Dec 13, 2024" },
        { name: "Emma Brown", email: "e.brown@email.com", loanType: "Home", amount: "₹12,00,000", status: "Rejected", appliedDate: "Dec 12, 2024" }
    ];
    if (!filter) return data;
    return data.filter(row => row.status.toLowerCase() === filter.toLowerCase());
};

const loanTypeClass = {
    Home: "loan-badge-home",
    Personal: "loan-badge-personal",
    Vehicle: "loan-badge-vehicle"
};

const ApplicationsTable = ({ filter }) => {
    const rows = getAppsData(filter);
    return (
        <div className="dash-table-wrapper">
            <table>
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
                    {rows.length === 0 ? (
                        <tr>
                            <td colSpan={6} className="table-empty">No applications.</td>
                        </tr>
                    ) : rows.map(({ name, email, loanType, amount, status, appliedDate }, idx) => (
                        <tr key={idx}>
                            <td>
                                {name}<br />
                                <span className="table-applicant-email">{email}</span>
                            </td>
                            <td>
                                <span className={`loan-type ${loanTypeClass[loanType] || ""}`}>
                                    {loanType}
                                </span>
                            </td>
                            <td>{amount}</td>
                            <td className={
                                status === "Approved" ? "status-approved"
                                : status === "Rejected" ? "status-rejected"
                                : status === "Pending" ? "status-pending"
                                : ""
                            }>{status}</td>
                            <td>{appliedDate}</td>
                            <td>
                                <a href="#" className="table-link">Open</a>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
            <div className="table-pagination">
                <button>Previous</button>
                <button>Next</button>
            </div>
        </div>
    );
};

export default ApplicationsTable;
src/pages/Dashboard/AdminDashboard.jsx

jsx
import React from "react";
import Filters from "../../common/Filters/Filters";
import ApplicationsTable from "../../common/ApplicationsTable/ApplicationsTable";
const bannerImg = "https://sustainability-news.net/wp-content/uploads/2024/08/SC-head-office-2022-scaled-1.jpg";

const StatsCards = () => (
    <div className="stats-cards">
        <div className="stats-card">
            <div className="stats-title">Total Applications</div>
            <div className="stats-value">24</div>
            <span className="stats-growth">↑ 12% from last month</span>
        </div>
        <div className="stats-card border-orange">
            <div className="stats-title">Pending Review</div>
            <div className="stats-value">8</div>
            <span className="stats-attention">⚠ Requires attention</span>
        </div>
        <div className="stats-card border-green">
            <div className="stats-title">Approved Today</div>
            <div className="stats-value">6</div>
            <span className="stats-progress">✅ Great progress!</span>
        </div>
        <div className="stats-card border-red">
            <div className="stats-title">Rejected</div>
            <div className="stats-value">2</div>
            <span className="stats-rejected">❌ This month</span>
        </div>
    </div>
);

const AdminDashboard = () => (
    <div>
        <section className="banner-section" style={{ backgroundImage: `url(${bannerImg})` }} />
        <StatsCards />
        <div className="dashboard-section">
            <h2 className="dashboard-title">Recent Applications</h2>
            <p className="dashboard-desc">Review and process loan applications</p>
            <Filters />
        </div>
        <ApplicationsTable />
    </div>
);

export default AdminDashboard;
src/pages/Dashboard/Approved.jsx

jsx
import React from "react";
import Filters from "../../common/Filters/Filters";
import ApplicationsTable from "../../common/ApplicationsTable/ApplicationsTable";

const Approved = () => (
    <div>
        <div className="dashboard-section">
            <h2 className="dashboard-title">Approved Applications</h2>
            <p className="dashboard-desc">These applications have been approved.</p>
            <Filters />
        </div>
        <ApplicationsTable filter="Approved"/>
    </div>
);

export default Approved;
src/pages/Dashboard/Rejected.jsx

jsx
import React from "react";
import Filters from "../../common/Filters/Filters";
import ApplicationsTable from "../../common/ApplicationsTable/ApplicationsTable";

const Rejected = () => (
    <div>
        <div className="dashboard-section">
            <h2 className="dashboard-title">Rejected Applications</h2>
            <p className="dashboard-desc">These applications have been rejected.</p>
            <Filters />
        </div>
        <ApplicationsTable filter="Rejected"/>
    </div>
);

export default Rejected;
src/pages/Dashboard/Pending.jsx

jsx
import React from "react";
import Filters from "../../common/Filters/Filters";
import ApplicationsTable from "../../common/ApplicationsTable/ApplicationsTable";

const Pending = () => (
    <div>
        <div className="dashboard-section">
            <h2 className="dashboard-title">Pending Applications</h2>
            <p className="dashboard-desc">These applications are waiting for review.</p>
            <Filters />
        </div>
        <ApplicationsTable filter="Pending"/>
    </div>
);

export default Pending;
src/App.jsx

jsx
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./common/Header/Navbar";
import Footer from "./common/Footer/Footer";
import AdminDashboard from "./pages/Dashboard/AdminDashboard";
import Approved from "./pages/Dashboard/Approved";
import Rejected from "./pages/Dashboard/Rejected";
import Pending from "./pages/Dashboard/Pending";

const App = () => (
    <Router>
        <Navbar />
        <main className="main-content">
            <Routes>
                <Route path="/" element={<AdminDashboard />} />
                <Route path="/approved" element={<Approved />} />
                <Route path="/rejected" element={<Rejected />} />
                <Route path="/pending" element={<Pending />} />
            </Routes>
        </main>
        <Footer />
    </Router>
);

export default App;
src/index.js

js
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./assets/styles/App.css";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
Place all CSS rules in App.css, and only reference classes in your JSX—as shown here.
Let me know if you need example CSS class definitions as well!
