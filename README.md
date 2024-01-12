# Tissue Sample Collection Web Application

## Overview

This web application provides an administrative interface for managing a Tissue Sample directory. Users can view collections, drill into collection details, add new samples to existing collections, and create new collections.

## Requirements

The minimum viable product includes the following features:

- Display a list of collections on the home page (including their title and associated disease).
- Drill into a collection’s record to view the details of their currently associated samples.
- Add a new sample to an existing collection.
- Create a new collection.

## Entities & Data

### Collections

| Id | Disease Term | Title                                |
|----|--------------|--------------------------------------|
| 1  | Cirrhosis of liver | Mothers Pregnancy Samples     |
| 2  | Malignant tumour of breast | Phase II multicentre study  |
| 3  | Fit and well | Lymphoblastoid cell lines           |
| 4  | Chronic fatigue syndrome | Samples available include ME/CFS Cases |
| 5  | Malignant tumour of breast | A randomised placebo-controlled trial |

### Samples

| Id | Collection_Id | Donor_Count | Material_Type         | Last_Updated |
|----|---------------|-------------|------------------------|--------------|
| 1  | 4             | 90210       | Cerebrospinal fluid    | 2019-06-03   |
| 2  | 2             | 512         | Cerebrospinal fluid    | 2019-03-08   |
| 3  | 2             | 7777        | Core biopsy            | 2019-05-04   |

## Project Structure

- **/Tissue-Sample-Collection-master**: Root directory of the project.
  - **/SampleApp**: Source code for the web application.
  - **/templates**: HTML templates.
  - **/static**: Static files (CSS, JavaScript).
  - **/venv**: Virtual environment for Python dependencies.
  - **/requirements.txt**: List of project dependencies.
  - **/manage.py**: Django management script.
  - **/README.md**: Project documentation.

## How to Execute the Project

1. Clone the repository:

   ```
   git clone https://github.com/brayokenya/Tissue-Sample-Collection.git


    # Navigate to the project directory
    cd Tissue-Sample-Collection/

    # Set up a virtual environment (optional but recommended)
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

    cd SampleApp/

    pytest -s tests.py

   
## Hosted Version

```
  https://brian2541.pythonanywhere.com/

```
## Future Plans


1. Ensure Collections and samples can only be deleted by their sole creators(Users that created the collections)

2. Dockerize the Application for easier Deployment

3. Use it as a learning tool to improve and maintain the current existing system at 
https://www.nottingham.ac.uk/