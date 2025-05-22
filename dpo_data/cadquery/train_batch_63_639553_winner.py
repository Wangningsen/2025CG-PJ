import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().segment((-80,52),(13,-47)).segment((68,-6)).segment((-31,99)).close().assemble().finalize().extrude(-200).union(w0.sketch().segment((-30,-18),(8,-99)).segment((80,-65)).arc((60,-17),(77,30)).close().assemble().finalize().extrude(-168))