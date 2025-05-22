import cadquery as cq
w0=cq.Workplane('YZ',origin=(-33,0,0))
r=w0.sketch().push([(-43.5,-39.5)]).rect(113,93).push([(87,75)]).circle(11).finalize().extrude(-30).union(w0.sketch().segment((39,-13),(45,-13)).arc((46,-11),(47,-13)).segment((100,-13)).segment((100,2)).segment((39,2)).close().assemble().push([(73,1)]).rect(2,2,mode='s').finalize().extrude(97))