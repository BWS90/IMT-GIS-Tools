# FDNY IMT GIS Standard Operating Procedures

## Personnel
### Training
#### ESRI Provided Training
##### Tier 1 (14 hours)
[ESRI GIS Fundamentals Training Plan](https://www.esri.com/training/catalog/5b73407f8659c25ea7014330/gis-fundamentals/)
##### Tier 2 (8 hours)
[ESRI ArcGIS Online Fundamentals](https://www.esri.com/training/catalog/5b733e9d2fad23092c930883/arcgis-online-fundamentals/)
##### Tier 3 (5 hours)
[ESRI ArcGIS Pro Fundamentals](https://www.esri.com/training/catalog/5b733d0c8659c25ea7013df9/arcgis-pro-fundamentals/)
##### Tier 4 (TBD)
Potential courses
- [Fundamentals of Data Management](https://www.esri.com/training/catalog/5b29686482573b5e7c2fd8a4/fundamentals-of-data-management/)
- [Collect Data in the Field Using ArcGIS Apps](https://www.esri.com/training/catalog/5e14deb736e7e15d09b53b8e/collect-data-in-the-field-using-arcgis-apps/)
- [ArcGIS Dashboards Fundamentals](https://www.esri.com/training/catalog/612e493d5e26781eda2f4940/arcgis-dashboards-fundamentals/)
- [Exploring Spatial Relationships](https://www.esri.com/training/catalog/60d1fa75b588b75ae084c42c/exploring-spatial-relationships/)
- Probably not all of it: [ArcGIS Workflows for Public Safety](https://www.esri.com/training/catalog/5f4e6d48de1e8d4c9244690a/arcgis-workflows-for-public-safety/)
- Plenty of other specialty tracks to work on:
  - Python
  - JS (App builder)

## Operations
### Tools
#### Mandatory
- ArcGIS Pro
- AGOL Account

#### Helpful
- QGIS
- Docker

### Standards
#### File System Structure
- IAW NIFC
#### File Naming Conventions

#### Map Products

#### Data Standards
- Reserved for future use (namely when ESRI Field Maps supports contingent values)

## Job Aides

## AGOL Org Guidelines
<!-- NIFC AUP Guidelines have some good starting points -->
- Minimize group usage for each incident ex.:
  - 2022 Incident - Editing
  - 2022 Incident - Mobile Collector
  - 2022 Incident - Viewer
  - 2022 Incident - Public
- Utilize feature service views to limit edit capabilities and data revealed to groups not requiring it.
- All data editors shall utilize named accounts
  - Content should be created utilizing named account.
  - Group or 'admin' accounts shall not be used. Changing of content owners can be accomplished by GISS's.
- Tags should be utilized on content where applicable. Specifically 'Authoratative' and 'Depreciated' tags. 
- Collectors shall utilize Recon user accounts
  - Procedures shall be implemented to maintain current contact info for user with ability to lookup user at a future period.
### Sensitive Content
    - Shall not be stored on AGOL
    - FDNY GIS may be a viable alternative for sensitive content.
