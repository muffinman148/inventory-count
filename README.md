# Inventory Count
This is an Inventory counting system developed for a homemade raspberrypi scale

## Overview
Many companies perform inventory counts on a monthly basis. Through the use of low cost technology,
such as: Raspberry Pi, scale and barcode reader, we can implement a system that will quickly
identify a product and using previously recorded weights provide an accurate count.

## Problem Statement
Taking inventory is usually done by an employee spending several hours individually counting items.
When items are in bulk, an employee could lose count easily and record an incorrect value.

## Target Users
Anyone who manually counts inventory of small items.

## User Requirements
• Secure login
• Setup screen or configuration file to control resource locations
• Initialize the system by creating databases if they don’t already exist or clearing any previous inventory counts.
• Print barcode labels using data stored locally, or in a remote database.
• Measurement mode to capture the weight of a container, and the average weight of 20-100 items (depending on size and accuracy requirements).
• Record the location(s) of inventory
• Count the inventory, including inventory located in multiple locations.
• Report to identify missing items and their last known locations.
• Export the data

## Required Materials
• Raspberry Pi
• Scale
• Barcode reader (mobile device or actual)

## Possible Technologies
• Python (Our first choice)
• Node.js
• PHP

## Possible Competitors
• AVTory - (previous Semester Inventory System)
• ASAP Systems - (actual Inventory System company)

## Primary Objectives
• Create Web landing page for user login
• Establish database on remote system (AWS or internal server via another Raspberry Pi)
• Record weights of individual items

## Secondary Objectives
• Archive old inventory counts from the month period
• Print labels for new items to be added
• Record inventory locations
• Export of data for a user friendly view

## Expected Outcome
• Secure Web System
• Cycleable database (monthly)
• Inventory is recorded
• Weight is recorded

## Resources
### Development Tools
• Google Doc (Documentation)
• Github (Versioning)
• Stack Overflow (Research and Dev)

### Frontend Technologies
• HTML
• CSS
• Javascript

### Backend Technologies
• Python
• MySQL

### Hardware
• Raspberry Pi
• Scale or Load Cells (x4)
• Barcode Reader (mobile or actual)

### Software
• Flask - Python web framework to base our application
• MySQL - Database management
