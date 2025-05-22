import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-23))
r=w0.sketch().push([(-71,17)]).circle(29).push([(68,-14)]).circle(32).circle(19,mode='s').finalize().extrude(47)