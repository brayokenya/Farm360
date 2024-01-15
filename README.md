# Farm360 Web Application

## Overview

Farm360 is a comprehensive web application designed to streamline farm management by providing an intuitive administrative interface. Users can efficiently manage their farm-related data, including events, livestock, and resources. The application offers features such as creating and scheduling events, tracking livestock details, and managing farm resources like equipment and inventory.

## Requirements

The minimum viable product includes the following features:

- Display a list of upcoming events and essential details on the home page.
- Efficiently manage livestock records, including details like name, type, sex, and status.
- Track and monitor available resources such as equipment, warehouses, and inventory.
- Create new events, add livestock records, and manage resources seamlessly.

## Entities & Data

### Events

| Id | Title                | Start Date  | End Date    |
|----|----------------------|-------------|-------------|
| 1  | Harvest Festival     | 2024-09-15  | 2024-09-17  |
| 2  | Livestock Vaccination| 2024-08-20  | 2024-08-20  |
| 3  | Crop Planting        | 2024-10-01  | 2024-10-05  |

### Livestock

| Id | Name    | Livestock Type | Sex    | Status  |
|----|---------|-----------------|--------|---------|
| 1  | Cow1    | Dairy           | Female | Active  |
| 2  | Chicken2| Poultry         | Male   | Active  |
| 3  | Pig3    | Swine           | Female | Inactive|

### Resources

| Id | Name         | Type      | Description                  | Quantity | Location      |
|----|--------------|-----------|------------------------------|----------|---------------|
| 1  | Tractor      | Equipment | Farming Tractor              | 2        | Equipment Shed|
| 2  | Fertilizer   | Inventory | Organic Fertilizer           | 100 bags | Warehouse A   |
| 3  | Greenhouse   | Warehouse | Automated Plant Growth       | 1        | Greenhouse 1  |

## Project Structure

- **/Farm360**: Source code for the Farm360 web application.
- **/templates**: HTML templates.
- **/static**: Static files (CSS, JavaScript).
- **/venv**: Virtual environment for Python dependencies.
- **/requirements.txt**: List of project dependencies.
- **/manage.py**: Django management script.
- **/README.md**: Project documentation.

## How to Execute the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/brayokenya/Farm360.git


    # Navigate to the project directory
    cd Farm360/

    # Set up a virtual environment
    make venv

    # Activate the virtual environment
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate

    # Install project dependencies
    make install

    # Run the development server
    make run

    #Running Tests

    cd Farm360/

    pytest -s tests.py

   
## Hosted Version

```
    https://brian2541.pythonanywhere.com/

```
## Future Plans


1. Ensure Events, Livestock, and Resources can only be deleted by their sole creators (Users that created them).

2. Dockerize the Application for easier Deployment.

3. Use actual weather data from satelites to guide farmers on when to plant, harvest or vaccinate