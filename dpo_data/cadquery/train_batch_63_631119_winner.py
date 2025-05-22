import cadquery as cq
w0=cq.Workplane('YZ',origin=(-55,0,0))
r=w0.sketch().segment((-100,-24),(15,-24)).segment((15,-21)).arc((100,1),(15,21)).segment((15,23)).segment((-100,23)).close().assemble().push([(59,-8)]).rect(34,20,mode='s').finalize().extrude(110)