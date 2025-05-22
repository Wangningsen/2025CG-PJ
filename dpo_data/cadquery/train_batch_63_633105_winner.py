import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,65,0))
r=w0.sketch().arc((79,23),(8,-60),(88,14)).segment((88,23)).close().assemble().finalize().extrude(-130).union(w0.sketch().segment((-100,52),(-61,23)).segment((-48,31)).segment((-55,20)).segment((-74,31)).segment((-70,10)).segment((-48,15)).segment((-54,36)).segment((-65,29)).segment((-54,75)).close().assemble().finalize().extrude(-53))