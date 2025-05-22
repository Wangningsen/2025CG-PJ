import cadquery as cq
w0=cq.Workplane('YZ',origin=(2,0,0))
r=w0.sketch().segment((-41,10),(-37,10)).segment((-37,-75)).segment((32,-75)).segment((32,10)).segment((66,10)).segment((66,75)).segment((-41,75)).close().assemble().finalize().extrude(-102).union(w0.sketch().push([(-29,7)]).circle(37).push([(-20.5,0.5)]).rect(27,27,mode='s').finalize().extrude(98))