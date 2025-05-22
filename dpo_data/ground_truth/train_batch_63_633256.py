import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-24,0))
r=w0.sketch().segment((-91,-100),(-67,-100)).segment((-67,-29)).arc((-63,-18),(-67,-7)).segment((-67,64)).segment((-91,64)).segment((-91,-7)).arc((-95,-18),(-91,-29)).close().assemble().finalize().extrude(3).union(w0.sketch().push([(75,74.5)]).rect(40,51).push([(91,92)]).circle(3,mode='s').finalize().extrude(48))