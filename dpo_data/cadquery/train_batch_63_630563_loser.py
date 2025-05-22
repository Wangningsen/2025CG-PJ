import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,57,0))
r=w0.sketch().segment((17,61),(17,98)).arc((-53,-85),(82,56)).segment((82,61)).close().assemble().rect(46,114,mode='s').finalize().extrude(-114)