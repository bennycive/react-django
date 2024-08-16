

import React from "react";
import axios from "axios";
import "./styles.css"; // Import the CSS file

class App extends React.Component {
  state = {
    departments: [],
    employees: []
  };

  componentDidMount() {
    this.fetchDepartments();
    this.fetchEmployees();
  }

  fetchDepartments = () => {
    axios
      .get("http://localhost:8000/api/departments/")
      .then(res => {
        this.setState({ departments: res.data });
      })
      .catch(err => {
        console.error("Error fetching departments:", err);
      });
  };

  fetchEmployees = () => {
    axios
      .get("http://localhost:8000/api/employees/")
      .then(res => {
        this.setState({ employees: res.data });
      })
      .catch(err => {
        console.error("Error fetching employees:", err);
      });
  };

  render() {
    return (
      <div className="container">
        <h2>Department Details</h2>
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            {this.state.departments.map((dept, id) => (
              <tr key={id}>
                <td data-label="Name">{dept.name}</td>
                <td data-label="Description">{dept.description}</td>
              </tr>
            ))}
          </tbody>
        </table>

        <h2>Employee Details</h2>
        <table>
          <thead>
            <tr>
              <th>First Name</th>
              <th>Middle Name</th>
              <th>Last Name</th>
              <th>Department</th>
            </tr>
          </thead>
          <tbody>
            {this.state.employees.map((emp, id) => (
              <tr key={id}>
                <td data-label="First Name">{emp.first_name}</td>
                <td data-label="Middle Name">{emp.middle_name}</td>
                <td data-label="Last Name">{emp.last_name}</td>
                <td data-label="Department">{emp.department ? emp.department : "N/A"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }
}
export default App;


