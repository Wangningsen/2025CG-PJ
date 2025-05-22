import cadquery as cq
w0=cq.Workplane('YZ',origin=(-78,0,0))
r=w0.workplane(offset=156/2).cylinder(156,100)