import cadquery as cq
w0=cq.Workplane('YZ',origin=(22,0,0))
r=w0.sketch().arc((-74,67),(63,-78),(-41,91)).segment((-41,67)).close().assemble().push([(2,1)]).circle(56,mode='s').finalize().extrude(-45)