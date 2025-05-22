import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-86))
r=w0.sketch().segment((-67,-97),(46,-100)).segment((49,-4)).segment((67,32)).segment((50,39)).segment((52,97)).segment((-61,100)).close().assemble().finalize().extrude(172)