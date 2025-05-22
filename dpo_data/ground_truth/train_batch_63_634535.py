import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-66,0))
w1=cq.Workplane('YZ',origin=(-19,0,0))
r=w0.workplane(offset=166/2).box(66,84,166).union(w1.workplane(offset=15/2).moveTo(-55.5,0).box(89,88,15))