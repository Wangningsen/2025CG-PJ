import cadquery as cq
w0=cq.Workplane('YZ',origin=(39,0,0))
r=w0.sketch().segment((-82,27),(-81,29)).segment((-78,29)).arc((-97,44),(-81,26)).close().assemble().finalize().extrude(-78).union(w0.sketch().arc((89,-48),(100,-9),(89,29)).segment((89,-12)).segment((97,-11)).segment((98,-20)).segment((89,-21)).close().assemble().finalize().extrude(-9))