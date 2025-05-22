import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,34))
w1=cq.Workplane('ZX',origin=(0,5,0))
r=w0.workplane(offset=-97/2).moveTo(-86,13).cylinder(97,14).union(w0.sketch().push([(36,2)]).circle(64).push([(36.5,2)]).rect(121,22,mode='s').finalize().extrude(-77)).union(w0.sketch().segment((-48,-2),(19,-69)).segment((48,-40)).segment((48,44)).segment((23,69)).close().assemble().finalize().extrude(-19)).union(w1.workplane(offset=-65/2).moveTo(49,36).cylinder(65,14))