import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-98))
r=w0.sketch().push([(-96,0)]).rect(8,54).push([(96,0)]).rect(8,54).finalize().extrude(162).union(w0.sketch().segment((-55,6),(6,-55)).segment((55,-6)).segment((-6,55)).close().assemble().reset().face(w0.sketch().segment((-39,14),(37,-19)).segment((39,-14)).segment((-37,19)).close().assemble(),mode='s').finalize().extrude(197))