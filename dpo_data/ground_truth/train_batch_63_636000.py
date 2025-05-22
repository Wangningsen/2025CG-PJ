import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,14))
r=w0.workplane(offset=-114/2).moveTo(51,-53).cylinder(114,7).union(w0.sketch().segment((-58,-51),(-31,-51)).arc((-57,5),(-31,60)).segment((-58,60)).close().assemble().finalize().extrude(51)).union(w0.sketch().push([(39.5,4)]).rect(13,76).push([(43,14)]).circle(2,mode='s').finalize().extrude(86))