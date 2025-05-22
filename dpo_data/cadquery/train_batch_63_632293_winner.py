import cadquery as cq
w0=cq.Workplane('YZ',origin=(9,0,0))
r=w0.workplane(offset=-109/2).moveTo(-25,-13).cylinder(109,17).union(w0.sketch().segment((-21,-61),(21,-61)).segment((21,-43)).arc((48,0),(21,42)).segment((21,61)).segment((-21,61)).segment((-21,42)).arc((-48,0),(-21,-43)).close().assemble().circle(28,mode='s').finalize().extrude(91))