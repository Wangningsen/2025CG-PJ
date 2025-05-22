import cadquery as cq
w0=cq.Workplane('YZ',origin=(27,0,0))
r=w0.sketch().push([(-6,-81)]).circle(19).push([(-6.5,-81)]).rect(33,14,mode='s').finalize().extrude(-81).union(w0.sketch().segment((-27,97),(-24,53)).segment((27,56)).segment((24,100)).close().assemble().push([(0,77)]).circle(21,mode='s').finalize().extrude(27))