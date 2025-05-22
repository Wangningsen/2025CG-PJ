import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,20))
w1=cq.Workplane('YZ',origin=(25,0,0))
r=w0.sketch().segment((-7,-45),(21,-45)).arc((50,-100),(81,-46)).segment((81,66)).segment((-7,66)).close().assemble().finalize().extrude(-101).union(w0.sketch().push([(-47,49)]).circle(40).push([(-44.5,49)]).rect(23,78,mode='s').finalize().extrude(-51)).union(w1.workplane(offset=-44/2).moveTo(49,30).cylinder(44,51))