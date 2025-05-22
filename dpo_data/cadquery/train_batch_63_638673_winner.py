import cadquery as cq
w0=cq.Workplane('YZ',origin=(-35,0,0))
w1=cq.Workplane('YZ',origin=(-90,0,0))
r=w0.sketch().circle(100).reset().face(w0.sketch().segment((51,68),(55,63)).segment((60,67)).segment((56,72)).close().assemble(),mode='s').finalize().extrude(-55).union(w1.sketch().push([(36,-75)]).circle(16).push([(36.5,-74.5)]).rect(27,13,mode='s').finalize().extrude(181))