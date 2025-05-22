import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-8))
r=w0.sketch().push([(-15,59)]).circle(41).push([(-44,45)]).circle(3,mode='s').push([(-18,53)]).circle(26,mode='s').finalize().extrude(-81).union(w0.sketch().segment((6,-100),(30,-100)).segment((30,-79)).arc((56,-45),(30,-9)).segment((30,10)).segment((6,10)).segment((6,-9)).arc((-20,-45),(6,-79)).close().assemble().finalize().extrude(97))