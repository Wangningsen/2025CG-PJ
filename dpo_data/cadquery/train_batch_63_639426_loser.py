import cadquery as cq
w0=cq.Workplane('YZ',origin=(61,0,0))
r=w0.sketch().segment((-93,71),(-61,-100)).segment((93,-71)).segment((61,100)).close().assemble().finalize().extrude(-122)