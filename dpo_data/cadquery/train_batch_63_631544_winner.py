import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,34))
w1=cq.Workplane('ZX',origin=(0,5,0))
r=w0.workplane(offset=-97/2).moveTo(-86,13).cylinder(97,14).union(w0.sketch().push([(36,2)]).circle(64).rect(122,22,mode='s').finalize().extrude(-77)).union(w0.sketch().segment((-48,0),(20,-68)).segment((59,-29)).segment((46,-17)).arc((37,2),(17,10)).segment((-7,33)).close().assemble().finalize().extrude(-19)).union(w1.sketch().push([(48,36)]).circle(15).circle(12,mode='s').finalize().extrude(-65))