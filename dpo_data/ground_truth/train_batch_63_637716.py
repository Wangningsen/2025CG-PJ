import cadquery as cq
w0=cq.Workplane('YZ',origin=(39,0,0))
r=w0.sketch().segment((-81,26),(-81,28)).segment((-78,28)).arc((-95,45),(-80,26)).close().assemble().finalize().extrude(-78).union(w0.sketch().arc((89,-48),(100,-10),(89,29)).segment((89,-15)).arc((97,-16),(89,-17)).close().assemble().finalize().extrude(-9))