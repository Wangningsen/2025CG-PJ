import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,46,0))
w1=cq.Workplane('XY',origin=(0,0,-57))
r=w0.sketch().push([(25,-68)]).circle(32).push([(41.5,-60)]).rect(7,18,mode='s').finalize().extrude(-97).union(w1.sketch().segment((38,38),(61,38)).segment((61,22)).arc((75,1),(50,-1)).segment((43,-1)).arc((69,-8),(90,9)).segment((100,9)).segment((100,33)).segment((90,33)).arc((66,51),(38,38)).assemble().finalize().extrude(8))