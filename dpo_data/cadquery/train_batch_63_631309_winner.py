import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-99))
r=w0.sketch().push([(-96,0)]).rect(8,54).push([(96,0)]).rect(8,54).finalize().extrude(163).union(w0.sketch().segment((-55,6),(5,-55)).segment((55,-6)).segment((-5,55)).close().assemble().reset().face(w0.sketch().segment((-33,11),(33,-17)).segment((33,-11)).segment((-33,17)).close().assemble(),mode='s').finalize().extrude(198))