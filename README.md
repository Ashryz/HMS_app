# HMS_app
Odoo app for hospital management system

### Models
- create patients model
  * using computed field to calculate age 
  * make relation with departments model
  * adding field state to the model
  * adding onChange on age field
  * make some validation and constrains on pcr,cr ratio
  * create relation many2many with doctor model
  * add mail field to patient and used apiConstrains
- create doctors model
- create departments model
- create customer inherit model from crm
  * make relation with patients model
### Views 
- create patient views
  * Kanban view
  * tree view 
  * form view
- create doctor views
  * Kanban view
  * tree view 
  * form view
- create department views
  * tree view
  * form view
- add field in inherited customer view
  
### Wizard
- create wizard to get patient history log