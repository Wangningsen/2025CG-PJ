import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,56))
r=w0.workplane(offset=-113/2).moveTo(20,-82).cylinder(113,3).union(w0.sketch().segment((-28,56),(-28,84)).arc((-93,0),(13,11)).segment((-19,11)).segment((-19,56)).close().assemble().push([(76,-14)]).circle(24).push([(74,1)]).circle(7,mode='s').finalize().extrude(-43))