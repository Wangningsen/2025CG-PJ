import cadquery as cq
w0=cq.Workplane('YZ',origin=(-23,0,0))
r=w0.sketch().segment((-82,67),(-82,57)).arc((59,-80),(-41,92)).segment((-41,67)).close().assemble().push([(2,1)]).circle(56,mode='s').finalize().extrude(45)