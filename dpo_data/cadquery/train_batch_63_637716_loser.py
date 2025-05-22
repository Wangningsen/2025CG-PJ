import cadquery as cq
w0=cq.Workplane('YZ',origin=(39,0,0))
r=w0.sketch().push([(-88,36)]).circle(12).push([(-81,27)]).circle(1,mode='s').finalize().extrude(-78).union(w0.sketch().arc((89,-48),(100,-9),(89,29)).segment((89,-12)).segment((97,-11)).segment((99,-21)).segment((89,-23)).close().assemble().finalize().extrude(-9))