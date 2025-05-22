import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,8,0))
w1=cq.Workplane('ZX',origin=(0,7,0))
r=w0.sketch().segment((27,-96),(34,-100)).segment((36,-98)).segment((29,-94)).close().assemble().push([(32,-97)]).circle(1,mode='s').finalize().extrude(-68).union(w0.sketch().segment((-23,85),(-23,86)).arc((-38,71),(-23,85)).assemble().finalize().extrude(-34)).union(w1.sketch().segment((38,-9),(42,-9)).arc((45,-17),(52,-22)).segment((52,5)).arc((45,0),(42,-8)).segment((38,-8)).close().assemble().finalize().extrude(54))