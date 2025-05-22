import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,40))
w1=cq.Workplane('YZ',origin=(73,0,0))
r=w0.sketch().arc((-92,22),(21,-59),(-64,51)).segment((-59,41)).segment((-65,38)).arc((-87,49),(-89,24)).close().assemble().finalize().extrude(-124).union(w0.sketch().segment((64,21),(64,22)).segment((66,22)).segment((66,20)).segment((65,20)).arc((74,42),(64,21)).assemble().finalize().extrude(-92)).union(w1.workplane(offset=27/2).moveTo(31,35).cylinder(27,50))