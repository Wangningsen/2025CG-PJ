import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,46,0))
w1=cq.Workplane('XY',origin=(0,0,-49))
r=w0.sketch().push([(25,-68)]).circle(32).push([(41.5,-60)]).rect(7,18,mode='s').finalize().extrude(-97).union(w1.sketch().arc((38,38),(69,20),(43,-1)).arc((75,-5),(100,10)).segment((100,29)).arc((87,38),(73,49)).arc((56,51),(38,38)).assemble().finalize().extrude(-8))