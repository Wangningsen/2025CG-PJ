import cadquery as cq
w0=cq.Workplane('YZ',origin=(11,0,0))
r=w0.sketch().push([(34,0)]).circle(66).circle(56,mode='s').finalize().extrude(-22).union(w0.sketch().segment((-100,-63),(-20,-63)).segment((-20,-53)).segment((-18,-53)).segment((-18,-37)).segment((-20,-37)).segment((-20,7)).segment((-100,7)).close().assemble().finalize().extrude(-9))