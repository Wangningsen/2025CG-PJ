import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,39))
r=w0.sketch().segment((-74,45),(56,-66)).segment((74,-45)).segment((-56,66)).close().assemble().finalize().extrude(-139).union(w0.sketch().segment((-33,-22),(-20,-22)).arc((-16,-19),(-13,-22)).segment((33,-22)).segment((33,22)).segment((-33,22)).close().assemble().finalize().extrude(61))