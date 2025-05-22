import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().segment((-63,-84),(63,-84)).segment((63,84)).segment((50,84)).segment((50,82)).segment((46,82)).segment((46,84)).segment((-63,84)).close().assemble().circle(23,mode='s').finalize().extrude(-200)