import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-15))
w1=cq.Workplane('YZ',origin=(1,0,0))
r=w0.workplane(offset=-85/2).moveTo(19,-27).cylinder(85,4).union(w0.sketch().segment((-29,-60),(-11,-63)).segment((-10,-71)).segment((-5,-71)).segment((-6,-63)).segment((25,-67)).segment((29,-31)).segment((10,-29)).arc((-1,-41),(-18,-45)).segment((-25,-44)).close().assemble().finalize().extrude(89)).union(w1.sketch().segment((34,6),(44,6)).segment((44,22)).arc((24,99),(34,20)).close().assemble().push([(32,60)]).circle(28,mode='s').finalize().extrude(16))