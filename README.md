# Inventory Count
This is an Inventory counting system developed for a homemade raspberrypi scale

## OVERVIEW
Many companies perform inventory counts on a monthly basis. Through the use of low cost technology,
such as: Raspberry Pi, scale and barcode reader, we can implement a system that will quickly
identify a product and using previously recorded weights provide an accurate count.

## PROBLEM STATEMENT
Taking inventory is usually done by an employee spending several hours individually counting items.
When items are in bulk, an employee could lose count easily and record an incorrect value.

## TARGET USERS
Anyone who manually counts inventory of small items.

## USER REQUIREMENTS
• Secure login
• Setup screen or configuration file to control resource locations
• Initialize the system by creating databases if they don’t already exist or clearing any previous inventory counts.
• Print barcode labels using data stored locally, or in a remote database.
• Measurement mode to capture the weight of a container, and the average weight of 20-100 items (depending on size and accuracy requirements).
• Record the location(s) of inventory
• Count the inventory, including inventory located in multiple locations.
• Report to identify missing items and their last known locations.
• Export the data

## REQUIRED MATERIALS
Raspberry Pi
Scale
Barcode reader (mobile device or actual)

## POSSIBLE TECHNOLOGIES
Python (Our first choice)
Node.js
PHP

## POSSIBLE COMPETITORS
AVTory
ASAP Systems

## PRIMARY OBJECTIVES
Create Web landing page for user login
Establish database on remote system (AWS or internal server via another Raspberry Pi)
Record weights of individual items

## SECONDARY OBJECTIVES
Archive old inventory counts from the month period
Print labels for new items to be added
Record inventory locations
Export of data for a user friendly view

## EXPECTED OUTCOME
Secure Web System
Cycleable database (monthly)
Inventory is recorded
Weight is recorded

## RESOURCES
### Development Tools
Google Doc (Documentation)
Github (Versioning)
Stack Overflow (Research and Dev)

### Frontend Technologies
HTML
CSS
Javascript

### Backend Technologies
Python
MySQL

### Hardware
Raspberry Pi
Scale or Load Cells (x4)
Barcode Reader (mobile or actual)

### Software
Flask - Python web framework to base our application
MySQL - Database management
