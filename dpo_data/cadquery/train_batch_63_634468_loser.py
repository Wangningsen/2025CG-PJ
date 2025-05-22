import cadquery as cq
w0=cq.Workplane('YZ',origin=(-54,0,0))
r=w0.sketch().segment((-88,-97),(85,-100)).segment((88,97)).segment((-85,100)).close().assemble().push([(-51,-22)]).circle(2,mode='s').finalize().extrude(108)