import cadquery as cq
w0=cq.Workplane('YZ',origin=(-55,0,0))
w1=cq.Workplane('YZ',origin=(-55,0,0))
r=w0.sketch().arc((-47,-22),(-33,-30),(-18,-35)).segment((-18,-55)).segment((18,-55)).segment((18,-35)).arc((33,-30),(47,-22)).close().assemble().finalize().extrude(42).union(w0.workplane(offset=110/2).box(180,200,110)).union(w1.workplane(offset=110/2).box(140,188,110))