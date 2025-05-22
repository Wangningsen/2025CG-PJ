import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,39))
w1=cq.Workplane('YZ',origin=(73,0,0))
r=w0.sketch().segment((-95,31),(-89,24)).arc((26,-53),(-70,47)).segment((-77,53)).close().assemble().reset().face(w0.sketch().segment((-68,40),(-61,40)).segment((-61,43)).arc((-60,45),(-61,47)).segment((-61,51)).segment((-68,51)).segment((-68,47)).arc((-69,45),(-68,43)).close().assemble(),mode='s').finalize().extrude(-124).union(w0.sketch().push([(73,30)]).circle(12).circle(5,mode='s').finalize().extrude(-92)).union(w1.workplane(offset=27/2).moveTo(31,36).cylinder(27,49))